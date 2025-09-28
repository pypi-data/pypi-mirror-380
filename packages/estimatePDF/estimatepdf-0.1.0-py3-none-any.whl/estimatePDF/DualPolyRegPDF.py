# %%
"""
# Set of Custom Functions for Generating DualPolyRegPDF()

**DualPolyRegPDF**: Dual Polynomial Regression Probabilty Desity Function

### Using only TensorFlow and Keras operations

**Author:** S. Sarkar

**Version:** 0.00

**Release:** Aug/2025

---
"""

# %%
"""
$$
\begin{aligned}
\textbf{RetFunc}\ (\\
                &x,                   &&\text{# Input tensor (W),(B, W) or (B, C, W)}\\
                &\text{Order},        &&\text{# Polynomial order (integer)}\\
                &\text{xMid},         &&\text{# Boundary point separating left and right intervals}\\
                &\text{CoefLeft},     &&\text{# Polynomial coefficients for left interval - compatible with Order}\\
                &\text{CoefRight},    &&\text{# Polynomial coefficients for Right interval - compatible with Order}\\
                &\text{xMin},         &&\text{# Minimum bound value for input x}\\
                &\text{xMax},         &&\text{# Maximum bound value for input x}\\
                &\text{MinProb}=1e{-}12, &&\text{# Minimum Clipping bound value for output probabilities}\\
                &\text{MaxProb}=1,    &&\text{# Maximum Clipping bound value for output probabilities}\\
                &\text{Auc}=1         &&\text{# Normalization constant (Integration PDF - Population)}\\
               )
\end{aligned}
$$

This function maps input tensor `x` to a probability tensor using dual piecewise polynomial functions defined over [xMin, xMid] and [xMid, xMax], with coefficients `CoefLeft` and `CoefRight`, respectively.

---


"""

# %%
"""
$$
\begin{aligned}
\textbf{Get_xTreshold}\ (\\
                            &x,                     &&\text{# 1D input array of x-values}\\
                            &y,                     &&\text{# 1D input array of y-values}\\
                            &xEdge                  &&\text{# x Coordinate @ Edge}\\
                            &\text{ThFactor}=0.005, &&\text{# Scaling factor for gradient threshold}\\
                            &\text{Up=False}        &&\text{# If True: Upward Slope | Else: Downward Slope}\\
                        ):
\end{aligned}
$$

Detects the x-value where the slope of y vs. x changes rapidly, checking the first half for upward changes 
and the second half for downward changes based on a gradient threshold scaled by ThFactor.

"""

# %%
"""
$$
\begin{aligned}
\textbf{DualPolyRegPDF}\ (\\
                  &\text{Superset},       &&\text{# Input tensor (Dataset)}\\
                  &\text{Points},         &&\text{# Number of evaluation points for KDE/HDE}\\
                  &\text{PolyOrder},      &&\text{# Polynomial order for curve fitting}\\ 
                  &\text{xMin=None},      &&\text{# Valid Lower bound - Optional}\\  
                  &\text{xMax=None},      &&\text{# Valid Upper bound - Optional}\\  
                  &\text{TimesStd=5},     &&\text{# Range in units of std. deviation for trimming}\\  
                  &\text{ThFactor=0.005}, &&\text{# Scaling factor for gradient threshold detection}\\
                  &\text{UseKDE=True},    &&\text{# If True, use KDE else HDE}\\
                  &\text{fSizeMin=3},     &&\text{# Min. Filter Size for HDE (Gaussian Filter)}\\
                  &\text{fSigma=2.5},     &&\text{# Smoothing Para. (h) for HDE (Gaussian Filter)}\\
                  &\text{RetProb=False},  &&\text{# If True, return PDF else callable Func to compute Prob.}\\
                  &\text{USE_MAX_Y=True}, &&\text{# If True, split curve at global max else at midpoint}\\
                  &\text{Print=False}     &&\text{# If True, print debug info.}\\
                         )
\end{aligned}
$$

This function creates a probability density function (PDF) approximation from a given dataset using either Kernel Density Estimation (KDE) or Histogram Density Estimation (HDE) on a trimmed subset of the data $\left(\text{within} \le \pm Th \cdot \sigma \right)$. The resulting PDF is approximated via separate polynomial fits (least squares) on the left and right of the main peak.  

---

"""

# %%
"""
# Import Required Libraries 

**Keras Tenforflow**

**NumPy**: Python package for N-dimensional arrays (Used For SciPiKDE)

### For Debugging

**Matplotlib**: Python plotting library

**SciPy**: Gaussian KDE Using SciPy API (For validation)

"""

# %%
DEBUG = False # Default Set it False
# -----------------------------------------------------------------------------
import tensorflow as tf
import numpy as np
from .DensityEstimate import SciPyKDE, KDE, HDE

