import numpy as np
from PIL import ImageDraw, Image, ImageFont
from fontTools import ttLib
from math import ceil
import string

class Glyph:
    def __init__(self, character):
        self.character = character

    def generate_array(self, font_path, font_size, dpi):
        """Creates a boolean array representing an image of the character"""
        font = ttLib.TTFont(font_path)
        # Calculate properties of character
        char_height = ceil(font_size * dpi / 72)
        char_width = ceil(font_size * dpi / 72 * font.getGlyphSet()[self.character].width / font['head'].unitsPerEm)
        # Draw character
        char_image = Image.new("1", (char_width, char_height), color=1)
        pillow_font = ImageFont.truetype(font_path, char_height)
        drawing = ImageDraw.Draw(char_image)
        drawing.text((0,0), self.character, 0, font=pillow_font, spacing=0)
        # Convert to array
        self.img_array = np.array(char_image, np.bool_)

    def compare_array(self, arr):
        pass


class Alphabet:
    def __init__(self, font_path, font_size, dpi=96):
        self.font_path = font_path
        self.font_size = font_size
        self.dpi = dpi

    def create_glyphs(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        self.glyphs = [Glyph(char) for char in characters]

    def find_optimal_glyph(self, arr):
        pass
