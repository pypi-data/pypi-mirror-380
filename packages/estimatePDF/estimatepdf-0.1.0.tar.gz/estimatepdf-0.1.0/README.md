# estimatePDF

**A Python library for Probability Density Function (PDF) estimation using Kernel Density, Histogram Density, and Dual Polynomial Regression.**

---

## Overview

`estimatePDF` estimatePDF is a Python package for probability density function (PDF) estimation and sampling. It provides computationally efficient, GPU-optimized implementations using TensorFlow along with custom polynomial regression methods designed to capture asymmetry in distributions.

---

## Features

- **Density Estimation**
  - SciPy Gaussian KDE
  - TensorFlow-based KDE (for graph execution)
  - Histogram Density Estimation (HDE)

- **Probability Density Functions**
  - Gaussian PDF
  - Asymmetric Laplace PDF & sampling
  - M-Wright functions and variants
  - Inverse Transform Sampling

- **Dual Polynomial Regression (DPR)**
  - Piecewise polynomial PDF approximation
  - Gradient-based threshold detection
  - Fits multimodal or skewed PDFs

---

## Installation

Install from PyPI:

```bash
pip install estimatePDF
