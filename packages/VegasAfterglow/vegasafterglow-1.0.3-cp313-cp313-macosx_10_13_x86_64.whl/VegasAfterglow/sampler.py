# src/vegasglow/sampler.py

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Optional, Sequence, Tuple, Type

import emcee
import numpy as np

from .types import FitResult, ModelParams, ObsData, Setups, VegasMC

logger = logging.getLogger(__name__)


class _log_prob:
    """
    Thread-safe log-probability callable for emcee.
    """

    def __init__(
        self,
        data: ObsData,
        config: Setups,
        to_params: Callable[[np.ndarray], ModelParams],
        pl: np.ndarray,
        pu: np.ndarray,
        model_cls: Type[VegasMC],
    ):
        self.data = data
        self.base_cfg = config
        self.to_params = to_params
        self.pl = pl
        self.pu = pu
        self.model_cls = model_cls
        self._models = {}

    def __call__(self, theta: np.ndarray) -> float:
        tid = threading.get_ident()
        if tid not in self._models:
            model = self.model_cls(self.data)
            model.set(self.base_cfg)
            self._models[tid] = model
        model = self._models[tid]

        # enforce simple uniform priors
        if np.any(theta < self.pl) or np.any(theta > self.pu):
            return -np.inf

        try:
            p = self.to_params(theta)
            chi2 = model.estimate_chi2(p)
            return -0.5 * chi2 if np.isfinite(chi2) else -np.inf
        except Exception:
            return -np.inf


class MultiThreadEmcee:
    """
    High-level MCMC runner for afterglow fitting with optional two-stage refinement.
    """

    def __init__(
        self,
        param_config: Tuple[Sequence[str], np.ndarray, np.ndarray, np.ndarray],
        to_params: Callable[[np.ndarray], ModelParams],
        model_cls: Type[VegasMC],
        num_workers: Optional[int] = None,
    ):
        self.labels, self.init, self.pl, self.pu = param_config
        self.ndim = len(self.init)
        self.nwalkers = 2 * self.ndim
        self.to_params = to_params
        self.model_cls = model_cls
        self.num_workers = num_workers

    def run(
        self,
        data: ObsData,
        base_cfg: Setups,
        resolution: Tuple[float, float, float] = (0.3, 1, 10),
        total_steps: int = 10_000,
        burn_frac: float = 0.2,
        thin: int = 1,
        moves: Optional[Sequence[Tuple[emcee.moves.Move, float]]] = None,
        refine_steps: int = 500,
        top_k: int = 10,
    ) -> FitResult:
        """
        Run coarse MCMC + optional stretch-move refinement at higher resolution.
        """

        cfg = self._make_cfg(base_cfg, *resolution)

        log_prob = _log_prob(
            data, cfg, self.to_params, self.pl, self.pu, self.model_cls
        )

        spread = 0.2 * (self.pu - self.pl)
        pos = self.init + spread * np.random.randn(self.nwalkers, self.ndim)
        eps = 1e-6 * (self.pu - self.pl)
        pos = np.clip(pos, self.pl + eps, self.pu - eps)

        if moves is None:
            moves = [
                (emcee.moves.StretchMove(), 0.6),
                (emcee.moves.DEMove(), 0.3),
                (emcee.moves.DESnookerMove(), 0.1),
            ]

        logger.info(
            "Running coarse MCMC at resolution %s for %d steps",
            resolution,
            total_steps,
        )
        with ThreadPoolExecutor(max_workers=self.num_workers) as pool:
            sampler = emcee.EnsembleSampler(
                self.nwalkers, self.ndim, log_prob, pool=pool, moves=moves
            )
            sampler.run_mcmc(pos, total_steps, progress=True)

        burn = int(burn_frac * total_steps)
        chain = sampler.get_chain(discard=burn, thin=thin)
        logp = sampler.get_log_prob(discard=burn, thin=thin)
        chain, logp, _ = self._filter_bad_walkers(chain, logp)

        flat_chain = chain.reshape(-1, self.ndim)
        flat_logp = logp.reshape(-1)

        sorted_idx = np.argsort(flat_logp)[::-1]

        # Round parameters to avoid floating point precision issues
        rounded_params = np.round(flat_chain[sorted_idx], decimals=12)

        # Find unique parameter combinations while preserving sort order
        _, unique_idx = np.unique(rounded_params, axis=0, return_index=True)
        # Keep original sort order, limit to top_k
        unique_idx = np.sort(unique_idx)[:top_k]

        final_idx = sorted_idx[unique_idx]
        top_k_params = flat_chain[final_idx]
        top_k_log_probs = flat_logp[final_idx]

        logger.info(
            "Found %d unique fits with log probabilities: %.2f to %.2f",
            len(top_k_params),
            top_k_log_probs[0],
            top_k_log_probs[-1],
        )

        return FitResult(
            samples=chain,
            log_probs=logp,
            labels=self.labels,
            top_k_params=top_k_params,
            top_k_log_probs=top_k_log_probs,
        )

    def _make_cfg(self, base_cfg: Setups, phi: float, theta: float, t: float) -> Setups:
        """
        Create a shallow copy of base_cfg and override its grid resolution.
        """
        cfg = type(base_cfg)()
        for attr in dir(base_cfg):
            if not attr.startswith("_") and hasattr(cfg, attr):
                try:
                    setattr(cfg, attr, getattr(base_cfg, attr))
                except Exception:
                    pass
        cfg.t_resol = t
        cfg.theta_resol = theta
        cfg.phi_resol = phi
        return cfg

    @staticmethod
    def _filter_bad_walkers(
        chain: np.ndarray, logp: np.ndarray, threshold_mad: float = 3.0
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Remove walkers whose mean log-prob is > threshold_mad·MAD below the median.
        """
        nsteps, nwalkers, _ = chain.shape
        mean_lp = np.mean(logp, axis=0)
        median = np.median(mean_lp)
        mad = np.median(np.abs(mean_lp - median))
        cutoff = median - threshold_mad * mad
        good = mean_lp > cutoff
        logger.info(
            "Filtered %d / %d bad walkers (cutoff=%.2f)",
            np.sum(~good),
            nwalkers,
            cutoff,
        )
        return chain[:, good, :], logp[:, good], good
