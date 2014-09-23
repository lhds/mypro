# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\mycode\qb0.3\qb_ui4.ui'
#
# Created: Mon Aug 25 10:42:49 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 800)
        MainWindow.setMinimumSize(QtCore.QSize(600, 800))
        MainWindow.setMaximumSize(QtCore.QSize(600, 800))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textEdit_1 = QtGui.QTextEdit(self.tab_1)
        self.textEdit_1.setReadOnly(True)
        self.textEdit_1.setObjectName(_fromUtf8("textEdit_1"))
        self.horizontalLayout_2.addWidget(self.textEdit_1)
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout_3.addWidget(self.textEdit_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.textEdit_3 = QtGui.QTextEdit(self.tab_3)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.horizontalLayout_4.addWidget(self.textEdit_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.textEdit_4 = QtGui.QTextEdit(self.tab_4)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.horizontalLayout_5.addWidget(self.textEdit_4)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab_5)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.textEdit_5 = QtGui.QTextEdit(self.tab_5)
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.horizontalLayout_6.addWidget(self.textEdit_5)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_6)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.textEdit_6 = QtGui.QTextEdit(self.tab_6)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.horizontalLayout_7.addWidget(self.textEdit_6)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.tab_7)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.textEdit_7 = QtGui.QTextEdit(self.tab_7)
        self.textEdit_7.setReadOnly(True)
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.horizontalLayout_8.addWidget(self.textEdit_7)
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "QB0.3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "热门", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "24小时精华", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "7天精华", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "30天精华", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "真相(硬菜)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "真相(时令)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "最新", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

