def main():
	p = 1000
	for a in range(1, p + 1):
		for b in range(a + 1, p + 1):
			c = p - a - b      # p = a + b + c
			if a * a + b * b == c * c:
				print(a * b * c)


if __name__ == "__main__":
	main()