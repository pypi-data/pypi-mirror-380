# ---------------------------------------
# __init__.py for estimatePDF package
# ---------------------------------------

# --------------------------
# DensityEstimate module
# --------------------------
# Import both the module and the main function
from . import DensityEstimate
from .DensityEstimate import SciPyKDE, KDE, HDE

# --------------------------
# ProbabilityDensityFunction module
# --------------------------
# Import both the module and the main function
from . import ProbabilityDensityFunction
from .ProbabilityDensityFunction import (
    GaussianPDF,
    InvTransformSampling,
    M_Wright,
    M_Wright_Reflect,
    M_CDF,
    Create_AWM_I_PDF,
    Create_AWM_II_PDF,
    AsymLaplacePDF,
    SampleAsymLaplace
)

# --------- DualPolyRegPDF ---------
# Import both the module and the main function
from . import DualPolyRegPDF
from .DualPolyRegPDF import RetFunc, Get_xTreshold, DualPolyRegPDF as DPRFunc

__all__ = [
    # DensityEstimate
    "DensityEstimate", #module
    #the functions
    "SciPyKDE", "KDE", "HDE",
    
    # ProbabilityDensityFunction
    "ProbabilityDensityFunction", #module
    #the functions
    "GaussianPDF", "InvTransformSampling", "M_Wright", "M_Wright_Reflect",
    "M_CDF", "Create_AWM_I_PDF", "Create_AWM_II_PDF",
    "AsymLaplacePDF", "SampleAsymLaplace",
    
    # DualPolyRegPDF
    "DualPolyRegPDF",  # module
    # the function
    "RetFunc",
    "Get_xTreshold",
    "DPRFunc",  
]