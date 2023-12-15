def calc_new_value(current, char):
    current += ord(char)
    current *= 17
    current %= 256
    return current
