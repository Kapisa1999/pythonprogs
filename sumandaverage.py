l = []
n = int(input("enter the size of the element"))
for i in range(0,n):
	ele = int(input("enter an element"))
	l.append(ele)
print(l)
print(sum(l))
print(sum(l)/len(l))
