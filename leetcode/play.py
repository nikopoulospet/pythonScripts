vals = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7}
s = "ABDEC"
index = len(s)
sum = 0
while index > 0:
	index -= 1
	sum += (26**index)*vals[s[index]]
	print(s[index])

print(sum)
