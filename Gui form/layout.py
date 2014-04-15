# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sat Apr 12 01:59:22 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class CustomListView(QtWidgets.QListView):
    trigger = QtCore.pyqtSignal([list])
    def __init__(self, type, parent=None):
        super(CustomListView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setIconSize(QtCore.QSize(72, 72))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.trigger.emit(links)
        else:
            event.ignore()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 296)
        MainWindow.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.centralwidget.setObjectName("centralwidget")
        MainWindow.verticalLayout = QtWidgets.QVBoxLayout(MainWindow.centralwidget)
        MainWindow.verticalLayout.setObjectName("verticalLayout")
        MainWindow.listView = CustomListView(MainWindow.centralwidget)
        MainWindow.listView.setAcceptDrops(True)
        MainWindow.listView.setObjectName("listView")
        MainWindow.verticalLayout.addWidget(MainWindow.listView)
        MainWindow.horizontalLayout = QtWidgets.QHBoxLayout()
        MainWindow.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        MainWindow.horizontalLayout.addItem(spacerItem)
        MainWindow.pushButton = QtWidgets.QPushButton(MainWindow.centralwidget)
        MainWindow.pushButton.setObjectName("pushButton")
        MainWindow.horizontalLayout.addWidget(MainWindow.pushButton)
        MainWindow.verticalLayout.addLayout(MainWindow.horizontalLayout)
        MainWindow.setCentralWidget(MainWindow.centralwidget)
        MainWindow.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(MainWindow.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

