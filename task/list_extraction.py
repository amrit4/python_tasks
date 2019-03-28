a=[]
m= int(input("Enter the number of elements in the first list:"))
for x in range(0,m):
    ele1=int(input("Enter elements in the first list:"))
    a.append(ele1)

b=[]
n= int(input("\nEnter the number of elements in the second list:"))
for y in range(0,n):
    ele2=int(input("Enter elements in the second list:"))
    b.append(ele2)

c=[]

print("\nExtracted list is: ")
for i in a:
	for j in b:
		if(i not in b):
			c.append(i)	
			
print(c)