# -----------------------------------------------------------------------------
if DEBUG:  
    import matplotlib.pyplot as plt


# %%
"""
## RetFunc: Dual Polynomial Regression for Probability Estimation (TensorFlow)

This function maps input tensor `x` to a probability tensor using dual piecewise polynomial functions defined over [xMin, xMid] and [xMid, xMax], with coefficients `CoefLeft` and `CoefRight`, respectively.

### **Memory Breakdown** for `RetFunc` Function

Approximate memory estimate for 1D input of length \( W \) and polynomial order \( O \) (ignoring batch size), assuming float32 data type (4 bytes):

| Tensor        | Shape   | Number of elements | Memory (bytes)  | Description       |
| ------------- | --------| ------------------ | --------------- | ----------------- |
| **x**         | (W,)    | W                  | 4 \* W          | Input vector      |
| **powers**    | (O,)    | O                  | 4 \* O          | Powers vector     |
| **xExpand**   | (W, 1)  | W                  | 4 \* W          | Expanded input    |
| **xPow**      | (W, O)  | W \* O             | 4 \* W \* O     | Powers of input   |
| **CoefLeft**  | (1, O)  | O                  | 4 \* O          | Coefficients      |
| **CoefRight** | (1, O)  | O                  | 4 \* O          | Coefficients      |
| **yLeftRaw**  | (W,)    | W                  | 4 \* W          | Polynomial result |
| **yRightRaw** | (W,)    | W                  | 4 \* W          | Polynomial result |
| **IdxLeft**   | (W,)    | W                  | 4 \* W          | Mask              |
| **IdxRight**  | (W,)    | W                  | 4 \* W          | Mask              |
| **Prob**      | (W,)    | W                  | 4 \* W          | Final output      |

Total memory (approximate):

$$
\text{Memory} \approx 4 \times \big( 7W + 3 \times \text{O} + W \times \text{Order} \big) \quad \text{bytes}
$$

$$
\text{Memory}_{\text{KB}} = \frac{\text{Memory}}{1024} = \frac{4 \times (7W + 3O + W \times O)}{1024} \quad \text{KB}
$$

$$
\text{Memory}_{\text{MB}} = \frac{\text{Memory}}{1024^2} = \frac{4 \times (7W + 3O + W \times O)}{1024^2} \quad \text{MB}
$$
"""

# %%
"""
RetFunc: Dual Polynomial Regression for Probability Estimation (TensorFlow)

Computes piecewise polynomial regression-based probabilities over input tensor `x`, 
with separate polynomial coefficients applied on left and right intervals defined by `xMid`. 

Parameters:
- x: Input tensor of shape (WinSize),(Batch, WinSize) or (Batch, WinNo, WinSize)
- Order: Polynomial order (integer)
- xMid: Boundary point separating left and right intervals (scalar)
- CoefLeft: Polynomial coefficients for left interval, shape compatible with `Order`
- CoefRight: Polynomial coefficients for right interval, shape compatible with `Order`
- xMin, xMax: Minimum and maximum bounds for input values
- MinProb, MaxProb: Clipping bounds for output probabilities
- Auc: Normalization constant (area under curve)

Returns:
- Probabilities tensor of same shape as `x`.
"""

