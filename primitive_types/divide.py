def divide(x,y):
	place = 32
	quotient = 0
	while x >= y:
		while y << place > x:
			place -= 1
		x -= y << place
		quotient += 1 << place
	return quotient
		

