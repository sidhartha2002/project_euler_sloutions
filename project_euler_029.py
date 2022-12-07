def main():


	ans = set(x**y for x in range(2, 101) for y in range(2, 101))
	print(len(ans))


if __name__ == "__main__":
	main()