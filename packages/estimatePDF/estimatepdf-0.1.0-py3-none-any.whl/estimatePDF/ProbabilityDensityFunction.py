# %%
"""
# Set of Custom Functions for Generating Probability Density Function 

## PDF for Different Symmetric & Asymmetric Distributions


**Author:** S. Sarkar

**Version:** 0.00

**Release:** Aug/2025

---
"""

# %%
"""
## `GaussianPDF`

| **Argument Name** | **Default** | **Comments**                                              |
|------------------|-------------|------------------------------------------------------------|
| `x`              | —           | Input values (array or tensor)                             |
| `mu`             | —           | Mean (location parameter)                                  |
| `sigma`          | —           | Standard deviation (scale parameter), \( \sigma > 0 \)     |
| `alpha`          | —           | Skewness parameter (shape)                                 |
| **Return**       | —           | PDF values evaluated at \( x \)                            |

"""

# %%
"""
## `InvTransformSampling`

| **Argument Name** | **Default** | **Comments**                                             |
|------------------|-------------|-----------------------------------------------------------|
| `pdf`            | —           | Probability density function values (array)               |
| `x`              | —           | Corresponding x-values (array)                            |
| `N`              | —           | Number of samples to generate (integer)                   |
| `Seed`           | None        | Optional random seed for reproducibility                  |
| **Return**       | —           | Samples drawn from the distribution defined by pdf and  x |

"""

# %%
"""
## `M_Wright`

| **Argument Name** | **Default** | **Comments**                                         |
|------------------|-------------|------------------------------------------------------|
| `x`              | —           | Input array \( x \geq 0 \)                           |
| `v`              | —           | Parameter \( 0 < v < 1 \)                            |
| `J`              | 50          | Number of series terms (integer)                     |
| `SafeCheck`      | True        | Replace NaNs/Infs with 0 (bool)                      |
| `Print`          | False       | Print debug info (bool)                              |
| **Return**       | —           |  M_v(x) computed via truncated series expansion |

"""

# %%
"""
## `M_Wright_Reflect`

| **Argument Name** | **Default** | **Comments**                                 |
|------------------|-------------|----------------------------------------------|
| `x`              | —           | Non-negative input array or scalar           |
| `v`              | —           | Parameter \( 0 < v < 1 \)                    |
| `J`              | 50          | Number of series terms (integer)             |
| `SafeCheck`      | True        | Replace NaNs/Infs with 0 (bool)              |
| `Print`          | False       | Print debug info (bool)                      |
| **Return**       | —           | M_v(x) using reflection formula for stability |

"""

# %%
"""
## `M_CDF`

| **Argument Name** | **Default** | **Comments**                                               |
|------------------|-------------|-------------------------------------------------------------|
| `y`              | —           | Input values at which to compute the CDF (array-like)       |
| `v`              | —           | Parameter of the M-Wright function, \( 0 < v < 1 \)         |
| `J`              | 50          | Number of terms in the series expansion (integer)           |
| **Return**       | —           | CDF values corresponding to input \( y \)                   |

"""

# %%
"""
## `Create_AWM_I_PDF`

| **Argument Name** | **Default** | **Comments**                                          |
|------------------|-------------|--------------------------------------------------------|
| `x`              | —           | Input values at which to compute the PDF (array-like)  |
| `v`              | —           | Parameter of the M-Wright function, \( 0 < v < 1 \)    |
| `lamda`          | —           | Scaling parameter applied to \( x \)                   |
| `J`              | 50          | Number of terms in the series expansion (integer)      |
| **Return**       | —           | PDF values evaluated at \( x \)                        |

"""

# %%
"""
## `Create_AWM_II_PDF`

| **Argument Name** | **Default** | **Comments**                                                |
|------------------|-------------|--------------------------------------------------------------|
| `x`              | —           | Input values (array-like or scalar)                          |
| `v`              | —           | Fractional parameter \( 0 $\leq$ v < 1 \)                    |
| `alpha`          | —           | Asymmetry parameter \( $\alpha$ > 0 \)                       |
| `J`              | 50          | Number of series terms in `M_Wright_Reflect`                 |
| **Return**       | —           | PDF values \( $f_v$(x; $\alpha$) \), same shape as \( x \)   |

"""

