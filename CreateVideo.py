import os
import cv2

path = "C:\\Users\\CLIENTE\\Downloads\\C117\\C117\\Images"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        images.append(images)
        file_name = path+"/"+file
        print(file_name)
        
print(len(images))
count = len(images)
print(images[0])
#print(cv2.imread(images[0]))
#frame = cv2.imread(images[0])
#height, width, channels = frame.shape
#size = (width,height)

#print(size)
#out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

#for i in range(0,count-1):
    #frame = cv2.imread(images[i])
    #out.write(frame)
    
#out.release()
#print("Tudo certo!!!")