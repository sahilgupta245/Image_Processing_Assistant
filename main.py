import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

import subprocess
import os
import cmd
import cv2
from PIL import Image
from pytesseract import pytesseract
import time
path_to_tesseract = r"Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract



class WelcomeHome(QDialog):
    def __init__(self):
        super(WelcomeHome, self).__init__()
        loadUi("ui\welcome.ui",self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.showFullScreen()
        self.start.clicked.connect(self.WelcomeScreen)
    
    def WelcomeScreen(self):
        welcomess=WelcomeScreen()
        widget.addWidget(welcomess)
        self.showFullScreen()
        widget.setCurrentIndex(widget.currentIndex()+1)

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("ui\mainhome.ui",self)
        self.showFullScreen()
        self.pushButton_3.clicked.connect(self.gotoimgsketch)
        self.handwritingbtn.clicked.connect(self.gototexthandwriting)
        self.pushButton_2.clicked.connect(self.gotoimgtext)
        self.pushButton_4.clicked.connect(self.gotohandgesture)
        self.pushButton_6.clicked.connect(self.gotomouse)
        self.pushButton_7.clicked.connect(self.gotoqrreader)
        self.exit.clicked.connect(lambda: os.system(cmd))
        self.home.clicked.connect(self.__init__)
  
    
    def gotoimgsketch(self):
        imgsketch=imgsketchscreen()
        widget.addWidget(imgsketch)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gototexthandwriting(self):
        texthandwriting=handwritingscreen()
        widget.addWidget(texthandwriting)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoimgtext(self):
        imgtxt=imgtxtscreen()
        widget.addWidget(imgtxt)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotohandgesture(self):
        command="python ..\Project_image\hand_gestures\handgesture.py"
        subprocess.Popen(command)
    
    def gotomouse(self):
        command="python ..\Project_image\mousegesture\mousehandgesture.py"
        subprocess.Popen(command)
    
    def gotoqrreader(self):
        command="python QR-Code-master\custom_qr.py"
        subprocess.Popen(command)


class imgtxtscreen(QDialog):
    def __init__(self):
        super(imgtxtscreen, self).__init__()
        loadUi("ui\img-txt.ui",self)
        self.home.clicked.connect(self.gotohome)
        self.pushButton_10.clicked.connect(self.getImage)
        self.imgtextconvert.clicked.connect(self.getText)
        self.resetbtn.clicked.connect(self.reset)
        self.exit.clicked.connect(lambda: os.system(cmd))

    def gotohome(self):
        welcomescreen=WelcomeScreen()
        widget.addWidget(welcomescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def reset(self):
        resetscreen=imgtxtscreen()
        widget.addWidget(resetscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','', "Image files (*.jpg *.jpeg *.png)")
        global imagepath
        imagepath = fname[0]
        pixmap = QPixmap(imagepath)
        self.label_4.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())

    def getText(self):
        img = Image.open(imagepath)
        text = pytesseract.image_to_string(img)

        path_text='..\Project_image\img_to_text\\text-output.txt'
        with open(path_text,'w') as filef:
            filef.write(str(text))
        subprocess.Popen(['notepad.exe', path_text], creationflags=subprocess.CREATE_NEW_CONSOLE)


class imgsketchscreen(QDialog):
    def __init__(self):
        super(imgsketchscreen, self).__init__()
        loadUi("ui\img-sketch.ui",self)
        self.home.clicked.connect(self.gotohome)
        self.pushButton_11.clicked.connect(self.haha)
        self.pushButton_10.clicked.connect(self.getImage)
        self.resetbtn.clicked.connect(self.reset)
        self.exit.clicked.connect(lambda: os.system(cmd))

    def reset(self):
        resetscreen=imgsketchscreen()
        widget.addWidget(resetscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','', "Image files (*.jpg *.jpeg *.png)")
        global imagepath
        imagepath = fname[0]
        pixmap = QPixmap(imagepath)
        self.label_4.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())
    
    def haha(self):       
        image = cv2.imread(imagepath)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        invert=cv2.bitwise_not(gray_image)
        blur=cv2.GaussianBlur(invert, (21, 21), 0)
        invertedblur = cv2.bitwise_not(blur)
        pencil_sketch = cv2.divide(gray_image, invertedblur,scale=225.0)
        resized_image = cv2.resize(pencil_sketch,(1080,720))
        resized_image2 = cv2.resize(image,(1080,720))
        cv2.imwrite("..\Project_image\img_to_sketch\output.png",resized_image)
        cv2.imshow("..\Project_image\img_to_sketch\original image", resized_image2)
        cv2.imshow("..\Project_image\img_to_sketch\pencil sketch", resized_image)
        cv2.waitKey()
        

    def save_text(self):
        text, ok = self.le.text()   
        filename=self.textEdit.toPlainText(self, 'Save File', '.')
        fname = open(filename, 'w')
        fname.write(self.le.setText(str(text)))
        fname.close()
    
    def gotohome(self):
        welcomescreen=WelcomeScreen()
        widget.addWidget(welcomescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class handwritingscreen(QDialog):
    def __init__(self):
        super(handwritingscreen, self).__init__()
        loadUi("ui\\text-handwriting.ui",self)
        self.home.clicked.connect(self.gotohome)
        self.resetbtn.clicked.connect(self.reset)
        self.convert.clicked.connect(self.goconvert)
        self.exit.clicked.connect(lambda: os.system(cmd))

        
    def goconvert(self):
        mytext = self.textEdit_2.toPlainText()
        with open('..\project_image\\text-to-handwritten\\textinput.txt', 'w') as filef:
            filef.write(str(mytext))
        

        os.system('python ..\project_image\\text-to-handwritten\\txttohandwriting.py')
        os.system('..\project_image\\text-to-handwritten\image_handwritten.pdf')
    
    def gotohome(self):
        welcomescreen=WelcomeScreen()
        widget.addWidget(welcomescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def reset(self):
        resetscreen=handwritingscreen()
        widget.addWidget(resetscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def pushButton_3_clicked():
        print("Opening Image to Sketch")
        command="python sketch.py"
        subprocess.Popen(command)



#main
app = QApplication(sys.argv)
welcome = WelcomeHome()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1080)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")





