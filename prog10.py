n = 12321
original = n
reversed_n = 0
while n > 0:
	reversed_n = reversed_n * 10 + n % 10
	n //= 10
if original == reversed_n:
	print(original, "is a palindrome")
else:
	print(original, "is not a palindrome")

