# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import requests
import threading
from bs4 import BeautifulSoup

from Ui_qb_ui4 import Ui_MainWindow

event = threading.Event()
type = 0

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    
    imgCount = 1
    isinit_1 = False
    isinit_2 = False
    isinit_3 = False
    isinit_4 = False
    isinit_5 = False
    isinit_6 = False
    isinit_7 = False
    
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.textEdit_1.verticalScrollBar(), SIGNAL("valueChanged(int)"), self.LoadQB_1)
        self.connect(self.textEdit_2.verticalScrollBar(), SIGNAL("valueChanged(int)"), self.LoadQB_2)
        self.connect(self.textEdit_3.verticalScrollBar(), SIGNAL("valueChanged(int)"), self.LoadQB_3)
        self.connect(self.textEdit_4.verticalScrollBar(), SIGNAL("valueChanged(int)"), self.LoadQB_4)
        self.connect(self.textEdit_5.verticalScrollBar(), SIGNAL("valueChanged(int)"), self.LoadQB_5)
        self.connect(self.textEdit_6.verticalScrollBar(), SIGNAL("valueChanged(int)"), self.LoadQB_6)
        self.connect(self.textEdit_7.verticalScrollBar(), SIGNAL("valueChanged(int)"), self.LoadQB_7)
        self.connect(self.tabWidget, SIGNAL("currentChanged(int)"), self.TabInit)
    
    def TabInit(self, tab_index):
        
        tab_num = tab_index + 1
        if tab_num == 1:
            if self.isinit_1 == False:
                self.LoadQB_1(0)
        elif tab_num == 2:
            if self.isinit_2 == False:
                self.LoadQB_2(0)
        elif tab_num == 3:
            if self.isinit_3 == False:
                self.LoadQB_3(0)
        elif tab_num == 4:
            if self.isinit_4 == False:
                self.LoadQB_4(0)
        elif tab_num == 5:
            if self.isinit_5 == False:
                self.LoadQB_5(0)
        elif tab_num == 6:
            if self.isinit_6 == False:
                self.LoadQB_6(0)
        elif tab_num == 7:
            if self.isinit_7 == False:
                self.LoadQB_7(0)
        else:
            return

    def LoadQB_1(self, position):
        
        max_position = self.textEdit_1.verticalScrollBar().maximum()
        if self.isinit_1:
            if position < max_position:
                return
        
        self.isinit_1 = True
        
        global type
        type = 1
        
        global event
        event.set()
    
    def LoadQB_2(self, position):
        
        max_position = self.textEdit_2.verticalScrollBar().maximum()
        if self.isinit_2:
            if position < max_position:
                return
        
        self.isinit_2 = True
        
        global type
        type = 2
        
        global event
        event.set()
    
    def LoadQB_3(self, position):
        
        max_position = self.textEdit_3.verticalScrollBar().maximum()
        if self.isinit_3:
            if position < max_position:
                return
        
        self.isinit_3 = True
        
        global type
        type = 3
        
        global event
        event.set()
    
    def LoadQB_4(self, position):
        
        max_position = self.textEdit_4.verticalScrollBar().maximum()
        if self.isinit_4:
            if position < max_position:
                return
        
        self.isinit_4 = True
        
        global type
        type = 4
        
        global event
        event.set()
        
    def LoadQB_5(self, position):
        
        max_position = self.textEdit_5.verticalScrollBar().maximum()
        if self.isinit_5:
            if position < max_position:
                return
        
        self.isinit_5 = True
        
        global type
        type = 5
        
        global event
        event.set()
        
    def LoadQB_6(self, position):
        
        max_position = self.textEdit_6.verticalScrollBar().maximum()
        if self.isinit_6:
            if position < max_position:
                return
        
        self.isinit_6 = True
        
        global type
        type = 6
        
        global event
        event.set()
        
    def LoadQB_7(self, position):
        
        max_position = self.textEdit_7.verticalScrollBar().maximum()
        if self.isinit_7:
            if position < max_position:
                return
        
        self.isinit_7 = True
        
        global type
        type = 7
        
        global event
        event.set()
        
    def ProcessGui(self, qb_content, image_content, have_img, tab_num):
        
        if tab_num == 1:
            textEdit = self.textEdit_1
        elif tab_num == 2:
            textEdit = self.textEdit_2
        elif tab_num == 3:
            textEdit = self.textEdit_3
        elif tab_num == 4:
            textEdit = self.textEdit_4
        elif tab_num == 5:
            textEdit = self.textEdit_5
        elif tab_num == 6:
            textEdit = self.textEdit_6
        elif tab_num == 7:
            textEdit = self.textEdit_7
        else:
            return
        
        cursor = QTextCursor(textEdit.document())
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
            charFormat.setFont(QFont('黑体', 12))
            childFrameCursor.insertText(qb_content, charFormat)
        
        if have_img:
            childFrameCursor.insertHtml('<br>')
            image = QImage()
            image.loadFromData(image_content)
            childFrameCursor.insertImage(image, str(self.imgCount))
            self.imgCount += 1
    
    
class ParseThread(threading.Thread, QObject):
    
    page_1 = 1
    page_2 = 1
    page_3 = 1
    page_4 = 1
    page_5 = 1
    page_6 = 1
    page_7 = 1
    
    def __init__(self):
        threading.Thread.__init__(self)
        QObject.__init__(self)
        
        
    def run(self):
        while(True):
            global event
            event.wait()
            event.clear()
            
            global type
            if type == 1:
                url = "http://www.qiushibaike.com/8hr/5/page/" + str(self.page_1)
                self.page_1 += 1
            elif type == 2:
                url = "http://www.qiushibaike.com/hot/5/page/" + str(self.page_2)
                self.page_2 += 1
            elif type == 3:
                url = "http://www.qiushibaike.com/week/5/page/" + str(self.page_3)
                self.page_3 += 1
            elif type == 4:
                url = "http://www.qiushibaike.com/month/5/page/" + str(self.page_4)
                self.page_4 += 1
            elif type == 5:
                url = "http://www.qiushibaike.com/imgrank/5/page/" + str(self.page_5)
                self.page_5 += 1
            elif type == 6:
                url = "http://www.qiushibaike.com/pic/5/page/" + str(self.page_6)
                self.page_6 += 1
            elif type == 7:
                url = "http://www.qiushibaike.com/late/5/page/" + str(self.page_7)
                self.page_7 += 1
            else:
                continue
                
            re = requests.get(url)
            html = BeautifulSoup(re.text)
            content_list = html.findAll("div",  {"class":"article block untagged mb15"})
        
            # 解析爬取的网页内容
            for i in range(len(content_list)):
                have_img = False
                for j in range(1, len(content_list[i].contents), 2):
                    if content_list[i].contents[j]['class'] == ['content']: # 内容
                        qb_content = content_list[i].contents[j].next
                    if content_list[i].contents[j]['class'] == ['thumb']: # 图片
                        image_url = content_list[i].contents[j].img['src']                    
                        re = requests.get(image_url)
                        image_content = re.content
                        have_img = True
                if have_img == False:
                    image_content = ''
                self.emit(SIGNAL("addItem(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), qb_content, image_content, have_img, type)
                

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyle('plastique')
    ui = MainWindow()
    ui.setWindowIcon(QIcon('1.jpg'))
    ui.show()
    pt = ParseThread()
    pt.setDaemon(True)
    pt.start()
    ui.connect(pt, SIGNAL("addItem(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), ui.ProcessGui)
    ui.TabInit(0)
    sys.exit(app.exec_())
