
def switch_bits(x,i,j):
    if x >> i & 1 != x >> j & 1:
        x ^= 1 << i
        x ^= 1 << j
    return x

def init_16bit_lookup():
    lookup = {}
    for x in range(0xFFFF+1):
        original = x
        for i in range(8):
            x = switch_bits(x,i,15-i)
        lookup[original] = x
    return lookup

def reverse_64bit_int(x):
    #

