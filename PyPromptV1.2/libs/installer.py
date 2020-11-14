from zipfile import ZipFile
import shutil
import time
import glob
import wget
import os

global version
version = "1.2"
dir_path = os.path.dirname(os.path.realpath("__file__"))

def tpiInstaller(PackageName):
    f = open(dir_path+"\\libs\\.tpidb", "r")
    for x in f:
        line = x.split("|")
        if line[2] == version:
            if line[0] == PackageName:
                url = line[1]
                wget.download(url)
                for file in glob.glob("*.zip"):
                    print(file)
                    shutil.move(dir_path+"\\"+file, dir_path+"\\libs\\")
                    with ZipFile(dir_path+"\\libs\\"+file, 'r') as zip: 
                        # printing all the contents of the zip file 
                        zip.printdir() 
                    
                        # extracting all the files 
                        print('Extracting all the files now...') 
                        zip.extractall(dir_path+"\\libs") 
                        print('done') 
                    os.remove(dir_path+"\\libs\\"+file)
            else:
                print("Package not found")
        else:
            print("Can't download insufficient Version")
            
def installPacks():
    os.system('cmd /c "pip install gTTS"')
    time.sleep(1)
    os.system('cmd /c "pip install wget"')
    time.sleep(1)
    os.system('cmd /c "pip install opencv-python"')
    time.sleep(1)
    os.system('cmd /c "pip install serial"')
    print('done')