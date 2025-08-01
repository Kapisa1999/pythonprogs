n = int(input("enter the no of rows:"))
k = 0
a = ['A','B','C','D','E']
for i in range(1,n+1):
		for j in range(1,i+1):
				print(a[k],end=" ")
		k+=1
		print(" ")
	
