a=int(input('enter a number'))
b=a
total=0
r=0
while a>0:
	i=1
	f=1
	r=a%10
	while i<=r:
		f=f*i
		i=i+1
	total=total+f
	a=a//10
if b==total:
	print('strong number',b)
else:
	print('not a strong number',b)