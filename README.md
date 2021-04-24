# model_tools_scripts


**Run the following scripts via terminal**
---------------------------------------------------------------------------------------------------

**<h2><b>1. image_batching.py</b></h2>**

Prerequisites and libs:
1. python 3.x
2. libs: os, cv2(OpenCv)

This script is for segregating a larget dataset folder into batches(folder) of fixed size(fixed number of images in each folder).<br>

To run the script run the following command:
```
$ python3 image_batching.py
```
And then provide the required **inputs**:<br>
**Inputs**:
1. img_source: path where all the images are present <br>
2. dist_path: folder where you want to create the batches <br>
3. max_img_count: number of images that should be present in every folder <br>
```
img_source: <path/where/images/are/present>
dist_path: <path/of/destination/folder>
max_img_count: <max/images/per/folder/to/store>
```

![uber](https://user-images.githubusercontent.com/30971790/113554114-6d2c5180-9616-11eb-9257-25d8e0d1c892.jpg)
---------------------------------------------------------------------------------------------------

<h2><b>2. kitti_bbox_score.py</b></h2>

Prerequisites and libs:
1. python 3.x
2. libs: os, cv2(OpenCv)

This script reads the following from the kitti file: 
1. class name
2. coordinates of class
3. score<br>

and stores image (with bounding box as per the coordinates and prints class name and score).<br>

**Keep the images and kitti file in same folder**<br>
To run the script run the following command:
```
$ python3 kitti_bbox_score.py
```
And then provide the required **inputs**:<br>
**Inputs**:
1. source_path: path where images and kitti files are present
2. save_path: save dir path where images will inference image will be stored.
```
source_path: <path/where/images/are/present>
save_path: <path/of/destination/folder>
```
![uber_bbox](https://user-images.githubusercontent.com/30971790/113556006-6fdc7600-9619-11eb-9cbb-1fa71363b0ac.jpg)
---------------------------------------------------------------------------------------------------

<h2><b>3. remove_xml_tag.py</b></h2>

Prerequisites and libs:
1. python 3.x
2. libs: os, xml.etree.ElementTree

This script  is for keeping  the required class name in the xml and
remove rest of the class name present in the xml from the object node.

**only takes one class name at a time**<br>
To run the script run the following command:
```
$ python3 remove_xml_tag.py
```
And then provide the required **inputs**:<br>
**Inputs**:
1. source_dir: where xmls are present
2. save_dir: location to store the new xmls 
3. class_keep: which class to keep in the tag. 
```
source_dir: </path/where/xmls/are/present>
save_dir: </path/where/you/want/to/store/new/xmls>
class_to_keep: <class name to keep in xml>
```
![uber_remove](https://user-images.githubusercontent.com/30971790/113556029-779c1a80-9619-11eb-99eb-312960c9ca9d.jpg)
---------------------------------------------------------------------------------------------------

<h2><b>4. replace_attribute.py</b></h2>

Prerequisites and libs:
1. python 3.x
2. libs: os, xml.etree.ElementTree

This script is for replacing the pre-existing class name with new class name<br>
To run the script run the following command:
```
$ python3 replace_attribute.py
```

And then provide the required **inputs**:<br>
**Inputs**:
1. source_dir: path where xmls are present
2. save_dir: path to store the new xmls
3. replace_attri: class name that you want to replace
4. new_attri: new class name. 
```
src_dir: </path/where/xmls/are/present>
save_dir: </path/where/you/want/to/store/new/xmls>
replace_attri: <class name that you want to replace>
new_attri: <new class name>
```
![uber_replace](https://user-images.githubusercontent.com/30971790/113556102-9a2e3380-9619-11eb-9c3d-f9efe8434507.jpg)
---------------------------------------------------------------------------------------------------

<h2><b>5. xml_cord_convert.py</b></h2>

Prerequisites and libs:
1. python 3.x
2. libs: os, xml.etree.ElementTree

This script is for converting the annotated coordinates in XML
as per the new image dimensions.<br>

It takes the new dims as input as per which you want to convert the coordinates.
calculates the new coordinates and saves them into the new XML.<br>
To run the script run the following command:
```
$ python3 xml_cord_convert.py
```
And then provide the required **inputs**:<br>
**Inputs**:
1. source_dir: directory where xmls are stored.
2. save_dir: directory where you want to store the new xmls.
3. new_wid: new width of the image.
4. new_hig: new heigh of the image.
```
source_dir: <directory/where/xmls/are/stored>
save_dir: <directory/where/you/want/to/store/the/new/xmls>
new_width: <new width of the image>
new_height: <new heigh of the image>
```
![uber_xmlcord](https://user-images.githubusercontent.com/30971790/113556141-a9ad7c80-9619-11eb-852d-bb3dd46d83ee.jpg)
----------------------------------------------------------------------------------------------------

<h2><b>6. xml_2_kitti.py</b></h2>

Prerequisites and libs:
1. python 3.x
2. libs: sys, os, xml.etree.ElementTree

This script is for replacing the pre-existing class name with new class name<br>
1. kitti template: 15 value format <br>
2. The converted kitti file has  15 values <br>

To run the script run the following command:
```
$ python3 xml_2_kitti.py </path/where/xmls/are/stored>
```
```
eg: python3 xml_3_kitti  home/foss/xmls_folder
```
![uber_kitti](https://user-images.githubusercontent.com/30971790/113556157-b03bf400-9619-11eb-81e4-e5a557a074ae.jpg)
----------------------------------------------------------------------------------------------------

<h2><b>7. resize_img.py</b></h2>

Prerequisites and libs:
1. python 3.x
2. libs: os, PIL

This script is for simply resizing the image to desired dims.<br>

It takes the new dims as input as per which you want to convert the coordinates.
calculates the new coordinates and saves them into the new XML.<br>
To run the script run the following command:
```
$ python3 resize_img.py
```
And then provide the required **inputs**:<br>
**Inputs**:
1. dir: path where images are stored.<br>
2. sv_img: path to save the new images.<br>
3. wid: new width.<br>
4. hig: new height.<br>
```
source_dir: <directory/where/xmls/are/stored>
save_dir: <directory/where/you/want/to/store/new/images>
new_width: <new width of the image>
new_height: <new heigh of the image>
```
![uber_resize](https://user-images.githubusercontent.com/30971790/113556177-b7fb9880-9619-11eb-9959-60c0ee8696a6.jpg)
----------------------------------------------------------------------------------------------------

<h2><b>8. img_padding_cord_convert.py</b></h2>

Prerequisites and libs:
1. python 3.x
2. libs: os, xml.etree.ElementTree, cv2(OpenCv)

This script os for resizing the image file without changing the aspect ratio of the original image 
and also changing the coordinates in the original xml as per new size.<br>

**The script adds padding to the original image so that the image does not lose its quality and is converted to desired size**<br>

To run the script run the following command:
```
$ python3 img_padding_cord_convert.py
```
And then provide the required **inputs**:<br>
**Inputs**:
1. images_dir: directory where the original images are stored.
2. xml_dir: directory where the original xmls are stored<br>
3. img_save_dir: path where new images will be stored.
4. xml_save_dir: path where new xmls will be stored.<br>
5. desired_width: new width
6. desired_height: new height<br>
```
images_dir: <path/where/original/images/are/present>
xml_dir: <path/where/original/XMLs/are/present>
img_save_dir: <path/where/you/want/to/save/new/images>
xml_save_dir: <path/where/you/want/to/save/new/xmls>
desired_width: <new width>
desired_height: <new height>
```
![uber_padding](https://user-images.githubusercontent.com/30971790/113719327-1e141880-970b-11eb-900b-0f21f01cee60.jpg)

----------------------------------------------------------------------------------------------------
