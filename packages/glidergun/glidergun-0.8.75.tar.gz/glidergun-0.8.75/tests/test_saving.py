import hashlib
import shutil

import rasterio

from glidergun._grid import grid
from glidergun._stack import stack

dem = grid("./.data/n55_e008_1arc_v3.bil").resample(0.01)
dem_color = grid("./.data/n55_e008_1arc_v3.bil").resample(0.01).color("terrain")

landsat = stack(
    ".data/LC08_L2SP_197021_20220324_20220330_02_T1_SR_B1.TIF",
    ".data/LC08_L2SP_197021_20220324_20220330_02_T1_SR_B2.TIF",
    ".data/LC08_L2SP_197021_20220324_20220330_02_T1_SR_B3.TIF",
    ".data/LC08_L2SP_197021_20220324_20220330_02_T1_SR_B4.TIF",
    ".data/LC08_L2SP_197021_20220324_20220330_02_T1_SR_B5.TIF",
    ".data/LC08_L2SP_197021_20220324_20220330_02_T1_SR_B6.TIF",
    ".data/LC08_L2SP_197021_20220324_20220330_02_T1_SR_B7.TIF",
)


def save(obj, file_name):
    obj.save(file_name)
    with open(file_name, "rb") as f:
        hash = hashlib.md5(f.read()).hexdigest()
    with rasterio.open(file_name) as d:
        compress = d.profile.get("compress", None)
    shutil.rmtree(".output/test")
    return hash, compress


def test_saving_dem_png():
    hash, compress = save(dem, ".output/test/dem.png")
    assert hash == "aa05e8bf7a3d9d450c6466392c3d96cd"


def test_saving_dem_jpg():
    hash, compress = save(dem, ".output/test/dem.jpg")
    assert hash


def test_saving_dem_tif():
    hash, compress = save(dem, ".output/test/dem.tif")
    assert compress == "lzw"


def test_saving_dem_img():
    hash, compress = save(dem, ".output/test/dem.img")
    assert hash == "0834c56700cf1cc3b7155a8ef6e8b922"


def test_saving_dem_bil():
    hash, compress = save(dem, ".output/test/dem.bil")
    assert hash == "ce6230320c089d41ddbc8b3f17fd0c0d"


def test_saving_dem_color_png():
    hash, compress = save(dem_color, ".output/test/dem_color.png")
    assert hash == "3a01653a1228fd4045392d2a32814ac9"


def test_saving_dem_color_jpg():
    hash, compress = save(dem_color, ".output/test/dem_color.jpg")
    assert hash


def test_saving_dem_color_tif():
    hash, compress = save(dem_color, ".output/test/dem_color.tif")
    assert compress == "lzw"


def test_saving_dem_color_img():
    hash, compress = save(dem_color, ".output/test/dem_color.img")
    assert hash == "0834c56700cf1cc3b7155a8ef6e8b922"


def test_saving_dem_color_bil():
    hash, compress = save(dem_color, ".output/test/dem_color.bil")
    assert hash == "ce6230320c089d41ddbc8b3f17fd0c0d"


def test_saving_landsat_png():
    hash, compress = save(landsat.color((5, 4, 3)), ".output/test/landsat_543_1.png")
    assert hash == "459c26b6902eac5ac9d2e01e2d5fe4bc"

    hash, compress = save(
        landsat.extract_bands(5, 4, 3), ".output/test/landsat_543_2.png"
    )
    assert hash == "459c26b6902eac5ac9d2e01e2d5fe4bc"


def test_saving_landsat_jpg():
    hash, compress = save(landsat.color((5, 4, 3)), ".output/test/landsat_543_1.jpg")
    assert hash

    hash, compress = save(
        landsat.extract_bands(5, 4, 3), ".output/test/landsat_543_2.jpg"
    )
    assert hash


def test_saving_landsat_tif():
    hash1, compress1 = save(landsat.color((5, 4, 3)), ".output/test/landsat_543_1.tif")
    hash2, compress2 = save(landsat.color((1, 2, 3)), ".output/test/landsat_543_2.tif")
    assert hash1 == hash2

    hash, compress = save(
        landsat.extract_bands(5, 4, 3), ".output/test/landsat_543_3.tif"
    )
    assert compress == "lzw"


def test_saving_landsat_img():
    hash1, compress1 = save(landsat.color((5, 4, 3)), ".output/test/landsat_543_1.img")
    hash2, compress2 = save(landsat.color((1, 2, 3)), ".output/test/landsat_543_2.img")
    assert hash1 == hash2

    hash, compress = save(
        landsat.extract_bands(5, 4, 3), ".output/test/landsat_543_3.img"
    )
    assert hash == "700167ccacd6f63a3f46fcf7c2e41f71"


def test_saving_landsat_bil():
    hash, compress = save(
        landsat.extract_bands(5, 4, 3), ".output/test/landsat_543_2.bil"
    )
    assert hash == "ff0b8c95a824c9550d12c203132ca4a9"
    assert compress is None
