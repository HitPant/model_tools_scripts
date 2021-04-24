from PIL import Image  
import os


def img_cvt():

    #[PROVIDE YOUR OWN PATH]
    dir= input("source_dir: ") # directory where images are stored
    sv_img= input("save_dir: ") # save directory path
    wid = int(input("new_width: ")) # new width
    hig = int(input("new_height: ")) # new height

    # iterate through the directory 
    for file in os.listdir(dir):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            
            try:

                #read xml file
                label_file = os.path.join(dir,file)
        
                # Opens a image in RGB mode  
                im = Image.open(label_file)
                
                # Size of the image in pixels (size of orginal image)  
                # (This is not mandatory)  
                width, height = im.size  
                
                newsize = (wid, hig) 
                im1 = im.resize(newsize)
                # Shows the image in image viewer  
                im1.save(sv_img+f"/{file}")
            except Exception as e:
                print(e, file)
                pass

if __name__ == "__main__":
    img_cvt()

