# %%
"""
# Set of Custom Functions for Density Estimations

### Using only TensorFlow and Keras operations

**Author:** S. Sarkar

**Version:** 0.00

**Release:** Aug/2025

---
"""

# %%
"""
## SciPyKDE(X, bandwidth=None, s=None, Points)

This function estimates the probability density function of a 1D dataset using SciPy’s Gaussian KDE with an adaptive bandwidth based on Silverman’s rule. It is build on NumPy and returns the evaluation points alongside the corresponding density values.

## KDE( X,  Bandwidth=None, s=None, Points ):

This function computes the kernel density estimate (KDE) of a 1D dataset using only TensorFlow and Keras operations, with a Gaussian kernel and adaptive bandwidth based on Silverman’s rule. It returns the estimated probability density over specified points efficiently within the TensorFlow graph.

## HDE(S, nBins=None, Epsilon=1e-6):

This function computes a normalized histogram density estimate for 1D data using only TensorFlow and Keras operations. It automatically selects the number of bins using the Freedman-Diaconis rule if not provided. It returns the bin centers, estimated density values, and bin width.




---
"""

# %%
"""
# Import Required Libraries 

**Keras Tenforflow**

**SciPy**: Gaussian KDE Using SciPy API (For validation)

**NumPy**: Python package for N-dimensional arrays (Used For SciPiKDE)

### For Debugging

**Matplotlib**: Python plotting library

"""

# %%
DEBUG = False # Default Set it False
# -----------------------------------------------------------------------------
import tensorflow as tf
import numpy as np
from scipy.stats import gaussian_kde
# -----------------------------------------------------------------------------
if DEBUG: import matplotlib.pyplot as plt


# %%
"""
# Gaussian KDE Using SciPy API

This function computes a kernel density estimate (KDE) of a 1D dataset using the SciPy library’s implementation (scipy.stats.gaussian_kde). It applies Silverman’s rule to select the bandwidth if none is provided, then evaluates the estimated probability density function over a specified number of points spanning the data range. The function returns both the evaluation points and the corresponding density values.

As the SciPy API functions are built on top of NumPy, we utilized NumPy functions when implementing the SciPyKDE() function

Virtanen, P., Gommers, R., Oliphant, T.E. et al. SciPy 1.0: fundamental algorithms for scientific computing in Python. Nat Methods 17, 261–272 (2020). https://doi.org/10.1038/s41592-019-0686-2
"""

# %%
"""
    Computes a 1D kernel density estimate (KDE) using SciPy's gaussian_kde.

    Parameters:
    -----------
    X : array-like : Input data (Population).
    bandwidth : str, scalar or callable, optional : Bandwidth for KDE. 
    If None: Using deafult Scott/Approx Silverman/Silverman.
    
    s: array-like :  Query Points (Default None).
    Points : int : Number of points where the KDE is evaluated between min and max of X.

    Returns:
    --------
    s : ndarray : Points where the KDE is evaluated.
    pdf : ndarray : Estimated density values at points x.
    
Note: 
If s is None using Points to estimate s using linspace 
If Scott is true it'll use Scott (1st pref)
"""
def SciPyKDE(X, bandwidth=None, s=None, Points=500, Scott=True, ApproxSilverman=True):
    X = np.ravel(X).astype(np.float32)
    N = X.size

    # Bandwidth selection (Silverman's /Scotts rule if None)
    # Approx Silverman - Assuming StdDev < IQR/1.34
    # BW: ‘scott’, ‘silverman’ # Using Computed Silverman
    if bandwidth is None:
        if Scott: bandwidth='scott'
        else:
            # Using Degree of Freedom = 0 as assuming X is the entire population
            #h = 1.06 min ( s , IQR / 1.34 ) n^(− 1 / 5)
            # Assuming X is the entire population (ddof=0)
            StdDev = np.std(X)  # Population standard deviation
            if ApproxSilverman: bandwidth = 1.06 * StdDev * N**(-1/5) 
            else:
                q75, q25 = np.percentile(X, [75 ,25])
                iqr = q75 - q25; IQRFactor=iqr/1.34
                # print(f"IQR:{iqr:.3f} IQR/1.34={IQRFactor:.3f}")
                bandwidth = 1.06 * min(StdDev,IQRFactor) * N**(-1/5)        

    if s is None:
        # Evaluate KDE at Points between min and max of data
        xMin, xMax = np.min(X), np.max(X)
        s = np.linspace(xMin, xMax, Points)

    # Use scipy KDE with bandwidth using Silverman's rule
    kde = gaussian_kde(X, bw_method=bandwidth)
    pdf = kde.evaluate(s)
    return s, pdf


# %%
"""
## For Evaluation / Debugging Purpose - SpiPyKDE Function
"""

