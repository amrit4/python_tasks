# a=[]
# n= int(input("Enter the number of elements in list:"))
# for x in range(0,n):
#     element=int(input("Enter element:"))
#     a.append(element)

# b=[]
# print("\nList after removing duplicates")
# for i in a: 
#         if i not in b: 
#             b.append(i) 
    
# print(b)


# a=['abc', 's', 'as','asfg','adgha','asfdba','aeth']
# print("Elements are: ")

# b=[i for i in a if len(i)>=2 and i[0]==i[-1]]

# print(b)

a=['abc', 's', 'as','asfg','adgha','asfdba','aeth']

b= (i for i in a if len(i)>=2 and i[0]==i[-1])

print(next(b))

# print(next(b))

# def count(b):
# 	b= [i for i in a if len(i)>=2 and i[0]==i[-1]]
# 	yield b

# print("ELements Are: ")

# for i in count(a):
# 	print i