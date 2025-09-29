"""
Basic uniform mesh refinement functions.
"""
from __future__ import absolute_import
import numpy as nm

from sfepy.discrete.fem import Mesh
from six.moves import range


def refine_1_2(mesh_in):
    """
    Refines 1D mesh by cutting each element in half
    """

    if not nm.all(mesh_in.coors[:-1] <= mesh_in.coors[1:]):
        raise ValueError("1D Mesh for refinement must have sorted coors array")

    cmesh = mesh_in.cmesh
    c_centres = cmesh.get_centroids(cmesh.tdim)
    new_coors = nm.zeros((2*mesh_in.n_nod - 1, 1))
    new_coors[0::2] = mesh_in.coors
    new_coors[1::2] = c_centres

    n_nod = len(new_coors)

    new_conn = nm.arange(n_nod, dtype=nm.uint32).repeat(2)[1:-1].reshape((-1, 2))

    new_mat_id = cmesh.cell_groups.repeat(2)

    mesh = Mesh.from_data(mesh_in.name + '_r', new_coors, None, [new_conn],
                          [new_mat_id], mesh_in.descs)
    return mesh

def refine_2_3(mesh_in):
    """
    Refines mesh out of triangles by cutting cutting each edge in half
    and making 4 new finer triangles out of one coarser one.
    """
    cmesh = mesh_in.cmesh

    # Unique edge centres.
    e_centres = cmesh.get_centroids(cmesh.tdim - 1)

    # New coordinates after the original ones.
    coors = nm.r_[mesh_in.coors, e_centres]

    o1 = mesh_in.n_nod

    cc = cmesh.get_conn(cmesh.tdim, cmesh.tdim - 1)

    conn = mesh_in.get_conn('2_3')
    n_el = conn.shape[0]

    e_nodes = cc.indices.reshape((n_el, 3)) + o1

    c, e = conn.T.astype(nm.uint32), e_nodes.T

    new_conn = nm.vstack([c[0], e[0], e[2],
                          e[0], e[1], e[2],
                          c[1], e[1], e[0],
                          c[2], e[2], e[1]]).T
    new_conn = new_conn.reshape((4 * n_el, 3))

    new_mat_id = cmesh.cell_groups.repeat(4)

    mesh = Mesh.from_data(mesh_in.name + '_r', coors, None, [new_conn],
                          [new_mat_id], mesh_in.descs )

    return mesh

def refine_2_4(mesh_in):
    """
    Refines mesh out of quadrilaterals by cutting cutting each edge in
    half and making 4 new finer quadrilaterals out of one coarser one.
    """
    cmesh = mesh_in.cmesh

    # Unique edge centres.
    e_centres = cmesh.get_centroids(cmesh.tdim - 1)

    # Unique element centres.
    centres = cmesh.get_centroids(cmesh.tdim)

    # New coordinates after the original ones.
    coors = nm.r_[mesh_in.coors, e_centres, centres]

    o1 = mesh_in.n_nod
    o2 = o1 + e_centres.shape[0]

    cc = cmesh.get_conn(cmesh.tdim, cmesh.tdim - 1)

    conn = mesh_in.get_conn('2_4')
    n_el = conn.shape[0]

    e_nodes = cc.indices.reshape((n_el, 4)) + o1
    nodes = nm.arange(n_el, dtype=nm.uint32) + o2

    c, e, b = conn.T.astype(nm.uint32), e_nodes.T, nodes.T

    new_conn = nm.vstack([c[0], e[0], b, e[3],
                          c[1], e[1], b, e[0],
                          c[2], e[2], b, e[1],
                          c[3], e[3], b, e[2]]).T
    new_conn = new_conn.reshape((4 * n_el, 4))

    new_mat_id = cmesh.cell_groups.repeat(4)

    mesh = Mesh.from_data(mesh_in.name + '_r', coors, None, [new_conn],
                          [new_mat_id], mesh_in.descs )

    return mesh

