#-*- coding : utf8 -*-
# /usr/bin/env python
import sys, ntpath
from PyQt5 import QtCore, QtGui, QtWidgets
from layout import Ui_MainWindow

class window():
    def __init__(self):
        self.ui = QtWidgets.QMainWindow()
        x = Ui_MainWindow()
        x.setupUi(self.ui)
        
        self.Files = QtGui.QStandardItemModel()
        
        self.connect()
        
    def connect(self):
        self.ui.listView.trigger.connect(self.receiveFile)
        
        self.ui.listView.setModel(self.Files)
       
    def receiveFile(self, urls):
        
        for url in urls: 	
            
            fileName, fileExtension = os.path.splitext(url)
            
            if (fileExtension == '.epub'):
                item = QtGui.QStandardItem()
                self.Files.appendRow(item)
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = window()
    MainWindow.ui.show()
    sys.exit(app.exec_())

