# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logs_table.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(930, 369)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 911, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 40, 911, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.logs_table = QtGui.QTableWidget(Dialog)
        self.logs_table.setGeometry(QtCore.QRect(10, 60, 911, 251))
        self.logs_table.setObjectName(_fromUtf8("logs_table"))
        self.logs_table.setColumnCount(0)
        self.logs_table.setRowCount(0)
        self.exit_bt = QtGui.QPushButton(Dialog)
        self.exit_bt.setGeometry(QtCore.QRect(790, 330, 131, 26))
        self.exit_bt.setObjectName(_fromUtf8("exit_bt"))
        self.save_logs_as_bt = QtGui.QPushButton(Dialog)
        self.save_logs_as_bt.setGeometry(QtCore.QRect(650, 330, 131, 26))
        self.save_logs_as_bt.setObjectName(_fromUtf8("save_logs_as_bt"))
        self.logs_settings_bt = QtGui.QPushButton(Dialog)
        self.logs_settings_bt.setGeometry(QtCore.QRect(510, 330, 131, 26))
        self.logs_settings_bt.setObjectName(_fromUtf8("logs_settings_bt"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 320, 181, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.total_log_positions = QtGui.QLabel(Dialog)
        self.total_log_positions.setGeometry(QtCore.QRect(200, 320, 131, 41))
        self.total_log_positions.setObjectName(_fromUtf8("total_log_positions"))
        self.clear_logs_bt = QtGui.QPushButton(Dialog)
        self.clear_logs_bt.setGeometry(QtCore.QRect(370, 330, 131, 26))
        self.clear_logs_bt.setObjectName(_fromUtf8("clear_logs_bt"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Logs - Storj GUI Client</span></p></body></html>", None))
        self.exit_bt.setText(_translate("Dialog", "Exit", None))
        self.save_logs_as_bt.setText(_translate("Dialog", "Save logs as...", None))
        self.logs_settings_bt.setText(_translate("Dialog", "Logs settings", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Total log positions:</span></p></body></html>", None))
        self.total_log_positions.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">0</span></p></body></html>", None))
        self.clear_logs_bt.setText(_translate("Dialog", "Clear logs", None))

