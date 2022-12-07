def main():
	res = 0
	x = 1  
	y = 2  
	n = 4000000
	while x <= n:
		if x % 2 == 0:
			res += x
		x, y = y, x + y
	print(res)


if __name__ == "__main__":
	main()