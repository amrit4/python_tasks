a=[22,3451342,1,4,54,56,0,11,34,6,7,234,1245456898]
l=len(a)
temp=0
for i in range(0,l):
	for j in range(0,l-i-1):
		if(a[j]>a[j+1]):
			temp=a[j+1]
			a[j+1]=a[j]
			a[j]=temp
print(a)

