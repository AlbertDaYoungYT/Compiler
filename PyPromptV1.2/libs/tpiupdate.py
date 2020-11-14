import shutil
import wget
import os

def update():
    os.remove(".\\libs\\.tpidb")
    wget.download("https://drive.google.com/uc?export=download&id=1Ef9iLGp7TsMxNTuhOOT8nv1L9JtpNP06")
    shutil.move(os.path.dirname(os.path.realpath("__file__"))+"\\.tpidb", os.path.dirname(os.path.realpath("__file__"))+"\\libs\\")