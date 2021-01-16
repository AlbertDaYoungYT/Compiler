LOGS = ".\\data\\logs\\"
log = open(LOGS+"zip.log", "w")
log.write("")
log.close()
log = open(LOGS+"zip.log", "a")
from zipfile import ZipFile
import os

def get_all_file_paths(directory):

    # initializing empty file paths list
    file_paths = []

    log.write("Getting all file paths\n")
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths

def main():
    log.write("Awating 'Operation' input...\n")
    file_operation = int(input("Enter File Operation (1=extract/2=write): "))

    if file_operation == 1:
        log.write("Awating 'File' input...\n")
        file_name = str(input("Enter File Name: "))
        with ZipFile(file_name, 'r') as zip:
            zip.printdir()

            log.write("Extracting all files...\n")
            print('Extracting all the files now...')
            zip.extractall()
            print('Done!')
            log.write("Done\n")
    else:
        pass
    # path to folder which needs to be zipped
    log.write("Awating 'Folder' input...\n")
    directory = str(input("Enter Folder Name: "))

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile
    with ZipFile(str(input("Enter Zipfile Name: ")),'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)

    log.write("All files zipped\n")
    print('All files zipped successfully!')