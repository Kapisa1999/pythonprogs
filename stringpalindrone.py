str = "MADAM"
rev_str = ''
for i in str:
		rev_str = i + rev_str
print(rev_str)
if rev_str==str:
	print(str,"palindrome")
else:
	print(str,"not a palindrome")
