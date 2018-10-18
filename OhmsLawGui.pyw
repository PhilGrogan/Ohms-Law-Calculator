#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OhmsLawGui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import scripts
import saves

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(290, 345)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 51, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 0, 211, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.v_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.v_edit.setObjectName("v_edit")
        self.verticalLayout_2.addWidget(self.v_edit)
        self.a_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.a_edit.setObjectName("a_edit")
        self.verticalLayout_2.addWidget(self.a_edit)
        self.w_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.w_edit.setObjectName("w_edit")
        self.verticalLayout_2.addWidget(self.w_edit)
        self.o_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.o_edit.setObjectName("o_edit")
        self.verticalLayout_2.addWidget(self.o_edit)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 210, 271, 89))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.calc_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.calc_button.setObjectName("calc_button")
        self.gridLayout.addWidget(self.calc_button, 0, 0, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout.addWidget(self.delete_button, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 290, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Premade_Chart = QtWidgets.QAction(MainWindow)
        self.actionOpen_Premade_Chart.setObjectName("actionOpen_Premade_Chart")
        self.actionSave_Current_Work = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Work.setObjectName("actionSave_Current_Work")
        self.actionDelete_Current_Work = QtWidgets.QAction(MainWindow)
        self.actionDelete_Current_Work.setObjectName("actionDelete_Current_Work")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionHow_To = QtWidgets.QAction(MainWindow)
        self.actionHow_To.setObjectName("actionHow_To")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen_Premade_Chart)
        self.menuFile.addAction(self.actionSave_Current_Work)
        self.menuFile.addAction(self.actionDelete_Current_Work)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionHow_To)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ohms Law Calculator"))
        self.label.setText(_translate("MainWindow", "Volts"))
        self.label_3.setText(_translate("MainWindow", "Amps"))
        self.label_2.setText(_translate("MainWindow", "Watts"))
        self.label_4.setText(_translate("MainWindow", "Ohms"))
        self.calc_button.setText(_translate("MainWindow", "Calculate"))
        self.calc_button.clicked.connect(self.calc_click)
        self.delete_button.setText(_translate("MainWindow", "Clear"))
        self.delete_button.clicked.connect(self.del_click)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_Premade_Chart.setText(_translate("MainWindow", "Open Premade Chart"))
        self.actionSave_Current_Work.setText(_translate("MainWindow", "Save Current Work"))
        self.actionDelete_Current_Work.setText(_translate("MainWindow", "Delete Current Work"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.triggered.connect(self.closed_clicked)
        self.actionHow_To.setText(_translate("MainWindow", "How To"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def del_click(self):
        saves.temp(float(self.v_edit.text()), float(self.a_edit.text()),\
                   float(self.w_edit.text()), float(self.o_edit.text()))
        self.v_edit.setText("")
        self.a_edit.setText("")
        self.o_edit.setText("")
        self.w_edit.setText("")

    def calc_click(self):
        v, a, o, w = scripts.calc_clicked(self.v_edit.text(), self.a_edit.text(),\
                                          self.w_edit.text(), self.o_edit.text())
        self.v_edit.setText(str(v))
        self.a_edit.setText(str(a))
        self.o_edit.setText(str(o))
        self.w_edit.setText(str(w))

    def closed_clicked(self):
        MainWindow.close()
        app.quit()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

