def parity(x):
    parity = 0
    while x:
        parity ^= 1
        x &= (x - 1)
    return parity

def init_lookup():
    lookup = {}
    for i in range(2**16):
        lookup[i] = parity(i)
    return lookup

def parity_64bit_word_w_lookup(w, lookup):
    bitmask = 2**16 - 1
    return ( ( ( lookup[w & bitmask] 
                ^ lookup[w >> 16 & bitmask] )
                ^ lookup[w >> 32 & bitmask] ) 
                ^ lookup[w >> 48] ) 

def main():
    import random
    import timeit
    random_64bit_ints = []
    for z in range(100000):
        random_64bit_ints.append(random.getrandbits(64))
    lookup = init_lookup()
    start = timeit.default_timer()
    for n in random_64bit_ints:
        parity(n)
    stop = timeit.default_timer()
    print("bitwise AND trick : {}".format(stop-start))
    start = timeit.default_timer()
    for n in random_64bit_ints:
        parity_64bit_word_w_lookup(n, lookup)
    stop = timeit.default_timer()
    print("lookup table : {}".format(stop-start))



    return 1

def naive_parity(x):
    parity = 0
    while x:
        parity ^= x & 1
        x >>= 1
    return int(parity)

if __name__ == "__main__":
    main()


