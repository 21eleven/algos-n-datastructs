import timeit

def brute_force_bitCounter(x):
	bits = 0
	while x:
		bits += x & 1
		x >>= 1
	return bits

def bitwAND_trick_bitCounter(x):
	bits = 0
	while x:
		bits += 1
		x &= (x - 1)
	return bits

def main():
	n = 1000000
	start1 = timeit.default_timer()
	for i in xrange(n):
		brute_force_bitCounter(i)		
	stop1 = timeit.default_timer()
	print("brute {}".format(stop1 - start1))
	start2 = timeit.default_timer()
	for i in xrange(n):
		bitwAND_trick_bitCounter(i)
	stop2 = timeit.default_timer()
	print("trick {}".format(stop2 - start2))

if __name__ == "__main__":
	main()
