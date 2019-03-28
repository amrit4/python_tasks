l=[]
n=int(input("Enter Limit: "))
for i in range(0,n):
 	a=int(input("Enter Elements: "))
 	l.append(a)

 s1=0
 s2=0
 s3=0

 for j in l:
 	if(j>0):
 		if(j%2==0):
 			s1=s1+j
 		else:
 			s2=s2+j
 	else:
 		s3=s3+j
print("Sum of all positive even numbersq:",s1)
print("Sum of all positive odd numbers:",s2)
print("Sum of all negative numbers:",s3)











