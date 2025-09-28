"""
visuals: a one‑stop, modular data visualization package.

Public API:
    from visuals.core import visualize
    # or import specific helpers from submodules
"""

from .core import visualize
from .auto_viz import auto_visualize
from .dashboard import launch_dashboard


__all__ = ["visualize"]
