s = "I am Kapisa surya"
print(s)
t = s.split()
print(t)
for word in t:
	if len(word) % 2 == 0:
		print(word)
