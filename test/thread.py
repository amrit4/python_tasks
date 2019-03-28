import threading 
  
def print_cube(num): 
    print("Cube: {}".format(num*num*num)) 
    
def print_square(num):
    print("Squatre:{}".format(num*num))
    
if __name__=="__main__":
    a=int(input("Enter number: "))
    t1 = threading.Thread(target=print_square, args=(a,)) 
    t2 = threading.Thread(target=print_cube, args=(a,)) 
 
    t1.start() 
    t2.start() 
  
    t1.join() 
    t2.join() 
    
    