LOGS = ".\\data\\logs\\"
log = open(LOGS+"ytdownloader.log", "w")
log.write("")
log.close()
log = open(LOGS+"ytdownloader.log", "a")
try:
    log.write("Trying to import modules...\n")
    from pytube import YouTube
except ModuleNotFoundError:
    log.write("Failed to import modules\nTrying to install modules...\n")
    import os
    os.system('cmd /c "pip install pytube"')
    log.write("Modules installed successfully\n")
log.close()

def main():
    log = open(LOGS+"ytdownloader.log", "a")
    #ask for the link from user
    log.write("Awating input...\n")
    link = input("Enter the link of YouTube video you want to download:  ")
    log.write("Importing link...\n")
    yt = YouTube(link)

    log.write("Showing details\n")
    #Showing details
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    print("Rating of video: ",yt.rating)
    #Getting the highest resolution possible
    log.write("Getting highest resolution...\n")
    ys = yt.streams.get_highest_resolution()

    log.write("Downloading...\n")
    #Starting download
    print("Downloading...")
    ys.download(".\\programs\\AppData\\videos\\")
    print("Download completed!!")
    log.write("Completed download\n")
    log.close()