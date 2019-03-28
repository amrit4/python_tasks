print("Enter the size of the list:")
N = int(input())
the_list=[]
# for x in range(N):
#     x = input("")    
#     the_list.append(x)
#     the_list.sort()

# print(the_list)

for x in range(N):
    x = input("Enter elements: ")
    try:  
        the_list.append(int(x))
    except ValueError:
        the_list.append(x)

print(the_list)