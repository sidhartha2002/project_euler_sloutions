def main():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	print(str(ans)) 


if __name__ == "__main__":
	main()