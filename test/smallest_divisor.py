n=int(input("enter number: "))

l=[]
for i in range(2,n+1):
	if(n%i==0):
		l.append(i)
l.sort()
print(l[0])