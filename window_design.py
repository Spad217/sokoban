# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 365)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionrestart = QtWidgets.QAction(MainWindow)
        self.actionrestart.setObjectName("actionrestart")
        self.actionchoice_level = QtWidgets.QAction(MainWindow)
        self.actionchoice_level.setObjectName("actionchoice_level")
        self.actionchoice_file = QtWidgets.QAction(MainWindow)
        self.actionchoice_file.setObjectName("actionchoice_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setShortcut('Ctrl+Z')
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setShortcut('Ctrl+Shift+Z')
        self.actionRedo.setObjectName("actionRedo")
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.menuFile.addAction(self.actionrestart)
        self.menuFile.addAction(self.actionchoice_level)
        self.menuFile.addAction(self.actionchoice_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionRestart)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle("Sokoban")
        self.menuFile.setTitle("File")
        self.menuEdit.setTitle("Edit")
        self.actionrestart.setText("Save")
        self.actionchoice_level.setText("Choice level")
        self.actionchoice_file.setText("Choice file")
        self.actionExit.setText("Exit")
        self.actionUndo.setText("Undo")
        self.actionRedo.setText("Redo")
        self.actionRestart.setText("Restart")
