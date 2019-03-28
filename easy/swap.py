n=int(input("Enter number of elements: "))
a=[]
temp=0

for i in range(0,n):
	ele=int(input("Enter numbers: "))
	a.append(ele)

print("swapped values are")

for x in a:
	temp=a[0]
	a[0]=a[n-1]
	a[n-1]=temp

print(a)