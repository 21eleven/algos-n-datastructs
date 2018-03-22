def multiply(x,y):
	result = 0 
	limit = 1
	while limit <= x:
		if (limit & x) != 0:
			result = add(result,y)
		limit <<= 1
		y <<= 1
	return result

def add(x,y):
	result = 0
	limit = 1
	carry = 0
	while (limit <= x) or (limit <= y) or carry == 1:
		if (x & limit) == 0 and (y & limit) == 0:
			if carry == 1:
				result ^= limit
				carry = 0
				limit <<= 1
			else:
				limit <<= 1
		elif (x & limit) > 0 and (y & limit) > 0:
			if carry == 1:
				result ^= limit
				limit <<= 1
			else:
				limit <<=1
				carry = 1
		else:
			if carry == 1:
				limit <<= 1
			else:
				result ^= limit
				limit <<=1
	return result
			

def elegant_add(x,y):
	while y:
		carry = x & y
		x ^= y
		y = carry << 1
	return x

def multiply2(x, y):
    def add2(a, b):
        running_sum, carry, k, temp_a, temp_b = 0,0,1,a,b
        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carryout = (ak & bk) | (ak & carry) | (bk & carry)
            running_sum != ak ^ bk ^ carry
            carry, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
        return running_sum | carry
    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum
