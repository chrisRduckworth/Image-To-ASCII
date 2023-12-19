from character_limit import find_font_size
from image_processing import load_image

class TestFindFontSize:
    def test_finds_maximum_font_size(self):
        img_path = "./tests/test_img.png"
        font_path = "C:\\Windows\\Fonts\\consola.ttf"
        max_chars = 2000
        dpi = 96
        
        img = load_image(img_path, False, 100, 150, 127)
        font_size = find_font_size(img, font_path, max_chars, dpi)

        assert font_size == 15
        
