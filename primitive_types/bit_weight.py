def flip_lowest_zero_and_one(x):
    """runs in O(n) time"""
    for i in range(64):
        if (x >> i) & 1 != (x >> i+1) & 1:
            x ^= 1 << i
            x ^= 1 << i+1
            return x

def lowest_set_bit(x):
    return x & ~(x-1)

def lowest_unset_bit(x):
    return ~x & (x+1)

def closest_int_same_weight(x):
    """runs in O(1) time)"""
    if lowest_set_bit(x) > lowest_unset_bit(x):
        return x^lowest_set_bit(x)^(lowest_set_bit(x) >> 1)
    else:
        return x^lowest_unset_bit(x)^(lowest_unset_bit(x)>>1)
    

def main():
    x = 4955
    print("{} ({}), closest integer with the same weight:\n{} ({})".format(x,bin(x),closest_int_same_weight(x),bin(closest_int_same_weight(x))))

if __name__ == "__main__":
    main()
