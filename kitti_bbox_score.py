'''
This script reads the following from the kitti file: 
1. class name
2. coordinates of class
3. score
and draws bounding box as per the coordinates and prints class name and score.
'''


import cv2
import os



# driver function
def kitti_print():

    dir= input("source_path: ")
    save_dir= input("save_path: ")
    #directory where kitti and images are stored

    #iterate over the directory 
    for file in os.listdir(dir):

        #get filename without extention
        img_nm= os.path.splitext(file)[0]
        imgq= img_nm+".jpg"
        #read the image
        img= cv2.imread(os.path.join(dir,imgq))

        if file.endswith(".txt"):
            # path= dir+file
            label_file = os.path.join(dir,file)

            #read the annotation file
            ann_file= open(label_file, "r")
            for i in ann_file:
                cam= (i.split())
                
                #get the required parameters from the kitti file
                class_name= cam[0]
                
                #get the coordinates 
                cord1= int(float(cam[4]))
                cord2= int(float(cam[5]))
                cord3= int(float(cam[6]))
                cord4= int(float(cam[7]))

                # score 
                score= cam[-1]
                
                #draw the rectangle and print the classs name along with the score.
                imgr= cv2.rectangle(img,(cord1,cord2),(cord3,cord4),(0,0,255),2)
                cv2.putText(imgr, class_name, (cord1-20,cord2+10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                cv2.putText(imgr, score, (cord1-55,cord2+25), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

            #save the image in provided path
            cv2.imwrite(save_dir+"/"+file,img)
            

#call the function
kitti_print()
