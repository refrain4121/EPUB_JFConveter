# -*- coding:utf-8 -*-
import os
import zipfile
from jianfan import *

class TypeUnknownError(Exception):
    pass

def parsePos(epubPos):
    pos = u""
    
    namelist = os.listdir(epubPos)
    print (namelist)
    if "OEBPS" in namelist: pos = "OEBPS/text"
    elif "OPS" in namelist: pos = "OPS"
    else: raise TypeUnknownError
    
    return os.path.join(epubPos, pos)
    
def translate(filepos, file):

    f = open(os.path.join(filepos, file), 'r', encoding = 'utf8')
    unconvert_text = f.read()
    converted = jtof(unconvert_text)
    f.close()
    f = open(os.path.join(filepos, file), 'w', encoding = 'utf8')
    f.write(converted)
    f.close()    

resorucePath = os.path.join(os.getcwd(), u"source")
workingFilePath = os.path.join(os.getcwd(), u"temp")

if not os.path.exists(workingFilePath): os.mkdir(u"temp")


for filename in  os.listdir(resorucePath):
    filePos = os.path.join(resorucePath, filename)
    
    if not (zipfile.is_zipfile(filePos)): continue
    
    new_filename = jtof(filename)
    new_filename = os.path.splitext(new_filename)[0]
    
    orginal = zipfile.ZipFile(filePos)
    tempFilePath = os.path.join(workingFilePath, new_filename)
    if not os.path.exists(tempFilePath): os.mkdir(tempFilePath)
    
    for file in orginal.namelist():
        orginal.extract(file, tempFilePath)
    orginal.close()
    
    try:
        textPos = parsePos(tempFilePath)
    except TypeUnknownError:
        print ("unknown type of EPUB, skip...")
        continue
    
    # convert text    
    for textfile in os.listdir(textPos):
        if os.path.isdir(os.path.join(textPos, textfile)): continue
        translate(textPos, textfile)
        

    # for dirpath, dirnames, filenames in os.walk(tempFilePath): 
        # for filename in filenames: 
            # if os.path.isdir(os.path.join(dirpath,filename)): continue
            # f = open(os.path.join(dirpath,filename), 'r', encoding = 'utf8')
            # unconvert_text = f.read()
            # converted = jtof(unconvert_text)
            # f.close()
            # f = open(os.path.join(dirpath,filename), 'w', encoding = 'utf8')
            # f.write(converted)
            # f.close()       
        
    newzip = zipfile.ZipFile("output/"+new_filename+".epub",'w',zipfile.ZIP_DEFLATED)  
    for dirpath, dirnames, filenames in os.walk(tempFilePath): 
        for filename in filenames: 
            newzip.write(os.path.join(dirpath,filename)) 
    newzip.close()

for the_file in os.listdir(workingFilePath):
    file_path = os.path.join(workingFilePath, the_file)
    if os.path.isfile(file_path):
        os.unlink(file_path)

        
        
        
