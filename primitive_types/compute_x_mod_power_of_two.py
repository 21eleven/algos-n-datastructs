def mod_pow2(x,pow2):
    """
    Compute x mod a power of two (in O(1) time)
    e.g., returns 13 for 77 mod 64
    """
    return x&(pow2-1)

def main():
    print("{} % {} (aka {} % {}) -> {} ({})".format(77,64,bin(77),bin(64),mod_pow2(77,64),bin(mod_pow2(77,64))))
    print("{} % {} (aka {} % {}) -> {} ({})".format(35,4,bin(35),bin(4),mod_pow2(35,4),bin(mod_pow2(35,4))))

if __name__ == "__main__":
    main()
