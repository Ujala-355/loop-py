n=input('enter')
i=0
b=n
while i<len(n):
	print(n[-1::-1])
	i+=1
	break
if b==(n[-1::-1]):
	print('palindrom',b)
else:
	print('not palindrom',b)