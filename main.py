import sys

from character_analysis import Alphabet
from image_processing import load_image, trim_whitespace, pad_height
from image_to_ascii import image_to_ascii

def main(img_path, font_path, **kwargs):
    # Process optional arguments
    font_size = int(kwargs["font_size"]) if "font_size" in kwargs else 8
    edge_detection = kwargs["edge_detection"].lower() == "true" if "edge_detection" in kwargs else True
    min_val = int(kwargs["min_val"]) if "min_val" in kwargs else 100
    max_val = int(kwargs["max_val"]) if "max_val" in kwargs else 150

    # Create font information
    alphabet = Alphabet(font_path, font_size)
    alphabet.create_glyphs()
    alphabet.find_black_character()
    alphabet.find_max_width()

    # process image
    img = load_image(img_path, edge_detection, min_val, max_val)
    img = trim_whitespace(img)
    img = pad_height(img, alphabet.glyphs[0].height)
    
    # convert to string
    ascii_string = image_to_ascii(img, alphabet)
    print(ascii_string)
    
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], **dict(arg.split("=") for arg in sys.argv[3:]))
