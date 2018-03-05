def count_bits(x):
    """
    Count the number of bits set to one in a positive integer
    """
    bits = 0
    while x:
        bits += x & 1
        x >>= 1
    return bits

def main():
    import sys
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
    else: 
        num = 12
    print("{} in binary is {}".format(num,bin(num)))
    print("{} bits".format(count_bits(num)))

if __name__ == "__main__":
    main()

