from sklearn.externals import joblib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from mainwindow_ui import Ui_MainWindow
import functions
import sys
import os

class MainWindow(Ui_MainWindow):
    file_loaded_model = None
    def __init__(self, w):
        Ui_MainWindow.__init__(self)
        self.setupUi(w)

        MainWindow.file_loaded_model = joblib.load('modelfile.pkl')
        if MainWindow.file_loaded_model == None:
            print("Model load fail!")

        self.pushButton.clicked.connect(self.predictStart)

    def predictStart(self):
        self.textBrowser.setText("")
        username = self.lineEdit.text()
        if self.radioButton.isChecked():
            server = "steam"
        elif self.radioButton_2.isChecked():
            server = "kakao"

        dataList, predictData = functions.player_data_collect(username, server)

        self.Score_Val_1.setText(str(round(dataList[0])) + "m")
        self.Score_Val_2.setText(str(round(dataList[1])) + "개")
        self.Score_Val_3.setText(str(round(dataList[2])) + "m")
        self.Score_Val_4.setText(str(round(dataList[3])) + "개")
        self.Score_Val_5.setText(str(round(dataList[4])) + "개")
        self.Score_Val_6.setText(str(round(dataList[5])))

        #데이터셋의 1~10위 평균 데이터
        topAvgData = [2813.5134925205784, 5.486616907085369, 75.0476587695883, \
                      3.3637369531495063, 3.566294544063871, 319.73547778285916]

        predictedList = []
        for n1, n2 in zip(topAvgData, dataList):
            predictedList.append(n1 - n2)

        print(predictedList)

        if predictedList[0] < 0:
            self.textBrowser.append("게임중 이동한 거리는 상위 랭커 평균보다 " + str(round(predictedList[0]*-1)) + " m 많습니다")
        else:
            self.textBrowser.append("게임중 이동한 거리는 상위 랭커 평균보다 " + str(round(predictedList[0])) + " m 적습니다")
        if predictedList[1] < 0:
            self.textBrowser.append("게임중 획득한 무기수는 상위 랭커 평균보다 " + str(round(predictedList[1]*-1)) + " 개 많습니다")
        else:
            self.textBrowser.append("게임중 획득한 무기수는 상위 랭커 평균보다 " + str(round(predictedList[1])) + " 개 적습니다")
        if predictedList[2] < 0:
            self.textBrowser.append("게임중 가장 멀리서 킬한 거리는 상위 랭커 평균보다 " + str(round(predictedList[2]*-1)) + " m 많습니다")
        else:
            self.textBrowser.append("게임중 가장 멀리서 킬한 거리는 상위 랭커 평균보다 " + str(round(predictedList[2])) + " m 적습니다")
        if predictedList[3] < 0:
            self.textBrowser.append("게임중 회복 아이템 사용횟수는 상위 랭커 평균보다 " + str(round(predictedList[3]*-1)) + " 개 많습니다")
        else:
            self.textBrowser.append("게임중 회복 아이템 사용횟수는 상위 랭커 평균보다 " + str(round(predictedList[3])) + " 개 적습니다")
        if predictedList[4] < 0:
            self.textBrowser.append("게임중 도핑 아이템 사용횟수는 상위 랭커 평균보다 " + str(round(predictedList[4]*-1)) + " 개 많습니다")
        else:
            self.textBrowser.append("게임중 도핑 아이템 사용횟수는 상위 랭커 평균보다 " + str(round(predictedList[4])) + " 개 적습니다")
        if predictedList[5] < 0:
            self.textBrowser.append("게임중 입힙 대미지는 상위 랭커 평균보다 " + str(round(predictedList[5]*-1)) + " 많습니다")
        else:
            self.textBrowser.append("게임중 입힙 대미지는 상위 랭커 평균보다 " + str(round(predictedList[5])) + " 적습니다")

        predictedRanking = MainWindow.file_loaded_model.predict(predictData)

        predictedRanking = int(predictedRanking*100)
        if predictedRanking == 1:
            predictedRanking = 1
        elif predictedRanking == 0:
            predictedRanking = 100
        else:
            predictedRanking = 101 - predictedRanking

        self.Ranking_label.setText(str(predictedRanking) + " 등")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = MainWindow(w)
    w.show()
    sys.exit(app.exec_())