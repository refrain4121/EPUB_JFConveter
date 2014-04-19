#-*- coding : utf8 -*-
# /usr/bin/env python
import os, sys, ntpath
from PyQt5 import QtCore, QtGui, QtWidgets
from layout import Ui_MainWindow
from EpubconvertScript import *

FILEPATHROLE = 33

class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        
        x = Ui_MainWindow()
        x.setupUi(self)
        
        self.converter = Converter()
        self.Files = QtGui.QStandardItemModel()
        
        self.connect()
    
    def connect(self):
        self.listView.trigger.connect(self.receiveFile)
        self.pushButton.clicked.connect(self.startConvert)
        
        self.listView.setModel(self.Files)
       
    def receiveFile(self, urls):
        
        for url in urls: 	
            
            fileName, fileExtension = os.path.splitext(os.path.basename(url))
            
            if (fileExtension == '.epub'):
                item = QtGui.QStandardItem(fileName)
                item.setData(url, FILEPATHROLE)
                self.Files.appendRow(item)
    
    def startConvert(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose Destination ", os.path.expanduser("~"), QtWidgets.QFileDialog.ShowDirsOnly)
        for index in range(self.Files.rowCount()):
            item = self.Files.item(index)
            self.converter.convert(item.data(FILEPATHROLE), dir)
        
        
    def closeEvent(self, event):
        self.converter.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = CustomMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

