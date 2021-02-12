"""
Specify paths before use!

If your files are using different naming scheme than "id. NAME.extension" change custom split to whatever fills your needs

Program is using a dict to sort files because "475" < "5".
"""

import os

sourcePath = r""
destinationPath = r""

customSplit = ". " # This can't be set to ".", all other options will work

while True:
    try:
        startID = int(input("Start with ID: "))
        break
    except ValueError:
        print("Start ID must be an integer!\n")

fileList = os.listdir(sourcePath)

sortingFiles = dict()

for i in fileList:
    sortingFiles[int(i.split(customSplit)[0])] = i

sortedFiles = sorted(sortingFiles.items())

for i in sortedFiles:
    for y in fileList:
        if i[1] == y:
            oldName = y.split(customSplit)[1]
            os.rename(sourcePath + "\\" + y, destinationPath + "\\" + str(startID) + customSplit + oldName) 
    startID += 1

print("Done")
