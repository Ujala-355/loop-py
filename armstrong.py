a=int(input('enter a number'))
b=a
sum=0
while a>0:
	sum=sum+(a%10)*(a%10)*(a%10)
	a=a//10
if b==sum:
	print('armstrong number',sum)
else:
	print('not armstrong',sum) 