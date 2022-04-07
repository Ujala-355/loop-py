a='my mane is naaz and my friends name is saai'
count=0
b=a.split()
i=0
while i<len(b):
	if b[i]=='is':
		count+=1
	i+=1
print(count)