//              __     __                            _      __  _                     _
//              \ \   / /___   __ _   __ _  ___     / \    / _|| |_  ___  _ __  __ _ | |  ___ __      __
//               \ \ / // _ \ / _` | / _` |/ __|   / _ \  | |_ | __|/ _ \| '__|/ _` || | / _ \\ \ /\ / /
//                \ V /|  __/| (_| || (_| |\__ \  / ___ \ |  _|| |_|  __/| |  | (_| || || (_) |\ V  V /
//                 \_/  \___| \__, | \__,_||___/ /_/   \_\|_|   \__|\___||_|   \__, ||_| \___/  \_/\_/
//                            |___/                                            |___/

#pragma once

#include <type_traits>
#include <utility>

#include "macros.h"
#include "mesh.h"

class Empty {};

// c++20 concept
template <typename T>
concept HasDmdt = requires(T t) {
    { t.dm_dt(0.0, 0.0, 0.0) };
};

template <typename T>
concept HasDedt = requires(T t) {
    { t.deps_dt(0.0, 0.0, 0.0) };
};

template <typename T>
concept HasSigma = requires(T t) {
    { t.sigma0(0.0, 0.0) };
};

template <typename T>
concept HasU = requires(T t) {
    { t.U2_th };
};

template <typename T>
concept HasMass = requires(T t) {
    { t.mass(0.0, 0.0, 0.0) };
};

#define MAKE_THIS_ODEINT_STATE(classname, data, array_size)                                                            \
    using array_type = std::array<Real, array_size>;                                                                   \
    using value_type = typename array_type::value_type;                                                                \
    using iterator = typename array_type::iterator;                                                                    \
    using const_iterator = typename array_type::const_iterator;                                                        \
    classname() : data{} {};                                                                                           \
    constexpr size_t size() const noexcept {                                                                           \
        return array_size;                                                                                             \
    }                                                                                                                  \
    constexpr iterator begin() noexcept {                                                                              \
        return data.begin();                                                                                           \
    }                                                                                                                  \
    constexpr iterator end() noexcept {                                                                                \
        return data.end();                                                                                             \
    }                                                                                                                  \
    constexpr const_iterator begin() const noexcept {                                                                  \
        return data.begin();                                                                                           \
    }                                                                                                                  \
    constexpr const_iterator end() const noexcept {                                                                    \
        return data.end();                                                                                             \
    }                                                                                                                  \
    constexpr value_type& operator[](size_t i) noexcept {                                                              \
        return data[i];                                                                                                \
    }                                                                                                                  \
    constexpr const value_type& operator[](size_t i) const noexcept {                                                  \
        return data[i];                                                                                                \
    }

void print_array(Array const& arr);

/**
 * <!-- ************************************************************************************** -->
 * @defgroup FunctionTypes Function Type Definitions
 * @brief Defines convenient aliases for unary, binary, and ternary functions operating on Reals.
 * @details These function types are used throughout the codebase for various mathematical operations
 *          and physical calculations.
 * <!-- ************************************************************************************** -->
 */

/// Function taking one Real argument
using UnaryFunc = std::function<Real(Real)>;
/// Function taking two Real arguments
using BinaryFunc = std::function<Real(Real, Real)>;
/// Function taking three Real arguments
using TernaryFunc = std::function<Real(Real, Real, Real)>;

/**
 * <!-- ************************************************************************************** -->
 * @namespace func
 * @brief Contains inline constexpr lambda functions that return constant values.
 * @details These functions are used throughout the codebase for various mathematical operations
 *          and physical calculations.
 * <!-- ************************************************************************************** -->
 */
namespace func {
    // Always returns 0 regardless of the input.
    inline constexpr auto zero_3d = [](Real phi, Real theta, Real t) constexpr noexcept { return 0.; };
    inline constexpr auto zero_2d = [](Real phi, Real theta) constexpr noexcept { return 0.; };
    // Always returns 1 regardless of the input.
    inline constexpr auto one_3d = [](Real phi, Real theta, Real t) constexpr noexcept { return 1.; };
    inline constexpr auto one_2d = [](Real phi, Real theta) constexpr noexcept { return 1.; };
} // namespace func