# %%
"""
## `AsymLaplacePDF`

| **Argument Name** | **Default** | **Comments**                                              |
|------------------|-------------|------------------------------------------------------------|
| `x`              | —           | Points at which to evaluate the PDF (array-like)           |
| `m`              | —           | Location parameter (mode)                                  |
| `lamda`          | —           | Scale parameter \( $\lambda$ > 0 \)                        |
| `kappa`          | —           | Asymmetry parameter \( $\kappa$ > 0 \)                     |
| **Return**       | —           | PDF values evaluated at \( x \)                            |

"""

# %%
"""
## `SampleAsymLaplace`

| **Argument Name** | **Default** | **Comments**                                       |
|------------------|-------------|-----------------------------------------------------|
| `m`              | —           | Location parameter (mode)                           |
| `lamda`          | —           | Scale parameter \( $\lambda$ > 0 \)                 |
| `kappa`          | —           | Asymmetry parameter \( $\kappa$ > 0 \)              |
| `size`           | —           | Number of samples to generate (integer)             |
| `Seed`           | None        | Optional random seed for reproducibility            |
| **Return**       | —           | Samples from the Asymmetric Laplace distribution    |

"""

# %%
"""
# Import Required Libraries 

**NumPy**: Python package for N-dimensional arrays 

**SciPy**: SciPy API for normal continuous random variable &  gamma function


### For Debugging

**Matplotlib**: Python plotting library

"""

# %%
DEBUG = False # True# Default Set it False
# -----------------------------------------------------------------------------
import numpy as np
from scipy.stats import norm
from scipy.special import gamma
from scipy.interpolate import interp1d

# -----------------------------------------------------------------------------
if DEBUG: import matplotlib.pyplot as plt


# %%
"""
## Skew-Guassian Distribution with Mean $\mu$ and Standard Deviation $\sigma$

$f(x; \mu, \sigma, \alpha) = \frac{2}{\sigma} \, \phi(z) \, \Phi(\alpha z)$

$\phi(z) = \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{z^2}{2}\right)$

$\Phi(\alpha z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\alpha z} \exp\left(-\frac{t^2}{2}\right) \, dt$

Where:
- $z = \frac{x - \mu}{\sigma}$
- $\phi(z)$ is the standard normal PDF  
- $\Phi(z)$ is the standard normal CDF  
- $\mu$: mean 
- $\sigma$: standard deviation 
- $\alpha$: skewness parameter  
    - $\alpha = 0$: symmetric (normal)  
    - $\alpha > 0$: right-skewed  
    - $\alpha < 0$: left-skewed

**PDF of Skew-Guassian Distribution with Mean $\mu$ and Standard Deviation $\sigma$**
$$
\int_{-\infty}^{\infty} f(x; \mu, \sigma, \alpha) \, dx = 1
$$

**Case 1:** Symmetric (Normal) - $\alpha = 0$ | $\mu = 0$ | $\sigma = \sqrt{V}, \quad \text{where } V \sim \mathcal{U}(1, 5)$ |

**Case 2:** Right-skewed - $\alpha \sim \mathcal{U}(1, 5)$ (i.e., $\alpha > 0$) | $\mu = 0$ | $\sigma = \sqrt{V}, \quad \text{where } V \sim \mathcal{U}(1, 5)$ |

**Case 3:** Left-skewed - $\alpha \sim -\mathcal{U}(1, 5)$ (i.e., $\alpha < 0$) | $\mu = 0$ | $\sigma = \sqrt{V}, \quad \text{where } V \sim \mathcal{U}(1, 5)$ |

"""

# %%
"""
# Function to create Gaussian PDF with or without skew

Args:
    x (array_like): Points to evaluate.
    mu (float): Mean of the distribution.
    sigma (float): Standard deviation (>0).
    alpha (float): Skewness (0=symmetric).

Returns:
    numpy.ndarray: PDF values at x.
"""
def GaussianPDF(x, mu, sigma, alpha):
    z = (x - mu) / sigma
    pdf = (2 / sigma) * norm.pdf(z) * norm.cdf(alpha * z)
    return pdf


