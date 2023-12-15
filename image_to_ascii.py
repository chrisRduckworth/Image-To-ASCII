from math import ceil
import numpy as np

def get_subarray(img, coords, dimensions):
    """returns the subarray of img starting at (x,y)"""
    x, y = coords
    length, height = dimensions

    subarray = [row[x:x+length] for row in img[y:y+height]]

    if len(subarray[0]) < length:
        to_add = [0] * (length - len(subarray[0]))
        subarray = [[*row, *to_add] for row in subarray]

    return np.array(subarray, dtype = img.dtype)

def image_to_ascii(img, alphabet):
    """converts a numpy array (img) to an ASCII string"""
    output_string = ""
    for y in range(0, len(img), alphabet.glyphs[0].height):
        x = 0
        while x <= len(img[0]):
            to_compare = get_subarray(img, (x,y), (alphabet.max_width, alphabet.glyphs[0].height))
            best_match = alphabet.find_optimal_glyph(to_compare)
            
            output_string += best_match.character
            x += best_match.width
        output_string += "\n"
    return output_string
