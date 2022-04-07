a=int(input('enter a number'))
i=0
sum=0
while a!=0:
	i=a%10
	sum=sum*10+i
	a=a//10
print("reverse",sum)