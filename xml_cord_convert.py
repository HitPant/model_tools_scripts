'''
This script is for converting the annotated coordinates in XML
as per the new image dimensions.

It takes the new dims as input as per which you want to convert the coordinates.
calculates the new coordinates and saves them into the new XML

It takes the following inputs:
dir: directory where xmls are stored.
save_dir: directory where you want to store the new xmls
new_wid: new width of the image
new_hig: new heigh of the image

'''



# import the necessary lib
import xml.etree.ElementTree as et
import glob
import os



def xml_cord_conv():
    
    #[PROVIDE YOUR OWN PATH]
    dir= input("source_dir: ")
    save_dir = input("save_dir: ")

    new_wid = int(input("new_width: "))
    new_hig = int(input("new_height: "))

    for file in os.listdir(dir):
        if file.endswith(".xml"):

            #read xml file
            label_file = os.path.join(dir,file)

            #parse the xml file
            tree = et.parse(label_file)
            root= tree.getroot()
            #iterate through the xml to specific attribute
            for (e,i) in zip(tree.iterfind('.//width'), tree.iterfind('.//height')):
                #converts the text in given attribute to lower case
                wid = int(e.text)
                heigh = int(i.text)

                # provide the new dimension
                r_w= new_wid/wid
                r_h= new_hig/heigh

                #replace the width and height in xml file
                tree.find("./size/width").text = str(new_wid)
                tree.find("./size/height").text = str(new_hig)

            #iterate over the object's coordinates
            for member in root.findall('object'):
                x1= str(member[4][0].text)
                y1= str(member[4][1].text)
                x2= str(member[4][2].text)
                y2= str(member[4][3].text)                
                
                #get the new coordinates
                xminNew = int(int(x1) * r_w)
                yminNew = int(int(y1) * r_h)
                xmaxNew = int(int(x2) * r_w)
                ymaxNew = int(int(y2) * r_h)

                #replace with new coordinates
                member[4][0].text = str(xminNew)
                member[4][1].text = str(yminNew)
                member[4][2].text = str(xmaxNew)
                member[4][3].text = str(ymaxNew)
                
            #write the new xml file to folder[PROVIDE YOUR OWN PATH]
            tree.write(os .path.join(save_dir,file))



#call the function
xml_cord_conv()
