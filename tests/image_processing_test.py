from image_processing import load_image
import numpy as np

class TestLoadImage:
    def test_returns_np_array(self):
        img = "./tests/test_img.png"

        loaded_img = load_image(img, False, 100, 150)

        assert loaded_img.dtype == np.bool_

    def test_runs_edge_detection(self):
        img = "./tests/test_img.png"

        loaded_img = load_image(img, False, 100, 150)
        loaded_with_edge_detection = load_image(img, True, 100, 150)

        assert not np.array_equal(loaded_img, loaded_with_edge_detection)
