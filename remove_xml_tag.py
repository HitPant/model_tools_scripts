'''
This script  is for keeping  the required class name in the xml and
remove rest of the tags present in the xml.

*******only takes one class name at a time**********

It takes following input:
dir: where xmls are present
save_dir: location to store the new xmls 
class_keep: which class to keep in the tag.
'''

import xml.etree.ElementTree as ET
import os


def xml_cord_conv():
    # [PROVIDE YOUR OWN PATH]
    dir = input("source_dir: ")
    save_dir = input("save_dir: ")

    class_keep = input("class_to_keep: ")
    
    #initialize the count
    per_count=0

    for file in os.listdir(dir):
        if file.endswith(".xml"):

            # read xml file
            label_file = os.path.join(dir,file)
            
            # parse the xml file
            tree = ET.parse(label_file)
            for e in tree.iterfind(f'.//name'): 
                if e.text == class_keep:
                    root = tree.getroot() # get the root of the xml 
                    parent_map = dict((c, p) for p in tree.getiterator() for c in p)
                    iterator = list(root.getiterator('object')) # get all the object tags present

                    # iterate through all the object tags and 
                    # remove all the tags other than the required tags
                    for item in iterator:
                        old = item.find('name')
                        text = old.text
                        if text != class_keep:
                            parent_map[item].remove(item)
                            continue

                    tree.write(f'/home/foss/Desktop/sas/b/{file}')
                    

xml_cord_conv()