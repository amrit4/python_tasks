import os
path = ('/home/amritapa/test/Images')

for filename in os.listdir(path):
    print(filename)

# for filename in glob.glob(os.path.join(path, '*.txt'))