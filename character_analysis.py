import numpy as np
from itertools import chain
from PIL import ImageFont
from fontTools.ttLib import TTFont
from math import ceil
import string

class Glyph:
    def __init__(self, character, character_name):
        self.character = character
        self.character_name = character_name

    def generate_array(self, font, pillow_font, font_size, dpi):
        """Creates a boolean array representing an image of the character"""
        char_height = ceil(font_size * dpi / 72)
        char_width = ceil(font_size * dpi / 72 * font.getGlyphSet()[self.character_name].width / font['head'].unitsPerEm)
        # whitespace doesn't draw so generate here
        if self.character == " ":
            img_array = np.zeros((char_height, char_width), np.bool_)
            self.img_array = img_array
            return

        # draw array of character
        bounding_box = pillow_font.getbbox(self.character, mode="1") 
        img_array = np.array(pillow_font.getmask(self.character, "1"), np.bool_)
        img_array = img_array.reshape((-1, bounding_box[2] - bounding_box[0]))
        
        # trim width
        while len(img_array[0]) > char_width:
            if (len(img_array[0]) - char_width) % 2 == 1:
                img_array = np.delete(img_array, len(img_array[0]) -1, 1)
            else:
                img_array = np.delete(img_array, 0, 1)
        # trim height:
        # I don't know if this is necessary but it doesn't hurt
        # I haven't seen excess height but it might appear somewhere
        while len(img_array) > char_height:
            if (len(img_array) - char_height) % 2 == 1:
                im_array = np.delete(img_array, 0, 0)
            else:
                img_array = np.delete(img_array, len(img_array) - 1, 0)
        
        # pad top & bottom
        img_array = np.insert(img_array, [0 for i in range(bounding_box[1])], 0, 0)
        img_array = np.insert(img_array, [len(img_array) for i in range(char_height - bounding_box[3])], 0, 0)
        # no need to pad width
        
        self.img_array = img_array 

    def compare_array(self, arr):
        pass


class Alphabet:
    def __init__(self, font_path, font_size, dpi=96):
        self.font_path = font_path
        self.font_size = font_size
        self.dpi = dpi

    def create_glyphs(self):
        """creates a glyph object for each character and creates their img_array"""
        font = TTFont(self.font_path)
        pillow_font = ImageFont.truetype(self.font_path, ceil(self.font_size * self.dpi / 72))
        characters = string.printable[:-5]
        all_characters = set(chain.from_iterable([table.cmap.items() for table in font["cmap"].tables]))
        desired_characters = [(chr(char[0]), char[1]) for char in all_characters if chr(char[0]) in characters]
        self.glyphs = [Glyph(char[0], char[1]) for char in desired_characters]
        for glyph in self.glyphs:
            glyph.generate_array(font, pillow_font, self.font_size, self.dpi)

    def find_optimal_glyph(self, arr):
        pass
