n = int(input("enter a number: "))
perfect = 0
for i  in range (1,n):
	if n % i == 0:
		perfect += i
if perfect == n:
		print(f"this is perfect number")
else:
		print(f"this is not perfect number")
