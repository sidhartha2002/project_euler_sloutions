import math


def main():
	n = math.factorial(100)
	ans = sum(int(i) for i in str(n))
	print(ans)


if __name__ == "__main__":
	main()