
def switch_bits(x,i,j):
	if (x >> i & 1) != (x >> j & 1):
		x ^= 1 << i
		x ^= 1 << j
	return x

def reverse_bits1(x,size):
	for i in range(int(size/2)):
		x = switch_bits(x,i,size-i-1)
	return x

def reverse_bits2(x): 
	"""Doesn't work for leading zeros"""
	r = 0
	while x:
		r <<= 1
		r |= x & 1
		x >>= 1
	return r

def init_lookup16bit():
	lookup = {}
	for x in range(0xFFFF+1):
		lookup[x] = reverse_bits1(x,16)
	return lookup

def reverse_64bit_w_lookup(x,lookup):
	return lookup[x & 0xFFFF] << 48 | lookup[x >> 16 & 0xFFFF] << 32 | lookup[x >> 32 & 0xFFFF] << 16 | lookup[x >> 48] 	
def b(n,digits):
	return format(n,'0{}b'.format(digits))


def reverse_w_lookup(x, lookup):
    mask_size = 16
    bitmask = 0xFFFF
    return (lookup[x & bitmask] << (3 * mask_size)
            | lookup[(x >> mask_size) & bitmask] << (2 * mask_size)
            | lookup[(x >> (2 * mask_size)) & bitmask] << mask_size
            | lookup[(x >> (3 * mask_size)) & bitmask])
