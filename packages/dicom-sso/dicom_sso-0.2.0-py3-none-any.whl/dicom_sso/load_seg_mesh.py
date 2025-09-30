""" https://gist.github.com/issakomi/29e48917e77201f2b73bfa5fe7b30451 """
import sys
from pathlib import Path

import pydicom
from vtkmodules.vtkIOGeometry import vtkSTLWriter
from vtkmodules.vtkRenderingCore import (vtkActor, vtkPolyDataMapper, vtkRenderWindow, vtkRenderWindowInteractor,
                                         vtkRenderer, vtkTextActor)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera

from dicom_sso.sso_vtk import Representation, get_surface


def load_seg_mesh(dataset: pydicom.Dataset) -> None:
    ren = vtkRenderer()
    ren.SetBackground(0.3254, 0.3490, 0.3764)

    count_surfaces = len(dataset.SurfaceSequence)
    count_points = 0
    count_polys = 0
    for s in dataset.SurfaceSequence:
        poly_data, info = get_surface(s)

        count_points += poly_data.GetPoints().GetNumberOfPoints()
        count_polys += poly_data.GetPolys().GetNumberOfCells()

        writer = vtkSTLWriter()
        writer.SetInputData(poly_data)
        writer.SetFileTypeToASCII()
        writer.SetFileName(f'{info.name}_dicom.stl')
        writer.Write()

        mapper = vtkPolyDataMapper()
        mapper.SetInputData(poly_data)

        # gen_normals = vtk.vtkPolyDataNormals()
        # gen_normals.SetInputData(poly_data)
        # gen_normals.ComputePointNormalsOn()
        # gen_normals.ComputeCellNormalsOff()
        # # noinspection PyArgumentList
        # gen_normals.Update()
        # mapper.SetInputData(gen_normals.GetOutput())

        actor = vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(*info.color)
        actor.GetProperty().SetOpacity(info.opacity)
        match info.representation:
            case Representation.SURFACE:
                actor.GetProperty().SetRepresentationToSurface()
            case Representation.WIREFRAME:
                actor.GetProperty().SetRepresentationToWireframe()
            case Representation.POINTS:
                actor.GetProperty().SetRepresentationToPoints()

        ren.AddActor(actor)

    message = str(count_surfaces) + (" surface, " if count_surfaces == 1 else " surfaces, ")
    message += str(count_points) + (" point, " if count_points == 1 else " points, ")
    message += str(count_polys) + (" triangle" if count_polys == 1 else " triangles")

    text = vtkTextActor()
    text.GetTextProperty().SetFontSize(16)
    text.GetTextProperty().SetColor(1.0, 1.0, 1.0)
    text.SetInput(message)
    text.SetPosition(4, 4)

    ren.AddViewProp(text)

    renwin = vtkRenderWindow()
    renwin.AddRenderer(ren)
    renwin.SetSize(1280, 800)

    iren = vtkRenderWindowInteractor()
    iren.SetInteractorStyle(vtkInteractorStyleTrackballCamera())
    iren.SetRenderWindow(renwin)
    iren.Initialize()
    iren.Start()


if __name__ == "__main__":
    load_seg_mesh(pydicom.dcmread(Path.resolve(Path(sys.argv[1]))))
