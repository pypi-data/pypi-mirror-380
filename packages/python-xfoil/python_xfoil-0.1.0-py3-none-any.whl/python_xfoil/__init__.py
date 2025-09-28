"""
PythonXfoil - A Python interface for XFOIL aerodynamic analysis

This module provides an interface to natively and intuitively run concurrent 
aerodynamic analyses using XFOIL. It allows users to define airfoil geometries, 
set analysis parameters, and execute XFOIL simulations programmatically.
"""

from .xfoil import Airfoil, Utils

__version__ = "0.1.0"
__all__ = ["Airfoil", "Utils"]
