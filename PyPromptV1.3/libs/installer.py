LOGS = ".\\data\\logs\\"
log = open(LOGS+"installer.log", "w")
log.write("")
log.close()
log = open(LOGS+"installer.log", "a")
try:
    log.write("Trying to import modules...\n")
    from zipfile import ZipFile
    import shutil
    import time
    import glob
    import wget
    import os
except ModuleNotFoundError:
    log.write("Failed to import modules\nTrying to install modules...\n")
    import os
    os.system('cmd /c "pip install wget"')
    log.write("Modules installed successfully\n")
finally:
    log.write("Importing modules...\n")
    from zipfile import ZipFile
    import shutil
    import time
    import glob
    import wget
    import os
log.write("Success\n")

global version
version = "1.3"
dir_path = os.path.dirname(os.path.realpath("__file__"))

def tpiInstaller(PackageName):
    log.write("Opening data file\n")
    f = open(dir_path+"\\libs\\data.tpidb", "r")
    for x in f:
        line = x.split("|")
        if line[2] == version:
            if line[0] == PackageName:
                url = line[1]
                log.write("Downloading package...\n")
                wget.download(url)
                for file in glob.glob("*.zip"):
                    log.write("\n")
                    print(file)
                    shutil.move(dir_path+"\\"+file, dir_path+"\\libs\\")
                    with ZipFile(dir_path+"\\libs\\"+file, 'r') as zip: 
                        # printing all the contents of the zip file 
                        zip.printdir() 
                    
                        # extracting all the files 
                        print('Extracting all the files now...') 
                        log.write("Extracting files...\n")
                        zip.extractall(dir_path+"\\libs") 
                        print('done') 
                    os.remove(dir_path+"\\libs\\"+file)
            else:
                log.write("ERROR: Package not found\n")
                print("Package not found")
        else:
            log.write("ERROR: Insufficient Version\n")
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