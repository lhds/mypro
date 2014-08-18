# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import requests
from bs4 import BeautifulSoup

from Ui_qb_ui2 import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    
    page = 1
    
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.LoadQB()
        
    def LoadQB(self):
        
        url = "http://www.qiushibaike.com/week/5/page/" + str(page)
        page += 1
        
        re = requests.get(url)
        html = BeautifulSoup(re.text)
        content_list = html.findAll("div",  {"class":"article block untagged mb15"})
        
        for i in range(len(content_list)):
            
            image = QImage()
            item_widget = QWidget()
            item_widget_layout = QVBoxLayout()
            item_widget_layout.setContentsMargins(0, 0, 0, 0)
            item_widget.setLayout(item_widget_layout)
            have_img = False
            
            for j in range(1, len(content_list[i].contents), 2):
                if content_list[i].contents[j]['class'] == ['content']:
                    label = QLabel(content_list[i].contents[j].next)
                    label.setWordWrap(True)
                    item_widget_layout.addWidget(label)
                    
                if content_list[i].contents[j]['class'] == ['thumb']:
                    image_url = content_list[i].contents[j].img['src']                    
                    re = requests.get(image_url)                    
                    image.loadFromData(re.content)
                    
                    have_img = True
                    
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
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