# %%
#*************************************************************
# Test Code
#*************************************************************
if DEBUG:
    X_np = np.random.normal(loc=1.0, scale=1.5, size=10000)
    # Run KDE
    x_vals, pdf_vals = SciPyKDE(X_np, s=X_np[:1000])
    print(f'X_np: {X_np.shape} x_vals: {x_vals.shape} pdf: {pdf_vals.shape}')

# %%
#*************************************************************
# Test Code
#*************************************************************
if DEBUG:
    def pSciPyKDE(X, bandwidth=None, Points=500, Scott=True, ApproxSilverman=True, Print=True):
        # Flatten and cast to float32
        X = np.ravel(X).astype(np.float32)
        if Print: print(f"1: X shape = {X.shape}")

        N = X.size
        if Print: print(f"2: N (number of samples) = {N}")

        if bandwidth is None:
            if Scott: Bandwidth='scott'
            else:
                # Using Degree of Freedom = 0 as assuming X is the entire population
                #h = 1.06 min ( s , IQR / 1.34 ) n^(− 1 / 5)
                # Assuming X is the entire population (ddof=0)
                StdDev = np.std(X)  # Population standard deviation
                if Print: print(f"3: StdDev = {StdDev}")
                if ApproxSilverman: bandwidth = 1.06 * StdDev * N**(-1/5) 
                else:
                    q75, q25 = np.percentile(X, [75 ,25])
                    iqr = q75 - q25; IQRFactor=iqr/1.34
                    if Print: print(f"3A: IQR:{iqr:.3f} IQR/1.34={IQRFactor:.3f}")
                    Bandwidth = 1.06 * min(StdDev,IQRFactor) * N**(-1/5) 
        else:
            Bandwidth = bandwidth
        if Print: print(f"4: Using provided Bandwidth = {Bandwidth}")

        # Evaluate KDE at evenly spaced points between min and max of data
        xMin, xMax = np.min(X), np.max(X)
        if Print: 
            print(f"5: xMin = {xMin}")
            print(f"6: xMax = {xMax}")

        x = np.linspace(xMin, xMax, Points)
        if Print: print(f"7: x shape = {x.shape}")

        # Use SciPy gaussian_kde
        kde = gaussian_kde(X, bw_method=Bandwidth)
        pdf = kde.evaluate(x)
        if Print: print(f"8: pdf shape = {pdf.shape}")

        return x, pdf
    #=====================================================================
    X_np = np.random.normal(loc=1.0, scale=1.5, size=10000)
    x_np, pdf_np = pSciPyKDE(X_np, Points=1000, Print=True)
    #----------------------------------
    # Plot
    plt.figure(figsize=(8,5))
    plt.plot(x_np, pdf_np, lw=1, c='r', label='SciPyKDE')
    #plt.plot(x, pdfSciPy, lw=1, ls='--', c='r', label='SciPy-KDE')
    plt.hist(X_np, bins=500, density=True, alpha=0.4, color='gray', lw=0.5, label='Histogram')

    plt.title('Kernel Density Estimation (SciPy-KDE)')
    plt.xlabel('x')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

# %%
"""
# Kernel Density Estimation (KDE) – Gaussian Kernel

Estimate a continuous probability density function (PDF) from a set of samples: $X = \{x_1, x_2, \dots, x_n\}$

### Kernel Density Estimate

The estimated PDF at a point $x$ using kernel density estimation is:

$\hat{f}(x) = \frac{1}{n h} \sum_{i=1}^{n} K\left( \frac{x - x_i}{h} \right)$

Where:
- $n$: Number of samples  
- $h$: Bandwidth (smoothing parameter)  
- $K(u)$: Kernel function (we use Gaussian)

---

### Gaussian Kernel

The Gaussian kernel is defined as:

$K(u) = \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{u^2}{2} \right)$

Substituting into the KDE formula:

$\hat{f}(x) = \frac{1}{n h \sqrt{2\pi}} \sum_{i=1}^{n} \exp\left( -\frac{(x - x_i)^2}{2 h^2} \right)$

---

### Bandwidth Estimation

If the bandwidth $h$ is not provided, we estimate it using **Silverman's rule of thumb**:

$h = 1.06 \cdot \hat{\sigma} \cdot n^{-1/5}$

Where $\hat{\sigma}$ is the standard deviation of the data.

---

### Evaluation Grid

To compute the estimated PDF on a grid:

$z_j \in [\min(X), \max(X)]$, for $j = 1, 2, \dots, M$

with $M$ being the number of points (typically $M = 500$).

---

### Final Estimation on Grid

At each grid point $z_j$, the KDE becomes:

$\hat{f}(z_j) = \frac{1}{n h \sqrt{2\pi}} \sum_{i=1}^{n} \exp\left( -\frac{(z_j - x_i)^2}{2 h^2} \right)$

---

## **Memory Breakdown** for `KDE` Function


| Tensor     | Shape  | Count |
| ---------- | ------ | ----- |
| `X_expand` | (N, 1) | N     |
| `x_expand` | (1, M) | M     |
| `diffSq`   | (N, M) | N×M   |
| `Exp`      | (N, M) | N×M   |
| `kernels`  | (N, M) | N×M   |
| `pdf`      | (M,)   | M     |


#### Total Memory (Worst Case)

$ \text{Total bytes} \approx 12 N M + 4 N + 8 M $

---

#### In Mega Bytes (MB) / Kilo Bytes (KB)

$ \text{Total MB} \approx \frac{12 N M + 4 N + 8 M}{1024^2} $

$\text{Total KB} \approx \frac{12 N M + 4 N + 8 M}{1024} $


Here, 

- $4$: Bytes per `float32`  
- $N$: Number of samples  
- $M$: Number of grid points


"""

