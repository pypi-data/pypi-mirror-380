import enum
from dataclasses import dataclass
from struct import unpack

import pydicom
from vtkmodules.vtkCommonCore import vtkFloatArray, vtkPoints
from vtkmodules.vtkCommonDataModel import vtkCellArray, vtkPolyData


def lab_inverse(x: float) -> float:
    return x * x * x if x >= 0.20689655172413793 else 108.0 / 841.0 * (x - 4.0 / 29.0)  # noqa: PLR2004


def gamma_correction(x: float) -> float:  # noqa: PLR2004
    return 12.92 * x if x <= 0.0031306684425005883 else 1.055 * pow(x, 0.4166666666666667) - 0.055  # noqa: PLR2004


def cielab2rgb(l: float, a: float, b: float) -> tuple[float, float, float]:  # noqa: E741
    l_tmp = (l + 16.0) / 116.0

    x = 0.950456 * lab_inverse(l_tmp + a / 500.0)
    y = 1.000000 * lab_inverse(l_tmp)
    z = 1.088754 * lab_inverse(l_tmp - b / 200.0)

    r_tmp = 3.2406 * x - 1.5372 * y - 0.4986 * z
    g_tmp = -0.9689 * x + 1.8758 * y + 0.0415 * z
    b_tmp = 0.0557 * x - 0.2040 * y + 1.0570 * z

    m = min(r_tmp, b_tmp) if r_tmp <= g_tmp else min(g_tmp, b_tmp)

    if m < 0:
        r_tmp -= m
        g_tmp -= m
        b_tmp -= m
    r = gamma_correction(r_tmp)
    g = gamma_correction(g_tmp)
    b = gamma_correction(b_tmp)

    return r, g, b


def bytes2int(data: bytes, *, big_endian: bool = False) -> int:
    ba = bytearray(data)
    if big_endian:
        ba = reversed(ba)  # type: ignore
    x = 0
    for offset, byte in enumerate(ba):
        x += byte << (offset * 8)
    return x


class Representation(enum.StrEnum):
    SURFACE = 'SURFACE'
    WIREFRAME = 'WIREFRAME'
    POINTS = 'POINTS'


@dataclass
class SurfaceInfo:
    name: str
    representation: Representation
    color: tuple[float, float, float]
    opacity: float


def get_surface(s: pydicom.Dataset) -> tuple[vtkPolyData, SurfaceInfo]:
    points = _read_points(s)
    polys = _read_triangles(s)
    normals = _read_normals(s)

    poly_data = vtkPolyData()
    poly_data.SetPoints(points)
    poly_data.SetPolys(polys)
    poly_data.GetPointData().SetNormals(normals)

    info = SurfaceInfo(
        name=s.SurfaceComments,
        color=get_rgb_color(s),
        representation=Representation(s.RecommendedPresentationType),
        opacity=s.RecommendedPresentationOpacity,
    )

    return poly_data, info


def get_rgb_color(s: pydicom.Dataset) -> tuple[float, float, float]:
    cielab = s.RecommendedDisplayCIELabValue
    l = (cielab[0] / 65535.0) * 100.0  # noqa: E741
    a = ((cielab[1] - 32896.0) / 65535.0) * 255.0
    b = ((cielab[2] - 32896.0) / 65535.0) * 255.0
    return cielab2rgb(l, a, b)


def _read_triangles(s: pydicom.Dataset) -> vtkCellArray:
    t_index = s.SurfaceMeshPrimitivesSequence[0].LongTrianglePointIndexList

    polys = vtkCellArray()  # type: ignore
    z = 0
    while z < len(t_index):
        # 12 bytes to 3 dwords
        polys.InsertNextCell(3)
        idx_1 = bytes2int(t_index[z: z + 3]) - 1
        idx_2 = bytes2int(t_index[z + 4: z + 7]) - 1
        idx_3 = bytes2int(t_index[z + 8: z + 11]) - 1
        polys.InsertCellPoint(idx_1)
        polys.InsertCellPoint(idx_2)
        polys.InsertCellPoint(idx_3)
        z += 12
    return polys


def _read_normals(s: pydicom.Dataset) -> vtkFloatArray:
    sequence = s.SurfacePointsNormalsSequence[0]
    num_normals = sequence.NumberOfVectors
    dimensionality = sequence.VectorDimensionality
    vectors = sequence.VectorCoordinateData
    coordinates = unpack(f"<{int(len(vectors) / 4)}f", vectors)

    normals = vtkFloatArray()
    normals.SetNumberOfComponents(dimensionality)
    for v_index in range(num_normals):
        vector = coordinates[v_index * 3: v_index * 3 + 3]
        normals.InsertNextTypedTuple(tuple(vector))

    return normals


def _read_points(s: pydicom.Dataset) -> vtkPoints:
    point_coordinates = s.SurfacePointsSequence[0].PointCoordinatesData
    coordinates = unpack(f"<{int(len(point_coordinates) / 4)}f", point_coordinates)
    points = vtkPoints()
    num_points = len(coordinates) // 3
    for p_index in range(num_points):
        point = coordinates[p_index * 3: p_index * 3 + 3]
        points.InsertNextPoint(point)
    return points