def refine_3_4(mesh_in):
    """
    Refines tetrahedra by cutting each edge in half and making 8 new
    finer tetrahedra out of one coarser one. Old nodal coordinates come
    first in `coors`, then the new ones. The new tetrahedra are similar
    to the old one, no degeneration is supposed to occur as at most 3
    congruence classes of tetrahedra appear, even when re-applied
    iteratively (provided that `conns` are not modified between two
    applications - ordering of vertices in tetrahedra matters not only
    for positivity of volumes).

    References:

    - Juergen Bey: Simplicial grid refinement: on Freudenthal s algorithm and
      the optimal number of congruence classes, Numer.Math. 85 (2000),
      no. 1, 1--29, or
    - Juergen Bey: Tetrahedral grid refinement, Computing 55 (1995),
      no. 4, 355--378, or
      http://citeseer.ist.psu.edu/bey95tetrahedral.html
    """
    cmesh = mesh_in.cmesh

    # Unique edge centres.
    e_centres = cmesh.get_centroids(cmesh.tdim - 2)

    # New coordinates after the original ones.
    coors = nm.r_[mesh_in.coors, e_centres]

    o1 = mesh_in.n_nod

    cc = cmesh.get_conn(cmesh.tdim, cmesh.tdim - 2)

    conn = mesh_in.get_conn('3_4')
    n_el = conn.shape[0]

    e_nodes = cc.indices.reshape((n_el, 6)) + o1

    c, e = conn.T.astype(nm.uint32), e_nodes.T

    new_conn = nm.vstack([c[0], e[0], e[2], e[3],
                          e[0], c[1], e[1], e[4],
                          e[2], e[1], c[2], e[5],
                          e[3], e[4], e[5], c[3],
                          e[0], e[2], e[3], e[4],
                          e[0], e[2], e[4], e[1],
                          e[2], e[3], e[4], e[5],
                          e[2], e[1], e[5], e[4]]).T

    new_conn = new_conn.reshape((8 * n_el, 4))

    new_mat_id = cmesh.cell_groups.repeat(8)

    mesh = Mesh.from_data(mesh_in.name + '_r', coors, None, [new_conn],
                          [new_mat_id], mesh_in.descs )

    return mesh

def refine_3_8(mesh_in):
    """
    Refines hexahedral mesh by cutting cutting each edge in half and
    making 8 new finer hexahedrons out of one coarser one.
    """
    cmesh = mesh_in.cmesh

    # Unique edge centres.
    e_centres = cmesh.get_centroids(cmesh.tdim - 2)

    # Unique face centres.
    f_centres = cmesh.get_centroids(cmesh.tdim - 1)

    # Unique element centres.
    centres = cmesh.get_centroids(cmesh.tdim)

    # New coordinates after the original ones.
    coors = nm.r_[mesh_in.coors, e_centres, f_centres, centres]

    o1 = mesh_in.n_nod
    o2 = o1 + e_centres.shape[0]
    o3 = o2 + f_centres.shape[0]

    ecc = cmesh.get_conn(cmesh.tdim, cmesh.tdim - 2)
    fcc = cmesh.get_conn(cmesh.tdim, cmesh.tdim - 1)

    conn = mesh_in.get_conn('3_8')
    n_el = conn.shape[0]

    st = nm.vstack

    e_nodes = ecc.indices.reshape((n_el, 12)) + o1
    f_nodes = fcc.indices.reshape((n_el, 6)) + o2
    nodes = nm.arange(n_el, dtype=nm.uint32) + o3

    c, e, f, b = conn.T.astype(nm.uint32), e_nodes.T, f_nodes.T, nodes.T

    new_conn = st([c[0], e[0], f[0], e[3], e[8], f[2], b, f[1],
                   c[1], e[1], f[0], e[0], e[9], f[4], b, f[2],
                   c[2], e[2], f[0], e[1], e[10], f[5], b, f[4],
                   c[3], e[3], f[0], e[2], e[11], f[1], b, f[5],
                   c[4], e[7], f[3], e[4], e[8], f[1], b, f[2],
                   c[5], e[4], f[3], e[5], e[9], f[2], b, f[4],
                   c[6], e[5], f[3], e[6], e[10], f[4], b, f[5],
                   c[7], e[6], f[3], e[7], e[11], f[5], b, f[1]]).T
    new_conn = new_conn.reshape((8 * n_el, 8))

    new_mat_id = cmesh.cell_groups.repeat(8)

    mesh = Mesh.from_data(mesh_in.name + '_r', coors, None, [new_conn],
                          [new_mat_id], mesh_in.descs )

    return mesh

