import os, os.path

QUIT = '7'

COMMANDS = ('1', '2', '3', '4', '5', '6', '7')

MENU = """1   List the current directory
2   Move up
3   Move down
4   Number of files in the directory
5   Size of the directory in bytes
6   Search for a filename
7   Quit the program"""

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        if command == '7':
            print("Have a nice day!")
            break
        runCommand(command)
        

def acceptCommand():
    while True:
        command = input("Enter a number: ")
        if not command in COMMANDS:
            print("Error: command not recognized")
        else:
            return command

def runCommand(command):
    """Selects and runs a command."""
    if command == '1':
        ListCurrentDir(os.getcwd())

    elif command == '2':
        moveUp()

    elif command == '3':
        moveDown(os.getcwd())

    elif command == '4':
        print("The total number of files is", \
                countFiles(os.getcwd()))
    
    elif command == '5':
        print("The total number of bytes is", \
                countBytes(os.getcwd()))
    
    elif command == '6':
        target   = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)
    elif command == '7':
        main()


def ListCurrentDir(dirName):
    """prints a list of the cwd's contents."""
    lyst = os.listdir(dirName)
    for element in lyst:
        print(element)

def moveUp():
    """Moved up to the parent directory."""
    os.chdir("..")

def moveDown(currentDir):
    """Moves down to the named subdirectory if it exists."""
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
            os.path.isdir(newDir):
                os.chdir(newDir)
    else:
        print("ERROR: no such name")

    
def countFiles(path):
    count = 0
    lyst  = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())


def countBytes(path):
    count = 0
    lyst  = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count



def findFiles(target, path):
    files = []
    lyst  = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(findFiles(target, os.getcwd()))
            os.chdir("..")
    return files

main()
