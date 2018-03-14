def switch_bits(x,i,j):
	"""
	Flips bits i and j in integer x in O(1) time,
	doesn't flip bits if they are the same.
	"""
	if (x >> i & 1) != (x >> j & 1):
		x ^= 1 << i
		x ^= 1 << j
	return x

def main():
	print("{} : flip bits at index 0 and 2 -> {}".format(bin(12),
						bin(switch_bits(12,0,2))))
	print("{} : flip bits at index 1 and 3 -> {}".format(bin(22),
						bin(switch_bits(22,1,3))))
if __name__ == "__main__":
	main()
