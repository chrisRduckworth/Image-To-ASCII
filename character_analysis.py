import numpy as np


class Glyph:
    def __init__(self, character):
        self.character = character

    def generate_array(self, font_path, font_size, dpi):
        self.img_array = np.array([], dtype=np.bool_)

    def compare_array(self, arr):
        pass


class Alphabet:
    def __init__(self, font_path, font_size, dpi=96):
        self.font_path = font_path
        self.font_size = font_size
        self.dpi = dpi

    def create_glyphs(self):
        pass

    def find_optimal_glyph(self, arr):
        pass
