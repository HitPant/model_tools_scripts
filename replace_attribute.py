'''
This script is for replacing the pre-existing class name 
with new class name
It takes the following parameters:
src_dir: path where xmls are present
save_dir: path to store the new xmls
ex_text: class name that you want to replace
replace: new class name. 
'''

import xml.etree.ElementTree as et
import glob
import os


def xml_attri():
    #PROVIDE YOUR OWN PATH
    src_dir= input("source_dir: ")
    save_dir= input("save_dir: ")

    ex_text= input("replace_attri: ")
    replace= input("new_attri: ")


    for file in os.listdir(src_dir):
        if file.endswith(".xml"):
            xml_path= os.path.join(src_dir,file)
            

            #parse the xml file
            tree = et.parse(xml_path)
            #iterate through the xml to specific attributes
            for e in tree.iterfind(f'.//name'):
                if e.text == ex_text:
                #converts the text in given attribute to lower case
                    e.text = replace
                    # print(e.text)

                #write the new xml file to folder[PROVIDE YOUR OWN PATH]
                tree.write(os.path.join(save_dir, file))

xml_attri()