# -----------------------------------------------------------------------------
@tf.function(reduce_retracing=True)
def RetFunc(x,                  # Input tensor (W),(B, W) or (B, C, W)
            Order,              # Polynomial order (integer)           
            xMid,               # Boundary point separating left and right intervals 
            CoefLeft,           # Polynomial coefficients for left interval - compatible with `Order`
            CoefRight,          # Polynomial coefficients for Right interval - compatible with `Order` 
            xMin,               # Minimum bound value for input x
            xMax,               # Maximum bound value for input x
            MinProb=1e-12,      # Minimum Clipping bound value for output probabilities
            MaxProb=1,          # Maximum Clipping bound value for output probabilities
            Auc=1):             # Normalization constant (Area Under Curve - PDF of Population)

    """
    x: Tensor of shape (WinSize), (Batch, WinSize) or (Batch, WinNo, WinSize)
    Returns: Probabilities of same shape
    """
    x = tf.cast(x, tf.float32)                     # shape: (Batch, WinSize) or (Batch, WinNo, WinSize)

    powers = tf.range(Order, dtype=tf.float32)     # shape: (Order,)
    xExpand = tf.expand_dims(x, axis=-1)           # shape (..., 1)
    xPow = tf.pow(xExpand, powers)                 # shape (..., Order)

    # Reshape coefficients for broadcasting
    ExpandShape = [1] * (len(x.shape)) + [Order]   # shape: [1, 1, ..., Order] matching xPow trailing dim
    CoefLeft = tf.reshape(CoefLeft, ExpandShape)   # shape: ExpandShape (broadcastable)
    CoefRight = tf.reshape(CoefRight, ExpandShape) # shape: ExpandShape (broadcastable)
    
    # Compute polynomials via einsum (more optimized on GPUs)
    #yLeftRaw = tf.reduce_sum(xPow * CoefLeft, axis=-1)
    yLeftRaw = tf.einsum('...o,...o->...', xPow, CoefLeft)    # shape: same as x without last dim
    # yRight = tf.reduce_sum(xPow * CoefRight, axis=-1)
    yRightRaw = tf.einsum('...o,...o->...', xPow, CoefRight)  # shape: same as x without last dim

    # Create masks
    # First index where x >= xMid
    Pointer = tf.argmax(tf.cast(x >= xMid, tf.float32), axis=-1, output_type=tf.int32)  
    # Create indices vector for last axis
    length = tf.shape(x)[-1]  # length of last axis
    idxs = tf.range(length)  # shape: (length,)
    # Reshape idxs for broadcasting, e.g., for 2D x with shape (B,L), idxs shape becomes (1,L)
    # For 3D shape (B1,B2,L), idxs shape will be (1,1,L)
    expand_shape = tf.concat([tf.ones(tf.rank(x)-1, dtype=tf.int32), [length]], axis=0)
    idxs_exp = tf.reshape(idxs, expand_shape)  # shape compatible for broadcasting with x and Pointer
    # Expand Pointer dims to add last dim for broadcasting
    Pointer_exp = tf.expand_dims(Pointer, axis=-1)  # shape: x.shape[:-1] + (1,)
    # MaskLeft: indices less than Pointer are 1, else 0
    MaskLeft = tf.cast(idxs_exp < Pointer_exp, tf.float32)
    # MaskRight: indices greater or equal to Pointer are 1, else 0
    MaskRight = tf.cast(idxs_exp >= Pointer_exp, tf.float32)
    EdgeMask = tf.cast(tf.logical_and(x >= xMin, x < xMax), tf.float32)
    # Apply masks and normalize
    Prob = (yLeftRaw * MaskLeft + yRightRaw * MaskRight) / Auc  # shape: same as x without last dim
    Prob = Prob*EdgeMask
    Prob = tf.clip_by_value(Prob, MinProb, MaxProb)             # shape: same as x without last dim       
    return Prob

# %%
"""
## For Evaluation / Debugging Purpose - RetFunc Function
"""