# %%
# -----------------------------------------------------------------------------
# KDE: Kernel Density Estimation using Gaussian kernels (with TensorFlow)
#
# This function estimates the probability density function (PDF) of a 1D input
# tensor `X` using Gaussian Kernel Density Estimation (KDE).
# 
# - Bandwidth selection: If not provided, it uses Silverman's rule of thumb.
# - Points: Number of grid points to evaluate the PDF over [min(X), max(X)].
# - Computes pairwise differences and evaluates Gaussian kernel at each point.
# - Uses @tf.function to compile and optimize the computation graph, with
#   reduce_retracing=True to avoid retracing when input shapes remain constant.
#
# -----------
# Parameters:
# -----------
#    X : array-like : Input data (Population).
#    bandwidth : float, optional : Bandwidth for KDE.  If None: Using deafult Scott/Approx Silverman/Silverman.
#    s: array-like :  Query Points (Default None).
#    Points : int : Number of points where the KDE is evaluated between min and max of X.
# -----------
# Returns:
# -----------
#   s    : The evaluation grid (linspace from min to max of X).
#   pdf  : The estimated probability density function over x.
#
# -----------
# Note: If s is None using Points to estimate x using linspace
# -----------
#
# -----------------------------------------------------------------------------
# Fewer retracings, thus better runtime as input varies
@tf.function(reduce_retracing=True)
# -----------------------------------------------------------------------------
def KDE(X, Bandwidth=None, s=None, Points=500, Scott=True, ApproxSilverman=True):
    # ----------------------------------------------
    Pi = tf.acos(tf.constant(-1.0, dtype=tf.float32))
    # ----------------------------------------------
    # Reshapes X into a 1D tensor with shape (N,) and Get N
    X = tf.cast(tf.reshape(X, [-1]), tf.float32) 
    N = tf.cast(tf.shape(X)[0], tf.float32)
    # ----------------------------------------------
    
    # Bandwidth selection (Silverman's Scott's rule if None)
    if Bandwidth is None:
        # Using Degree of Freedom = 0 as assuming X is the entire population
        # Assuming X is the entire population (ddof=0)
        # h = 1.06 min ( s , IQR / 1.34 ) n − 1 / 5
        # Approx Silverman - Assuming StdDev < IQR/1.34
        # Equation 6.42. @Multivariate Density Estimation: Theory, Practice, and Visualization (1992)
        # Scott's Rule:  s*n^(− 1 / [d+1]) -> d=1 ->  s*n^(− 0.2)
        
        StdDev = tf.math.reduce_std(X)
        
        if Scott: Bandwidth = StdDev * tf.pow(N, -0.2)        
        else:  
            if ApproxSilverman: Bandwidth = 1.06* StdDev * tf.pow(N, -0.2) 
            else:
                # Sort values for quantile computation
                X_sorted = tf.sort(X)
                # Indices for 25th and 75th percentiles
                idx_q25 = tf.cast(tf.floor(0.25 * (N - 1)), tf.int32)
                idx_q75 = tf.cast(tf.floor(0.75 * (N - 1)), tf.int32)
                q25 = X_sorted[idx_q25]
                q75 = X_sorted[idx_q75]
                # Interquartile range (IQR)
                iqr = q75 - q25
                IQRFactor = iqr / 1.34
                # Bandwidth rule-of-thumb 
                Bandwidth = 1.06 * tf.minimum(StdDev, IQRFactor) * tf.pow(N, -0.2)

    # ----------------------------------------------
    # s is a 1D tensor of shape (M,) — Query points
    if s is None: # Using Points to estimate x using linspace
        xMin, xMax = tf.reduce_min(X), tf.reduce_max(X)
        S = tf.linspace(xMin, xMax, Points)
    else: S = tf.cast(tf.identity(s), tf.float32)
    # ----------------------------------------------
    # Pairwise differences, normalized by bandwidth
    X_Expand = tf.expand_dims(X, axis=1) # shape: (N, 1)
    S_Expand = tf.expand_dims(S, axis=0) # shape: (1, M)
    difSq = tf.square((S_Expand - X_Expand) / Bandwidth) # shape: (N, M)
    # ----------------------------------------------
    Exp=tf.exp(-0.5 * difSq) # shape: (N, M)
    Kernels = Exp / (Bandwidth * tf.sqrt(2.0 * Pi)) # shape: (N, M)
    pdf = tf.reduce_mean(Kernels, axis=0) # shape: (M)
    # ----------------------------------------------
    return S, pdf

