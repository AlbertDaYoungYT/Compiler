LOGS = ".\\data\\logs\\"
log = open(LOGS+"tpiupdate.log", "w")
log.write("")
log.close()
log = open(LOGS+"tpiupdate.log", "a")
try:
    log.write("Trying to import modules...\n")
    import requests
    import shutil
    import wget
    import os
except ModuleNotFoundError:
    log.write("Failed to import modules\nTrying to install modules...\n")
    import os
    os.system('cmd /c "pip install wget"')
    os.system('cmd /c "pip install requests"')
    log.write("Modules installed successfully\n")
finally:
    log.write("Importing modules...\n")
    import requests
    import shutil
    import wget
    import os
log.write("Success\n")

def update():
    log.write("Sending request to Github...\n")
    r = requests.get('https://raw.githubusercontent.com/AlbertDaYoungYT/PyPrompt/main/update/db.config')

    log.write("Opening config file...\n")
    file = open(".\\libs\\db.config", "w")
    log.write("Writing to config file...\n")
    file.write(r.text)
    file.close()
    log.write("Done\n")

    file = open(".\\libs\\db.config", "r")

    try:
        log.write("Deleting data file...\n")
        os.remove(".\\libs\\data.tpidb")
    except Exception:
        pass
    log.write("Downloading data file...")
    wget.download(file.read())
    shutil.move(os.path.dirname(os.path.realpath("__file__"))+"\\data.tpidb", os.path.dirname(os.path.realpath("__file__"))+"\\libs\\")
    file.close()
    print()
    log.write("Done\n")
log.close()