a=[]
b=[]
c=[]

n=int(input("Enter number of elements: "))

for i in range(0,n):
	ele=int(input("\nEnter the numbers: "))
	a.append(ele)

for i in a:
	if(i%2==0):
		b.append(i)
	else:
		c.append(i)

print("\nOdd Numbers: ")
print(c)

print("\nEven Numbers: ")
print(b)