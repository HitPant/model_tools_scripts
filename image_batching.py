'''
This script is for creating batches of fixed number of images from a large dataset.
img_source: path where all the images are present
dist_path: folder where you want to create the batches
max_img_count: number of images that should be present in every folder
'''

import os
import cv2

# driver function
def img_seg_cp():

    
    img_source = input("img_source: ")# path where images are stored
    dist_path= input("dist_path: ") # destination path

    max_img_count= int(input("max_img_count: ")) # maximum images in a folder

    # initialize the count for image and folder
    img_count = 0
    folder_count = 1

    # iterate throught the folder
    for file in sorted(os.listdir(img_source)):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            path = os.path.join(dist_path,str(folder_count))

            # increment the counter 
            img_count += 1

            img = cv2.imread(os.path.join(img_source, file))
            # print(os.path.join(img_source, file))
            
            if not os.path.exists(path):
                os.mkdir(path)

            # segregate the image as per the image_count
            if len(os.listdir(path))<(max_img_count+1):
                img_name = os.path.join(path, file)
                # print(img_name)
                cv2.imwrite(img_name, img)
            
            # move to next folder 
            if img_count == max_img_count:
                folder_count+=1
                img_count = 0

            # if c == 30000:
            #     break

# function call 
img_seg_cp()