def parity(x):
    """
    Returns the parity of a positive integer: returns
    1 if there are an odd number of 1s in the binary representation
    of the integer, returns 0 if the number of 1s is even
    """
    parity = 0

    while x:
        parity ^= x & 1
        x = x&(x-1)
    return parity

def main():
    import sys
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
    else: 
        num = 12
    print("{} in binary is {}".format(num,bin(num)))
    print("parity is {}".format(parity(num)))

if __name__ == "__main__":
    main()

