def parity_64bit_shift_assoc(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

def parity(x):
    parity = 0
    while x:
        parity ^= 1
        x &= (x - 1)
    return parity

def main():
    import random
    import timeit
    random_64bit_ints = [random.getrandbits(64) for r in range(100000)]
    start = timeit.default_timer()
    for n in random_64bit_ints:
        parity(n)
    stop = timeit.default_timer()
    print("bitwise AND trick : {}".format(stop - start))
    start = timeit.default_timer()
    for n in random_64bit_ints:
        parity_64bit_shift_assoc(n)
    stop = timeit.default_timer()
    print("shift assoc trick : {}".format(stop - start))

if __name__ == "__main__":
    main()

    