# %%
#*************************************************************
# Test Code
#*************************************************************
if DEBUG:
    @tf.function#(reduce_retracing=True)
    def pRetFunc(x, Order, xMid, CoefLeft, CoefRight, 
                xMin, xMax, MinProb=1e-12, MaxProb=1, Auc=1, Print=False):
        """
        x: Tensor of shape (Batch, WinSize) or (Batch, WinNo, WinSize)
        Returns: Probabilities of same shape (and memory if RetMem)
        """
        x = tf.cast(x, tf.float32)
        if Print: tf.print('1. x: ', x.shape)

        powers = tf.range(Order, dtype=tf.float32)
        if Print: tf.print('2. powers: ', powers.shape)

        xExpand = tf.expand_dims(x, axis=-1)           # shape (..., 1)
        if Print: tf.print('3. xExpand: ', xExpand.shape)

        xPow = tf.pow(xExpand, powers)                 # shape (..., Order)
        if Print: tf.print('4. xPow: ', xPow.shape)

        # Reshape coefficients for broadcasting
        ExpandShape = [1] * (len(x.shape)) + [Order]   # shape: [1, 1, ..., Order] matching xPow trailing dim
        if Print: tf.print('5. ExpandShape: ', ExpandShape)

        CoefLeft = tf.reshape(CoefLeft, ExpandShape)   # shape: ExpandShape (broadcastable)
        if Print: tf.print('6. CoefLeft: ', CoefLeft.shape,' CoefLeft: ',CoefLeft)
        CoefRight = tf.reshape(CoefRight, ExpandShape) # shape: ExpandShape (broadcastable)
        if Print: tf.print('7. CoefRight: ', CoefRight.shape, ' CoefRight: ',CoefRight)

        # Compute polynomials via einsum (more optimized on GPUs)
        #yLeftRaw = tf.reduce_sum(xPow * CoefLeft, axis=-1)
        yLeftRaw = tf.einsum('...o,...o->...', xPow, CoefLeft)    # shape: same as x without last dim
        if Print: tf.print('8. yLeftRaw: ', yLeftRaw.shape); 
        #tf.print('8A. yLeftRaw: ', yLeftRaw, summarize=-1)
        #yRightRaw = tf.reduce_sum(xPow * CoefRight, axis=-1)
        yRightRaw = tf.einsum('...o,...o->...', xPow, CoefRight)  # shape: same as x without last dim
        if Print: tf.print('9. yRightRaw: ', yRightRaw.shape); 
        #tf.print('9A. yRightRaw: ', yRightRaw, summarize=-1)

        # Create masks
        Pointer = tf.argmax(tf.cast(x >= xMid, tf.float32), axis=-1, output_type=tf.int32)  # First index where x >= xMid
        if Print: tf.print("Pointer dtype:", Pointer.dtype)
        # Create indices vector for last axis
        length = tf.shape(x)[-1]  # length of last axis
        idxs = tf.range(length)  # shape: (length,)
        # Reshape idxs for broadcasting, e.g., for 2D x with shape (B,L), idxs shape becomes (1,L)
        # For 3D shape (B1,B2,L), idxs shape will be (1,1,L)
        expand_shape = tf.concat([tf.ones(tf.rank(x)-1, dtype=tf.int32), [length]], axis=0)
        idxs_exp = tf.reshape(idxs, expand_shape)  # shape compatible for broadcasting with x and Pointer
        # Expand Pointer dims to add last dim for broadcasting
        Pointer_exp = tf.expand_dims(Pointer, axis=-1)  # shape: x.shape[:-1] + (1,)
        # MaskLeft: indices less than Pointer are 1, else 0
        MaskLeft = tf.cast(idxs_exp < Pointer_exp, tf.float32)
        if Print:
            Tot1 = tf.reduce_sum(MaskLeft)
            tf.print(f'MaskLeft:', tf.shape(MaskLeft), '  Tot1:',Tot1)
            tf.print(MaskLeft)
        
        # MaskRight: indices greater or equal to Pointer are 1, else 0
        MaskRight = tf.cast(idxs_exp >= Pointer_exp, tf.float32)
        if Print:
            Tot1 = tf.reduce_sum(MaskRight)
            tf.print(f'MaskRight:', tf.size(MaskRight), '  Tot1:',Tot1)
            tf.print(MaskRight)
        
        EdgeMask = tf.cast(tf.logical_and(x >= xMin, x < xMax), tf.float32)
        if Print:
            Tot1 = tf.reduce_sum(EdgeMask)
            tf.print(f'EdgeMask:', tf.size(EdgeMask), '  Tot1:',Tot1)
            tf.print(EdgeMask)

    
        # Apply masks and normalize
        Prob = (yLeftRaw * MaskLeft + yRightRaw * MaskRight) / Auc  # shape: same as x without last dim
        Prob = Prob*EdgeMask
        Prob = tf.clip_by_value(Prob, MinProb, MaxProb)           # shape: same as x without last dim       
        
        if Print: # Print the arguments Used
            tf.print('Order', Order)
            tf.print('xMid', xMid)
            tf.print('xMin', xMin)
            tf.print('xMax', xMax)
            tf.print('MinProb', MinProb)
            tf.print('MaxProb', MaxProb)
            tf.print('AUC', Auc)
        
        return Prob   

    #=====================================================================
    Order = 2
    xMin, xMid, xMax = -0.9, 0.0, 0.9
    MinProb, MaxProb, Auc = 1e-12, 1.0, 1.0
    N=40; O=5 # Offset
    # Random coefficients of shape (Order,)
    CoefLeft =  tf.ones([Order], dtype=tf.float32)*0.1
    CoefRight = tf.ones([Order], dtype=tf.float32)*0.1
    X=np.linspace(-1,1,N)
    print(f'X:{X.shape}  CoefLeft:{CoefLeft} CoefRight:{CoefRight}')    
    #--------------------------------------------------------------------
    # Case 1: 1D Tensor
    x1=X
    print("\n********************************************************")
    print("Case 1: ",x1.shape)
    print("********************************************************")
    p1 = pRetFunc(x1, Order, xMid, CoefLeft, CoefRight, xMin, xMax, MinProb, MaxProb, Auc, Print=True)
    print("Case 1 output shape:", p1.shape)
    print("Case 1 output sample[100:105]:", p1[O:O+5].numpy())
    print("Case 1 output sample[-105:-100]:", p1[N-O-5:N-O].numpy())
    print("*************************************\n")
    #--------------------------------------------------------------------        
    # Case 2: 2D Tensor
    x2 = tf.stack([X, X + 0.1])  # shape (2, 100)
    print("\n********************************************************")
    print("Case 2: ",x2.shape)
    print("********************************************************")
    p2 = pRetFunc(x2, Order, xMid, CoefLeft, CoefRight, xMin, xMax, MinProb, MaxProb, Auc, Print=True)
    print("Case 2 output shape:", p2.shape)
    print("Case 2 output sample[0,100:105]:", p2[0, O:O+5].numpy())
    print("Case 2 output sample[0,-105:-100]:", p2[0,N-O-5:N-O].numpy())
    print("*************************************\n")
    #--------------------------------------------------------------------
    # Case 3: 3D Tensor
    x3 = tf.stack([X, X + 0.1])          # (2, 100)
    x3 = tf.stack([x3, x3 + 0.2, x3 + 0.3], axis=1)  # (2, 3, 100)
    print("\n********************************************************")
    print("Case 3: ",x3.shape)
    print("********************************************************")
    p3 = pRetFunc(x3, Order, xMid, CoefLeft, CoefRight, xMin, xMax, MinProb, MaxProb, Auc, Print=True)
    print("Case 3 output shape:", p2.shape)
    print("Case 3 output sample[0,0,100:105]:", p3[0,0, O:O+5].numpy())
    print("Case 3 output sample[0,0,-105:-100]:", p3[0,0,N-O-5:N-O].numpy())
    print("*************************************\n")
    #--------------------------------------------------------------------        
    plt.plot(X,p1, label=f'Case1:{x1.shape}')
    plt.plot(X,p2[1], label=f'Case2:{x2.shape}')
    plt.plot(X,p3[1,1,:], label=f'Case3:{x3.shape}')
    plt.legend()


