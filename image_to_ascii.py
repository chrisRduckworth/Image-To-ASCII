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

def main():
  pass

if __name__ == "__main__":
  main()