a=[]
b=[]
c=[]
n=int(input("Enter number of elements: "))
t=0

for x in range(0,n):
	ele=int(input("Enter elements: "))
	a.append(ele)

print("Two Digit numbers are: ")

for i in a:
	if(10<=i<=99):
		b.append(i)
	
print(b)

print("Tho elements with same first and last characters are: ")

for p in a:
	temp=p
	n=p%10
	while(temp>=10):
		temp=temp/10
	if(n==temp):
		c.append(p)

print(c)


			