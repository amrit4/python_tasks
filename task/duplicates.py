a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element:"))
    a.append(element)

print("\nDuplicates:")
for j in range(0,n):
	for k in range(j+1,n):
		if(a[j]==a[k]):
			print(a[j])

			