"""Classes for RESQML objects related to surfaces."""

__all__ = [
    'BaseSurface', 'CombinedSurface', 'Mesh', 'TriangulatedPatch', 'PointSet', 'Surface', 'TriMesh', 'TriMeshStencil',
    'distill_triangle_points', '_adjust_flange_z'
]

from ._base_surface import BaseSurface
from ._combined_surface import CombinedSurface
from ._mesh import Mesh
from ._triangulated_patch import TriangulatedPatch
from ._pointset import PointSet
from ._surface import Surface, distill_triangle_points, nan_removed_triangles_and_points, _adjust_flange_z
from ._tri_mesh import TriMesh
from ._tri_mesh_stencil import TriMeshStencil

# Set "module" attribute of all public objects to this path.
for _name in __all__:
    _obj = eval(_name)
    if hasattr(_obj, "__module__"):
        _obj.__module__ = __name__