# %%
"""
## For Evaluation / Debugging Purpose - KDE Function
"""

# %%
#*************************************************************
# Test Code
#*************************************************************
if DEBUG:
    X_np = np.random.normal(loc=1.0, scale=1.5, size=10000)
    # Convert to Tensor
    X_tf = tf.constant(X_np, dtype=tf.float32)
    # Run KDE
    x_vals, pdf_vals = KDE(X_tf, s=X_tf[:1000].numpy())
    print(f'X_np: {X_np.shape} X_tf: {X_tf.shape}')
    print(f'x_vals: {x_vals.shape} pdf: {pdf_vals.shape}')

# %%
#*************************************************************
# Test Code
#*************************************************************
if DEBUG:
    @tf.function#(reduce_retracing=True)
    def pKDE(X, Bandwidth=None, Points=500, Scott= True, ApproxSilverman=True, Print=True):
        # ----------------------------------------------
        if Print:
            def tfprint(name, value):
                if isinstance(value, tf.Tensor):
                    if value.shape.rank == 0:  # scalar tensor
                        tf.print(f"{name}: scalar =", value)
                    else:
                        tf.print(f"{name}: shape =", tf.shape(value))
                else:
                    print(f"{name}: value =", value)
        # ----------------------------------------------
        Pi = tf.acos(tf.constant(-1.0, dtype=tf.float32)); 
        if Print: tfprint("Pi", Pi)    
        # ----------------------------------------------    
        # Reshapes X into a 1D tensor with shape (N,) and Get N
        X = tf.cast(tf.reshape(X, [-1]), tf.float32); 
        if Print: tfprint("X", X) 
        N = tf.cast(tf.shape(X)[0], tf.float32); 
        if Print: tfprint("N", N)
        # ----------------------------------------------
        # Bandwidth selection (Silverman's Scott's rule if None)
        if Bandwidth is None:
            # Using Degree of Freedom = 0 as assuming X is the entire population
            # Assuming X is the entire population (ddof=0)
            # h = 1.06 min ( s , IQR / 1.34 ) n − 1 / 5
            # Approx Silverman - Assuming StdDev < IQR/1.34
            # Equation 6.42. @Multivariate Density Estimation: Theory, Practice, and Visualization (1992)
            # Scott's Rule:  s*n^(− 1 / [d+1]) -> d=1 ->  s*n^(− 0.2)

            StdDev = tf.math.reduce_std(X)
            if Print: tf.print("StdDev = ",StdDev)
            if Scott: 
                tf.print("BW Type: Scott")
                Bandwidth = StdDev * tf.pow(N, -0.2)        
            else:  
                if ApproxSilverman: 
                    tf.print("BW Type: ApproxSilverman")
                    Bandwidth = 1.06* StdDev * tf.pow(N, -0.2) 
                else:
                    tf.print("BW Type: ApproxSilverman")
                    # Sort values for quantile computation
                    X_sorted = tf.sort(X)
                    # Indices for 25th and 75th percentiles
                    idx_q25 = tf.cast(tf.floor(0.25 * (N - 1)), tf.int32)
                    idx_q75 = tf.cast(tf.floor(0.75 * (N - 1)), tf.int32)
                    q25 = X_sorted[idx_q25]
                    q75 = X_sorted[idx_q75]
                    # Interquartile range (IQR)
                    iqr = q75 - q25
                    IQRFactor = iqr / 1.34
                    if Print: tf.print("IQR: ",iqr," IQR/1.34= " ,IQRFactor)
                    # Bandwidth rule-of-thumb 
                    Bandwidth = 1.06 * tf.minimum(StdDev, IQRFactor) * tf.pow(N, -0.2)
        else: tf.print("BW Type: Scalar")
        # ----------------------------------------------
        if Print: tfprint("Bandwidth", Bandwidth)
        # ----------------------------------------------
        # x is a 1D tensor of shape (M,) — Query points
        xMin, xMax = tf.reduce_min(X), tf.reduce_max(X) 
        if Print: 
            tfprint("xMin", xMin); 
            tfprint("xMax", xMax)

        x = tf.linspace(xMin, xMax, Points); 
        if Print: tfprint("x", x)
        # ----------------------------------------------
        # Pairwise differences, normalized by bandwidth
        X_Expand = tf.expand_dims(X, axis=1); 
        if Print: tfprint("X_Expand", X_Expand)           # shape: (N, 1)
        x_Expand = tf.expand_dims(x, axis=0); 
        if Print: tfprint("x_Expand", x_Expand)           # shape: (1, M)
        difSq = tf.square((x_Expand - X_Expand) / Bandwidth); 
        if Print: tfprint("difSq", difSq)                 # shape: (N, M)
        # ----------------------------------------------
        Exp=tf.exp(-0.5 * difSq); 
        if Print: tfprint("Exp", Exp)                     # shape: (N, M)
        Kernels = Exp / (Bandwidth * tf.sqrt(2.0 * Pi)); 
        if Print: tfprint("Kernels", Kernels)             # shape: (N, M)
        pdf = tf.reduce_mean(Kernels, axis=0); 
        if Print:  tfprint("pdf", pdf)                    # shape: (M)
        # ----------------------------------------------
        return x, pdf

    #=====================================================================
    X_np = np.random.normal(loc=1.0, scale=1.5, size=10000)
    # Convert to Tensor
    X_tf = tf.constant(X_np, dtype=tf.float32)
    # Run KDE
    x_vals, pdf_vals = pKDE(X_tf, Points=1000, Print=True)
    # Convert output tensors to numpy for plotting
    x_np = x_vals.numpy()
    pdf_np = pdf_vals.numpy()
    #----------------------------------
    # Use scipy KDE with bandwidth using Silverman's rule
    # Bandwidth selection (Silverman's rule if None)
    x, pdfSciPy = SciPyKDE(X_np, bandwidth=None, Points=500)
    #----------------------------------
    # Plot
    plt.figure(figsize=(8,5))
    plt.plot(x_np, pdf_np, lw=3, c='yellow', label='KDE')
    plt.plot(x, pdfSciPy, lw=1, ls='--', c='r', label='SciPy-KDE')
    plt.hist(X_np, bins=500, density=True, alpha=0.4, color='gray', lw=0.5, label='Histogram')

    plt.title('Kernel Density Estimation (KDE)')
    plt.xlabel('x')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

