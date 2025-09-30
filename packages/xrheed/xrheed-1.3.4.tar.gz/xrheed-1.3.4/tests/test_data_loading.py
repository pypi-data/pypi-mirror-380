import unittest
from pathlib import Path

import numpy as np
import xarray as xr
from xrheed.loaders import load_data, load_data_manual


class TestDataLoading(unittest.TestCase):
    def setUp(self):
        self.plugin_file_map = {
            "dsnp_arpes_raw": "Si_111_7x7_112_phi_00.raw",
            "dsnp_arpes_bmp": "Test_image_UMCS_DSNP_ARPES.BMP",
        }

        self.manual_load_file = "Test_image_UMCS_DSNP_ARPES.BMP"

        # Load plugin-based images
        self.loaded_images = {}
        for plugin, filename in self.plugin_file_map.items():
            file_path = Path(__file__).parent / "data" / filename
            self.loaded_images[plugin] = load_data(file_path, plugin=plugin)

    def test_plugin_attributes(self):
        required_attrs = ["screen_scale", "beam_energy", "screen_sample_distance"]

        for plugin, image in self.loaded_images.items():
            with self.subTest(plugin=plugin):
                attrs = image.attrs
                for attr in required_attrs:
                    self.assertIn(
                        attr, attrs, msg=f"[{plugin}] Missing attribute: {attr}"
                    )
                    self.assertIsInstance(
                        attrs[attr],
                        (float, int),
                        msg=f"[{plugin}] {attr} is not a number",
                    )

    def test_dataarray_structure(self):
        for plugin, image in self.loaded_images.items():
            with self.subTest(plugin=plugin):
                # Check it's a DataArray
                self.assertIsInstance(
                    image, xr.DataArray, msg=f"[{plugin}] Not a DataArray"
                )
                self.assertIn(
                    "sx", image.dims, msg=f"[{plugin}] Missing 'sx' dimension"
                )
                self.assertIn(
                    "sy", image.dims, msg=f"[{plugin}] Missing 'sy' dimension"
                )
                self.assertEqual(len(image.shape), 2, msg=f"[{plugin}] Data is not 2D")

                # Check dtype is uint8
                self.assertEqual(
                    image.dtype, np.uint8, msg=f"[{plugin}] Data is not uint8"
                )

    def test_sy_asymmetry(self):
        for plugin, image in self.loaded_images.items():
            with self.subTest(plugin=plugin):
                sy_coords = image.coords["sy"].values

                if not np.any(sy_coords < 0) or not np.any(sy_coords > 0):
                    self.skipTest(
                        f"[{plugin}] sy axis does not span both negative and positive values"
                    )

                # Integrate over sx to get intensity profile along sy
                sy_profile = image.sum(dim="sx")

                # Separate positive and negative sy regions
                negative_sy_mask = sy_coords < 0
                positive_sy_mask = sy_coords > 0

                neg_sy_total = (
                    sy_profile.sel(sy=sy_coords[negative_sy_mask]).sum().item()
                )
                pos_sy_total = (
                    sy_profile.sel(sy=sy_coords[positive_sy_mask]).sum().item()
                )

                self.assertGreater(
                    neg_sy_total,
                    pos_sy_total,
                    msg=(
                        f"[{plugin}] Bright region expected at bottom (negative sy), "
                        f"but integrated intensity is not greater than top (positive sy)"
                    ),
                )

    def test_manual_loader(self):
        file_path = Path(__file__).parent / "data" / self.manual_load_file

        # Provide required manual parameters
        da_manual = load_data_manual(
            file_path,
            screen_sample_distance=309.2,
            screen_scale=9.04,
            beam_energy=18_600,  # eV
        )

        # Basic checks (same as plugin)
        self.assertIsInstance(da_manual, xr.DataArray)
        self.assertIn("sx", da_manual.dims)
        self.assertIn("sy", da_manual.dims)
        self.assertEqual(len(da_manual.shape), 2)
        self.assertEqual(da_manual.dtype, np.uint8)

        # Check essential attributes
        for attr in ["screen_sample_distance", "screen_scale", "beam_energy"]:
            self.assertIn(attr, da_manual.attrs)
            self.assertIsInstance(da_manual.attrs[attr], (float, int))


if __name__ == "__main__":
    unittest.main()
