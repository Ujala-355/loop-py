b=input('enter')
i=0
v=0
n=0
while i<len(b):
	if b[i]=='a' or b[i]=='e' or b[i]=='i' or b[i]=='o' or b[i]=='u':
		print(b[i],'v')
	else:
		print(b[i],'not v')
	i=i+1