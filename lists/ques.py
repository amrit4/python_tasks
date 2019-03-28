a=[]
b=[]
str1=raw_input("Enter elements: ")
st=str1.split()

print("Two figured elements are: ")

for i in st:
	if (len(i)==2):
		a.append(i)

print(a)

print("Elements with same first and last characters are: ")

for j in st:
	if(j[0]==j[-1]):
		b.append(j)

print(b)
