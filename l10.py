a=int(input('enter a number'))
b=a
i=1
sum=0
while a!=0:
	i=a%10
	sum=sum*10+i
	a=a//10
if b==sum:
	print('pindrom')
else:
	print('no pindrom')