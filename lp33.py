a='neeraj  ujala best friends'
i=0
str=' '
while i<len(a):
	if ' ' not in a[i]:
		str=str+a[i]
	i=i+1
print(str)