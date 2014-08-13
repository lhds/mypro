# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import requests
from bs4 import BeautifulSoup
import sys

from Ui_qb_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    
    page_num = 1
    image = QImage()
    
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        url = 'http://www.qiushibaike.com/week/1/page/' + str(self.page_num)
        self.page_num += 1
        
        re = requests.get(url)
        html = BeautifulSoup(re.text)
        
        # 获取文字内容
        content = html.findAll('div', {'class':'content'})[0].next
        self.label_3.setText(content)
        # 获取图片内容(可能不存在，需要进行判断)
        thumb = html.findAll('div', {'class':'thumb'})
        if 0 != len(thumb):
            image_url = thumb[0].img['src']

            re = requests.get(image_url)
            self.image.loadFromData(re.content)
            self.label_4.setPixmap(QPixmap.fromImage(self.image))
        else:
            self.label_4.setPixmap(QPixmap.fromImage(QImage()))

app = QApplication(sys.argv)
window = MainWindow()
window.setWindowIcon(QIcon("1.jpg"))
window.show()
app.exec_()
