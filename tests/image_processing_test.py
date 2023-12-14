from image_processing import load_image, trim_whitespace, pad_height
import numpy as np

class TestLoadImage:
    def test_returns_np_array(self):
        img = "./tests/test_img.png"

        loaded_img = load_image(img, False, 100, 150)

        assert loaded_img.dtype == np.bool_

    def s_test_runs_edge_detection(self):
        img = "./tests/test_img.png"

        loaded_img = load_image(img, False, 100, 150)
        loaded_with_edge_detection = load_image(img, True, 100, 150)

        assert not np.array_equal(loaded_img, loaded_with_edge_detection)

class TestTrimWhitespace:
    def test_doesnt_trim_when_no_whitespace(self):
        img = [[1,0,1], [0,1,0], [1,0,1]]
        img = np.array(img, np.bool_)
        expected = [[1,0,1], [0,1,0], [1,0,1]]
        expected = np.array(img, np.bool_)

        trimmed = trim_whitespace(img)

        assert np.array_equal(trimmed, expected)
        
    def test_trims_top_row(self):
        img = [[0,0,0],[0,1,0],[0,0,0]]
        img = np.array(img, np.bool_)

        trimmed = trim_whitespace(img)
        
        assert any(trimmed[0])

    def test_trims_bottom_row(self):
        img = [[0,0,0],[0,1,0],[0,0,0]]
        img = np.array(img, np.bool_)

        trimmed = trim_whitespace(img)

        assert any(trimmed[-1])

    def test_trims_left_column(self):
        img = [[0,0,0],[0,1,0],[0,0,0]]
        img = np.array(img, np.bool_)

        trimmed = trim_whitespace(img)

        left_column = [r[0] for r in trimmed]

        assert any(left_column)

    def test_trims_right_column(self):
        img = [[0,0,0],[0,1,0],[0,0,0]]
        img = np.array(img, np.bool_)

        trimmed = trim_whitespace(img)

        right_column = [r[-1] for r in trimmed]

        assert any(right_column)

    def test_trims_rows_and_columns(self):
        img = [[0,0,0],[0,1,0],[0,0,0]]
        img = np.array(img, np.bool_)

        trimmed = trim_whitespace(img)

        assert np.array_equal(trimmed, np.array([[1]], np.bool_))

    def test_trims_multiple_rows_and_columns(self):
        img = [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        img = np.array(img, np.bool_)

        trimmed = trim_whitespace(img)

        assert np.array_equal(trimmed, np.array([[1]], np.bool_))

class TestPadHeight:
    def test_does_nothing_on_compatible_heights(self):
        img = np.ones((8,4), np.bool_)
        expected = np.copy(img)
        char_height = 4

        padded = pad_height(img, char_height)

        assert np.array_equal(padded, expected)

    def test_pads_height_to_have_correct_height(self):
        img = np.ones((8,4), np.bool_)
        char_height = 5

        padded = pad_height(img, char_height)

        assert padded.shape == (10, 4)

    def test_pads_with_zeros(self):
        img = np.ones((8,4), np.bool_)
        char_height = 5

        padded = pad_height(img, char_height)

        assert np.array_equal(padded[-2:], np.zeros((2,4), np.bool_))
    
    def test_does_not_change_rest_of_array(self):
        img = np.ones((8,4), np.bool_)
        expected = np.copy(img)
        char_height = 5

        padded = pad_height(img, char_height)

        assert np.array_equal(padded[:8], expected)
