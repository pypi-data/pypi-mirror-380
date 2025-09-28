import pathlib
from a003558.export_blender import export_octa_cube_obj, export_label_spheres_obj

def test_export_objs(tmp_path: pathlib.Path):
    out = export_octa_cube_obj(out_dir=str(tmp_path), basename="scene")
    assert all(pathlib.Path(p).exists() for p in out.values())
    lab = export_label_spheres_obj(path=str(tmp_path / "labels.obj"))
    assert pathlib.Path(lab).exists()