# %%
"""
## Sampling from a PDF using Inverse Transform Sampling

**Given:** A function $f(x)$ defined on the domain $[a, b]$, representing an unnormalized or normalized probability density function (PDF).

---

### 1. Discretize the domain into $N$ points:

$$
x_i = a + (i-1)\Delta x, \quad i = 1, 2, \dots, N, \quad \Delta x = \frac{b - a}{N - 1}
$$

---

### 2. Normalize the PDF:

$$
f_i = \frac{f(x_i)}{\sum_{j=1}^N f(x_j)\, \Delta x}
\quad \text{so that} \quad
\sum_{i=1}^N f_i \Delta x = 1
$$

---

### 3. Compute the discrete cumulative distribution function (CDF):

$$
F_i = \sum_{k=1}^i f_k \Delta x,
\quad F_1 = f_1 \Delta x, \quad F_N = 1
$$

---

### 4. Define the inverse CDF using interpolation:

$$
F^{-1} : [0, 1] \to [a, b]
$$

$$
F^{-1}(u) \approx x_j \quad \forall\, u \in [0, 1], \quad \text{where} \quad F_j \leq u < F_{j+1}
$$

---

### 5. Generate samples:

- Draw $u_n \sim \mathcal{U}(0, 1)$ for $n = 1, 2, \dots, M$
- Map each $u_n$ to a sample:

$$
x_{\text{sample}, n} = F^{-1}(u_n)
$$

"""

# %%
"""
Generate samples from a given PDF using Inverse Transform Sampling.

Args:
    pdf: probability distribution
    x: 1D array of points in the domain [a, b]
    N: Number of samples to generate
    Seed: If None - Do not use Random seed else Use Seed Value for reproducibility

Returns:
    samples: 1D array of sampled points from the PDF
"""

def InvTransformSampling(pdf, x, N, Seed=None):
    x=np.linspace(np.amin(x),np.amax(x),pdf.size)

    dx = np.diff(x)
    dx = np.append(dx, dx[-1])  # Handle last element spacing

    # Normalize PDF to ensure it integrates to 1
    pdf = pdf / np.sum(pdf * dx)

    # Compute the CDF
    cdf = np.cumsum(pdf * dx)
    cdf[-1] = 1.0  # Ensure numerical stability

    # Build the inverse CDF interpolator
    inv_cdf = interp1d(cdf, x, bounds_error=False, fill_value=(x[0], x[-1]))

    # Sample from uniform distribution and map via inverse CDF
    if Seed is not None:
        rng = np.random.RandomState(Seed)  # fixed seed for reproducibility
        u = rng.uniform(0, 1, N)
    else: u = np.random.uniform(0, 1, N)
    samples = inv_cdf(u)    
    return samples


# %%
"""
# M-Wright Function

The M-Wright function is a special function that appears in the study of fractional calculus, anomalous diffusion, and time-fractional differential equations. 

$M_\nu(x) = \sum_{j=0}^\infty \frac{(-x)^j}{j! \, \Gamma(-\nu j + 1 - \nu)}$

**Where:**

- $\nu \in (0, 1)$: shape parameter (controls tail heaviness and spread)
- $x \in \mathbb{R}$: real-valued input (evaluation point)
- $j \in \mathbb{N}_0$: summation index (non-negative integers, i.e., $j = 0, 1, 2, \dots$)
- $\Gamma(\cdot)$: Gamma function (generalizes factorial, where $\Gamma(n) = (n - 1)!$ for $n \in \mathbb{N}$)

For positive integers $n$, the Gamma function $\Gamma$ satisfies:  $\Gamma(n) = (n - 1)!$

    
"""

# %%

