dict = {};
dict['a'] = 0.08167
dict['b'] = 0.01492
dict['c'] = 0.02782
dict['d'] = 0.04253
dict['e'] = 0.12702
dict['f'] = 0.02228
dict['g'] = 0.02015
dict['h'] = 0.06094
dict['i'] = 0.06966
dict['j'] = 0.00153
dict['k'] = 0.00772
dict['l'] = 0.04025
dict['m'] = 0.02406
dict['n'] = 0.06749
dict['o'] = 0.07507
dict['p'] = 0.01929
dict['q'] = 0.00095
dict['r'] = 0.05987
dict['s'] = 0.06327
dict['t'] = 0.09056
dict['u'] = 0.02758
dict['v'] = 0.00978
dict['w'] = 0.02360
dict['x'] = 0.00150
dict['y'] = 0.01974
dict['z'] = 0.00074

def scoreof(decoded_bytes):
    if len(decoded_bytes) == 0: return 0
    count = 0
    counts = {}
    for char_byte in decoded_bytes:
        char = chr(char_byte)
        counts.setdefault(char, 0)
        counts[char] += 1
        count += 1
    score = 0.0
    for char in dict:
        letter_count = counts.get(char, 0)
        difference = abs((letter_count / count) - dict.get(char, 0.0))
        score += difference
    return score

