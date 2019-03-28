


a=[]
n= int(input("Enter the number of elements in list:"))
temp=0
for x in range(0,n):
    element=int(input("Enter element:"))
    a.append(element)

# print("Duplicates:")
for j in range(0,len(a)):
	for k in range(1,len(a)):
		if(a[j]==a[k]):
			print("Duplicates:")
			print(a[j])
