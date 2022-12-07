import math

def main():
	ans = 1
	for i in range(1, 21):
		ans *= i // math.gcd(i, ans)
	print(ans)


if __name__ == "__main__":
	main()