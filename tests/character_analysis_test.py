from character_analysis import Glyph, Alphabet
import numpy as np


class TestGlyph:
    def test_init(self):
        glyph = Glyph("a")
        """glyph is initiated with the correct character attribute"""
        assert glyph.character == "a"

    def test_generate_array(self):
        glyph = Glyph("a")

        glyph.generate_array("consola", 12, 96)

        """creates an array attribute"""
        assert hasattr(glyph, "img_array")

        """generates a boolean array"""
        assert glyph.img_array.dtype == np.bool_
