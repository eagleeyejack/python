def mult(a, b):
	if b == 1:
		return a
	else:
		print(b - 1)
		return a + mult(a, b - 1)


print(mult(7, 8))