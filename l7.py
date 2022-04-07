a=input('enter a number')
i=0
s=' '
while i<len(a):
	if a[i]=='1':
		s+='one'
	if a[i]=='2':
		s+='two '
	if a[i]=='3':
		s+='three'
	if a[i]=='4':
		s+='four'
	if a[i]=='5':
		s+='five'
	if a[i]=='6':
		s+='six'
	if a[i]=='7':
		s+='saven'
	if a[i]=='8':
		s+='eight'
	if a[i]=='9':
		s+='nine'
	if a[i]=='10':
		s+='ten'
	if a[i]=='0':
		s+='zero'
	i+=1
print(s)