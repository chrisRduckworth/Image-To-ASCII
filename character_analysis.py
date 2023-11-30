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
            self.width = len(img_array[0])
            self.height = len(img_array)
            return

        # draw array of character
        bounding_box = list(pillow_font.getbbox(self.character, mode="1"))
        if bounding_box[3] > char_height:
            # for characters that are too tall
            bounding_box[1] -= bounding_box[3] - char_height
            bounding_box[3] -= bounding_box[3] - char_height
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
                img_array = np.delete(img_array, 0, 0)
            else:
                img_array = np.delete(img_array, len(img_array) - 1, 0)
        
        # pad top & bottom
        img_array = np.insert(img_array, [0 for i in range(bounding_box[1])], 0, 0)
        img_array = np.insert(img_array, [len(img_array) for i in range(char_height - bounding_box[3])], 0, 0)
        # no need to pad width
        
        self.img_array = img_array 
        self.width = len(img_array[0])
        self.height = len(img_array)

    def compare_array(self, arr):
        """returns a score for how close the input matches the character"""
        if arr.shape != self.img_array.shape:
            raise ValueError("input shape must match glyph shape")
        """
        We want to increase the score for each element in the array
        that matches the input. Eg, comparing
        [[1,0],
         [0,1]]
        with 
        [[1,0],
         [1,0]]
        then we only want 1s at:
        [[1,1],
         [0,0]]
        Or, we want 0s where they are different. This is equivalent
        to NOT XOR
        Then we just sum over the array and normalize by the size
        of the array to get a score between 0 and 1
        """
        return np.sum(~(self.img_array ^ arr))/arr.size

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

    def find_black_character(self):
        """finds the character closest to a black square"""
        scores = {}
        for glyph in self.glyphs:
            black_square = np.ones(glyph.img_array.shape, np.bool_)
            score = glyph.compare_array(black_square)
            scores[glyph] = score
        best_character = max(scores, key=scores.get)

        self.black_character = best_character
    
    def find_max_width(self):
        """finds the maximum width of glyphs"""
        widths = [len(glyph.img_array[0]) for glyph in self.glyphs]
        self.max_width = max(widths)

    def find_optimal_glyph(self, arr):
        """finds the glyph which most closely matches the input array"""
        # check if it's a white or black box to save time
        space = next(g for g in self.glyphs if g.character == " ")
        columns_to_delete = [len(arr[0]) - (i + 1) for i in range(len(arr[0]) - space.width)]
        trimmed_arr = np.delete(arr, columns_to_delete, 1)
        if np.array_equal(trimmed_arr, space.img_array):
            return space
        
        black_arr = np.ones((self.black_character.height, self.black_character.width),np.bool_)
        columns_to_delete = [len(arr[0]) - (i + 1) for i in range(len(arr[0]) - self.black_character.width)]
        trimmed_arr = np.delete(arr, columns_to_delete, 1)
        if np.array_equal(trimmed_arr, black_arr):
            return self.black_character

        # calculate scores and return max
        scores = {glyph: glyph.compare_array(arr) for glyph in self.glyphs}
        return max(scores, key=scores.get)
