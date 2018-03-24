def swap(x, y):
	x ^= y
	y ^= x
	x ^= y
	return x, y

def swap2(a, b):
	a -= b
	b += a
	a = b - a
	return a, b

def swap3(i, j):
	return j, i # ;]

