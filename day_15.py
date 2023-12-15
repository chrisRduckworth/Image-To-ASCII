from functools import reduce

def calc_new_value(current, char):
    current += ord(char)
    current *= 17
    current %= 256
    return current

def calc_value(seq):
    """calculates the value of a sequence"""
    total = reduce(calc_new_value, seq, 0)
    return total
