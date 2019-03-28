def intersection(c):
	for i in a:
		for j in b:
			if(i==j):
				c.append(i)
	return c

a=[]
b=[]
c=[]
n=int(input("Enter the number of elemnts: "))

for x in range(0,n):
	ele1=int(input("\nEnter elements of first list: "))
	a.append(ele1)

for y in range(0,n):
	ele2=int(input("\nEnter elements of second list: "))
	b.append(ele2)

print("\nIntersection is: ")

# for i in a:
# 	for j in b:
# 		if (i==j):
# 			c.append(i)
			
print(intersection(c))