n = 1234
sum_of_digits = 0
while n > 0:
	sum_of_digits += n % 10
	n //= 10
print(f"sum of digits:", sum_of_digits)
