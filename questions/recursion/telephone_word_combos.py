def telephone_word_combos(tel_number, combos=None, word='', i=0):
    """
    accepts a tel_number as a string of digits (no hash marks)
    returns a list of word combinations derived from
    that number
    """
    if not combos:
        combos = []

    if len(tel_number) == len(word):
        combos.append(word)
    else:
        digit = tel_number[i]
        for letter in map_digit_to_letter(digit):
            combos = telephone_word_combos(
                tel_number = tel_number,
                combos = combos,
                word = word + letter,
                i = i+1,
                )

    return combos

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
    if digit in digit_map:
        return digit_map[digit]
    else:
        return False
