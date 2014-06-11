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

        self.Files = QtGui.QStandardItemModel()
        self.converter = Converter()
        
        x = Ui_MainWindow()
        x.setupUi(self)
        
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
        self.pushButton.setEnabled(False)
        self.progressBar.reset()
        self.progressBar.setMaximum(self.Files.rowCount())
        
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose Destination ", os.path.expanduser("~"), QtWidgets.QFileDialog.ShowDirsOnly)
        
        translateList = []
        for index in range(self.Files.rowCount()):
            item = self.Files.item(index)
            translateList.append(item.data(FILEPATHROLE))
        
        index = 0
        for file in translateList:
            self.converter.convert(file, dir)
            index += 1
            self.progressBar.setValue(index)            

            
        self.Files.removeRows(0, self.Files.rowCount())
        self.progressBar.reset()
        self.pushButton.setEnabled(True)
        
        
    def closeEvent(self, event):
        self.converter.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = CustomMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

