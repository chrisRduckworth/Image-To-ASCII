from fontTools.ttLib import TTFont
import math

def find_font_size(img, font_path, max_chars, dpi):
    width, height = img.shape 
    font = TTFont(font_path)
    space_width = font.getGlyphSet()['space'].width
    units_per_em = font['head'].unitsPerEm
    
    font_size = math.ceil(math.sqrt((width * height * units_per_em * 72 * 72)/(max_chars * dpi * dpi * space_width)))

    return font_size
