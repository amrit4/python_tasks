n=int(input("Enter number: "))
for i in range(2,n):
	if(n%i==0):
		for j in range(2,i):
			if(i%j!=0):
				print("Prime factors are: ")
				print(i)

