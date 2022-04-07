i=100
sum=0
while i<=500:
	sum=sum+i
	i+=1
	if sum%2==0:
		print(sum,'even sum')
	else:
		print(sum,'odd sum')