def M_Wright(x, v, J=50, SafeCheck=True, Print=False):
    """
    Compute the M-Wright function M_nu(x) using a truncated series expansion.
    Handles potential NaNs by skipping invalid terms.
    
    Args:
        x: Input array (x ≥ 0).
        v: Parameter (0 < v < 1).
        J: Number of series terms.
    Returns:
        M_v(x) computed via truncated series.
    
    Assumes x >= 0 and 0 < v < 1. 
    """
    x = np.asarray(x, dtype=np.float32)
    M = np.zeros_like(x)
    Err_NaN_Inf=False
    Err_OF_ZD_VE_FPE=False
    for j in range(int(J)):
        try:
            denom = np.math.factorial(j) * gamma(-v * j + 1 - v)
            if np.isnan(denom) or np.isinf(denom):
                Err_NaN_Inf=True
                continue  # Skip term if invalid
            Term = ((-x) ** j) / denom
            M += Term
        except (OverflowError, ZeroDivisionError, ValueError, FloatingPointError):
            Err_OF_ZD_VE_FPE=True
            continue  # Gracefully skip problematic term
    
    # Final safety check: replace any resulting NaNs with 0
    if SafeCheck: M = np.nan_to_num(M, nan=0.0, posinf=0.0, neginf=0.0)
    if Print:
        if Err_NaN_Inf: print("M_Wright(): NaN / Inf");
        if Err_OF_ZD_VE_FPE: print("M_Wright(): OverflowError/ZeroDivisionError/ValueError/FloatingPointError");
        print(f'x: {x.shape}')
        print(f'Term: {Term.shape}')
        print(f'M: {M.shape}')
        
    return M



# %%
"""
# M-Wright Function Using Gamma Function Reflection Formula

$$
\Gamma(1 - \tau) \, \Gamma(\tau) = \frac{\pi}{\sin(\pi \tau)}, \quad \text{for } \tau \notin \mathbb{Z}
$$

If we define:
$$
\tau = \nu j + \nu \quad \Rightarrow \quad -\nu j + 1 - \nu = 1 - (\nu j + \nu) = 1 - \tau
$$

Then:
$$
\Gamma(-\nu j + 1 - \nu) = \Gamma(1 - \tau) = \frac{\pi}{\Gamma(\tau)\sin(\pi \tau)}
$$

---

#### Substituting into the M-Wright Series:

**Original Series**:
$$
M_\nu(x) = \sum_{j=0}^{\infty} \frac{(-x)^j}{j! \, \Gamma(-\nu j + 1 - \nu)}
$$

**Using the reflection formula**:
$$
M_\nu(x) = \sum_{j=0}^{\infty} \frac{(-x)^j \, \Gamma(\nu j + \nu) \, \sin(\pi (\nu j + \nu))}{j! \, \pi}
$$

---

#### Final Expression:
$$
M_\nu(x) = \frac{1}{\pi} \sum_{j=0}^{\infty} \frac{(-x)^j \, \Gamma(\nu j + \nu) \, \sin(\pi (\nu j + \nu))}{j!}
$$

---

#### Benefit:
This form avoids the singularities of the Gamma function in the original denominator and may improve numerical stability — especially when
$-\nu j + 1 - \nu$ becomes negative.

"""

# %%
def M_Wright_Reflect(x, v, J=50, SafeCheck=True, Print=False):
    """
    Compute the M-Wright function M_v(x) using the reflection formula
    for improved numerical stability.
    
    Parameters:
    - x : array-like or scalar, non-negative input
    - v : float, 0 < v < 1
    - J : int, number of terms in the series (default 50)
    
    Returns:
    - M : array-like, same shape as x
    """
    x = np.asarray(x, dtype=np.float64)
    M = np.zeros_like(x)
    Err_NaN_Inf=False
    Err_OF_ZD_VE_FPE=False
    for j in range(int(J)):
        try:
            tau = v * j + v
            numerator = (-x)**j * gamma(tau) * np.sin(np.pi * tau)
            denominator = np.math.factorial(j) * np.pi
            coeff = numerator / denominator
            if np.isnan(coeff).any() or np.isinf(coeff).any():
                Err_NaN_Inf=True
                continue  # Skip term if invalid            
            M += coeff
        except (OverflowError, ZeroDivisionError, ValueError, FloatingPointError):
            Err_OF_ZD_VE_FPE=True
            continue  # Gracefully skip problematic term
            
    # Final safety check: replace any resulting NaNs with 0
    if SafeCheck: M = np.nan_to_num(M, nan=0.0, posinf=0.0, neginf=0.0)
    if Print:
        if Err_NaN_Inf: print("M_Wright_Reflect(): NaN / Inf");
        if Err_OF_ZD_VE_FPE: print("M_Wright_Reflect(): OverflowError/ZeroDivisionError/ValueError/FloatingPointError");
        print(f'x: {x.shape}')
        print(f'coeff: {coeff.shape}')
        print(f'M: {M.shape}')    
    return M


