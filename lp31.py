a=int(input('enter a number'))
i=0
sum=0
while i<=a:
	if i%2==0:
		sum+=i
		print(sum,'even')
	elif i%2!=0:
		sum+=i
		print(sum,'odd')
	i=i+1