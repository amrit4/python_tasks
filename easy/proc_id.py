import threading

import os

def task1():
	print("Task1 assigned to thread:{}".format(threading.current_thread().name))
	print("Get id of process running:{}".format(os.getpid()))

def task2():
	print("Task2 assigned to thread:{}".format(threading.current_thread().name))
	print("Get id of process running:{}".format(os.getpid()))

if __name__=="__main__": 
  
  t1 = threading.Thread(target=task1, name='t1') 
  t2 = threading.Thread(target=task2, name='t2')   
  
  t1.start() 
  t2.start() 

  t1.join() 
  t2.join() 