import os

# path=('/home/amritapa/test/Images')
# l=[]
m=[]
n=[]
myfile=open('flickr_logos_27_dataset_training_set_annotation.txt')
f= myfile.readlines()



# for directory in os.listdir(path):
# 	# print(directory)
# 	for i in os.listdir(os.path.join(path,directory)):
# 		print ("image: ", i)
	
# 		o=['']
# 		fs = ''
# 		for item in f:
# 			# print (item)
# 			item = item.strip("\r\n").strip()
# 			item = item.split(' ')
# 			# print ("item: ",item)
# 			name = item[0]
# 			annotation = (' ').join(item[3:])
# 			# print(type(annotation))
# 			# l.append(annotation)
# 			# print("annotation: ")
# 			# for k in l:
# 			# 	print(k)

			
# 			if i == name:
# 				# print("found matched")
# 				count=count+1
# 				# print(count)
# 				# out.insert(0, str(count))
# 				o[0]= str(count)
# 				o.append(annotation)
				
# 		# print("output: ",out)
# 		# print("*"*20)
# 		# print("\n")
# 		# print("\n")

# 		for k in o:
# 			fs = fs+ k + '\n'

# 		print(fs)
# 		print("\n")


def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
	except OSError:
		print ('Error: Creating directory. ' +  directory)
		
createFolder('./data/')

for t in f:
	spl=t.split(" ")
	r1=spl[1]
	r2=spl[0]
	m.append(r1)
	n.append(r2)


for g in m:
	createFolder('./data/'+g)

for v in n:
	df= open('./data/'+g+'/'+v+".txt")