# %%
"""
## Test Code to Evaluate M_Wright( ) &  M_Wright_Reflect( )
"""

# %%
if DEBUG:
    # Test
    v = 0.25
    J=100
    x = np.linspace(0, 5, 100)
    mw_x = M_Wright(x, v, J, SafeCheck=False, Print=True)
    nan_count = np.sum(np.isnan(mw_x))
    print(f'Number of NaN values in mw_x: {nan_count}\n')   
    
    mwR_x = M_Wright_Reflect(x, v, J, SafeCheck=False, Print=True)
    nan_count = np.sum(np.isnan(mwR_x))
    print(f'Number of NaN values in mwR_x: {nan_count}\n')
    # Plot
    plt.plot(x, mw_x, c='r', ls=':', lw=2)
    plt.plot(x, mwR_x, c='b',ls='--', lw=1)
    plt.title(f'M-Wright Function ($\\nu$={v}, J={J})')
    plt.xlabel('x')
    plt.ylabel(f'$M_\\nu(x)$')
    plt.grid(True)
    plt.show()


# %%
"""
## Asymmetric M-Wright Type I Distribution: $\mathrm{AWM}_\nu^{I}(\lambda)$

A random variable $X$ follows the **Asymmetric M-Wright Type I distribution** if its probability density function is given by:

$$
f_\nu(x; \lambda) = M_\nu(|x|) \cdot \mathfrak{M}_\nu(\lambda x), \quad 0 \leq \nu < 1
$$

Here,

- $M_\nu(|x|)$: This is the M-Wright function, which acts as a PDF kernel centered at zero. It is non-negative, integrable, and has exponential-type decay.

- $\mathfrak{M}_\nu(\lambda x)$: This is the cumulative distribution function (CDF) associated with the symmetric M-Wright PDF.

$$
\mathfrak{M}_\nu(y) = \frac{1}{2} \left[ 1 + \operatorname{sgn}(y) \left( 1 - \sum_{j=0}^\infty \frac{(-|y|)^j}{j! \, \Gamma(1 - \nu j)} \right) \right]
$$


This form introduces asymmetry by modulating the symmetric PDF $M_\nu(|x|)$ with its CDF $\mathfrak{M}_\nu(\lambda x)$. The parameter $\lambda$ governs the asymmetry and skewness.


"""

# %%
def M_CDF(y, v, J=50):
    """
    Compute the cumulative distribution function (CDF) of the M-Wright distribution.

    Args:
        y (array-like): Input values at which to compute the CDF.
        v (float): Parameter of the M-Wright function, 0 < v < 1.
        J (int, optional): Number of terms in the series expansion (default is 50).

    Returns:
        numpy.ndarray: CDF values corresponding to input y.
    """
    y = np.asarray(y, dtype=np.float64)
    sign_y = np.sign(y)
    M_val = M_Wright_Reflect(np.abs(y), v, J)
    cdf = 0.5 * (1 + sign_y * (1 - M_val))
    return cdf
#********************************************************
def Create_AWM_I_PDF(x, v, lamda, J=50):
    """
    Compute the Asymmetric M-Wright type I PDF using series expansions and reflection.

    Args:
        x (array-like): Input values at which to compute the PDF.
        v (float): Parameter of the M-Wright function, 0 < v < 1.
        lamda (float): Scaling parameter applied to x.
        J (int, optional): Number of terms in the series expansion (default is 50).

    Returns:
        numpy.ndarray: Probability density function values evaluated at x.
    """    
    x = np.asarray(x, dtype=np.float64)
    Mx = M_Wright_Reflect(np.abs(x), v, J)    
    y=x*lamda
    cdf = M_CDF(y, v, J)
    return Mx*cdf
    sign_y = np.sign(y)
    My=M_Wright_Reflect(y, v, J)
    CDF_val = 0.5 * (1 + sign_y * (1 - My))
    #
    pdf = Mx * My
    dx = x[1] - x[0]
    pdf /= np.sum(pdf * dx)  # Normalize so that integral ≈ 1
    
    return pdf
#********************************************************


