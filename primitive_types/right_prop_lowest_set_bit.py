def right_propagate_rightmost_set_bit(x):
    """
    Right propagate the rightmost set bit in x (in O(1) time)
    e.g., 01010000 -> 01011111
    """
    return x | x - 1

def main():
    print("{} -> {}".format(bin(192),
                     bin(right_propagate_rightmost_set_bit(192))))
    print("{} -> {}".format(bin(208),
                     bin(right_propagate_rightmost_set_bit(208))))

if __name__ == "__main__":
    main()