# %%
"""
# Histogram Density Estimation (HDE)

Given a sample set 
$ S = \{ s_1, s_2, \ldots, s_n \} $, we want to estimate the probability density function (PDF) by computing a histogram with bins determined by the Freedman-Diaconis rule.

### Number of bins ($ n_{\text{bins}} $)

if not provided use the Freedman-Diaconis rule, to calculate the optimal number of bins $ n_{\text{bins}} $ based on the sample size and variability in data.

### Bin edges

Define the bin edges as equally spaced points between the minimum and maximum sample values:

$$
\text{edges} = \{ e_0, e_1, \ldots, e_{n_{\text{bins}}} \}, \quad e_0 = \min(S), \quad e_{n_{\text{bins}}} = \max(S)
$$

where

$$
e_i = \min(S) + i \cdot \Delta, \quad \Delta = \frac{\max(S) - \min(S)}{n_{\text{bins}}}
$$

### Histogram counts

For each bin $ i = 1, 2, \ldots, n_{\text{bins}} $, count the number of samples falling into the bin interval $ [e_{i-1}, e_i) $:

$$
c_i = \text{number of samples } s_j \text{ such that } e_{i-1} \leq s_j < e_i
$$

The total number of samples is:

$$
N = \sum_{i=1}^{n_{\text{bins}}} c_i = n
$$

### Bin width

The bin width is:

$$
h = \frac{\max(S) - \min(S)}{n_{\text{bins}}}
$$

### Density estimation

The histogram-based density estimate at bin $ i $ is: $\hat{f}(x_i) = \frac{c_i}{N \cdot h}$

where $ x_i $ is the bin center: $x_i = \frac{e_{i-1} + e_i}{2}$

### Gaussian Filtering for Smoothing

Applied **Gaussian filtering** on the raw histogram density estimate $\hat{f}(x)$ to produce a smoother estimate.

#### Gaussian kernel

Utilized a 1D Normalized Gaussian kernel of size $m$ and Smoothing Parameter $h$ is

$$
g_k = \frac{\exp\left(-\frac{1}{2} \left(\frac{k}{h}\right)^2\right)}{\sum_{j=-\lfloor m/2 \rfloor}^{\lfloor m/2 \rfloor} \exp\left(-\frac{1}{2} \left(\frac{j}{h}\right)^2\right)},  
\quad k \in \left[-\lfloor m/2 \rfloor, \ldots, \lfloor m/2 \rfloor\right]
$$

Here, 

- $\sum_k g_k = 1$ 
- $\text{Kernel size}\ (m)\ = \max\left(f_{\text{min}},\; \left\lfloor 6\sigma \right\rfloor \;\right)$ 
- $f_{\text{min}}\ = 5\ (\text{default})$ 
- $\text{Smoothing Parameter}\ (h) = 2.5 (\text{default})$ 


#### Convolution

The smoothed density is obtained via

$$
\tilde{f}(x_i) = \sum_{k=-\lfloor m/2 \rfloor}^{\lfloor m/2 \rfloor} g_k \cdot \hat{f}(x_{i-k})
$$


---

### Freedman–Diaconis Rule for Histogram Binning

The **Freedman–Diaconis rule** is a robust, data-driven method to determine the optimal bin width for a histogram that approximates the **probability density function (PDF)** of a continuous variable.

**The Freedman–Diaconis rule is:** $h = 2 \cdot \frac{\text{IQR}}{n^{1/3}}$

Here,

- $n$: number of samples  
- $Q_1$: 25th percentile (first quartile)  
- $Q_3$: 75th percentile (third quartile)  
- $\text{IQR} = Q_3 - Q_1$: interquartile range (IQR)  
- $h$: optimal bin width  


#### Number of Bins

Let $\text{Range} = \max(X) - \min(X)$, then the number of bins $k$ is:

$$
k = \left\lceil \frac{\text{Range}}{h} \right\rceil 
= \left\lceil \frac{\max(X) - \min(X)}{2 \cdot \text{IQR} / n^{1/3}} \right\rceil
$$


#### Reference

Freedman, David, and Persi Diaconis. "On the Histogram as a Density Estimator: L2 Theory." Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete, vol. 57, no. 4, 1981, pp. 453–476.

---

## **Memory Breakdown** for `HDE` Function

| **Tensor** |  **Shape** |**Count**|     **Description**    |
|:----------:|:----------:|:-------:|:----------------------:|
| S          | ( N, )     | $N$     | Input vector           |
| X\_sorted  | ( N, )     | $N$     | Sorted values          |
| edges      | ( M+1, )   | $M{+}1$ | Bin edges              |
| counts     | ( M, )     | $M$     | Bin counts (int)       |
| centers    | ( M, )     | $M$     | Bin centers            |
| density    | ( M, )     | $M$     | Normalized density     |
| x          | ( 1, M, 1 )| $M$     | Reshaped density       |
| kernel     | ( S, 1, 1 )| $S$     | Gaussian Kernel (S<<M) |
| xFiltered  | ( 1, M, 1 )| $M$     | Filtered Output        |
| pdf        | ( M, )     | $M$     | Probabilty density     |


#### Total Memory ( Estimation )

$ \text{Total bytes} \approx 4 \cdot (2N + 7M) $

Ignored $S\ ( Kernel\ size)$ and and approximated $M+1\approx M$

---

#### In Mega Bytes (MB) / Kilo Bytes (KB)

$ \text{Total MB} \approx \frac{4 \cdot (2N + 7M)}{1024^2} $

$\text{Total KB} \approx \frac{4 \cdot (2N + 7M)}{1024} $


Here, 

- $4$: Bytes per `float32`  
- $N$: Number of samples  
- $M$: Number of grid points

"""