# %%
"""
## Function Get_xTreshold():

This function calculates a threshold point on the x-axis where the slope of y with respect to x changes significantly. For detecting upward rapid changes (when `Up=True`), it analyzes the first half of the data, and for downward rapid changes (when `Up=False`), it analyzes the second half. It computes the gradient of y over the specified half, applies a scaled threshold factor to identify where the slope crosses this threshold, and returns the corresponding x-value indicating a significant slope change.
"""

# %%
"""
Detects the x-value where the slope of y vs. x changes rapidly, checking the first half for upward changes 
and the second half for downward changes based on a gradient threshold scaled by ThFactor.

Args:
    x (array-like or tf.Tensor): 1D input array of x-values.
    y (array-like or tf.Tensor): 1D input array of y-values.
    xEdge (Scalar) : x Coordinate to consider as Edge - For Up: xEdge is Start For Dn: xEdge is End
    ThFactor (float): Scaling factor for gradient threshold detection. (Default 1%)
    Up (bool): If True, detects rapid upward slope change; 
               if False, detects rapid downward slope change.

Returns:
    float: The x-value where the slope crosses the threshold.
"""

def Get_xTreshold(x,y, xEdge,ThFactor=0.01,  Up=False):
    # Convert tensors to NumPy arrays (float32)
    if tf.is_tensor(x): x = x.numpy().astype(np.float32)
    if tf.is_tensor(y): y = y.numpy().astype(np.float32)
   
    #For Upward Direction Consider 1st Half For Downward Direction Consider 2nd Half 
    if Up:
        EdgeIdx=np.where(x>xEdge)[0][0] 
        sIdx=EdgeIdx
        eIdx=max(EdgeIdx+3, x.size//2)
    else:
        EdgeIdx=np.where(x<xEdge)[0][-1] 
        eIdx=EdgeIdx
        sIdx= min(x.size//2,EdgeIdx-3) 

    #print(f'EdgeIdx:{EdgeIdx} sIdx:{sIdx} eIdx:{eIdx}')
    # Compute first derivative
    dy = np.gradient(y[sIdx:eIdx], x[sIdx:eIdx])
    # Thresholding: 
    # For Upward Direction - Find where slope starts increasing rapidly → look where it becomes more positive
    # For Downward Direction - Find where slope stops decreasing rapidly → look where it becomes less negative
    threshold = ThFactor * np.max(dy)  if Up else ThFactor * np.min(dy)

    idx = np.argmax(dy > threshold)
    x_change = x[sIdx:eIdx][idx]
    return x_change


# %%
"""
## For Evaluation / Debugging Purpose - Get_xTreshold()
"""

# %%
#*************************************************************
# Test Code
#*************************************************************
if DEBUG:
    fig, ax = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    #-----------------------------------
    # Case 1 - Upward Direction
    x = np.linspace(0, 5, 500)
    y = 1 / (1 + np.exp(-5*(x - 3)))  # sigmoid-like function with sharp rise near x=3
    x_Up= Get_xTreshold(x,y, xEdge=2, ThFactor=0.01, Up=True)
    ax[0].plot(x, y, label='y(x)')
    ax[0].axvline(x_Up, color='r', linestyle='--', label=f"Sharp Change @ x={x_Up:.2f}")
    ax[0].legend()
    ax[0].set_ylabel("y")
    #-----------------------------------
    # Case 2 - Downward -  decreasing then flattening
    x = tf.linspace(0.0, 5.0, 500)
    y = 1 - tf.math.sigmoid(tf.exp(x))
    x_Dn= Get_xTreshold(x,y, xEdge=4.5, ThFactor=0.005, Up=False)
    ax[1].plot(x, y, label='y(x)')
    ax[1].axvline(x_Dn, color='r', linestyle='--', label=f"Sharp Change @ x={x_Dn:.2f}")
    ax[1].legend()
    ax[1].set_ylabel("y")
    #-----------------------------------
    plt.tight_layout()
    plt.show()


# %%
"""
## Creates a Dual Polynomial Function Approximating a PDF

This function creates a probability density function (PDF) approximation from a given dataset using either Kernel Density Estimation (KDE) or Histogram Density Estimation (HDE) on a trimmed subset of the data $\left(\text{within} \le \pm Th \cdot \sigma \right)$. The resulting PDF is approximated via separate polynomial fits (least squares) on the left and right of the main peak. 

During training inside `DualRegPolyPDF()`, the density function is estimated using either **KDE** (with bandwidth computed via Silverman’s rule) or **HDE** (with the number of bins determined via the Freedman–Diaconis rule).

### Steps:
    1.  Flatten and cast the input dataset to float32.
    2.  Compute mean and standard deviation.
    3.  Define trimming bounds (xMin, xMax) or use ±TimesStd * σ.
    4.  Select subset within the bounds.
    5.  Estimate density using KDE (Silverman bandwidth) or HDE.
    6.  Sort and split density curve at maximum point.
    7.  Identify bounds where density gradient drops below threshold.
    8.  Fit separate polynomials to left and right intervals.
    9.  Normalize area under the curve (AUC).
    10. Return either normalized (x, y) points or a callable PDF function.

"""

# %%
"""
-----------------------------------------------------------------------------
DualPolyRegPDF: Creates a Piecewise Polynomial Function Approximating a PDF
-----------------------------------------------------------------------------
Args:
    Superset (tf.Tensor): Input dataset.
    Points (int):         Number of evaluation points for KDE/HDE.
    PolyOrder (int):      Polynomial order for curve fitting.
    xMin, xMax (float):   Optional explicit bounds. [Default None]
    TimesStd (float):     Range in units of standard deviation for trimming.
    ThFactor (float):     Scaling factor for gradient threshold detection. (Default 0.5%)
    UseKDE (bool):        If True, use KDE; otherwise use HDE.
    fSizeMin (int):       Minimum Filter Size - Required for HDE (Gaussian Filter). [Default 3]
    fSigma (float):       Smoothing Parameter (h) - Required for HDE(Gaussian Filter). [Default 2.5]
    RetProb (bool):       If True, return normalized points; else return PDF function.
    USE_MAX_Y (bool):     If True, split curve at global max; else at midpoint.
    Print (bool):         If True, print debug info.

Returns:
    If RetProb=True: Tuple[tf.Tensor, tf.Tensor] → (x_values, normalized_density)
    Else: Callable[[tf.Tensor], tf.Tensor] → PDF function mapping x → probability.

Possible Options:
    - Points: Any positive integer (e.g., 100, 200, 512)
    - PolyOrder:  Integer ≥ 1 (e.g., 3, 5, 7)
    - xMin, xMax:  None (auto-calculated) or float values for manual bounds
    - TimesStd:  Positive float (default=5 trims to ±TimesStd × σ)
    - UseKDE:
        * True → Kernel Density Estimation
        * False → Histogram Density Estimation
    - RetProb:
        * True → Returns (x, normalized y)
        * False → Returns callable PDF function
    - Print:
        * True → Verbose debugging output
        * False → Silent
    - USE_MAX_Y:
        * True → Split at density peak
        * False → Split at midpoint of X
Notes:
    - KDE bandwidth is computed using Silverman's rule.
    - Polynomial fitting is done separately on each side of the peak to improve fit accuracy.
    - The returned PDF function enforces clipping between MinProb and MaxProb.
"""
# -----------------------------------------------------------------------------
# Should pass the whole data with outlier
def DualPolyRegPDF(Superset, 
                   Points=100, 
                   PolyOrder=5, 
                   xMin=None, 
                   xMax=None, 
                   TimesStd=5,
                   ThFactor=0.01,
                   UseKDE=True,
                   fSizeMin=3,      # Minimum Filter Size - Required for HDE (Gaussian Filter)
                   fSigma=2.5,      # Smoothing Parameter (h) - Required for HDE(Gaussian Filter)
                   RetProb=False, 
                   USE_MAX_Y=True,
                   Print=False
                  ):
    
    if Print: tf.print("0. Superset: ",Superset.shape )
    Superset = tf.cast(tf.reshape(Superset, [-1]), tf.float32)
    if Print: tf.print("1. Superset: ",Superset.shape )
    Epsilon = tf.constant(1e-12, tf.float32)
    if Print: tf.print("2. Epsilon: ",Epsilon )
        
    mean, std = tf.reduce_mean(Superset), tf.math.reduce_std(Superset)
    if Print: tf.print("3. mean: ",mean, "\tstd: ", std)
        
    xMinLeft = tf.cast(xMin, tf.float32) if xMin is not None else mean - TimesStd * std
    xMaxRight = tf.cast(xMax, tf.float32) if xMax is not None else mean + TimesStd * std
    if Print: tf.print("4. xMinLeft: ",xMinLeft, "\txMaxRight: ", xMaxRight)
        
    Mask99 = tf.math.logical_and(Superset > xMinLeft, Superset < xMaxRight)
    if Print: tf.print("5. Mask99: ",Mask99.shape )
        
    # Subset using boolean_mask
    Superset99 = tf.boolean_mask(Superset, Mask99)
    Count99=tf.reduce_sum(tf.cast(Mask99, tf.int32))
    if Print: 
        tf.print("6. Superset99: ",Superset99.shape, "\tCount99: ",Count99)
        tf.print('Superset99 StdDev: ',tf.math.reduce_std(Superset99))
    
    # For KDE Computing BW using Silverman's rule
    if UseKDE: X, Y = KDE(X=Superset99, Points=Points) 
    # For HDE Computing No of Bins (nBins) using Freedman–Diaconis rule
    else: X, Y,_ = HDE(S=Superset99, nBins=None, Epsilon=Epsilon,fSizeMin=fSizeMin, fSigma=fSigma);
    if Print: tf.print("7. X: ",X.shape,"  Y: ",Y.shape)
        
    SortedIdx = tf.argsort(X)
    if Print: tf.print("8. SortedIdx: ", SortedIdx.shape)
    xSorted, ySorted = tf.gather(X, SortedIdx), tf.gather(Y, SortedIdx)
    if Print: tf.print("9. xSorted: ",xSorted.shape, "\tySorted: ",ySorted.shape)
        
    MaxY = tf.reduce_max(ySorted)
    MidIdx = tf.argmax(ySorted) if USE_MAX_Y else Points // 2
    xAtMid = xSorted[MidIdx];# yAtMid=ySorted[MidIdx]
    if Print:tf.print("10. MaxY:", MaxY, "\tMidIdx:", MidIdx, "\txAtMid:", xAtMid)
        
    UpX, DnX = xSorted[:MidIdx], xSorted[MidIdx:]
    if Print: tf.print("11. UpX: ",UpX.shape, "\tDnX: ",DnX.shape)    
    UpY, DnY = ySorted[:MidIdx], ySorted[MidIdx:]
    if Print: 
        tf.print("12. UpY: ",UpY.shape, "\tDnY: ",DnY.shape)
        tf.print("13A. xMinLeft: ",xMinLeft )  
        
    # Update xMinLeft to x Point before which Gradient of y is very low
    xUpTh=Get_xTreshold(UpX,UpY, xMinLeft, ThFactor, Up=True)
    if xUpTh > xMinLeft: xMinLeft=xUpTh
    if Print:         
        tf.print("13. xUpTh: ",xUpTh, "\txMinLeft: ",xMinLeft )
        tf.print("14A. xMaxRight: ",xMaxRight )  
        
    # Update xMaxRight to x Point after which Gradient of y is very low
    xDnTh=Get_xTreshold(DnX,DnY, xMaxRight, ThFactor, Up=False)
    if xDnTh < xMaxRight: xMaxRight=xDnTh
    if Print: tf.print("14. xDnTh: ",xDnTh, "\txMaxRight: ",xMaxRight )
        
    xOrder = tf.stack([tf.pow(xSorted, i) for i in range(PolyOrder)], axis=1)
    if Print: tf.print("15. xOrder: ", xOrder.shape)
        
    UpX, DnX = xOrder[:MidIdx], xOrder[MidIdx:]
    if Print: tf.print("16. UpX: ",UpX.shape, "\tDnX: ",DnX.shape) 
    ExUpY, ExDnY = tf.expand_dims(ySorted[:MidIdx], axis=1), tf.expand_dims(ySorted[MidIdx:], axis=1)
    if Print: tf.print("17. ExUpY: ",ExUpY.shape, "\tExDnY: ",ExDnY.shape) 
        
    CoefUp = tf.linalg.lstsq(UpX, ExUpY)
    CoefDn = tf.linalg.lstsq(DnX, ExDnY)
    if Print: 
        tf.print("18. CoefUp: ",CoefUp.shape, "\tCoefDn: ",CoefDn.shape) 
        tf.print("18. CoefUp: ",CoefUp, "\tCoefDn: ",CoefDn)   
    
    xUp = tf.linspace(xSorted[0], xSorted[MidIdx-1], Points)
    xDn = tf.linspace(xSorted[MidIdx], xSorted[-1], Points)
    if Print: tf.print("19. xUp: ",xUp.shape, "\txDn: ",xDn.shape) 
        
    yUp = tf.add_n([CoefUp[i] * tf.pow(xUp, i) for i in range(PolyOrder)])
    yDn = tf.add_n([CoefDn[i] * tf.pow(xDn, i) for i in range(PolyOrder)])
    if Print: tf.print("20. xUp: ",xUp.shape, "\txDn: ",xDn.shape) 
        
    xFit = tf.concat([xDn, xUp], axis=0)
    yFit = tf.concat([yDn, yUp], axis=0)
    yFit = tf.clip_by_value(yFit, Epsilon, MaxY)
    if Print: 
        tf.print("21. xFit: ",xFit.shape, "\tyFit: ",yFit.shape) 
        tf.print("22. Min(yFit):", tf.reduce_min(yFit), "\tMax(yFit):", tf.reduce_max(yFit))

        
    SortedIdx = tf.argsort(xFit)
    if Print: tf.print("23. SortedIdx: ",SortedIdx.shape)
        
    xFitSorted, yFitSorted = tf.gather(xFit, SortedIdx), tf.gather(yFit, SortedIdx)
    if Print: tf.print("24. xFitSorted: ",xFitSorted.shape, "\tyFitSorted: ",yFitSorted.shape) 
        
    dx = xFitSorted[1:] - xFitSorted[:-1]
    Av_dy = (yFitSorted[1:] + yFitSorted[:-1]) / 2.0
    BaseAUC = tf.reduce_sum(dx * Av_dy)
    if Print: tf.print("25. dx: ",dx.shape, "\tAv_dy: ",Av_dy.shape, "\tBaseAUC: ",BaseAUC) 
    

    if RetProb:
        return xFitSorted, yFitSorted/BaseAUC
    else:
        # Return a Polynomila Regression Function with Pre-trained coefficients and settings
        return lambda x: RetFunc(x,                  # Input tensor (W),(B, W) or (B, C, W)
                                 Order=PolyOrder,    # Polynomial order (integer)           
                                 xMid=xAtMid,        # Boundary point separating left and right intervals 
                                 CoefLeft=CoefUp,    # Polynomial coefficients for left interval
                                 CoefRight=CoefDn,   # Polynomial coefficients for Right interval  
                                 xMin=xMinLeft,      # Minimum bound value for input x
                                 xMax=xMaxRight,     # Maximum bound value for input x
                                 MinProb=Epsilon,    # Minimum Clipping bound value for output probabilities
                                 MaxProb=MaxY,       # Maximum Clipping bound value for output probabilities
                                 Auc=BaseAUC)        # Normalization constant (Area Under Curve - PDF of Population)
                                 #Print=True)

# %%
"""
## For Evaluation / Debugging Purpose - DualPolyRegPDF()

"""

# %%
if DEBUG: 
    np.random.seed(0)
    fig, bx = plt.subplots(1, 1, figsize=(9, 9));
    data = np.random.normal(loc=0.5, scale=1.5, size=10000)
    print(f'std: {np.std(data):.3f}')
    data_tf = tf.constant(data, dtype=tf.float32)

    cases = [   {"UseKDE": True,  "RetProb": True,  "label": "Case 1: KDE + RetProb=True"},
                {"UseKDE": True,  "RetProb": False, "label": "Case 2: KDE + RetProb=False"},    
                {"UseKDE": False, "RetProb": True,  "label": "Case 3: HDE + RetProb=True"},
                {"UseKDE": False, "RetProb": False, "label": "Case 4: HDE + RetProb=False"},]

    for case in cases:
        print("\n" + "="*80)
        print(case["label"])
        print("="*80)

        result = DualPolyRegPDF(
                                Superset=data_tf,
                                Points=200,
                                PolyOrder=5,
                                TimesStd=5,
                                UseKDE=case["UseKDE"],
                                RetProb=case["RetProb"],
                                Print=True
                               )

        if case["RetProb"]:
            # result is (x, y)
            x_fit, y_fit = result
        else:
            # result is a callable function → compute probabilities
            func = result
            x_fit = np.linspace(np.min(data), np.max(data), 200).astype(np.float32)
            yHat = func(tf.constant(x_fit, dtype=tf.float32))
            y_fit =yHat.numpy()

        auc = np.trapz(y_fit, x_fit)
        print("AUC (np.trapz(y_fit, x_fit)):", auc)

        bx.plot(x_fit, y_fit, label=case["label"])

    bx.set_title("Comparison of CreateFunc4PDF Cases")
    bx.set_xlabel("x")
    bx.set_ylabel("PDF")
    bx.legend()
    plt.show();


# %%
