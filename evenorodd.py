l = []
e = []
o = []
n = int(input("enter the size of the element"))
for i in range(0,n):
	ele = int(input("enter an element"))
	l.append(ele)
print(l)
for i in range(0,n):
		if l[i]%2==0:
				e.append(l[i])
		else:
				o.append(l[i])
print(e)
print(o)
