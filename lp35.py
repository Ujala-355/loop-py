num=int(input("enter a number"))
i=1
c=0
while i<=num:
	b=i
	sum=0
	while b>0:
		c=b%10
		sum+=c
		b=b//10
	if i%sum==0:
		print('harshad number',i)
	i=i+1