a=[]
b=[]
n=int(input("Enter length: "))

print("\n")
for i in range(0,n):
	ele=int(input("Enter numbers: "))
	a.append(ele)

print("\nThe squared tuples are")
for j in a:
	a=[(j,j**2)]
	print(a)