def telephone_word_combos(tel_number):
    """
    accepts a tel_number in the form 111-1111 or 1111111
    returns a list of word combinations derived from
    that number
    """
    return False

def map_digit_to_letter(digit):
    """
    maps digit to letter according to the standard
    """
    digit_map = {
        '0' : '0',
        '1' : '1',
        '2' : 'ABC',
        '3' : 'DEF',
        '4' : 'GHI',
        '5' : 'JKL',
        '6' : 'MNO',
        '7' : 'PRS',
        '8' : 'TUV',
        '9' : 'WXY'
    }
    return digit_map[digit]
