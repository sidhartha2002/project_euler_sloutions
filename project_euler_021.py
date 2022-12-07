def main():
	
	divisor_sum = [0] * 10000
	for i in range(1, len(divisor_sum)):
		for j in range(i * 2, len(divisor_sum), i):
			divisor_sum[j] += i
	
	
	ans = 0
	for k in range(1, len(divisor_sum)):
		j = divisor_sum[k]
		if j != k and j < len(divisor_sum) and divisor_sum[j] == k:
			ans += k
	print(ans)


if __name__ == "__main__":
	main()