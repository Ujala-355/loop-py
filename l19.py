n=int(input('enter a number'))
i=1
sum=0
while n>i:
	if n%i==0:
		sum=sum+i
	i=i+1
if n==sum:
	print(sum,'perfect number')
else:
	print('not a perfect number')