# %%
"""
## Test Code to Evaluate Func. M_CDF( ) & Create_AWM_I_PDF( )

#### Utilizing Func M_Wright_Reflect( )
"""

# %%
if DEBUG:
   
    # Test
    v = 0.25
    J=100
    Lamda=2#-0.5
    x = np.linspace(-10, +10, 500)
    y=Lamda*x
    M_cdf = M_CDF(y, v, J)#, Print=True)
    nan_count = np.sum(np.isnan(M_cdf))
    print(f'Number of NaN values in Mw_xLamda: {nan_count}')
    
    Mv_xLamda = M_Wright_Reflect(y, v, J)
    nan_count = np.sum(np.isnan(Mv_xLamda))
    print(f'Number of NaN values in Mv_xLamda: {nan_count}')    
    
    Mv_xAbs = M_Wright_Reflect(np.abs(x), v, J)
    nan_count = np.sum(np.isnan(Mv_xAbs))
    print(f'Number of NaN values in Mv_xAbs: {nan_count}')
     
    pdf = Create_AWM_I_PDF(x, v, Lamda, J)
    nan_count = np.sum(np.isnan(pdf))
    print(f'Number of NaN values in pdf: {nan_count}')  
    print(f"PDF AUC: {np.trapz(pdf, x):.3f}") #TensorAUC(x, pdf)
    # Plot
    plt.plot(x, M_cdf, c='b', ls=':', lw=2, label=r'$\mathfrak{M}_\nu(\lambda \cdot x)$')
    #plt.plot(x, Mv_xLamda, c='k', ls=':', lw=2, label=r'$M_\nu(x\lambda)$')
    plt.plot(x, Mv_xAbs, c='g', ls=':', lw=2, label=r'$M_\nu(|x|)$')
    plt.plot(x, pdf, c='r',ls='--', lw=1, label=r'$f_\nu(x; \lambda)$')
    plt.title(f'M-Wright Function ($\\nu$={v}, $\\lambda$={Lamda}, J={J})')
    plt.xlabel('x')
    plt.ylabel(r'$f_\nu(x; \lambda)$ | $\mathfrak{M}_\nu(\lambda \cdot x)$ | $M_\nu(|x|)$')
    plt.legend()
    plt.grid(True)
    plt.show()



# %%
"""
## Asymmetric M-Wright Distribution Type II ( $\mathrm{AMW}_\nu^{\mathrm{II}}(\alpha)$ ) :


A random variable $X$ follows the **Asymmetric M-Wright Type II distribution** if its probability density function is given by:

$$
f_\nu(x; \alpha) =\frac{\alpha}{(1 + \alpha^2)}
\begin{cases}
M_\nu(\alpha x), & \text{if } x \geq 0 \\\\
M_\nu(-\frac{x}{ \alpha}), & \text{if } x < 0
\end{cases}
$$

where:
- $M_\nu(x)$ is the **M-Wright function** (PDF kernel),
- $0 \le \nu < 1$ is the shape parameter,
- $\alpha > 0$ is the asymmetry parameter.


"""

# %%
# Function to create Asymmetric M-Wright Type II Distribution 
def Create_AWM_II_PDF(x, v, alpha, J=50):
    """
    Compute the Asymmetric M-Wright Type II PDF:
    
        f_v(x; alpha) = (alpha / (1 + alpha^2)) * 
                        M_v(alpha * x) if x >= 0,
                        M_v(-x / alpha) if x < 0

    Parameters:
    - x : array-like or scalar input
    - v : fractional parameter (0 <= v < 1)
    - alpha : asymmetry parameter (alpha > 0)
    - J : number of series terms in M_Wright_Reflect

    Returns:
    - f : PDF values, same shape as x
    """
    x = np.asarray(x, dtype=np.float64)
    f = np.zeros_like(x)

    norm_const = alpha / (1 + alpha**2)

    # For x >= 0
    mask_pos = x >= 0
    f[mask_pos] = norm_const * M_Wright_Reflect(alpha * x[mask_pos], v, J)

    # For x < 0
    mask_neg = ~mask_pos
    f[mask_neg] = norm_const * M_Wright_Reflect(-x[mask_neg] / alpha, v, J)

    return f



# %%
"""
## Test Code to Evaluate Func. Create_AWM_II_PDF( )

#### Utilizing Func M_Wright_Reflect( )
"""