def refine_reference(geometry, level):
    """
    Refine reference element given by `geometry`.

    Notes
    -----
    The error edges must be generated in the order of the connectivity
    of the previous (lower) level.
    """
    from sfepy.discrete.fem import FEDomain
    from sfepy.discrete.fem.geometry_element import geometry_data

    gcoors, gconn = geometry.coors, geometry.conn
    if level == 0:
        return gcoors, gconn, None

    gd = geometry_data[geometry.name]
    conn = nm.array([gd.conn], dtype=nm.int32)
    mat_id = conn[:, 0].copy()
    mat_id[:] = 0

    mesh = Mesh.from_data('aux', gd.coors, None, [conn],
                          [mat_id], [geometry.name])
    domain = FEDomain('aux', mesh)

    for ii in range(level):
        domain = domain.refine()

    coors = domain.mesh.coors
    conn = domain.get_conn()

    n_el = conn.shape[0]

    if geometry.name == '2_3':
        aux_conn = conn.reshape((n_el // 4, 4, 3))

        ir = [[0, 1, 2], [2, 2, 3], [3, 3, 0]]
        ic = [[0, 0, 0], [0, 1, 0], [0, 1, 0]]

    elif geometry.name == '2_4':
        aux_conn = conn.reshape((n_el // 4, 4, 4))

        ir = [[0, 0, 1], [1, 1, 2], [2, 2, 3], [3, 3, 0], [0, 0, 2], [3, 3, 1]]
        ic = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 2, 1], [1, 2, 1]]

    elif geometry.name == '3_4':
        aux_conn = conn.reshape((n_el // 8, 8, 4))

        ir = [[0, 0, 1], [1, 1, 2], [2, 0, 0], [3, 1, 1], [3, 2, 2], [3, 0, 0]]
        ic = [[0, 1, 1], [1, 2, 2], [2, 2, 0], [3, 3, 1], [3, 3, 2], [3, 3, 0]]

    elif geometry.name == '3_8':
        aux_conn = conn.reshape((n_el // 8, 8, 8))

        ir = [[0, 0, 1], [1, 1, 2], [2, 2, 3], [3, 0, 0], [0, 0, 2], [0, 0, 1],
              [0, 0, 1], [1, 1, 2], [2, 2, 3], [3, 0, 0], [0, 0, 2], [0, 0, 1],
              [4, 4, 5], [5, 5, 6], [6, 6, 7], [7, 4, 4], [4, 4, 6], [4, 4, 5],
              [0, 0, 4], [1, 1, 5], [2, 2, 6], [3, 3, 7],
              [0, 0, 4], [1, 1, 5], [2, 2, 6], [0, 0, 4],
              [0, 0, 4]]
        ic = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 3, 0], [1, 2, 1], [3, 2, 1],
              [4, 5, 4], [4, 5, 4], [4, 5, 4], [4, 7, 4], [5, 6, 5], [7, 6, 5],
              [0, 3, 0], [0, 3, 0], [0, 3, 0], [0, 1, 0], [3, 2, 3], [1, 2, 3],
              [0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 4, 0],
              [1, 5, 3], [1, 5, 3], [1, 5, 3], [3, 7, 1],
              [2, 6, 2]]

    else:
        raise ValueError('unsupported geometry! (%s)' % geometry.name)

    conn = nm.array(conn, dtype=nm.int32)
    error_edges = aux_conn[:, ir, ic]

    return coors, conn, error_edges
