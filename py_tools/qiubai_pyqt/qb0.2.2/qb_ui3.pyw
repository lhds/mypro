# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import requests
import threading
from bs4 import BeautifulSoup

from Ui_qb_ui3 import Ui_MainWindow

event = threading.Event()

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    
    isinit = False
    imgCount = 1
        
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.textEdit.verticalScrollBar(), SIGNAL("valueChanged(int)"), self.LoadQB)
        
    def LoadQB(self, position):
        
        max_position = self.textEdit.verticalScrollBar().maximum()
        if self.isinit:
            if position < max_position:
                return
        
        self.isinit = True
        
        global event
        event.set()
        
    
    def ProcessGui(self, qb_content, image_content, have_img):
        
        cursor = QTextCursor(self.textEdit.document())
        cursor.movePosition(QTextCursor.End)
        frameFormat = QTextFrameFormat()
        frameFormat.setBackground(QBrush(QColor(245, 245, 245)))
        frameFormat.setBorder(2)
        frameFormat.setBorderBrush(QBrush(QColor(192, 192, 192)))
        childFrame = cursor.insertFrame(frameFormat)
        childFrameCursor = QTextCursor(childFrame)
        
        # 选择文字显示方式
        if 1: 
            html = '<font size=5>' + qb_content + '</font>'
            childFrameCursor.insertHtml(html)
        else:
            charFormat = QTextCharFormat()
            charFormat.setFont(QFont('隶书', 12))
            childFrameCursor.insertText(qb_content, charFormat)
        
        if have_img:
            childFrameCursor.insertHtml('<br>')
            image = QImage()
            image.loadFromData(image_content)
            childFrameCursor.insertImage(image, str(self.imgCount))
            self.imgCount += 1
        

class ParseThread(threading.Thread, QObject):
    
    page = 1
    
    def __init__(self):
        threading.Thread.__init__(self)
        QObject.__init__(self)
        
        
    def run(self):
        while(True):
            global event
            event.wait()
            event.clear()
            url = "http://www.qiushibaike.com/week/5/page/" + str(self.page)
            self.page += 1
        
            re = requests.get(url)
            html = BeautifulSoup(re.text)
            content_list = html.findAll("div",  {"class":"article block untagged mb15"})
        
            for i in range(len(content_list)):
                have_img = False
                for j in range(1, len(content_list[i].contents), 2):
                    if content_list[i].contents[j]['class'] == ['content']:
                        qb_content = content_list[i].contents[j].next
                    if content_list[i].contents[j]['class'] == ['thumb']:
                        image_url = content_list[i].contents[j].img['src']                    
                        re = requests.get(image_url)
                        image_content = re.content
                        have_img = True
                if have_img == False:
                    image_content = ''
                self.emit(SIGNAL("addItem(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), qb_content, image_content, have_img)
            


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.setWindowIcon(QIcon('1.jpg'))
    ui.show()
    pt = ParseThread()
    pt.setDaemon(True)
    pt.start()
    ui.connect(pt, SIGNAL("addItem(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), ui.ProcessGui)
    ui.LoadQB(0)
    sys.exit(app.exec_())
