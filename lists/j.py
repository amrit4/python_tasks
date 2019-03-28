
z=int(input ("enter number: "))
a=[]
b=[]
c=[]
t=0
for q in range(0,z):
	ele=int(input("Enter elements: "))
	a.append(ele)

for p in a:
	temp=p
	n=p%10
	while(temp>=10):
		temp=temp/10
	if(n==temp):
		t=t+1
		c.append(p)
print(c)
# 	b.append(temp)
# 	c.append(n)
	
# for i in b:
# 	for j in c:
# 		if(i==j):
# 			t=t+1
# 			d.append(i)
# if(t>=1):
# 	print(d)




# print(b)
