# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 635)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 70, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(10, 100, 381, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 361, 21))
        self.label_3.setObjectName("label_3")
        self.splitter_4 = QtWidgets.QSplitter(self.centralWidget)
        self.splitter_4.setEnabled(True)
        self.splitter_4.setGeometry(QtCore.QRect(180, 150, 152, 131))
        self.splitter_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setOpaqueResize(False)
        self.splitter_4.setChildrenCollapsible(False)
        self.splitter_4.setObjectName("splitter_4")
        self.Score_Val_1 = QtWidgets.QLabel(self.splitter_4)
        self.Score_Val_1.setObjectName("Score_Val_1")
        self.Score_Val_2 = QtWidgets.QLabel(self.splitter_4)
        self.Score_Val_2.setObjectName("Score_Val_2")
        self.Score_Val_3 = QtWidgets.QLabel(self.splitter_4)
        self.Score_Val_3.setObjectName("Score_Val_3")
        self.Score_Val_4 = QtWidgets.QLabel(self.splitter_4)
        self.Score_Val_4.setObjectName("Score_Val_4")
        self.Score_Val_5 = QtWidgets.QLabel(self.splitter_4)
        self.Score_Val_5.setObjectName("Score_Val_5")
        self.Score_Val_6 = QtWidgets.QLabel(self.splitter_4)
        self.Score_Val_6.setObjectName("Score_Val_6")
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(10, 280, 381, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 361, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(30, 320, 361, 21))
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 350, 351, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setGeometry(QtCore.QRect(20, 40, 221, 21))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 0, 91, 22))
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 0, 81, 22))
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralWidget)
        self.splitter_2.setEnabled(True)
        self.splitter_2.setGeometry(QtCore.QRect(20, 10, 241, 27))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setOpaqueResize(False)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.splitter_3 = QtWidgets.QSplitter(self.centralWidget)
        self.splitter_3.setGeometry(QtCore.QRect(30, 150, 152, 131))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setOpaqueResize(False)
        self.splitter_3.setChildrenCollapsible(False)
        self.splitter_3.setObjectName("splitter_3")
        self.Score_label_1 = QtWidgets.QLabel(self.splitter_3)
        self.Score_label_1.setObjectName("Score_label_1")
        self.Score_label_2 = QtWidgets.QLabel(self.splitter_3)
        self.Score_label_2.setObjectName("Score_label_2")
        self.Score_label_3 = QtWidgets.QLabel(self.splitter_3)
        self.Score_label_3.setObjectName("Score_label_3")
        self.Score_label_4 = QtWidgets.QLabel(self.splitter_3)
        self.Score_label_4.setObjectName("Score_label_4")
        self.Score_label_5 = QtWidgets.QLabel(self.splitter_3)
        self.Score_label_5.setObjectName("Score_label_5")
        self.Score_label_6 = QtWidgets.QLabel(self.splitter_3)
        self.Score_label_6.setObjectName("Score_label_6")
        self.Ranking_label = QtWidgets.QLabel(self.centralWidget)
        self.Ranking_label.setGeometry(QtCore.QRect(210, 300, 67, 21))
        self.Ranking_label.setObjectName("Ranking_label")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PUBG Ranking Predict Program"))
        self.pushButton.setText(_translate("MainWindow", "예측시작"))
        self.label_3.setText(_translate("MainWindow", "당신의 평균 전적은..."))
        self.Score_Val_1.setText(_translate("MainWindow", "0"))
        self.Score_Val_2.setText(_translate("MainWindow", "0"))
        self.Score_Val_3.setText(_translate("MainWindow", "0"))
        self.Score_Val_4.setText(_translate("MainWindow", "0"))
        self.Score_Val_5.setText(_translate("MainWindow", "0"))
        self.Score_Val_6.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "당신의 예상 순위는 100명 중               입니다."))
        self.label_5.setText(_translate("MainWindow", "순위를 더 올리려면?"))
        self.label.setText(_translate("MainWindow", "서버"))
        self.radioButton.setText(_translate("MainWindow", "Steam"))
        self.radioButton_2.setText(_translate("MainWindow", "Kakao"))
        self.label_2.setText(_translate("MainWindow", "아이디"))
        self.Score_label_1.setText(_translate("MainWindow", "게임중 이동한 거리       :"))
        self.Score_label_2.setText(_translate("MainWindow", "게임중 획득한 무기수   : "))
        self.Score_label_3.setText(_translate("MainWindow", "가장 멀리서 킬한 거리  : "))
        self.Score_label_4.setText(_translate("MainWindow", "회복 아이템 사용횟수   : "))
        self.Score_label_5.setText(_translate("MainWindow", "도핑 아이템 사용횟수   : "))
        self.Score_label_6.setText(_translate("MainWindow", "입힌 대미지                    : "))
        self.Ranking_label.setText(_translate("MainWindow", "0등"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
