n = 1234
reversed_n = 0
while n > 10:
	reversed_n = reversed_n * 10 + n % 10
	n //= 10
print(f"reversed number:", reversed_n)