# %%
#----------------------------------------------------
# Function: Freedman-Diaconis Rule for Bins
#----------------------------------------------------
# Fewer retracings, thus better runtime as input varies
@tf.function(reduce_retracing=True)
def BinsFreedmanDiaconisRule(X):
    n = tf.cast(tf.size(X), tf.float32)  # Scalar

    X_sorted = tf.sort(X)  # Shape: (N,), sorted samples

    idx_25 = tf.cast(tf.round(0.25 * (n - 1)), tf.int32)  # Scalar index
    idx_75 = tf.cast(tf.round(0.75 * (n - 1)), tf.int32)  # Scalar index

    q25 = X_sorted[idx_25]  # Scalar (25th percentile)
    q75 = X_sorted[idx_75]  # Scalar (75th percentile)

    iqr = q75 - q25  # Scalar (interquartile range)
    bin_width = 2.0 * iqr / tf.pow(n, 1.0 / 3.0)  # Scalar (bin width)
    if bin_width == 0: bin_width = 1e-12 # Fail safe
    range_X = tf.reduce_max(X) - tf.reduce_min(X)  # Scalar (range)

    bins = tf.math.ceil(range_X / bin_width) # Scalar (number of bins)

    return tf.cast(bins, tf.int32)  # Scalar (int)

