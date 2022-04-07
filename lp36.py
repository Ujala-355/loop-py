i=1
while i<=1000:
	b=i
	sum=0
	j=1
	while j<b:
		if b%j==0:
			sum+=j
		j=j+1
	if sum==b:
		print(j,'perfect number')
	i=i+1