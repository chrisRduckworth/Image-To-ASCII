from character_analysis import Glyph, Alphabet
from math import ceil
import numpy as np
import string

from PIL import ImageFont
from fontTools import ttLib
import pytest


class TestGlyph:
    def test_init(self):
        glyph = Glyph("a", "a")
        """glyph is initiated with the correct character attribute"""
        assert glyph.character == "a"
        assert glyph.character_name == "a"

    def test_generate_array(self):
        glyph = Glyph("a", "a")
        expected = [[False, False, False, False, False, False],
                    [False, False, False, False, False, False],
                    [False, False, False, False, False, False],
                    [False, False,  True,  True,  True, False],
                    [False, False, False, False, False,  True],
                    [False, False,  True,  True,  True,  True],
                    [False,  True, False, False, False,  True],
                    [False,  True, False, False,  True,  True],
                    [False, False,  True,  True,  True,  True],
                    [False, False, False, False, False, False],
                    [False, False, False, False, False, False]]
        expected = np.array(expected, np.bool_)
        font_path = "C:\\Windows\\Fonts\\consola.ttf"
        font = ttLib.TTFont(font_path)
        pillow_font = ImageFont.truetype(font_path, ceil(8*96/72))

        glyph.generate_array(font, pillow_font, 8, 96)

        """creates an array attribute"""
        assert hasattr(glyph, "img_array")

        """generates a boolean array"""
        assert glyph.img_array.dtype == np.bool_

        """generated array should be correct"""
        assert np.array_equal(expected, glyph.img_array)

        """creates width and height attributes"""
        assert glyph.height == 11
        assert glyph.width == 6

    def test_compare_array(self):
        glyph = Glyph("a", "a")
        input_arr = np.zeros((11,6), np.bool_)
        font_path = "C:\\Windows\\Fonts\\consola.ttf"
        font = ttLib.TTFont(font_path)
        pillow_font = ImageFont.truetype(font_path, ceil(8*96/72))

        glyph.generate_array(font, pillow_font, 8, 96)

        score = glyph.compare_array(input_arr)

        """returns a score equal to the amount of matching entries"""
        assert score == 49/66

        """throws an error when input array is the wrong shape"""
        with pytest.raises(ValueError) as exc_info:
            glyph.compare_array(np.empty(0, np.bool_))
        assert exc_info.type is ValueError
        assert exc_info.value.args[0] == "input shape must match glyph shape"

class TestAlphabet:
    def test_init(self):
        font_path = "C:\\Windows\\Fonts\\consola.ttf"
        font_size = 8
        alphabet = Alphabet(font_path, font_size)
        """Alphabet is initiatied with the correct attributes"""
        assert alphabet.font_path == font_path
        assert alphabet.font_size == font_size
        assert alphabet.dpi == 96

    def test_create_glyphs(self):
        font_path = "C:\\Windows\\Fonts\\consola.ttf"
        font_size = 8
        alphabet = Alphabet(font_path, font_size)

        alphabet.create_glyphs()

        """creates a glyphs property"""
        assert hasattr(alphabet, "glyphs")

        """glyphs property is an array of glyph objects"""
        for glyph in alphabet.glyphs:
            assert isinstance(glyph, Glyph)

        """creates a glyph object for each character"""
        characters = string.printable[:-5]
        glyphs_characters = [glyph.character for glyph in alphabet.glyphs]
        assert len(alphabet.glyphs) == len(characters)
        for char in characters:
            assert char in glyphs_characters

        """creates the img_array for each glyph"""
        for glyph in alphabet.glyphs:
            assert hasattr(glyph, "img_array")

    def test_find_black_character(self):
        font_path = "C:\\Windows\\Fonts\\consola.ttf"
        font_size = 8
        alphabet = Alphabet(font_path, font_size)
        alphabet.create_glyphs()
        
        alphabet.find_black_character()

        """creates a black_character property"""
        assert hasattr(alphabet, "black_character")

        """sets black_character to glyph closest to black square"""
        assert alphabet.black_character.character == "@"
    
    def test_find_max_width(self):
        font_path = "C:\\Windows\\Fonts\\arial.ttf"
        font_size = 8
        alphabet = Alphabet(font_path, font_size)
        alphabet.create_glyphs()

        alphabet.find_max_width()

        """creates a max_width property"""
        assert hasattr(alphabet, "max_width")

        """sets max_width to the maximum width of all glyphs"""
        assert alphabet.max_width == 11
