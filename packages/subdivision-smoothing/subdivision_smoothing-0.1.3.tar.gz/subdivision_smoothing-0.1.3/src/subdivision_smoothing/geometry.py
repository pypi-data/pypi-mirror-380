"""
Provides subdivision and smoothing algorithms for 3D meshes using the trimesh library.

This module offers a collection of static methods for manipulating 3D meshes.
The main methods handle common subdivision and smoothing tasks, while other public methods are intended for advanced or internal use.

Main Provided Methods
---------------------
- :func:`SubdivisionSmoothing.simple_subdivide`: Performs a basic subdivision.
- :func:`SubdivisionSmoothing.simple_smooth`: Applies a modified Laplacian smoothing algorithm.
- :func:`SubdivisionSmoothing.edge_erosion_subdivision`: Performs a specialized subdivision with edge erosion.

.. note::
   Some public methods are primarily intended for internal use and may have less stable APIs and minimal documentation.
"""

import sys
from typing import Literal, Callable

import numpy as np
import trimesh
import numba
from numba import njit, jit
from numba.typed import List as NumbaList
from scipy.interpolate import InterpolatedUnivariateSpline


class SubdivisionSmoothing:
    def __init__(self):
        raise NotImplementedError("This class is not meant to be instantiated directly.")

    @staticmethod
    def edges_in_mesh(mesh: trimesh.Trimesh, edges: np.ndarray):
        """
        Check which items in an ndarray of edges are present in a mesh. Public method that validates input types and dimensions.

        :param mesh: The mesh to analyze.
        :type mesh: trimesh.Trimesh
        :param edges: An ndarray of shape (n, 2) of edges or pairs of vertex indices, where n is the number of edges.
        :type edges: np.ndarray
        :return: ndarray of shape (n) boolean values indicating if each edge is present in the mesh, where n is the number of edges.
        :rtype: np.ndarray
        :raises TypeError: If mesh is not a trimesh.Trimesh object or edges is not a numpy ndarray.
        :raises ValueError: If edges is not a 2D array with shape (n, 2), if edges is empty, if mesh is empty, or if mesh is not watertight.
        """
        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Mesh must be a trimesh.Trimesh object.")
        if not isinstance(edges, np.ndarray):
            raise TypeError("Edges must be a numpy ndarray.")
        if edges.ndim != 2 or edges.shape[1] != 2:
            raise ValueError("Edges must be a 2D array with shape (n, 2).")
        if edges.shape[0] == 0:
            return np.zeros(0, dtype=bool)
        if mesh.is_empty:
            return np.zeros(0, dtype=bool)

        return SubdivisionSmoothing._edges_in_mesh(mesh, edges)

    @staticmethod
    def _edges_in_mesh(mesh: trimesh.Trimesh, edges: np.ndarray):
        """
        Check which items in an ndarray of edges are present in a mesh. Private method that performs the actual check with no input validation.

        :param mesh: The mesh to analyze.
        :type mesh: trimesh.Trimesh
        :param edges: An ndarray of shape (n, 2) of edges or pairs of vertex indices, where n is the number of edges.
        :type edges: np.ndarray
        :return: ndarray of shape (n) boolean values indicating if each edge is present in the mesh, where n is the number of edges.
        :rtype: np.ndarray
        """
        sorted_edges = np.sort(edges, axis=1)
        mesh_edges = np.sort(mesh.face_adjacency_edges, axis=1)
        # View as structured arrays for row-wise comparison
        dtype = [('v0', sorted_edges.dtype), ('v1', sorted_edges.dtype)]
        sorted_edges_view = sorted_edges.view(dtype)
        mesh_edges_view = mesh_edges.view(dtype)
        # Use np.isin for fast membership check
        mask = np.isin(sorted_edges_view, mesh_edges_view)

        return mask

    @staticmethod
    def get_row_inds(arr1: np.ndarray, arr2: np.ndarray):
        """
        Get the row indices of arr1 that are present in arr2. Public method that validates input types and dimensions.

        :param arr1: The first array to check.
        :type arr1: np.ndarray
        :param arr2: The second array to check against.
        :type arr2: np.ndarray
        :return: ndarray of indices of rows in arr1 that are present in arr2.
        :rtype: np.ndarray
        :raises TypeError: If arr1 or arr2 are not numpy ndarrays.
        :raises ValueError: If arr1 or arr2 are not 2D arrays.
        """
        if not isinstance(arr1, np.ndarray):
            raise TypeError("arr1 must be a numpy ndarray.")
        if not isinstance(arr2, np.ndarray):
            raise TypeError("arr2 must be a numpy ndarray.")
        if arr1.ndim != 2:
            raise ValueError("arr1 must be a 2D array.")
        if arr2.ndim != 2:
            raise ValueError("arr2 must be a 2D array.")

        return SubdivisionSmoothing._get_row_inds(arr1, arr2)

    @staticmethod
    def _get_row_inds(arr1: np.ndarray, arr2: np.ndarray):
        """
        Get the row indices of arr1 that are present in arr2. Private method that performs the actual check with no input validation.

        :param arr1: The first array to check.
        :type arr1: np.ndarray
        :param arr2: The second array to check against.
        :type arr2: np.ndarray
        :return: ndarray of indices of rows in arr1 that are present in arr2.
        :rtype: np.ndarray
        :raises TypeError: If arr1 or arr2 are not numpy ndarrays.
        :raises ValueError: If arr1 or arr2 are not 2D arrays.
        """

        dtype = np.dtype((np.void, arr1.dtype.itemsize * arr1.shape[2]))
        A_view = arr1.view(dtype).ravel()
        B_view = arr2.view(dtype).ravel()

        sort_idx = np.argsort(B_view)
        B_sorted = B_view[sort_idx]
        found_idx = np.searchsorted(B_sorted, A_view)
        mask = (found_idx < len(B_sorted))
        valid_idx = np.where(mask)[0]
        mask_valid = (B_sorted[found_idx[valid_idx]] == A_view[valid_idx])
        mask[valid_idx] = mask_valid
        indices = np.full(arr1.shape[0] * arr1.shape[1], -1)
        indices[mask] = sort_idx[found_idx[mask]]

        return indices

    @staticmethod
    def get_edge_normals(mesh: trimesh.Trimesh):
        """
        Get the normals for each edge in a mesh. Public method that validates input types and dimensions.
        .. note::
            This method only works for watertight meshes and when every provided edge is present in the mesh.

        :param mesh: The mesh to analyze.
        :type mesh: trimesh.Trimesh
        :return: ndarray of normals for each edge of shape (n, 3) where n is the number of edges.
        :rtype: np.ndarray
        :raises TypeError: If mesh is not a trimesh.Trimesh object.
        :raises ValueError: If mesh is empty, if mesh is not watertight
        """
        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Mesh must be a trimesh.Trimesh object.")
        if mesh.is_empty:
            return np.zeros((0, 3), dtype=float)
        if not mesh.is_watertight:
            raise ValueError("Mesh must be watertight to compute edge normals.")

        return SubdivisionSmoothing._get_edge_normals(mesh)

    @staticmethod
    def _get_edge_normals(mesh: trimesh.Trimesh):
        """
        Get the normals for each edge in a mesh. Private method that performs the actual computation with no input validation.
        .. note::
            This method only works for watertight meshes and when every provided edge is present in the mesh.

        :param mesh: The mesh to analyze.
        :type mesh: trimesh.Trimesh
        :return: ndarray of normals for each edge of shape (n, 3) where n is the number of edges.
        :rtype: np.ndarray
        """
        neighbors = mesh.face_adjacency
        normals = mesh.face_normals
        normals = normals[neighbors.T]
        normals1 = normals[0]
        normals2 = normals[1]
        e_normals = (normals1 + normals2) / 2
        e_normals /= np.linalg.norm(e_normals, axis=1)[:, None]

        return e_normals

    @staticmethod
    def get_opposite(faces: np.ndarray, edges: np.ndarray):
        """
        Get the opposite vertex indices for each edge in a set of faces.

        :param faces: An ndarray of shape (n, 3) representing the faces of the mesh.
        :type faces: np.ndarray
        :param edges: An ndarray of shape (n, 2) representing the edges of the mesh.
        :type edges: np.ndarray
        :return: An ndarray of shape (n,) containing the opposite vertex indices for each edge, where w is the number of edges.
        :rtype: np.ndarray
        :raises TypeError: If faces or edges are not numpy ndarrays.
        :raises ValueError: If faces is not a 2D array with shape (n, 3) or if edges is not a 2D array with shape (n, 2).
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a numpy ndarray.")
        if not isinstance(edges, np.ndarray):
            raise TypeError("Edges must be a numpy ndarray.")
        if faces.ndim != 2 or faces.shape[1] != 3:
            raise ValueError("Faces must be a 2D array with shape (n, 3).")
        if edges.ndim != 2 or edges.shape[1] != 2:
            raise ValueError("Edges must be a 2D array with shape (n, 2).")

        return SubdivisionSmoothing._get_opposite(faces, edges)

    @staticmethod
    def _get_opposite(faces: np.ndarray, edges: np.ndarray):
        """
        Get the opposite vertex indices for each edge in a set of faces. Private method that performs the actual computation with no input validation.

        :param faces: An ndarray of shape (n, 3) representing the faces of the mesh.
        :type faces: np.ndarray
        :param edges: An ndarray of shape (n, 2) representing the edges of the mesh.
        :type edges: np.ndarray
        :return: An ndarray of shape (n,) containing the opposite vertex indices for each edge, where w is the number of edges.
        :rtype: np.ndarray
        """
        mask = (faces[:, :, None] == edges[:, None, :])
        mask_any = np.any(mask, axis=2)
        opposite = faces[~mask_any]

        return opposite

    @staticmethod
    def get_signed_angles(mesh: trimesh.Trimesh):
        """
        Get the signed angles between adjacent faces at each edge of a mesh. Public method that validates input types and dimensions.

        :param mesh: The mesh to analyze.
        :type mesh: trimesh.Trimesh
        :return: An ndarray of shape (n,) containing the signed angles in radians.
        :rtype: np.ndarray
        :raises TypeError: If mesh is not a trimesh.Trimesh object
        :raises ValueError: If mesh is not watertight.
        """
        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Mesh must be a trimesh.Trimesh object.")
        if mesh.is_empty:
            return np.zeros(0, dtype=float)
        if not mesh.is_watertight:
            raise ValueError("Mesh must be watertight to compute signed angles.")

        return SubdivisionSmoothing._get_signed_angles(mesh)

    @staticmethod
    def _get_signed_angles(mesh: trimesh.Trimesh):
        """
        Get the signed angles between adjacent faces at each edge of a mesh. Private method that performs the actual computation with no input validation.

        :param mesh: The mesh to analyze.
        :type mesh: trimesh.Trimesh
        :return: An ndarray of shape (n,) containing the signed angles in radians.
        :rtype: np.ndarray
        """
        neighbors = mesh.face_adjacency
        normals = mesh.face_normals[neighbors.T]
        angles = np.arccos(np.clip(np.einsum('ij,ij->i', normals[0], normals[1]), -1.0, 1.0))
        return angles

    @staticmethod
    def simple_subdivide(mesh: trimesh.Trimesh, alpha: float=0.5, beta: float=0.5, iterations=1):
        """
        Simple subdivision of a mesh by splitting each triangle into 4 smaller triangles. Public method that validates input types and dimensions.

        :param mesh: The mesh to subdivide.
        :type mesh: trimesh.Trimesh
        :param alpha: A scaling factor for where new vertices are placed relative to existing vertices. Default is 0.5.
        :type alpha: float
        :param beta: A scaling factor for the amount of change applied to each existing vertex and edge. Default is 0.5.
        :type beta: float
        :return: trimesh.Trimesh The subdivided mesh.
        :raises TypeError: If mesh is not a trimesh.Trimesh object or alpha is not a number.
        :raises ValueError: If alpha is not in the range (0, 1), if beta is not in the range [0, 1), or if the mesh is empty or not watertight.
        """
        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Mesh must be a trimesh.Trimesh object.")
        if not isinstance(alpha, float):
            raise TypeError("Alpha must be a float.")
        if not isinstance(beta, float):
            raise TypeError("Beta must be a float.")
        if mesh.is_empty:
            return mesh
        if not mesh.is_watertight:
            raise ValueError("Mesh must be watertight to perform subdivision.")
        if alpha <= 0 or alpha >= 1:
            raise ValueError("Alpha must be in the range (0, 1).")
        if beta < 0 or beta >= 1:
            raise ValueError("Beta must be in the range [0, 1).")

        for i in range(iterations):
            mesh = SubdivisionSmoothing._simple_subdivide(mesh, alpha, beta)
        return mesh

    @staticmethod
    def _simple_subdivide(mesh: trimesh.Trimesh, alpha: float=0.5, beta: float=0.5):
        """
        Simple subdivision of a mesh by splitting each triangle into 4 smaller triangles. Private method that performs the actual subdivision with no input validation.

        :param mesh: The mesh to subdivide.
        :type mesh: trimesh.Trimesh
        :param alpha: A scaling factor for where new vertices are placed relative to existing vertices. Default is 0.5.
        :type alpha: float
        :param beta: A scaling factor for the amount of change applied to each existing vertex and edge. Default is 0.5.
        :type beta: float
        :return: trimesh.Trimesh The subdivided mesh.
        """
        angles = SubdivisionSmoothing._get_signed_angles(mesh)
        new_factors = np.sin(angles) * alpha
        old_factors = np.sin(angles) * beta
        edges = mesh.face_adjacency_edges
        neighbors = mesh.face_adjacency
        edge_norms = SubdivisionSmoothing._get_edge_normals(mesh)
        i_edge_norms = -edge_norms

        opposites1 = SubdivisionSmoothing._get_opposite(mesh.faces[neighbors.T[0]], edges)
        opposites2 = SubdivisionSmoothing._get_opposite(mesh.faces[neighbors.T[1]], edges)
        face1_edge1_int = mesh.vertices[edges[:, 0]] * new_factors[:, None] + mesh.vertices[opposites1] * \
                          (1 - new_factors)[:, None]
        face2_edge1_int = mesh.vertices[edges[:, 0]] * new_factors[:, None] + mesh.vertices[opposites2] * \
                          (1 - new_factors)[:, None]
        face1_change1 = face1_edge1_int - mesh.vertices[edges[:, 0]]
        face2_change1 = face2_edge1_int - mesh.vertices[edges[:, 0]]

        dist1 = np.einsum('ij,ij->i', face1_change1, i_edge_norms)
        dist2 = np.einsum('ij,ij->i', face2_change1, i_edge_norms)
        dists = np.min(np.column_stack([dist1, dist2]), axis=1)

        mesh = mesh.subdivide()
        edge_dir1 = mesh.vertices[edges[:, 1]] - mesh.vertices[edges[:, 0]]
        edge_dir1 /= np.linalg.norm(edge_dir1, axis=1)[:, None]
        edge_dir2 = mesh.vertices[edges[:, 0]] - mesh.vertices[edges[:, 1]]
        edge_dir2 /= np.linalg.norm(edge_dir2, axis=1)[:, None]
        np.add.at(mesh.vertices, edges[:, 0], dists[:, None] * edge_dir1 / 2 * old_factors[:, None])
        np.add.at(mesh.vertices, edges[:, 1], dists[:, None] * edge_dir2 / 2 * old_factors[:, None])
        mesh.process()
        return mesh

    @staticmethod
    def simple_smooth(mesh: trimesh.Trimesh, alpha: int | float = 0.5, dist_effect: Literal["ignore", "weaker", "stronger"] = "weaker", iterations: int=1):
        """
        Smooth a mesh in place using a modified Laplacian smoothing algorithm. Public method that validates input types and dimensions.

        :param mesh: The mesh to smooth.
        :type mesh: trimesh.Trimesh
        :param alpha: A scaling factor for the amount of change applied to each vertex and edge.
        :type alpha: float
        :param dist_effect: How the distance between vertices effects smoothing. Options are "ignore" which ignores distance, "weaker" which give vertices farther away less weight, and "stronger" which gives vertices farther away more weight. Default is "weaker".
        :type dist_effect: Literal["ignore", "weaker", "stronger"]
        :param iterations: Number of smoothing iterations to perform. Default is 1.
        :type iterations: int
        :return: The smoothed mesh.
        :rtype: trimesh.Trimesh
        :raises TypeError: If mesh is not a trimesh.Trimesh object, iterations is not an integer, alpha is not a number, or dist_effect is not a string.
        :raises ValueError: If iterations is less than 1, alpha is not in the range (0, 1], or dist_effect is not "ignore", "weaker", or "stronger".
        """
        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Mesh must be a trimesh.Trimesh object.")
        if not isinstance(iterations, int):
            raise TypeError("Iterations must be an integer.")
        if not isinstance(alpha, (int, float)):
            raise TypeError("Alpha must be a float.")
        if not isinstance(dist_effect, str):
            raise TypeError("dist_effect must be a string.")
        if iterations < 1:
            raise ValueError("Iterations must be at least 1.")
        if alpha <= 0 or alpha > 1:
            raise ValueError("Alpha must be in the range (0, 1].")
        if dist_effect not in ["ignore", "weaker", "stronger"]:
            raise ValueError('dist_effect must be "ignore", "weaker", or "stronger".')
        if mesh.is_empty:
            return

        for _ in range(iterations):
            SubdivisionSmoothing._simple_smooth(mesh, alpha, dist_effect)
            mesh = mesh.subdivide()
        return mesh

    @staticmethod
    def _simple_smooth(mesh: trimesh.Trimesh, alpha: int | float = 0.5, dist_effect: Literal["ignore", "weaker", "stronger"] = "weaker"):
        """
        Smooth a mesh in place using a modified Laplacian smoothing algorithm. Private method that performs the actual smoothing with no input validation.

        :param mesh: The mesh to smooth.
        :type mesh: trimesh.Trimesh
        :param alpha: A scaling factor for the amount of change applied to each vertex and edge.
        :type alpha: float
        :param dist_effect: How the distance between vertices effects smoothing. Options are "ignore" which ignores distance, "weaker" which give vertices farther away less weight, and "stronger" which gives vertices farther away more weight. Default is "weaker".
        :type dist_effect: Literal["ignore", "weaker", "stronger"]
        :return: None. The mesh is modified in place.
        """

        vertices = mesh.vertices
        max_neighbors = max(map(len, mesh.vertex_neighbors))
        neighbors = np.full((vertices.shape[0], max_neighbors), -1)
        for i in range(vertices.shape[0]):
            neighbors[i, :len(mesh.vertex_neighbors[i])] = mesh.vertex_neighbors[i]
        neighbor_verts = vertices[neighbors]
        neighbor_verts[neighbors == -1] = np.repeat(vertices[:, None, :], max_neighbors, axis=1)[neighbors == -1]
        diffs = neighbor_verts - vertices[:, None, :]
        dists = np.linalg.norm(diffs, axis=2)
        weights = None
        match dist_effect:
            case "ignore":
                weights = np.where(dists == 0, 0, 1 / dists)
            case "weaker":
                weights = np.where(dists == 0, 0, 1 / dists ** 2)
            case "stronger":
                weights = np.where(dists == 0, 0, dists)
        avg_point = np.average(diffs, axis=1, weights=np.repeat(weights[:, :, None], 3, axis=2))
        new = avg_point * alpha + vertices
        mesh.vertices = new
        mesh.process()

    @staticmethod
    def edge_erosion_subdivision(mesh: trimesh.Trimesh, alpha: float, beta: float, iterations: int = 1, proximity_digits: int = 6, interp: Callable | None = None, test = False):
        """
        Smooth a mesh in place using intelligent edge and vertex addition.

        :param mesh: The mesh to smooth.
        :type mesh: trimesh.Trimesh
        :param alpha: A scaling factor for the amount of change applied to each vertex and edge.
        :type alpha: float
        :param beta: A scaling factor for where new vertices are placed relative to existing vertices.
        :type beta: float
        :param iterations: Number of smoothing iterations to perform. Default is 1.
        :type iterations: int
        :param proximity_digits: Number of digits to round vertex positions to for proximity checks. Default is 6.
        :type proximity_digits: int
        :param interp: An optional pre-defined interpolation function to use for determining new vertex positions based on edge angles. If None, a default spline will be used. Default is None.
        :type interp: Callable | None
        .. note::
            This parameter should be the actual interpolation function, not a callable that returns the function. It is recommended for it to have a minimum domain of [-π, 2π] and range of [0, 1]
        :param test: If True, saves intermediate steps to the debug/debug_save directory for debugging purposes. Default is False.
        :type test: bool
        :return: None. The mesh is modified in place.
        :raises TypeError: If mesh is not a trimesh.Trimesh object, iterations is not an integer, or alpha is not a number.
        :raises ValueError: If iterations is less than 1, alpha is not in the range (0, 1), if beta is not in the range [0, 1), if change_tol is negative, if the mesh is not watertight, or if e_mode is not "memory_efficient" or "time_efficient."
        """
        if not isinstance(iterations, int):
            raise TypeError("Iterations must be an integer.")
        if not isinstance(alpha, float):
            raise TypeError("Alpha must be a number.")
        if not isinstance(beta, float):
            raise TypeError("Beta must be a number.")
        if not isinstance(proximity_digits, int):
            raise TypeError("Proximity tolerance must be an int.")
        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Mesh must be a trimesh.Trimesh object.")
        if iterations < 1:
            raise ValueError("Iterations must be at least 1.")
        if alpha <= 0 or alpha >= 1:
            raise ValueError("Alpha must be in the range (0, 1).")
        if beta < 0 or beta >= 1:
            raise ValueError("Beta must be in the range [0, 1).")
        if proximity_digits < 1:
            raise ValueError("Proximity tolerance must be non-negative.")
        if mesh.is_empty:
            return
        if not mesh.is_watertight:
            raise ValueError("Mesh must be watertight to perform smoothing.")

        for _ in range(iterations):
            SubdivisionSmoothing._edge_erosion_subdivision(mesh, alpha, beta, proximity_digits, interp, test)

    @staticmethod
    def _edge_erosion_subdivision(mesh: trimesh.Trimesh, alpha: float, beta: float, proximity_digits: int = 6, interp: Callable | None = None, test = False):
        """
        Smooth a mesh in place using intelligent edge and vertex addition. Private method that performs the actual smoothing with no input validation.

        :param mesh: The mesh to smooth.
        :type mesh: trimesh.Trimesh
        :param alpha: A scaling factor for where new vertices are placed relative to existing vertices.
        :type alpha: float
        :param beta: A scaling factor for the amount of change applied to each existing vertex and edge.
        :type beta: float
        :param proximity_digits: Number of digits to round vertex positions to for proximity checks. Default is 6.
        :type proximity_digits: int
        :param interp: An optional pre-defined interpolation function to use for determining new vertex positions based on edge angles. If None, a default spline will be used. Default is None.
        :type interp: Callable | None
        .. note::
            This parameter should be the actual interpolation function, not a callable that returns the function. It is recommended for it to have a minimum domain of [-π, 2π] and range of [0, 1]
        :param test: If True, saves intermediate steps to the debug/debug_save directory for debugging purposes. Default is False.
        :type test: bool
        :return: An ndarray, shape (n, 2), of edges to feed into ExtendedTrimesh.simple_smooth for the best smoothing results.
        :rtype: np.ndarray
        """
        # Get base values
        if interp is None:
            spline_set = np.array([[-np.pi * 1 / 1, 0            ],
                                   [-np.pi * 4 / 5, alpha * 1 / 2],
                                   [-np.pi * 3 / 4, alpha * 2 / 3],
                                   [-np.pi * 1 / 2, alpha * 1 / 1],
                                   [-np.pi * 2 / 5, alpha * 1 / 2],
                                   [-np.pi * 1 / 4, alpha * 1 / 3],
                                   [0,              0            ],
                                   [np.pi * 1 / 5,  alpha * 1 / 2],
                                   [np.pi * 1 / 2,  alpha * 1 / 1],
                                   [np.pi * 3 / 4,  alpha * 1 / 2],
                                   [np.pi * 4 / 5,  alpha * 1 / 3],
                                   [np.pi * 1 / 1,  0            ],
                                   [np.pi * 6 / 5,  alpha * 1 / 2],
                                   [np.pi * 5 / 4,  alpha * 2 / 3],
                                   [np.pi * 3 / 2,  alpha * 1 / 1],
                                   [np.pi * 8 / 5,  alpha * 1 / 2],
                                   [np.pi * 7 / 4,  alpha * 1 / 3],
                                   [np.pi * 2 / 1,  0            ]])
            w = np.array([4, 1, 2, 3, 1, 2, 4, 1, 3, 2, 1, 4, 1, 2, 3, 1, 2, 4])
            interp = InterpolatedUnivariateSpline(spline_set.T[0], spline_set.T[1], bbox=[-np.pi, 2 * np.pi], w=w, ext=1)

        if test:
            mesh.export("../../debug/debug_save/init_trimesh_model.obj")  # Debugging output
        edges = mesh.face_adjacency_edges
        neighbors = mesh.face_adjacency
        angles = SubdivisionSmoothing._get_signed_angles(mesh)
        new_factors = interp(angles)
        edge_norms = SubdivisionSmoothing._get_edge_normals(mesh)
        i_edge_norms = -edge_norms

        # Calculate intermediate values
        opposites1 = SubdivisionSmoothing._get_opposite(mesh.faces[neighbors.T[0]], edges)
        opposites2 = SubdivisionSmoothing._get_opposite(mesh.faces[neighbors.T[1]], edges)
        if test:
            np.savez_compressed("../../debug/debug_save/debug_opposites", edges=mesh.vertices[edges], opposites=mesh.vertices[np.column_stack((opposites1, opposites2))])  # Debugging output
        face1_edge1_int = mesh.vertices[edges[:, 0]] * (1 - new_factors)[:, None] + mesh.vertices[opposites1] * new_factors[:, None]
        face1_edge2_int = mesh.vertices[edges[:, 1]] * (1 - new_factors)[:, None] + mesh.vertices[opposites1] * new_factors[:, None]
        face2_edge1_int = mesh.vertices[edges[:, 0]] * (1 - new_factors)[:, None] + mesh.vertices[opposites2] * new_factors[:, None]
        face2_edge2_int = mesh.vertices[edges[:, 1]] * (1 - new_factors)[:, None] + mesh.vertices[opposites2] * new_factors[:, None]

        if test:
            np.savez_compressed("../../debug/debug_save/debug_init_intersections", init_points=mesh.vertices[edges], intersections=np.stack([face1_edge1_int, face1_edge2_int, face2_edge1_int, face2_edge2_int], axis=1))  # Debugging output

        face1_change1 = face1_edge1_int - mesh.vertices[edges[:, 0]]
        face1_change2 = face1_edge2_int - mesh.vertices[edges[:, 1]]
        face2_change1 = face2_edge1_int - mesh.vertices[edges[:, 0]]
        face2_change2 = face2_edge2_int - mesh.vertices[edges[:, 1]]

        dist1 = np.vecdot(face1_change1, i_edge_norms, axis=1)
        dist2 = np.vecdot(face2_change1, i_edge_norms, axis=1)
        dist12 = np.column_stack([dist1, dist2])
        dists = np.where(np.abs(dist1) < np.abs(dist2), dist1, dist2)
        """
        changes = dists[:, None] * i_edge_norms
        np.savez_compressed("debug/debug_save/debug_changes_calc", init_points=mesh.vertices[edges], changes=np.repeat(changes[:, None, :], 2, axis=1), norms=np.repeat(i_edge_norms[:, None, :], 2, axis=1))  # Debugging output
        """

        # Find actual intersection points
        face1_int1 = mesh.vertices[edges[:, 0]] + (face1_change1 * np.abs(dists[:, None])) / np.where(np.linalg.norm(face1_change1, axis=1) == 0, 1, np.linalg.norm(face1_change1, axis=1))[:, None]
        face1_int1[np.linalg.norm(face1_change1, axis=1) == 0] = mesh.vertices[edges[:, 0]][np.linalg.norm(face1_change1, axis=1) == 0]
        face1_int2 = mesh.vertices[edges[:, 1]] + (face1_change2 * np.abs(dists[:, None])) / np.where(np.linalg.norm(face1_change2, axis=1) == 0, 1, np.linalg.norm(face1_change2, axis=1))[:, None]
        face1_int2[np.linalg.norm(face1_change2, axis=1) == 0] = mesh.vertices[edges[:, 1]][np.linalg.norm(face1_change2, axis=1) == 0]
        face2_int1 = mesh.vertices[edges[:, 0]] + (face2_change1 * np.abs(dists[:, None])) / np.where(np.linalg.norm(face2_change1, axis=1) == 0, 1, np.linalg.norm(face2_change1, axis=1))[:, None]
        face2_int1[np.linalg.norm(face2_change1, axis=1) == 0] = mesh.vertices[edges[:, 0]][np.linalg.norm(face2_change1, axis=1) == 0]
        face2_int2 = mesh.vertices[edges[:, 1]] + (face2_change2 * np.abs(dists[:, None])) / np.where(np.linalg.norm(face2_change2, axis=1) == 0, 1, np.linalg.norm(face2_change2, axis=1))[:, None]
        face2_int2[np.linalg.norm(face2_change2, axis=1) == 0] = mesh.vertices[edges[:, 1]][np.linalg.norm(face2_change2, axis=1) == 0]

        # Add vertices to the mesh
        new_vertices_debug = np.stack([face1_int1, face1_int2, face2_int1, face2_int2], axis=1)
        new_vertices = np.vstack([face1_int1, face1_int2, face2_int1, face2_int2])
        old_verts = mesh.vertices.copy()

        if test:
            arrow_dirs = np.stack(arrays=[np.where(np.linalg.norm(face1_change1, axis=1)[:, None] != 0, (face1_change1 * np.abs(dists[:, None])) / np.linalg.norm(face1_change1, axis=1)[:, None], face1_change1 * 0),
                                          np.where(np.linalg.norm(face1_change2, axis=1)[:, None] != 0, (face1_change2 * np.abs(dists[:, None])) / np.linalg.norm(face1_change2, axis=1)[:, None], face1_change2 * 0),
                                          np.where(np.linalg.norm(face2_change1, axis=1)[:, None] != 0, (face2_change1 * np.abs(dists[:, None])) / np.linalg.norm(face2_change1, axis=1)[:, None], face2_change1 * 0),
                                          np.where(np.linalg.norm(face2_change2, axis=1)[:, None] != 0, (face2_change2 * np.abs(dists[:, None])) / np.linalg.norm(face2_change2, axis=1)[:, None], face2_change2 * 0)],
                                  axis=1)
            arrow_starts=np.stack(arrays=[mesh.vertices[edges[:, 0]],
                                          mesh.vertices[edges[:, 1]],
                                          mesh.vertices[edges[:, 0]],
                                          mesh.vertices[edges[:, 1]]], axis=1)
            np.savez_compressed("../../debug/debug_save/debug_changes", init_points=old_verts[edges], final_points=new_vertices_debug, arrow_dirs=arrow_dirs, arrow_starts=arrow_starts) # Debugging output

        new_vert_inds = np.arange(old_verts.shape[0], old_verts.shape[0] + new_vertices.shape[0])
        edges = np.sort(mesh.face_adjacency_edges, axis=1)
        new_vertices = np.vstack([mesh.vertices, new_vertices])

        # Add vertices to the graph
        face1_int1_edges = np.sort(np.column_stack([edges[:, 0], opposites1]), axis=1)
        face1_int2_edges = np.sort(np.column_stack([edges[:, 1], opposites1]), axis=1)
        face2_int1_edges = np.sort(np.column_stack([edges[:, 0], opposites2]), axis=1)
        face2_int2_edges = np.sort(np.column_stack([edges[:, 1], opposites2]), axis=1)
        new_vert_edges = np.sort(np.vstack(
            [face1_int1_edges[:, None, :], face1_int2_edges[:, None, :], face2_int1_edges[:, None, :],
             face2_int2_edges[:, None, :]]), axis=1)
        new_vert_edge_inds = SubdivisionSmoothing._get_row_inds(new_vert_edges, edges)
        sort_idx = np.argsort(new_vert_edge_inds)
        sorted_vert_edge_inds = new_vert_edge_inds[sort_idx]
        sorted_verts = new_vert_inds[sort_idx]
        unique_edge_inds, group_starts = np.unique(sorted_vert_edge_inds, return_index=True)
        verts_by_edge = np.array(np.split(sorted_verts, group_starts[1:]))

        if test:
            np.savez_compressed("../../debug/debug_save/debug_point_sorting",
                                verts_by_edge=new_vertices[verts_by_edge])  # Debugging output

        dist_from_start = np.linalg.norm(new_vertices[verts_by_edge] - new_vertices[edges[:, 0]][:, None, :], axis=2)
        edge_dirs = new_vertices[edges[:, 1]] - new_vertices[edges[:, 0]]
        order = np.argsort(dist_from_start, axis=1)
        verts_by_edge = np.take_along_axis(verts_by_edge, order, axis=1)

        if test:
            np.savez_compressed("../../debug/debug_save/debug_point_dirs", verts_by_edge=new_vertices[verts_by_edge],
                                starts=new_vertices[edges[:, 0]], edge_dirs=edge_dirs)  # Debugging output

        polygons = SubdivisionSmoothing._add_verts_to_edge(mesh, edges, verts_by_edge)

        if test:
            np.savez_compressed("../../debug/debug_save/debug_polygons", vertices=new_vertices, polygons=polygons) # Debugging output
            np.savez_compressed("../../debug/debug_save/debug_triangles", vertices=new_vertices, triangles=SubdivisionSmoothing._triangulate_polygons(polygons, flatten=False)) # Debugging output

        new_triangles = SubdivisionSmoothing._triangulate_polygons(polygons, flatten=True)

        # Add new faces to the mesh and process it
        mesh.vertices = new_vertices.copy()
        mesh.faces = new_triangles

        if test:
            temp_mesh = trimesh.Trimesh(mesh.vertices.copy(), mesh.faces.copy())
            temp_mesh.process()
            temp_mesh._cache.clear()
            temp_mesh.merge_vertices(digits_vertex=proximity_digits)
            SubdivisionSmoothing._remove_degen_faces(temp_mesh)
            trimesh.repair.fill_holes(temp_mesh)
            temp_mesh.remove_unreferenced_vertices()
            temp_mesh.process()
            temp_mesh._cache.clear()
            temp_mesh.export("debug/debug_save/middle_trimesh_model.obj")  # Debugging output

        # Calculate edge changes
        edge_factor = dists * beta
        edge_vectors = mesh.vertices[edges[:, 1]] - mesh.vertices[edges[:, 0]]
        edge_vectors /= np.linalg.norm(edge_vectors, axis=1)[:, None]
        plane_norms = np.cross(edge_vectors, edge_norms)
        plane_norms /= np.linalg.norm(plane_norms, axis=1)[:, None]

        """ Method 1 (Face-Based Vectors + Total Edge Move)
        target = np.average(np.stack([mesh.vertices[opposites1], mesh.vertices[opposites2]], axis=1), axis=1)
        e1_vec_unit = target - mesh.vertices[edges[:, 0]] # Calculate a rough edge vector by average the vectors to each face intersection point, therefore accounting for some inward movement instead of just along the edge normal
        e1_vec_unit /= np.linalg.norm(e1_vec_unit, axis=1)[:, None] # Normalize the calculated edge vector
        i_norm_e1_diff = np.vecdot(e1_vec_unit, plane_norms, axis=1)[:, None] * plane_norms # Get the component of the calculated edge vector that is perpendicular to the inverse edge normal and the edge vector
        e1_adjusted_vec = e1_vec_unit - i_norm_e1_diff # Remove the perpendicular component from the calculated edge vector to get a vector that is only along the inverse edge normal and the edge vector
        e1_adjusted_vec /= np.linalg.norm(e1_adjusted_vec, axis=1)[:, None] # Normalize the adjusted edge vector
        e1_i_edge_dot = np.vecdot(e1_adjusted_vec, i_edge_norms, axis=1) # Get the similarity between the inverse edge normal and the adjusted edge vector
        e1_vec = e1_adjusted_vec * np.where(e1_i_edge_dot != 0, (edge_factor**2 / e1_i_edge_dot), 0)[:, None] # Scale the adjusted edge vector by the right amount to match the desired edge movement along the inverse edge normal

        e2_vec_unit = target - mesh.vertices[edges[:, 1]] # Calculate a rough edge vector by average the vectors to each face intersection point, therefore accounting for some inward movement instead of just along the edge normal
        e2_vec_unit /= np.linalg.norm(e2_vec_unit, axis=1)[:, None] # Normalize the calculated edge vector
        i_norm_e2_diff = np.vecdot(e2_vec_unit, plane_norms, axis=1)[:, None] * plane_norms # Get the component of the calculated edge vector that is perpendicular to the inverse edge normal and the edge vector
        e2_adjusted_vec = e2_vec_unit - i_norm_e2_diff # Remove the perpendicular component from the calculated edge vector to get a vector that is only along the inverse edge normal and the edge vector
        e2_adjusted_vec /= np.linalg.norm(e2_adjusted_vec, axis=1)[:, None] # Normalize the adjusted edge vector
        e2_i_edge_dot = np.vecdot(e2_adjusted_vec, i_edge_norms, axis=1) # Get the similarity between the inverse edge normal and the adjusted edge vector
        e2_vec = e2_adjusted_vec * np.where(e2_i_edge_dot != 0, (edge_factor**2 / e2_i_edge_dot), 0)[:, None] # Scale the adjusted edge vector by the right amount to match the desired edge movement along the inverse edge normal

        np.savez_compressed("debug/debug_save/debug_edge_vectors", vertices=new_vertices, edges=edges, rough_edge_vectors=np.stack([e1_vec_unit, e2_vec_unit], axis=1), adjusted_edge_vectors=np.stack([e1_adjusted_vec, e2_adjusted_vec], axis=1), final_edge_vectors=np.stack([e1_vec, e2_vec], axis=1), edge_vectors=edge_vectors, norms=edge_norms, planes=plane_norms, target=i_edge_norms * edge_factor[:, None])  # Debugging output

        #np.savez_compressed("debug/debug_save/debug_edge_changes", vertices=mesh.vertices, edges=mesh.vertices[edges], changes=np.stack([e1_vec, e2_vec], axis=1), combined=vert_moves_temp, norms=i_edge_norms)  # Debugging output
        # Method 1.1 Edge Movement + Minimum Vertex Movement
        # Calculate vertex changes
        vert_vecs_init = target[:, None, :] - mesh.vertices[verts_by_edge]
        vert_vecs_unit = vert_vecs_init / np.linalg.norm(vert_vecs_init, axis=2)[:, :, None]
        vert_vec_diffs = np.vecdot(vert_vecs_unit, np.repeat(plane_norms[:, None, :], 4, axis=1), axis=2)[:, :, None] * plane_norms[:, None, :]
        vert_vecs_unit = vert_vecs_unit - vert_vec_diffs
        vert_vecs_unit /= np.linalg.norm(vert_vecs_unit, axis=2)[:, :, None]
        vert_i_edge_dots = np.vecdot(vert_vecs_unit, i_edge_norms[:, None, :], axis=2)
        vert_vecs = vert_vecs_unit * ((edge_factor**2)[:, None] / vert_i_edge_dots)[:, :, None]

        vert_moves_init = np.zeros(mesh.vertices.shape, dtype=mesh.vertices.dtype)
        np.add.at(vert_moves_init, verts_by_edge[:, 0], vert_vecs[:, 0])
        np.add.at(vert_moves_init, verts_by_edge[:, 1], vert_vecs[:, 1])
        np.add.at(vert_moves_init, verts_by_edge[:, 2], vert_vecs[:, 2])
        np.add.at(vert_moves_init, verts_by_edge[:, 3], vert_vecs[:, 3])
        np.add.at(vert_moves_init, edges[:, 0], e1_vec)
        np.add.at(vert_moves_init, edges[:, 1], e2_vec)
        vert_move_norms = np.linalg.norm(vert_moves_init, axis=1)
        vert_moves_unit = vert_moves_init / np.where(vert_move_norms != 0, vert_move_norms, 1)[:, None]
        
        ignore_main = set()
        for _ in range(4):
            mesh.faces, ignore = ExtendedTrimesh.combine_vertices(mesh, 10 ** -proximity_digits)
            ignore_main.update(ignore)

        ignore = np.array(list(ignore_main), dtype=np.int64)
        

        # TODO: Consider neighbor based edge vertex changes, then edge vertex based vertex changes.
        vert_moves = ExtendedTrimesh._compute_vertex_changes(mesh.vertices, vert_vecs, np.stack([e1_vec, e2_vec], axis=1), verts_by_edge, edges, vert_moves_unit)

        np.savez_compressed("debug/debug_save/debug_vertex_moves", vertices=new_vertices, vert_moves_unit=vert_moves_unit, vert_moves=vert_moves, edge_moves=np.stack([e1_vec, e2_vec], axis=1), edges=edges, verts_by_edge=verts_by_edge, vert_vecs=vert_vecs)  # Debugging output

        # Method 2 (Edge-Based Vectors + Minimum Vertex Movement)
        vert_moves_init = np.zeros(mesh.vertices.shape, dtype=mesh.vertices.dtype)
        np.add.at(vert_moves_init, edges[:, 0], e1_vec)
        np.add.at(vert_moves_init, edges[:, 1], e2_vec)
        vert_move_norms = np.linalg.norm(vert_moves_init, axis=1)
        vert_moves_unit = vert_moves_init / np.where(vert_move_norms != 0, vert_move_norms, 1)[:, None]

        copy_mesh = trimesh.Trimesh(mesh.vertices.copy(), mesh.faces.copy())
        copy_mesh.merge_vertices(digits_vertex=proximity_digits)
        mesh.faces = copy_mesh.faces

        nbrs = NumbaList()
        for i in range(mesh.vertices.shape[0]):
            if len(mesh.vertex_neighbors[i]) != 0:
                nbrs.append(NumbaList(mesh.vertex_neighbors[i]))
            else:
                nbrs.append(NumbaList.empty_list(numba.types.int64))
        vert_moves = ExtendedTrimesh._compute_edge_changes(mesh.vertices, edges, vert_moves_unit, nbrs) * beta
        np.savez_compressed("debug/debug_save/debug_edge_moves", vertices=new_vertices, vert_moves_unit=vert_moves_unit, vert_moves=vert_moves, edge_moves=np.stack([e1_vec, e2_vec], axis=1), edges=edges)  # Debugging output
        dist_from_start = np.linalg.norm(new_vertices[verts_by_edge] - new_vertices[edges[:, 0]][:, None, :], axis=2)
        edge_dists = np.linalg.norm(new_vertices[edges[:, 1]] - new_vertices[edges[:, 0]], axis=1)
        weights = np.stack([dist_from_start, edge_dists[:, None] - dist_from_start], axis=2)
        middle_vert_affectors = np.stack([vert_moves[edges[:, 0]], vert_moves[edges[:, 1]]], axis=1)
        middle_vert_affectors = np.repeat(middle_vert_affectors[:, None, :, :], 4, axis=1)
        middle_vert_moves = np.average(middle_vert_affectors, axis=2, weights=np.repeat(weights[:, :, :, None], 3, axis=3))
        i_middle_verts_dot = np.vecdot(middle_vert_moves, plane_norms[:, None, :], axis=2)
        middle_vert_moves_adjusted = middle_vert_moves - i_middle_verts_dot[:, :, None] * plane_norms[:, None, :]
        np.add.at(vert_moves, verts_by_edge[:, 0], middle_vert_moves_adjusted[:, 0])
        np.add.at(vert_moves, verts_by_edge[:, 1], middle_vert_moves_adjusted[:, 1])
        np.add.at(vert_moves, verts_by_edge[:, 2], middle_vert_moves_adjusted[:, 2])
        np.add.at(vert_moves, verts_by_edge[:, 3], middle_vert_moves_adjusted[:, 3])
        """

        face1_int1_inds = np.arange(old_verts.shape[0], old_verts.shape[0] + face1_int1.shape[0])
        face1_int2_inds = np.arange(old_verts.shape[0] + face1_int1.shape[0], old_verts.shape[0] + face1_int1.shape[0] + face1_int2.shape[0])
        face2_int1_inds = np.arange(old_verts.shape[0] + face1_int1.shape[0] + face1_int2.shape[0], old_verts.shape[0] + face1_int1.shape[0] + face1_int2.shape[0] + face2_int1.shape[0])
        face2_int2_inds = np.arange(old_verts.shape[0] + face1_int1.shape[0] + face1_int2.shape[0] + face2_int1.shape[0], old_verts.shape[0] + face1_int1.shape[0] + face1_int2.shape[0] + face2_int1.shape[0] + face2_int2.shape[0])
        edge_set = np.vstack([np.column_stack([face1_int1_inds, face1_int2_inds]), np.column_stack([face2_int1_inds, face2_int2_inds])])

        old_vertices = mesh.vertices.copy()

        #mesh.vertices += vert_moves

        #np.savez_compressed("debug/debug_save/debug_final_changes", new_vertices=mesh.vertices, old_vertices=old_vertices, faces=mesh.faces, edges=edges, verts_by_edge=verts_by_edge, moves=vert_moves) # Debugging output

        # Cleanup
        #mesh.merge_vertices(digits_vertex=proximity_digits)
        mesh.faces = SubdivisionSmoothing.combine_vertices(mesh, 10 ** -proximity_digits)[0]
        SubdivisionSmoothing._remove_degen_faces(mesh)
        trimesh.repair.fill_holes(mesh)
        mesh.process()

        if test:
            mesh.export("../../debug/debug_save/final_trimesh_model.obj")  # Debugging output
        return edge_set

    @staticmethod
    @njit()
    def _compute_edge_changes(vertices: np.ndarray, edges: np.ndarray, vert_moves_unit: np.ndarray, neighbors: numba.typed.List):
        """
        Compute the change in for each original vertices (the ones that were present before edge subdivision) based on the provided vertices and neighbors. Private method that performs the actual computation with no input validation.
        .. note::
            This method is not meant to be used externally, only by the edge_erosion_subdivision method (for numba optimization), and therefore does not have a public counterpart and has limited documentation)

        :param vertices: The vertices of the mesh, shape (m, 3) where m is the number of vertices in the mesh.
        :type vertices: np.ndarray
        :param edges: The edge endpoint vertex indices, shape (n, 2), where n is the number of edges
        :type edges: np.ndarray
        :param vert_moves_unit: The unit movement vectors for each vertex in the mesh, shape (m, 3) where m is the number of vertices in the mesh.
        :type vert_moves_unit: np.ndarray
        :param neighbors: The neighboring vertex indices for each vertex.
        :type neighbors: numba.typed.List
        :return: The movement vector for each original vertex in the mesh, shape (k, 3) where k is the number of original vertices in the mesh.
        :rtype: np.ndarray
        """
        vert_move_min_proj_dist = np.full(vertices.shape[0], np.inf)
        for i in range(edges.shape[0]):
            for j in range(2):
                v = edges[i, j]
                for k in range(len(neighbors[v])):
                    nbr = neighbors[v][k]
                    vec = vertices[nbr] - vertices[v]
                    if np.linalg.norm(vec) == 0:
                        continue
                    proj_dist = np.dot(vec, vert_moves_unit[v])
                    if np.abs(proj_dist) < np.abs(vert_move_min_proj_dist[v]):
                        vert_move_min_proj_dist[v] = proj_dist
        vert_moves = vert_moves_unit * np.where(vert_move_min_proj_dist[:, None] != np.inf, vert_move_min_proj_dist[:, None], 0)
        return vert_moves

    @staticmethod
    def combine_vertices(mesh: trimesh.Trimesh, tol: float = 1e-6):
        """
        Combine vertices that are within a certain tolerance of each other. Public method that validates input types and dimensions.

        :param mesh: The mesh to process.
        :type mesh: trimesh.Trimesh
        :param tol: The tolerance for considering two vertices as the same. Default is 1e-6.
        :type tol: float
        :return: The updated faces and a list of removed vertex indices.
        :rtype: Tuple[np.ndarray, List[int]]
        :raises TypeError: If mesh is not a trimesh.Trimesh instance or if tol is not a float.
        :raises ValueError: If tol is not positive.
        """
        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Mesh must be a trimesh.Trimesh instance.")
        if not isinstance(tol, float):
            raise TypeError("Tolerance must be a float.")
        if tol <= 0:
            raise ValueError("Tolerance must be positive.")
        if mesh.is_empty:
            return

        neighbors = NumbaList()
        for item in mesh.vertex_neighbors:
            if len(item) == 0:
                neighbors.append(np.empty(0, dtype=np.int64))
            else:
                neighbors.append(np.array(item, dtype=np.int64))
        return SubdivisionSmoothing._combine_vertices(mesh.vertices, mesh.faces, neighbors, tol)

    @staticmethod
    @njit()
    def _combine_vertices(verts: np.ndarray, faces: np.ndarray, neighbors: numba.typed.List, tol=1e-6):
        """
        Combine vertices that are within a certain tolerance of each other. Private method that performs the actual combination with no input validation.

        :param verts: The vertices of the mesh, shape (m, n) where m is the number of vertices and n is the dimension (usually 3).
        :type verts: np.ndarray
        :param faces: The faces of the mesh, shape (k, l) where k is the number of faces and l is the number of vertices per face.
        :type faces: np.ndarray
        :param neighbors: The neighboring vertex indices for each vertex.
        :type neighbors: numba.typed.List
        :param tol: The tolerance for considering two vertices as the same. Default is 1e-6.
        :type tol: float
        :return: The updated faces and a list of removed vertex indices.
        :rtype: Tuple[np.ndarray, List[int]]
        """

        faces = faces.copy()
        to_remove = []
        for i, nbrs in enumerate(neighbors):
            if i in to_remove:
                continue
            for nbr in nbrs:
                if nbr in to_remove:
                    continue
                if np.allclose(verts[i], verts[nbr], atol=tol):
                    for face in faces:
                        face[face == nbr] = i
                    to_remove.append(nbr)
        return faces, to_remove

    @staticmethod
    def triangulate_polygons(polygons: np.ndarray, flatten: bool = True):
        """
        Returns faces created by triangulating all input polygons. Public method that validates input types and dimensions.

        .. note::
            This method is specialized, and only works with polygons that have exactly 15 vertices. For general polygon triangulation, consider using methods like mapbox-earcut, or scipy.spatial.Delaunay

        :param polygons: An ndarray of polygons shaped (n, 15), where each polygon is a list of vertex indices and n is the number of polygons. Polygons must have exactly 15 vertices.
        :type polygons: ndarray
        :param flatten: If True, return a flat array of shape (n*13, 3) where n is the number of original polygons. If False, return an array of shape (n, 13, 3) where each sub-array contains the triangles for that polygon. Default is True.
        :type flatten: bool
        :return: The triangulated faces
        :rtype: np.ndarray
        :raises TypeError: If polygons is not a numpy ndarray or if flatten is not a boolean.
        :raises ValueError: If polygons is not a 2D array with shape (n, 15).
        """
        if len(polygons) == 0:
            return np.zeros((0, 3), dtype=int) if flatten else np.zeros((0, 13, 3), dtype=int)
        if not isinstance(polygons, np.ndarray):
            raise TypeError("Polygons must be a numpy ndarray with shape (n, 15).")
        if polygons.ndim != 2 or polygons.shape[1] != 15:
            raise ValueError("Polygons must be a 2D array with shape (n, 15).")
        if not isinstance(flatten, bool):
            raise TypeError("Flatten must be a boolean.")

        return SubdivisionSmoothing._triangulate_polygons(polygons, flatten)

    @staticmethod
    def _triangulate_polygons(polygons: np.ndarray, flatten: bool = True):
        """
        Returns a list of edges to create to triangulate every polygon. Private method that performs the actual triangulation with no input validation.

        .. note::
            This method is specialized, and only works with polygons that have exactly 15 vertices. For general polygon triangulation, consider using methods like mapbox-earcut, or scipy.spatial.Delaunay

        :param polygons: An ndarray of polygons shaped (n, 15), where each polygon is a list of vertex indices and n is the number of polygons. Polygons must have exactly 15 vertices.
        :type polygons: ndarray
        :param flatten: If True, return a flat array of shape (n*13, 3) where n is the number of original polygons. If False, return an array of shape (n, 13, 3) where each sub-array contains the triangles for that polygon. Default is True.
        :type flatten: bool
        :return: The triangulated faces
        :rtype: np.ndarray
        """
        face1 = polygons[:, [14, 0, 1]]
        face2 = polygons[:, [4, 5, 6]]
        faces3 = polygons[:, [9, 10, 11]]
        faces4 = polygons[:, [14, 1, 2]]
        faces5 = polygons[:, [4, 6, 7]]
        faces6 = polygons[:, [9, 11, 12]]
        faces7 = polygons[:, [13, 14, 2]]
        faces8 = polygons[:, [3, 4, 7]]
        faces9 = polygons[:, [8, 9, 12]]
        faces10 = polygons[:, [13, 2, 3]]
        faces11 = polygons[:, [3, 7, 8]]
        faces12 = polygons[:, [8, 12, 13]]
        faces13 = polygons[:, [13, 3, 8]]
        if flatten:
            all_faces = np.vstack((face1, face2, faces3, faces4, faces5, faces6, faces7, faces8, faces9, faces10, faces11, faces12, faces13))
        else:
            all_faces = np.stack((face1, face2, faces3, faces4, faces5, faces6, faces7, faces8, faces9, faces10, faces11, faces12, faces13), axis=1)
        return all_faces

    @staticmethod
    def add_verts_to_edge(mesh: trimesh.Trimesh, edges: np.ndarray, replacements: np.ndarray):
        """
        Add new vertices to a mesh along specified edges. Public method that validates input types and dimensions.

        :param mesh: The mesh to modify.
        :type mesh: trimesh.Trimesh
        :param edges: An ndarray of shape (n, 2) of edges or pairs of vertex indices, where n is the number of edges. Each edge must exist in the mesh.
        :type edges: np.ndarray
        :param replacements: An ndarray of shape (n, m) of new vertex positions to add along each edge, where m is the number of new vertices to add per edge. Each row must correspond to the edge in the same row of edges.
        :type replacements: np.ndarray
        :return: An ndarray of polygons shaped (n, 3m+3)
        :rtype: np.ndarray
        :raises TypeError: If mesh is not a trimesh.Trimesh object, if edges or replacements are not numpy ndarrays.
        :raises ValueError: If edges is not a 2D array with shape (n, 2), if replacements is not a 2D array with shape (n, m), if edges and replacements have different first dimensions, or if the mesh is empty.
        """
        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Mesh must be a trimesh.Trimesh object.")
        if not isinstance(edges, np.ndarray):
            raise TypeError("Edges must be a numpy ndarray.")
        if not isinstance(replacements, np.ndarray):
            raise TypeError("Replacements must be a numpy ndarray.")
        if edges.ndim != 2 or edges.shape[1] != 2:
            raise ValueError("Edges must be a 2D array with shape (n, 2).")
        if replacements.ndim != 2:
            raise ValueError("Replacements must be a 2D array with shape (n, m).")
        if edges.shape[0] != replacements.shape[0]:
            raise ValueError("Edges and replacements must have the same first dimension.")
        if edges.shape[0] == 0:
            return
        if mesh.is_empty:
            return

        return SubdivisionSmoothing._add_verts_to_edge(mesh, edges, replacements)

    @staticmethod
    def _add_verts_to_edge(mesh: trimesh.Trimesh, edges: np.ndarray, replacements: np.ndarray):
        """
        Add new vertices to a mesh along specified edges. Private method that performs the actual addition with no input validation.

        :param mesh: The mesh to modify.
        :type mesh: trimesh.Trimesh
        :param edges: An ndarray of shape (n, 2) of edges or pairs
        :type edges: np.ndarray
        :param replacements: An ndarray of shape (n, m) of new vertex positions to add along each edge, where m is the number of new vertices to add per edge. Each row must correspond to the edge in the same row of edges.
        :type replacements: np.ndarray
        :return: An ndarray of polygons shaped (n, 3m+3)
        :rtype: np.ndarray
        """
        edges_sorted = np.sort(edges, axis=1)
        faces = mesh.faces

        edges1 = faces[:, [0, 1]]
        edges1_sort = np.argsort(edges1, axis=1)
        edges1_sorted = np.take_along_axis(edges1, edges1_sort, axis=1)
        edges2 = faces[:, [1, 2]]
        edges2_sort = np.argsort(edges2, axis=1)
        edges2_sorted = np.take_along_axis(edges2, edges2_sort, axis=1)
        edges3 = faces[:, [2, 0]]
        edges3_sort = np.argsort(edges3, axis=1)
        edges3_sorted = np.take_along_axis(edges3, edges3_sort, axis=1)

        matches1 = (edges_sorted[:, 0] == edges1_sorted[:, None, 0]) & (edges[:, 1] == edges1_sorted[:, None, 1])
        matches2 = (edges_sorted[:, 0] == edges2_sorted[:, None, 0]) & (edges[:, 1] == edges2_sorted[:, None, 1])
        matches3 = (edges_sorted[:, 0] == edges3_sorted[:, None, 0]) & (edges[:, 1] == edges3_sorted[:, None, 1])
        edges1_idx = np.where(matches1)[1]
        edges2_idx = np.where(matches2)[1]
        edges3_idx = np.where(matches3)[1]

        edges1_rep = replacements[edges1_idx]
        edges2_rep = replacements[edges2_idx]
        edges3_rep = replacements[edges3_idx]

        flip_arr = np.array([1, 0])
        flip_mask1 = (edges1_sort[:, 0] == flip_arr[None, 0]) & (edges1_sort[:, 1] == flip_arr[None, 1])
        flip_mask2 = (edges2_sort[:, 0] == flip_arr[None, 0]) & (edges2_sort[:, 1] == flip_arr[None, 1])
        flip_mask3 = (edges3_sort[:, 0] == flip_arr[None, 0]) & (edges3_sort[:, 1] == flip_arr[None, 1])
        edges1_rep[flip_mask1] = edges1_rep[flip_mask1][:, ::-1]
        edges2_rep[flip_mask2] = edges2_rep[flip_mask2][:, ::-1]
        edges3_rep[flip_mask3] = edges3_rep[flip_mask3][:, ::-1]

        new_faces = np.hstack((edges1[:, 0][:, None], edges1_rep, edges2[:, 0][:, None], edges2_rep, edges3[:, 0][:, None], edges3_rep))

        return new_faces

    @staticmethod
    def remove_degen_faces(mesh: trimesh.Trimesh):
        """
        Remove degenerate faces from a mesh by removing faces with zero area. Public method that validates input types and dimensions.

        :param mesh: The mesh to process.
        :type mesh: trimesh.Trimesh
        :return: None. The mesh is modified in place.
        :raises TypeError: If mesh is not a trimesh.Trimesh object.
        """
        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Mesh must be a trimesh.Trimesh object.")
        if mesh.is_empty:
            return

        SubdivisionSmoothing._remove_degen_faces(mesh)

    @staticmethod
    def _remove_degen_faces(mesh: trimesh.Trimesh):
        """
        Remove degenerate faces from a mesh by removing faces with zero area. Private method that performs the actual removal with no input validation.

        :param mesh: The mesh to process.
        :type mesh: trimesh.Trimesh
        :return: None. The mesh is modified in place.
        """
        areas = mesh.area_faces
        mask = areas > 1e-6
        mesh.update_faces(mask)
        mesh.remove_unreferenced_vertices()

    @staticmethod
    def closest_vertices(mesh: trimesh.Trimesh):
        """
        Find the closest vertices in a mesh to each other. Public method that validates input types and dimensions.

        :param mesh: The mesh to analyze.
        :type mesh: trimesh.Trimesh
        :return: 2 ndarrays of shape (n, 1) containing pairs of vertex indices that are closest to each other.
        :rtype: tuple(np.ndarray)
        :raises TypeError: If mesh is not a trimesh.Trimesh object.
        :raises ValueError: If mesh is empty.
        """
        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Mesh must be a trimesh.Trimesh object.")
        if mesh.is_empty:
            return np.zeros((0, 2), dtype=int)

        return SubdivisionSmoothing._closest_vertices(mesh)

    @staticmethod
    def _closest_vertices(mesh: trimesh.Trimesh):
        """
        Find the closest vertices in a mesh to each other. Private method that performs the actual computation with no input validation.

        :param mesh: The mesh to analyze.
        :type mesh: trimesh.Trimesh
        :return: 2 ndarrays of shape (n, 1) containing pairs of vertex indices that are closest to each other.
        :rtype: tuple(np.ndarray)
        """
        dists = np.linalg.norm(mesh.vertices[:, None, :] - mesh.vertices[None, :, :], axis=2)
        np.fill_diagonal(dists, np.inf)
        closest_indices = np.argmin(dists, axis=1)
        closest_distances = dists[np.arange(len(mesh.vertices)), closest_indices]
        return closest_indices, closest_distances


if __name__ == "__main__":
    # Example usage
    thing = "inward_pyramid"
    np.set_printoptions(threshold=sys.maxsize)
    mesh = trimesh.load_mesh(f"../../meshes/{thing}/{thing}.obj")
    simple_sub_mesh = ExtendedTrimesh.simple_subdivide(mesh, alpha=0.5, beta=0.5, iterations=5)
    simple_sub_mesh.export(f"../../meshes/{thing}/{thing}_simple.obj")
    simple_smooth_mesh = ExtendedTrimesh.simple_smooth(mesh, alpha=0.3, iterations=5, dist_effect="stronger")
    simple_smooth_mesh.export(f"../../meshes/{thing}/{thing}_simple_smooth.obj")
    SubdivisionSmoothing.edge_erosion_subdivision(mesh, alpha=0.9, beta=0.5, iterations=2, proximity_digits=6)
    mesh.export(f"../../meshes/{thing}/{thing}_edge_erosion3.obj")
    np.savez_compressed(f"../../debug/debug_save/broken_faces.npz", broken_faces=trimesh.repair.broken_faces(mesh), edge_face_ownership=mesh.edges_face, edges=mesh.edges, vertices=mesh.vertices, neighborhood=mesh.face_neighborhood, faces=mesh.faces)