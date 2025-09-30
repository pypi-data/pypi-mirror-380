"""
epe_maria: Symbolic audit framework for model divergence and integrity.

Available functions:
- phi(f, g, domain=None): Structural divergence
- delta_phi(f, g, domain=None): Rate divergence
- phi_star(f, g, alpha=0.5, beta=0.5, domain=None): Fusion metric
- drift(f, g, domain=None): Directional drift
- curvature(f, domain=None): Average curvature
"""

from .metrics import phi, delta_phi, phi_star
from .monitor import drift, curvature

__all__ = ["phi", "delta_phi", "phi_star", "drift", "curvature"]
