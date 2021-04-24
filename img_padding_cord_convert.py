'''
This script os for resizing the image file 
without changing the aspect ratio of the original image 
and also changing the coordinates in the original xml as per new size.

This script adds padding to the original image 
so that the image does not lose its quality and is converted to desired size.

Imp Input parameters:
1. images_dir: directory where the original images are stored.
2. xml_dir: directory where the original xmls are stored
-----------------------------------------------------------------
3. img_save_dir: path where new images will be stored.
4. xml_save_dir: path where new xmls will be stored.
-----------------------------------------------------------------
5. desired_width: new width
6. desired_height: new height
'''

import cv2
import xml.etree.ElementTree as et
import glob
import os

def pad_img():
    count = 0

    print("IMAGE and XML source dir")
    images_dir= input("images_dir: ")
    xml_dir=  input("xml_dir: ")
    xml_dir = xml_dir+"/"

    print("-----------------------------------------------------")
    print("IMAGE and XML save path")
    img_save_dir = input("img_save_dir: ")
    xml_save_dir = input("xml_save_dir: ")

    print("-----------------------------------------------------")

    print("New WIDTH and HEIGHT")
    desired_width =  int(input("desired_width: "))
    desired_height = int(input("desired_height: "))

    print("-----------------------------------------------------")


    for file in sorted(os.listdir(images_dir)):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            count += 1
            print(count)
            path= os.path.join(images_dir,file)
            
            #read the image
            im = cv2.imread(path)
            old_height,old_width = im.shape[:2] # old_size is in (height, width) format
            new_width = (old_width*desired_height)/old_height
            new_height = desired_height

            if new_width>desired_width:

                new_height = (desired_width*desired_height)/new_width
                new_width = desired_width
                # print("Before Resize 1: ", new_height,new_width)
                im = cv2.resize(im, (int(new_width), int(new_height)))
                delta_w = desired_width - new_width
                delta_h = desired_height - new_height
                top, bottom = delta_h//2, delta_h-(delta_h//2)
                left, right = delta_w//2, delta_w-(delta_w//2)

                color = [0, 0, 0]
                new_im = cv2.copyMakeBorder(im, int(top), int(bottom), int(left), int(right), cv2.BORDER_CONSTANT,value=color)
                new_im = cv2.resize(new_im, (int(desired_width), int(desired_height)))
                path= xml_dir+file[:-4]+".xml"
                #read xml file
                label_file = path

                if os.path.exists(label_file):
                    
                    #parse the xml file
                    tree = et.parse(label_file)
                    root= tree.getroot()
                    #iterate through the xml to specific attribute
                    for (e,i) in zip(tree.iterfind('.//width'), tree.iterfind('.//height')):
                        #converts the text in given attribute to lower case
                        wid = int(e.text)
                        heigh = int(i.text)

                        try:
                            r_w= new_width/wid
                            r_h= new_height/heigh
                        except Exception as e:
                            print(file)
                            print(e)
                            continue

                        #replace the width and height in xml file
                        tree.find("./size/width").text = str(desired_width)
                        tree.find("./size/height").text = str(desired_height)
                    
                    # change the coordinates in the xml
                    for member in tree.iterfind('.//xmin'):
                        try:
                            x1= str(member.text)
                            xminNew = int((int(x1) * r_w)+left)
                            member.text = str(xminNew)
                        except Exception as e:
                            print(file)
                            print(e)
                    for member in tree.iterfind('.//ymin'):
                        try:
                            y1= str(member.text)
                            yminNew = int((int(y1) * r_h)+top)
                            member.text = str(yminNew)
                        except Exception as e:
                            print(file)
                            print(e)
                    for member in tree.iterfind('.//xmax'):
                        try:
                            x2= str(member.text)
                            xmaxNew = int((int(x2) * r_w)+left)
                            member.text = str(xmaxNew)
                        except Exception as e:
                            print(file)
                            print(e)
                    for member in tree.iterfind('.//ymax'):
                        try:
                            y2= str(member.text)
                            ymaxNew = int((int(y2) * r_h)+top)
                            member.text = str(ymaxNew)
                        except Exception as e:
                            print(file)
                            print(e)
                    file1 = file[:-4]+".xml"
                    #write the new xml file to folder
                    tree.write(os.path.join(xml_save_dir,file1))
                

            else:
                # print("Before Resize 2: ", new_height,new_width)
                im = cv2.resize(im, (int(new_width), int(new_height)))
                # print("After Resize 2: ", im.shape[:2])
                delta_w = desired_width - new_width
                delta_h = desired_height - new_height
                top, bottom = delta_h//2, delta_h-(delta_h//2)
                left, right = delta_w//2, delta_w-(delta_w//2)
            
                color = [0, 0, 0]
                new_im = cv2.copyMakeBorder(im, int(top), int(bottom), int(left), int(right), cv2.BORDER_CONSTANT,value=color)
                new_im = cv2.resize(new_im, (int(desired_width), int(desired_height)))
                # print("New Shape2: ", new_im.shape[:2])
                path= xml_dir+file[:-4]+".xml"
                #read xml file
                label_file = path

                if os.path.exists(label_file):
                    
                    #parse the xml file
                    tree = et.parse(label_file)
                    root= tree.getroot()
                    #iterate through the xml to specific attribute
                    for (e,i) in zip(tree.iterfind('.//width'), tree.iterfind('.//height')):
                        #converts the text in given attribute to lower case
                        wid = int(e.text)
                        heigh = int(i.text)

                        try:
                            r_w= new_width/wid
                            r_h= new_height/heigh
                        except Exception as e:
                            print(file)
                            print(e)
                            continue

                        #replace the width and height in xml file
                        tree.find("./size/width").text = str(desired_width)
                        tree.find("./size/height").text = str(desired_height)
                    
                    # change the coordinates in the xml
                    for member in tree.iterfind('.//xmin'):
                        try:
                            x1= str(member.text)
                            xminNew = int((int(x1) * r_w)+left)
                            member.text = str(xminNew)
                        except Exception as e:
                            print(file)
                            print(e)
                    for member in tree.iterfind('.//ymin'):
                        try:
                            y1= str(member.text)
                            yminNew = int((int(y1) * r_h)+top)
                            member.text = str(yminNew)
                        except Exception as e:
                            print(file)
                            print(e)
                    for member in tree.iterfind('.//xmax'):
                        try:
                            x2= str(member.text)
                            xmaxNew = int((int(x2) * r_w)+left)
                            member.text = str(xmaxNew)
                        except Exception as e:
                            print(file)
                            print(e)
                    for member in tree.iterfind('.//ymax'):
                        try:
                            y2= str(member.text)
                            ymaxNew = int((int(y2) * r_h)+top)
                            member.text = str(ymaxNew)
                        except Exception as e:
                            print(file)
                            print(e)
                    file1 = file[:-4]+".xml"
                    #write the new xml file to folder[PROVIDE YOUR OWN PATH]
                    tree.write(os.path.join(xml_save_dir,file1))


            # get the image name
            f = file[:-4]+".jpg"

            #write the image with new dims
            cv2.imwrite(os.path.join(img_save_dir,f), new_im)

pad_img()