# %%
if DEBUG:
    # Test
    v = 0.25 # 0 < v < 0.3
    J= 100
    Alpha=0.5 # 0.3-0.7 or 1.3 - 1.7
    x = np.linspace(-10, 10, 500)
    xPos = x[np.where(x >= 0)[0]]; y=xPos*Alpha
    M_AlphaPosX = M_Wright_Reflect(y, v, J, SafeCheck=False, Print=True)
    nan_count = np.sum(np.isnan(M_AlphaPosX))
    print(f'Number of NaN values in M_AlphaPosX: {nan_count}')
    
    xNeg = x[np.where(x < 0)[0]]; y=-xNeg/Alpha
    M_AlphaNegX = M_Wright_Reflect(y, v, J,SafeCheck=False, Print=True)
    nan_count = np.sum(np.isnan(M_AlphaNegX))
    print(f'Number of NaN values in M_AlphaNegX: {nan_count}')    
    M_AlphaAllX = np.concatenate([M_AlphaNegX, M_AlphaPosX])


    pdf = Create_AWM_II_PDF(x, v, Alpha, J)
    nan_count = np.sum(np.isnan(pdf))
    print(f'Number of NaN values in pdf: {nan_count}') 
    print(f"PDF AUC: {np.trapz(pdf, x):.3f}") #TensorAUC(x, pdf)
    # Plot
    plt.plot(x, M_AlphaAllX, c='b', ls=':', lw=2,label=r'$M_\nu(y)$')
    plt.plot(x, pdf, c='r',ls='--', lw=1, label=r'$f_\nu(x; \alpha)$')
    
    plt.title(f'M-Wright Function ($\\nu$={v}, $\\alpha$={Alpha}, J={J})')
    plt.xlabel('x')
    plt.ylabel(r'$f_\nu(x; \alpha)$  and  $M_\nu(y)$')
    plt.legend()
    plt.grid(True)
    plt.show()


# %%
"""
# Asymmetric Laplace PDF

The **Asymmetric Laplace Distribution (ALD)** is a continuous distribution extending the classic Laplace by allowing different decay rates on each side of its central location. Here’s the mathematical form:

\\[
X \sim \text{AL}(m, \lambda, \kappa),
\\]  
where:

- \( $m$ \): location parameter  
- \( $\lambda > 0 $\): scale  
- \( $\kappa > 0 $\): asymmetry factor

The **probability density function (PDF)** is:

\\[
f(x \mid m, \lambda, \kappa) =
\frac{\lambda}{\kappa + \frac{1}{\kappa}}
\begin{cases}
\exp\left( -\frac{\lambda}{\kappa}(|x - m|) \right), & x < m \\\\
\exp\left( -\lambda \kappa (|x - m|) \right), & x \ge m
\end{cases}
\\]

When \( $\kappa = 1 $\), this reduces to the symmetric Laplace distribution.

# Inverse Transform Sampling for the Asymmetric Laplace Distribution

### Algorithm:

Define \( p \), the split probability between left and right tails: $ p = \frac{\kappa^2}{1 + \kappa^2} $

\( p \) is a probability value that splits the distribution into two parts (left and right tails)

---

Generate uniform random values: $ u \sim \text{Uniform}(0, 1)$

---

Apply inverse CDF sampling piecewise:

- If $u < p$ → Left tail, solve for $x$ from: $u = p \cdot \exp\left(\lambda \kappa (x - m)\right)$

Rearranged to isolate \( x \): $x = m + \frac{\kappa}{\lambda} \ln\left(\frac{u}{p}\right)$

---
- If $u \ge p$ → Right tail, solve for $x$ from: $u = 1-(1-p)\exp\left(-\frac{\lambda}{\kappa} (x - m)\right)$

Rearranged to isolate \( x \): $x = m - \frac{1}{\lambda \kappa} \ln\left(\frac{1-u}{1-p}\right)$

Kotz, S., Kozubowski, T.J., Podgórski, K. (2001). Asymmetric Laplace Distributions. In: The Laplace Distribution and Generalizations. Birkhäuser, Boston, MA. https://doi.org/10.1007/978-1-4612-0173-1_3

"""

