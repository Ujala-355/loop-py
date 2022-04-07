a=int(input('enter a number'))
mul=1
while a>0:
	mul=mul*(a%10)
	a=a//10
print("total digit multipal=",mul)