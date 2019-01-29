# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testqt5.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 490)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.replaceAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.replaceAllButton.setObjectName("replaceAllButton")
        self.gridLayout.addWidget(self.replaceAllButton, 4, 1, 1, 1)
        self.textLog = QtWidgets.QTextBrowser(self.centralwidget)
        self.textLog.setObjectName("textLog")
        self.gridLayout.addWidget(self.textLog, 0, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.PickSourceFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.PickSourceFileButton.setObjectName("PickSourceFileButton")
        self.gridLayout.addWidget(self.PickSourceFileButton, 4, 0, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 5, 1, 1, 1)
        self.pickRuleFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.pickRuleFileButton.setObjectName("pickRuleFileButton")
        self.gridLayout.addWidget(self.pickRuleFileButton, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")

        self.retranslateUi(MainWindow)
        self.PickSourceFileButton.clicked.connect(MainWindow.picksourcefile)
        self.replaceAllButton.clicked.connect(MainWindow.replaceall)
        self.clearButton.clicked.connect(MainWindow.cleartable)
        self.pickRuleFileButton.clicked.connect(MainWindow.pickrulefile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "regexMe"))
        self.replaceAllButton.setText(_translate("MainWindow", "Replace All"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "RegEx"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Replacement"))
        self.PickSourceFileButton.setText(_translate("MainWindow", "Pick Source File (.txt)"))
        self.clearButton.setText(_translate("MainWindow", "Clear Regex and Replacements"))
        self.pickRuleFileButton.setText(_translate("MainWindow", "Pick Regex Rule File (.txt)"))
        self.actionClose.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

