l = []
n = int(input("enter the size of the element"))
for i in range(0,n):
	ele = int(input("enter an element"))
	l.append(ele)
print(l)
for i in range(0,n):
		if max(l)==l[i]:
			maxindex = i	
print(maxindex)
for i in range(0,n):
		if min(l)==l[i]:
			minindex = i
print(minindex)
