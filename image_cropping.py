import cv2
import numpy as np
import os



dir = input("destination folder: ")
save_folder = input("save_path: ")

height= int(input("height: ")) 
width = int(input("width: "))

count = 0

for img in sorted(os.listdir(dir)):
    if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg"):
        image = cv2.imread(os.path.join(dir,img))
        

        roi = cv2.selectROI(image)

        crop_img = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

        resized_img = cv2.resize(crop_img, (height, width))
        cv2.imwrite(os.path.join(save_folder, str(count)+".jpg"), resized_img)
        count+=1




