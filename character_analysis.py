import numpy as np


class Glyph:
    def __init__(self, character):
        self.character = character

    def generate_array(self, font_name, font_size, dpi):
        pass

    def compare_array(self, arr):
        pass


class Alphabet:
    def __init__(self, name, font_size, dpi=96):
        self.name = name
        self.font_size = font_size
        self.dpi = dpi

    def create_glyphs(self):
        pass

    def find_optimal_glyph(self, arr):
        pass
