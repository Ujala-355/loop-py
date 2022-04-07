str=input('enter the name')
i=0
d=0
a=0
while i<len(str):
	if str[i]>='0' and str[i]<='9':
		d+=1
	elif str[i]>='a' and str[i]<='z':
		a=a+1
	i=i+1
print("alphabet count",a)
print("digit count",d)