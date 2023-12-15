import sys

from character_analysis import Alphabet
from image_processing import load_image, trim_whitespace, pad_height
from image_to_ascii import image_to_ascii

def main(img_path, font_path, **kwargs):
    # Create font information
    alphabet = Alphabet(font_path, 8)
    alphabet.create_glyphs()
    alphabet.find_black_character()
    alphabet.find_max_width()

    # process image
    img = load_image(img_path, True, 100, 150)
    img = trim_whitespace(img)
    img = pad_height(img, alphabet.glyphs[0].height)
    
    # convert to string
    ascii_string = image_to_ascii(img, alphabet)
    print(ascii_string)
    
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], **dict(arg.split("=") for arg in sys.argv[3:]))