# %%
#***********************************************************
# Define the PDF of the Asymmetric Laplace Distribution
#***********************************************************
def AsymLaplacePDF(x, m, lamda, kappa):
    """
    Args:
        x (array-like): Points to evaluate the PDF.
        m (float): Location parameter (mode).
        lamda (float): Scale parameter (>0).
        kappa (float): Asymmetry parameter (>0).
        
    Returns:
        np.ndarray: PDF values at x.
    """    
    norm_const = lamda / (kappa + 1/kappa)
    pdf = np.where(
        x < m,
        norm_const * np.exp((-lamda / kappa) * np.abs(x - m)), 
        norm_const * np.exp((-lamda * kappa) * np.abs(x - m))
    )
    return pdf

#***********************************************************
# Inverse transform sampling function
#***********************************************************
def SampleAsymLaplace(m, lamda, kappa, size, Seed=None):
    """
    Args:
        m (float): Location parameter (mode).
        lamda (float): Scale parameter (>0).
        kappa (float): Asymmetry parameter (>0).
        size (int): Number of samples to generate.
        Seed (int, optional): Random seed for reproducibility.

    Returns:
        np.ndarray: Samples drawn from the Asymmetric Laplace distribution.
    """    
    if Seed is not None:
        rng = np.random.RandomState(42)  # fixed seed for reproducibility
        u = rng.uniform(0, 1, size)        
    else: u = np.random.uniform(0, 1, size)
        
    p = kappa**2 / (1 + kappa**2)
    samples = np.where(u < p,
                       m + kappa / lamda * np.log(u / p),
                       m - 1 / (lamda * kappa) * np.log((1 - u) / (1 - p)))
    
    return samples
#***********************************************************


# %%
"""
## Test Code to Evaluate Func. AsymLaplacePDF() & SampleAsymLaplace( )
"""

# %%

if DEBUG: 
    # Parameters for the Asymmetric Laplace Distribution
    m = 0.2       # location
    lamda = 2 # scale
    kappa = 2.5 # asymmetry
    N=500
    
    # Generate x values and corresponding PDF values
    x_vals = np.linspace(-10, 10, N)
    pdf_vals = AsymLaplacePDF(x_vals, m, lamda, kappa)

    # Generate the dataset X^
    X_hat = SampleAsymLaplace(m, lamda, kappa, 10000)

    # Plot the distribution
    plt.figure(figsize=(8, 4))
    plt.hist(X_hat, bins=100, density=True, alpha=0.6, label="Sampled Histogram")
    plt.plot(x_vals, pdf_vals, label=f"m={m}, λ={lamda}, κ={kappa}")
    plt.title("Asymmetric Laplace Distribution")
    plt.xlabel("x")
    plt.ylabel("PDF")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    print(f"PDF AUC: {np.trapz(pdf_vals, x_vals):.3f}")#TensorAUC(x_vals, pdf_vals):.3f}")

# %%
"""
## References 

- Cahoy, D. O. (2014). Some Skew-Symmetric Distributions Which Include the Bimodal Ones. Communications in Statistics - Theory and Methods, 44(3), 554–563. https://doi.org/10.1080/03610926.2012.746986

- Mainardi, F., Mura, A., Pagnini, G., & Liu, F. (2010). The M-Wright Function in Time-Fractional Diffusion Processes: A Tutorial Survey. International Journal of Differential Equations, 2010(1), 23–51. https://doi.org/10.1155/2010/104505

- Kotz, S., Kozubowski, T. J., & Podgr̤ski, K. (2001). The Laplace distribution and generalizations : a revisit with applications to communications, economics, engineering, and finance. Birkhũser.

- Punzo, A., & Bagnato, L. (2025). Asymmetric Laplace scale mixtures for the distribution of cryptocurrency returns. Advances in Data Analysis and Classification, 19(2), 275–322. https://doi.org/10.1007/s11634-024-00606-5

- Kozubowski, T. J., & Podgórski, K. (2000). A multivariate and asymmetric generalization of Laplace distribution. Computational Statistics, 15(4). https://doi.org/10.1007/pl00022717

- Devroye, Luc. (1986). Non-uniform random variate generation . In Non-uniform random variate generation. Springer-Verlag.
"""

# %%
