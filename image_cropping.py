import cv2
import numpy as np
import os



dir = "/home/foss/Documents/Deep_learning_prep/gesture_dataset"

count = 67

for img in sorted(os.listdir(dir)):
    if img.endswith(".jpg"):
        image = cv2.imread(os.path.join(dir,img))
        

        roi = cv2.selectROI(image)

        crop_img = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

        resized_img = cv2.resize(crop_img, (300,300))
        cv2.imwrite(f"/home/foss/Music/img{count}.jpg", resized_img)
        count+=1




