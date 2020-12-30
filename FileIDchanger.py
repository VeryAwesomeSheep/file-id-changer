import os

sourcePath = r""
destinationPath = r""

while True:
    try:
        startID = int(input("Start with ID: "))
        break
    except ValueError:
        print("Start ID must be an integer!\n")

fileList = os.listdir(sourcePath)

sortingFiles = dict()

for i in fileList:
    sortingFiles[int(i.split(". ")[0])] = i

sortedFiles = sorted(sortingFiles.items())

for i in sortedFiles:
    for y in fileList:
        if i[1] == y:
            oldName = y.split(". ")[1]
            os.rename(sourcePath + "\\" + y, destinationPath + "\\" + str(startID) + ". " + oldName) 
    startID += 1

print("Done")