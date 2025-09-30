"""
Submodule `kinematics` provides tools for constructing 2D lattices and performing
Ewald constructions. These tools can be used to calculate and visualize diffraction
spot positions based on kinematic theory.
"""

from .ewald import Ewald

__all__ = ["Ewald"]