#--------------------------------------------------------
# Gaussian Kernel For Gaussian Filtering 
#--------------------------------------------------------
@tf.function(reduce_retracing=True)
def GaussianKernel(size, Sigma=2.5):
    x = tf.range(-size // 2 + 1, size // 2 + 1, dtype=tf.float32)
    kernel = tf.exp(-0.5 * (x / Sigma) ** 2)
    kernel /= tf.reduce_sum(kernel)
    return tf.reshape(kernel, [size, 1, 1])  # [filter_width, in_channels, out_channels]
#--------------------------------------------------------
# Gaussian Filter to Smooth the Histogram Density Estimation
#--------------------------------------------------------
@tf.function(reduce_retracing=True)
def GaussianFilter(x, fSizeMin=5, Sigma=2.5):
    Stddev = tf.math.reduce_std(x)               # sample stddev 
    val = 6.0 * Stddev                           # tensor multiplication
    val_int = tf.cast(tf.floor(val), tf.int32)   # floor and cast to int tensor
    val_odd = val_int | 1                        # bitwise OR to make it odd
    Size = tf.maximum(fSizeMin, val_odd)         # ensure minimum size fSizeMin

    x = tf.reshape(x, [1, -1, 1])
    kernel = GaussianKernel(Size, Sigma)
    xFiltered = tf.nn.conv1d(x, kernel, stride=1, padding='SAME')
    return tf.squeeze(xFiltered)    


# %%
# Fewer retracings, thus better runtime as input varies
@tf.function(reduce_retracing=True)
# -----------------------------------------------------------------------------
def HDE(S, nBins=None, Epsilon=1e-12, fSizeMin=5, fSigma=2.5):
    S = tf.cast(tf.reshape(S, [-1]), tf.float32)  # Shape: (N,), flatten input samples
    #--------------------------------------------------------
    # Compute No of Bins Freedman-Diaconis Rule If nBins=None Else use provided nBins as-is
    #-------------------------------------------------------- 
    if nBins is None: nBins = BinsFreedmanDiaconisRule(S)  # Scalar (number of bins)
        
    #--------------------------------------------------------
    # Compute histogram
    #--------------------------------------------------------
    nBins = tf.maximum(nBins, 1)  # Ensure at least 1 bin, scalar
    
    min_S = tf.reduce_min(S)  # Scalar (minimum value)
    max_S = tf.reduce_max(S)  # Scalar (maximum value)
    
    edges = tf.linspace(min_S, max_S, nBins + 1)  # Shape: (nBins+1,), bin edges
    
    counts = tf.histogram_fixed_width(S, [min_S, max_S], nbins=nBins) # Shape: (nBins,), count of samples/bin
    
    bin_width = (max_S - min_S) / tf.cast(nBins, tf.float32)  # Scalar (width of each bin)
    
    total = tf.reduce_sum(counts)  # Scalar (total number of samples)
    
    density = tf.cast(counts, tf.float32) / (tf.cast(total, tf.float32) * bin_width) # Shape: (nBins,), normalized density per bin
    pdf=GaussianFilter(density, fSizeMin, fSigma)
    centers = (edges[:-1] + edges[1:]) / 2.0  # Shape: (nBins,), bin centers
    return centers, pdf, float(bin_width)

# %%
"""
## For Evaluation / Debugging Purpose - HDE Function
"""

# %%
#*************************************************************
# Test Code
#*************************************************************
if DEBUG:
    @tf.function#(reduce_retracing=True)
    def pHDE(S, nBins=None, Epsilon=1e-12, fSizeMin=5, fSigma=2.5, Print=True):
        #--------------------------------------------------------
        # Function to print Tensor
        #--------------------------------------------------------       
        def tfprint(name, value):
            if isinstance(value, tf.Tensor):
                if value.shape.rank == 0:  # scalar tensor
                    tf.print(f"{name}: scalar =", value)
                else:
                    tf.print(f"{name}: shape =", tf.shape(value))
            else:
                print(f"{name}: value =", value)
        
        #--------------------------------------------------------
        S = tf.cast(tf.reshape(S, [-1]), tf.float32)  # Shape: (N,), flatten input samples
        if Print: tfprint("S", S)
        #--------------------------------------------------------
        # Compute No of Bins Freedman-Diaconis Rule If nBins=None Else use provided nBins as-is
        #-------------------------------------------------------- 
        if nBins is None: 
            #----------------------------------------------------
            # Inner Function: Freedman-Diaconis Rule for Bins
            #----------------------------------------------------
            def BinsFreedmanDiaconisRule(X):
                n = tf.cast(tf.size(X), tf.float32)  # Scalar
                if Print: tfprint("n (sample size)", n)

                X_sorted = tf.sort(X)  # Shape: (N,), sorted samples
                if Print: tfprint("X_sorted", X_sorted)

                idx_25 = tf.cast(tf.round(0.25 * (n - 1)), tf.int32)  # Scalar index
                idx_75 = tf.cast(tf.round(0.75 * (n - 1)), tf.int32)  # Scalar index
                if Print: tfprint("idx_25", idx_25)
                if Print: tfprint("idx_75", idx_75)

                q25 = X_sorted[idx_25]  # Scalar (25th percentile)
                q75 = X_sorted[idx_75]  # Scalar (75th percentile)
                if Print: tfprint("q25", q25)
                if Print: tfprint("q75", q75)

                iqr = q75 - q25  # Scalar (interquartile range)
                if Print: tfprint("iqr", iqr)

                bin_width = 2.0 * iqr / tf.pow(n, 1.0 / 3.0)  # Scalar (bin width)
                if tf.equal(bin_width, 0.0):
                    bin_width = Epsilon  # Fail safe
                if Print: tfprint("bin_width", bin_width)

                range_X = tf.reduce_max(X) - tf.reduce_min(X)  # Scalar (range)
                if Print: tfprint("range_X", range_X)

                bins = tf.math.ceil(range_X / bin_width)  # Scalar (number of bins)
                if Print: tfprint("bins (nBins)", bins)

                return tf.cast(bins, tf.int32)  # Scalar (int)
            #----------------------------------------------------
            nBins = BinsFreedmanDiaconisRule(S)  # Scalar (number of bins)
        #--------------------------------------------------------
        nBins = tf.maximum(nBins, 1)  # Ensure at least 1 bin, scalar   
        if Print: tfprint("nBins final", nBins)        
        #--------------------------------------------------------
        # Gaussian Kernel For Gaussian Filtering 
        #--------------------------------------------------------
        def GaussianKernel(size, Sigma=fSigma):
            x = tf.range(-size // 2 + 1, size // 2 + 1, dtype=tf.float32)
            if Print: tfprint("GaussianKernel - x", x) 
            kernel = tf.exp(-0.5 * (x / Sigma) ** 2)
            kernel /= tf.reduce_sum(kernel)
            if Print: tfprint("GaussianKernel - kernel", kernel) 
            return tf.reshape(kernel, [size, 1, 1])  # [filter_width, in_channels, out_channels]
        #--------------------------------------------------------
        # Gaussian Filter to Smooth the Histogram Density Estimation
        #--------------------------------------------------------
        def GaussianFilter(x, Sigma=fSigma):
            Stddev = tf.math.reduce_std(x)               # sample stddev 
            if Print: tfprint("GaussianFilter - Stddev", Stddev)
            val = 6.0 * Stddev                           # tensor multiplication
            val_int = tf.cast(tf.floor(val), tf.int32)   # floor and cast to int tensor
            val_odd = val_int | 1                        # bitwise OR to make it odd
            if Print: tf.print("val:", val, " val_int:", val_int, " val_odd:", val_odd)
            Size = tf.maximum(fSizeMin, val_odd)         # ensure minimum size fSizeMin
            if Print: tf.print("GaussianFilter - Size", Size) 
            x = tf.reshape(x, [1, -1, 1])
            if Print: tfprint("GaussianFilter - x", x) 
            kernel = GaussianKernel(Size, Sigma)
            if Print: tfprint("GaussianFilter - kernel", kernel) 
            xFiltered = tf.nn.conv1d(x, kernel, stride=1, padding='SAME')
            if Print: tfprint("GaussianFilter - xFiltered", xFiltered) 
            return tf.squeeze(xFiltered)    
        #--------------------------------------------------------
        # Compute histogram
        #--------------------------------------------------------        
        min_S = tf.reduce_min(S)  # Scalar (minimum value)
        max_S = tf.reduce_max(S)  # Scalar (maximum value)
        if Print:
            tfprint("min_S", min_S)
            tfprint("max_S", max_S)

        edges = tf.linspace(min_S, max_S, nBins + 1)  # Shape: (nBins+1,), bin edges
        if Print: tfprint("edges", edges)

        counts = tf.histogram_fixed_width(S, [min_S, max_S], nbins=nBins)  # Shape: (nBins,), count of samples/bin
        if Print: tfprint("counts", counts)

        bin_width = (max_S - min_S) / tf.cast(nBins, tf.float32)  # Scalar (width of each bin)
        if Print: tfprint("bin_width", bin_width)

        total = tf.reduce_sum(counts)  # Scalar (total number of samples)
        if Print: tfprint("total", total)

        density = tf.cast(counts, tf.float32) / (tf.cast(total, tf.float32) * bin_width)  # Shape: (nBins,), normalized density per bin
        if Print: tfprint("density", density)
            
        pdf=GaussianFilter(density)
        if Print: tfprint("pdf", pdf)
        
        centers = (edges[:-1] + edges[1:]) / 2.0  # Shape: (nBins,), bin centers
        if Print: tfprint("centers", centers)

        return centers, pdf, float(bin_width)

    #=====================================================================
    X_np = np.random.normal(loc=1.0, scale=1.5, size=10000)
    # Convert to Tensor
    X_tf = tf.constant(X_np, dtype=tf.float32)
    # Run histogram density estimation with print enabled
    x_vals, pdf_vals, bin_width = pHDE(X_tf, Print=True)    
    # Convert output tensors to numpy for plotting
    x_np = x_vals.numpy()
    pdf_np = pdf_vals.numpy()
    #----------------------------------
    # Use scipy KDE with bandwidth using Silverman's rule
    # Bandwidth selection (Silverman's rule if None)
    x, pdfSciPy = SciPyKDE(X_np, bandwidth=None, Points=500)
    #----------------------------------
    # Plot
    plt.figure(figsize=(8,5))
    plt.plot(x_np, pdf_np, lw=3, c='yellow', label='HDE')
    plt.plot(x, pdfSciPy, lw=1, ls='--', c='r', label='SciPy-KDE')
    plt.hist(X_np, bins=500, density=True, alpha=0.4, color='gray', lw=0.5, label='Histogram')

    plt.title('Density Estimation Using HDE')
    plt.xlabel('x')
    plt.ylabel('Density')
    plt.legend()
    plt.show()


# %%
