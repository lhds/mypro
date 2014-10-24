# -*- coding:utf-8 -*-
__author__ = 'Lxixi'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from postblog_ui import Ui_MainWindow
import requests
import chardet

class Ui(QMainWindow):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.action, SIGNAL('triggered(bool)'), self.ShowAbout)
        self.connect(self.ui.pushButton, SIGNAL('clicked()'), self.ChoseFile)
        self.connect(self.ui.pushButton_2, SIGNAL('clicked()'), self.PostBlog)

    def ShowAbout(self):
        QMessageBox.information(self, '关于'.decode('utf-8'), '本工具只可用于http://www.lxixi.com.cn博客！\n联系作者luhengdan@163.com'.decode('utf-8'))

    def ChoseFile(self):
        file = QFileDialog.getOpenFileName(self)
        self.ui.lineEdit_4.setText(file)

    def PostBlog(self):
        user = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        title = self.ui.lineEdit_3.text()
        file = self.ui.lineEdit_4.text()

        s = requests.Session()

        s.get('http://www.lxixi.com.cn/admin/login.php')

        re = s.post('http://www.lxixi.com.cn/index.php/action/login', data={'name': unicode(user), 'password': unicode(password)}) # 使用unicode()的原因为：用text()取得的user等变量为QString类型的，需要转换成Python类型
        if 'Set-Cookie' not in re.headers: # 判断是否登录成功
            QMessageBox.warning(self, 'Error', '用户名或密码错误！'.decode('utf-8'))
            return -1

        s.get('http://www.lxixi.com.cn/admin/write-post.php')

        fp = open(file, 'rb')
        text = fp.read()
        fp.close()

        post_data = {'title': unicode(title),
                     'text': unicode(text, chardet.detect(text)['encoding']),
                     'fieldTypes[]': 'str',
                     'do': 'publish',
                     'markdown': '1',
                     'visibility': 'publish',
                     'allowComment': '1',
                     'allowPing': '1',
                     'allowFeed': '1'}
        re = s.post('http://www.lxixi.com.cn/index.php/action/contents-post-edit', data=post_data)

        s.close()

        QMessageBox.information(self, 'Attention', '发送完成'.decode('utf-8'))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Ui()
    ui.show()
    sys.exit(app.exec_())