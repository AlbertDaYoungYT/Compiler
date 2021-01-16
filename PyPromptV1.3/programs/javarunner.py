from subprocess import call

def CallScript(FileName, process):
    call([process, FileName])