import os

path = "/home/amritapa/test/dataset"

access_rights = 0o755

try:  
    os.mkdir(path, access_rights)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s" % path)

# filename = "/home/amritapa/Downloads/flickr_logos_27_dataset_training_set_annotation.txt"
# print("filename==>", filename)
# # file = open(filename, "r")
# # print("file==>", file)
# with open(filename, "r") as file:
# 	print("file==>", file)
# 	for line in file:
# 		print("------------------------")
# 	   	split = line.split(" ")
# 	   	a = split[0]
# 	   	b = split[1]
	 
# 	   	path = "/home/amritapa/test/dataset/"+ b 
# 		access_rights = 0o755
# 		try:  
# 		    os.mkdir(path, access_rights)
# 		    print("path==>", path)
# 		except OSError:  
# 		    print (OSError)
# 		else:  
# 		    print ("Successfully created the directory %s" % path)

# 		for i in line:
# 			file = open("/home/amritapa/test/dataset/"+b+"/"+a+".txt", "w")
		
		
# 		def file_read(fname):
#         	with open(fname) as f:
#                 	content_list = f.readlines()
#                 	for i  in content_list:
#                 		spl=line.split(" ")
                		

# 		file_read("/home/amritapa/Downloads/flickr_logos_27_dataset_training_set_annotation.txt")