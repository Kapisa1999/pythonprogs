i = 0
j = 1
fib = 0
print("the fibonacci series is: ")
print(i,j," ",end=" ")
while fib<10000:
	fib = i + j
	temp = fib
	print(fib," ",end = " ")
	i = j
	j = fib
