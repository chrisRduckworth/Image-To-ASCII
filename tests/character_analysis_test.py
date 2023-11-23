from character_analysis import Glyph, Alphabet
import numpy as np


class TestGlyph:
    def test_init(self):
        glyph = Glyph("a")
        """glyph is initiated with the correct character attribute"""
        assert glyph.character == "a"

    def test_generate_array(self):
        glyph = Glyph("a")
        expected = [
            [True,  True,  True,  True,  True,  True,],
            [True,  True,  True,  True,  True,  True,],
            [True,  True,  True,  True,  True,  True,],
            [True,  True, False, False, False,  True,],
            [True,  True,  True,  True,  True, False,],
            [True,  True, False, False, False, False,],
            [True, False,  True,  True,  True, False,],
            [True, False,  True,  True, False, False,],
            [True,  True, False, False, False, False,],
            [True,  True,  True,  True,  True,  True,],
            [True,  True,  True,  True,  True,  True,]
            ]
        expected = np.array(expected, np.bool_)

        glyph.generate_array("C:\\Windows\\Fonts\\consola.ttf", 8, 96)

        """creates an array attribute"""
        assert hasattr(glyph, "img_array")

        """generates a boolean array"""
        assert glyph.img_array.dtype == np.bool_

        """generated array should be correct"""
        assert np.array_equal(expected, glyph.img_array) 

class TestAlphabet:
    def test_init(self):
        font_path = "C:\\Windows\\Fonts\\consola.ttf"
        font_size = 8
        alphabet = Alphabet(font_path, font_size)
        """Alphabet is initiatied with the correct attributes"""
        assert alphabet.font_path == font_path
        assert alphabet.font_size == font_size
        assert alphabet.dpi == 96