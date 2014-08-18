# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import requests
import threading
from bs4 import BeautifulSoup

import datetime

from Ui_qb_ui2 import Ui_MainWindow

event = threading.Event()

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    
    isinit = False
    
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.listWidget.verticalScrollBar(), SIGNAL("valueChanged(int)"), self.LoadQB)
        
     
    def LoadQB(self, position):
        
        max_position = self.listWidget.verticalScrollBar().maximum()
        if self.isinit:
            if position < max_position:
                return
        
        self.isinit = True
        
        global event
        event.set()
        
    
    def ProcessGui(self, qb_content, image_content, have_img):
        
        #starttime = datetime.datetime.now()
        image = QImage()
        item_widget = QWidget()
        item_widget_layout = QVBoxLayout()
        item_widget_layout.setContentsMargins(0, 0, 0, 0)
        item_widget.setLayout(item_widget_layout)

        label = QLabel(qb_content)
        label.setWordWrap(True)
        item_widget_layout.addWidget(label)
        
        if have_img:
            image.loadFromData(image_content)        
            image_label = QLabel()
            image_label.setPixmap(QPixmap.fromImage(image))
            item_widget_layout.addWidget(image_label)
        
        item = QListWidgetItem()
        if have_img:
            item.setSizeHint(QSize(100, 500))
        else:
            item.setSizeHint(QSize(100, 150))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, item_widget)
        
        #endtime = datetime.datetime.now()
        #print 'UI'
        #print (endtime - starttime)
        

class ParseThread(threading.Thread, QObject):
    
    page = 1
    
    def __init__(self):
        threading.Thread.__init__(self)
        QObject.__init__(self)
        
        
    def run(self):
        while(True):
            #starttime = datetime.datetime.now()
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
        
            #endtime = datetime.datetime.now()
            #print 'HTML'
            #print (endtime - starttime)
            

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
