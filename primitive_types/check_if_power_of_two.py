
def checkPowTwo(x):
        """
        Returns true if x is a power of 2 
        (in O(1) time)
        """
	return (x > 0) and (x & (x-1) == 0)

def main():
	for n in range(0,130):
		print(bin(n), n, checkPowTwo(n))

if __name__ == "__main__":
	main()
