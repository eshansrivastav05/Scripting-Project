import os

def fileNamer(fileName):

    file = fileName + ".txt"

    cwd = os.getcwd()

    file = os.path.join(cwd, file)

    return file

def fileCreator(fileName, data):

    with open(fileName, 'w', encoding="utf-8") as fileObject:

        for objects in data:

            fileObject.write(objects)

    return fileObject