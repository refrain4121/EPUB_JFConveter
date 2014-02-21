#-*- coding:utf-8 -*-
import os, shutil, zipfile
from jianfan import *
    
def translate(dirPath, filename):
    rf = open(os.path.join(dirPath, filename), encoding = "utf8")
    translated = []
    for line in rf:
        translated.append(jtof(line)) 
    rf.close()
    
    wf = open(os.path.join(dirPath, filename), "w", encoding = "utf8")
    wf.writelines(translated)
    wf.close()
    
path = os.getcwd()
sourcePath = os.path.join(path, "Source")
outputPath = os.path.join(path, "Output")
workingPath = os.path.join(path, "temp")
textFileFilter = [".txt", ".html", ".xhtml", ".ncx", ".opf"]

if not os.path.exists(sourcePath): 
    os.mkdir(sourcePath)
    print ("put epub in source folder and run again")
if not os.path.exists(outputPath): os.mkdir(outputPath)
if not os.path.exists(workingPath): os.mkdir(workingPath)

for file in os.listdir(sourcePath):
    filename, exten = os.path.splitext(file)
    if exten != ".epub": continue

    newname = jtof(file)
    print ("processing", newname)

    tempFilePath = os.path.join(workingPath, newname)
    if not os.path.exists(tempFilePath): os.mkdir(tempFilePath)
    
    original = zipfile.ZipFile(os.path.join(sourcePath, file))
    for file in original.namelist():
        original.extract(file, tempFilePath)
        
    original.close()
        
    for dirPath, dirNames, fileNames in os.walk(tempFilePath):
        for i in fileNames:
            name, extension = os.path.splitext(i)
            if extension in textFileFilter:
                translate(dirPath, i)
                
    newZip = zipfile.ZipFile(os.path.join(outputPath, newname), "w")
    for dirPath, dirNames, fileNames in os.walk(tempFilePath):
        
        for obj in fileNames:
            tmp = dirPath.replace(tempFilePath, u"")
            newZip.write(os.path.join(dirPath, obj), os.path.join(tmp, obj))
    newZip.close()
    
    shutil.rmtree(tempFilePath)

