#-*- coding : utf8 -*-
# /usr/bin/env python

import os,shutil, zipfile
from TSConvertScript import ZhTranslator

class Converter(object):
    def __init__(self):
        self.tempFolder = os.path.join(os.getcwd(), "Temp")
        self.textFileFilter = [".txt", ".html", ".xhtml", ".ncx", ".opf"]
        
        self.zhTranslator = ZhTranslator()
        
        if not os.path.exists(self.tempFolder): os.mkdir(self.tempFolder)
        
    def convert(self, filepath, destinatonPath):
        fileName, fileExtend = os.path.splitext(os.path.basename(filepath))
        
        newname = zhTranslator.StoT(fileName)
        
        # create temp folder
        tempFilePath = os.path.join(self.tempFolder, newname)
        os.mkdir(tempFilePath)
        
        #copy file to temp folder
        originalZip = zipfile.ZipFile(filepath)
        for file in originalZip.namelist():
            originalZip.extract(file, tempFilePath)
        originalZip.close()
        
        # translate text file
        for dirPath, dirNames, fileNames in os.walk(tempFilePath):
            for i in fileNames:
                name, extension = os.path.splitext(i)
                if extension in self.textFileFilter:
                    self.translate(dirPath, i)    
        
        # compress into new folder
        newZip = zipfile.ZipFile(os.path.join(destinatonPath, newname+".epub"), "w")
        for dirPath, dirNames, fileNames in os.walk(tempFilePath):
            for obj in fileNames:
                tmp = dirPath.replace(tempFilePath, u"")
                newZip.write(os.path.join(dirPath, obj), os.path.join(tmp, obj))
        newZip.close()

    
    # need tp rewrite
    def translate(self, dirPath, filename):
        rf = open(os.path.join(dirPath, filename), encoding = "utf8")
        translated = []
        for line in rf:
            translated.append(zhTranslator.StoT(line)) 
        rf.close()
        
        wf = open(os.path.join(dirPath, filename), "w", encoding = "utf8")
        wf.writelines(translated)
        wf.close()                
        
        
    def close(self):
        shutil.rmtree(self.tempFolder)
        