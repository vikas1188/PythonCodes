import glob2
from datetime import datetime

# fileList = glob2.glob("fil*.txt")
# print (fileList[0], fileList[1], fileList[2])
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", "w") as finalFile:
    for i in [1,2,3]:
        with open("file"+str(i)+".txt","r") as myfile:
            finalFile.write(myfile.read())
