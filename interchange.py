l = []
n = int(input("enter the size of the element"))
for i in range(0,n):
	ele = int(input("enter an element"))
	l.append(ele)
print(l)
temp = l[0]
l[0] = l[-1]
l[-1] = temp
print(l)
