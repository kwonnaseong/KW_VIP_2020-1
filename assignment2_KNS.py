#2017203062 소프트웨어학부 권나성
#다학년다학기 프로젝트 2차 과제
#이미지 불러와 상하반전시켜 출력

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import numpy as np
import qimage2ndarray

basic_ui = uic.loadUiType("Simplewidget.ui")[0] #ui파일 로드하여 basic_ui 클래스 생성
class WindowClass(QMainWindow, basic_ui): #QMainWindow 클래스와 basic_ui클래스로부터 다중상속 받는 WindowClass 생성
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #각 버튼의 singal clicked()와 slot Imageshow() 연결
        self.pushButton.clicked.connect(lambda:self.Imageshow(0)) #load 버튼 클릭 
        self.pushButton_2.clicked.connect(lambda:self.Imageshow(1)) #flip 버튼 클릭 

    def Imageshow(self,num):

        if num == 0: #load버튼을 클릭한 경우
            self.fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "") #Folder dialog 출력
             
        if self.fileName:
            self.image = QImage(self.fileName) #클래스 Qimage형 멤버변수 image에 이미지 로드

            if self.image.isNull():
                QMessageBox.information(self, "Image Viewr", "Cannot load %s." %fileName)
                return

        if num == 1: #flip버튼을 클릭한 경우
            image_array = qimage2ndarray.rgb_view(self.image) #Qimage를 numpy로 변환
            image_array=np.flip(image_array,0) #image_array에 상하반전 수행
            self.image=qimage2ndarray.array2qimage(image_array, normalize=False) #numpy를 Qimage로 변환 
                
        qPixmapVar = QPixmap.fromImage(self.image) #Qimage를 Qpixmap으로 변환
        qPixmapVar = qPixmapVar.scaled(256,256) #이미지의 가로 세로 크기 조절
        self.label.setPixmap(qPixmapVar) #Label의 영역에 사진 표시 
    
        self.show()
        
if __name__=="__main__":
    app=QApplication(sys.argv) #프로그램을 실행시켜주는 클래스
    myWindow=WindowClass() #WindowClass의 인스턴스 생성
    myWindow.show() #프로그램 화면을 보여줌
    app.exec_() #프로그램을 작동시킴
    
        
