n = 17
if n > 1:
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			print(n, "is not prime")
			break
		else:
				print(n, "is prime")
	else:
		print(n, "is not prime")