/**
 * <!-- ************************************************************************************** -->
 * @defgroup BasicMath Basic Math Functions
 * @brief Inline functions for specific power calculations, a step function, and unit conversion.
 * @details These functions are used throughout the codebase for various mathematical operations
 *          and physical calculations.
 * <!-- ************************************************************************************** -->
 */

/**
 * <!-- ************************************************************************************** -->
 * @brief Computes a^(5/2)
 * @param a The base value
 * @return a^(5/2)
 * <!-- ************************************************************************************** -->
 */
inline Real pow52(Real a) {
    return std::sqrt(a * a * a * a * a);
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Computes a^(4/3)
 * @param a The base value
 * @return a^(4/3)
 * <!-- ************************************************************************************** -->
 */
inline Real pow43(Real a) {
    return std::cbrt(a * a * a * a);
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Computes a^(2/3)
 * @param a The base value
 * @return a^(2/3)
 * <!-- ************************************************************************************** -->
 */
inline Real pow23(Real a) {
    return std::cbrt(a * a);
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Step function that returns 1 if x > 0, otherwise 0
 * @param x Input value
 * @return 1 if x > 0, otherwise 0
 * <!-- ************************************************************************************** -->
 */
inline Real stepFunc(Real x) {
    return x > 0 ? 1 : 0;
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Converts electron volt (eV) to frequency (Hz)
 * @param eV Energy in electron volts
 * @return Frequency in Hertz
 * <!-- ************************************************************************************** -->
 */
inline Real eVtoHz(Real eV) {
    return eV / con::h;
}

/**
 * <!-- ************************************************************************************** -->
 * @defgroup Interpolation Interpolation Functions
 * @brief Functions for interpolating values between points in arrays.
 * @details These functions are used throughout the codebase for various mathematical operations
 *          and physical calculations.
 * <!-- ************************************************************************************** -->
 */

/**
 * <!-- ************************************************************************************** -->
 * @brief General interpolation function
 * @param x0 X-value at which to interpolate
 * @param x Array of x-coordinates
 * @param y Array of y-coordinates
 * @param lo_extrap Whether to extrapolate for x0 < min(x)
 * @param hi_extrap Whether to extrapolate for x0 > max(x)
 * @return Interpolated y-value at x0
 * <!-- ************************************************************************************** -->
 */
Real interp(Real x0, Array const& x, Array const& y, bool lo_extrap = false, bool hi_extrap = false);

/**
 * <!-- ************************************************************************************** -->
 * @brief Interpolation for equally spaced x-values
 * @param x0 X-value at which to interpolate
 * @param x Array of equally spaced x-coordinates
 * @param y Array of y-coordinates
 * @param lo_extrap Whether to extrapolate for x0 < min(x)
 * @param hi_extrap Whether to extrapolate for x0 > max(x)
 * @return Interpolated y-value at x0
 * <!-- ************************************************************************************** -->
 */
Real eq_space_interp(Real x0, Array const& x, Array const& y, bool lo_extrap = false, bool hi_extrap = false);

/**
 * <!-- ************************************************************************************** -->
 * @brief Log-log interpolation (both x and y are in log space)
 * @param x0 X-value at which to interpolate
 * @param x Array of x-coordinates
 * @param y Array of y-coordinates
 * @param lo_extrap Whether to extrapolate for x0 < min(x)
 * @param hi_extrap Whether to extrapolate for x0 > max(x)
 * @return Interpolated y-value at x0
 * <!-- ************************************************************************************** -->
 */
Real loglog_interp(Real x0, Array const& x, Array const& y, bool lo_extrap = false, bool hi_extrap = false);

/**
 * <!-- ************************************************************************************** -->
 * @brief Log-log interpolation for equally spaced x-values in log space
 * @param x0 X-value at which to interpolate
 * @param x Array of equally spaced x-coordinates in log space
 * @param y Array of y-coordinates
 * @param lo_extrap Whether to extrapolate for x0 < min(x)
 * @param hi_extrap Whether to extrapolate for x0 > max(x)
 * @return Interpolated y-value at x0
 * <!-- ************************************************************************************** -->
 */
Real eq_space_loglog_interp(Real x0, Array const& x, Array const& y, bool lo_extrap = false, bool hi_extrap = false);

/**
 * <!-- ************************************************************************************** -->
 * @defgroup RootFinding Root Finding Methods
 * @brief Functions for finding roots of equations.
 * @details These functions are used throughout the codebase for various mathematical operations
 *          and physical calculations.
 * <!-- ************************************************************************************** -->
 */

/**
 * <!-- ************************************************************************************** -->
 * @brief Finds the root of a function using the bisection method
 * @tparam Fun Type of the function
 * @param f Function whose root we want to find
 * @param low Lower bound of the search interval
 * @param high Upper bound of the search interval
 * @param eps Desired accuracy (default: 1e-6)
 * @return Approximation of the root
 * <!-- ************************************************************************************** -->
 */
template <typename Fun>
auto root_bisect(Fun f, decltype(f(0)) low, decltype(f(0)) high, decltype(f(0)) eps = 1e-6) -> decltype(f(0)) {
    using Scalar = decltype(f(0));
    for (; (high - low) > std::fabs((high + low) * 0.5) * eps;) {
        Scalar mid = 0.5 * (high + low);
        if (f(mid) * f(high) > 0)
            high = mid;
        else
            low = mid;
    }
    return 0.5 * (high + low);
}

/**
 * <!-- ************************************************************************************** -->
 * @defgroup UtilityTemplates Utility Templates
 * @brief Template functions for common operations.
 * @details These functions are used throughout the codebase for various mathematical operations
 *          and physical calculations.
 * <!-- ************************************************************************************** -->
 */

/**
 * <!-- ************************************************************************************** -->
 * @brief Returns the value of a single parameter
 * @tparam T Type of the value
 * @param value The value to return
 * @return The input value
 * <!-- ************************************************************************************** -->
 */
template <typename T>
T min(T value) {
    return value;
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Returns the minimum of multiple values
 * @tparam T Type of the first value
 * @tparam Args Types of the remaining values
 * @param first First value
 * @param args Remaining values
 * @return The minimum value
 * <!-- ************************************************************************************** -->
 */
template <typename T, typename... Args>
T min(T first, Args... args) {
    return std::min(first, std::min(args...));
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Returns the value of a single parameter
 * @tparam T Type of the value
 * @param value The value to return
 * @return The input value
 * <!-- ************************************************************************************** -->
 */
template <typename T>
T max(T value) {
    return value;
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Returns the maximum of multiple values
 * @tparam T Type of the first value
 * @tparam Args Types of the remaining values
 * @param first First value
 * @param args Remaining values
 * @return The maximum value
 * <!-- ************************************************************************************** -->
 */
template <typename T, typename... Args>
T max(T first, Args... args) {
    return std::max(first, std::max(args...));
}

/**
 * <!-- ************************************************************************************** -->
 * @defgroup FastMath Fast Math Functions
 * @brief Optimized versions of common mathematical functions.
 * @details These functions provide fast approximations of exponential and logarithm functions using
 *          alternative methods when EXTREME_SPEED is defined.
 * <!-- ************************************************************************************** -->
 */

/**
 * <!-- ************************************************************************************** -->
 * @brief Fast approximation of the exponential function
 * @param x The exponent
 * @return e^x
 * <!-- ************************************************************************************** -->
 */
inline Real fast_exp(Real x) {
#ifdef EXTREME_SPEED
    // if (std::isnan(x)) return std::numeric_limits<Real>::quiet_NaN();
    // if (x == std::numeric_limits<Real>::infinity()) return std::numeric_limits<Real>::infinity();
    // if (x == -std::numeric_limits<Real>::infinity()) return 0.0;

    constexpr Real ln2 = 0.6931471805599453;
    constexpr Real inv_ln2 = 1.4426950408889634;

    Real y = x * inv_ln2;
    int64_t k = static_cast<int64_t>(y + (y >= 0 ? 0.5 : -0.5));
    Real r = x - k * ln2;

    // Real p = 1.0 + r * (1.0 + r * (0.5 + r * (0.166666666666666 + r * 0.041666666666666664)));

    Real p = 1.0 + r * (1.0 + r * (0.5 + r * (0.166666666666666)));

    return std::ldexp(p, k);
#else
    return std::exp(x);
#endif
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Fast approximation of the natural logarithm
 * @param x The input value
 * @return ln(x)
 * <!-- ************************************************************************************** -->
 */
inline double fast_log(double x) {
#ifdef EXTREME_SPEED
    if (x <= 0.)
        return -std::numeric_limits<double>::infinity();
    if (std::isnan(x))
        return std::numeric_limits<double>::quiet_NaN();
    if (x == std::numeric_limits<double>::infinity())
        return std::numeric_limits<double>::infinity();

    uint64_t bits;
    std::memcpy(&bits, &x, sizeof(x));
    int64_t exponent = ((bits >> 52) & 0x7FF) - 1023;
    bits = (bits & 0x000FFFFFFFFFFFFFULL) | 0x3FF0000000000000ULL;
    double f;
    std::memcpy(&f, &bits, sizeof(f));
    double p = -1.49278 + (2.11263 + (-0.729104 + 0.10969 * f) * f) * f;
    return p + 0.6931471806 * exponent;
#else
    return std::log(x);
#endif
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Fast approximation of the base-2 logarithm
 * @param val The input value
 * @return log2(val)
 * <!-- ************************************************************************************** -->
 */
inline double fast_log2(double val) {
#ifdef EXTREME_SPEED
    int64_t* const exp_ptr = reinterpret_cast<int64_t*>(&val);
    int64_t x = *exp_ptr;
    int log2 = ((x >> 52) & 0x7FF) - 1023; // extract exponent bits

    // Step 2: Normalize mantissa to [1.0, 2.0)
    x &= ~(0x7FFLL << 52); // clear exponent bits
    x |= (1023LL << 52);   // set exponent to 0
    *exp_ptr = x;          // val is now normalized to [1.0, 2.0)
    double mantissa = val;

    // Step 3: Polynomial approximation of log2(mantissa) in [1, 2)
    double y = mantissa - 1.0; // small value in [0, 1)
    double log2_mantissa =
        y * (1.44269504088896340736 + y * (-0.721347520444482371076 + y * (0.479381953382630073738)));

    /*double log2_mantissa =
        y * (1.44269504088896340736 +  // 1/ln(2)
        y * (-0.721347520444482371076 +
        y * (0.479381953382630073738 +
        y * (-0.360673760222241834679 +
        y * (0.288539008177138356808 +
        y * (-0.139304958445395653244))))));*/

    return log2_mantissa + log2;
#else
    return std::log2(val);
#endif
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Fast approximation of 2 raised to a power
 * @param x The exponent
 * @return 2^x
 * <!-- ************************************************************************************** -->
 */
inline double fast_exp2(double x) {
#ifdef EXTREME_SPEED
    int int_part = (int)x;
    double frac_part = x - int_part;

    // Polynomial approximation for 2^frac_part where 0 <= frac_part < 1
    // 4th order polynomial gives good balance of speed and accuracy
    /*double poly = 1.0 + frac_part * (0.693147180559945 +
                                     frac_part * (0.240226506959101 +
                                                  frac_part * (0.0555041086648216 + frac_part *
       0.00961812910762848)));*/
    double poly =
        1.0 + frac_part * (0.693147180559945 + frac_part * (0.240226506959101 + frac_part * (0.0555041086648216)));

    // Combine with integer power of 2 using bit manipulation
    int64_t bits = ((int64_t)(int_part + 1023)) << 52;
    double factor = *reinterpret_cast<double*>(&bits);

    return (poly * factor);
#else
    return std::exp2(x);
#endif
}

/**
 * <!-- ************************************************************************************** -->
 * @brief Fast approximation of a raised to the power of b
 * @param a The base
 * @param b The exponent
 * @return a^b
 * <!-- ************************************************************************************** -->
 */
inline Real fast_pow(Real a, Real b) {
    return fast_exp2(b * fast_log2(a));
}
