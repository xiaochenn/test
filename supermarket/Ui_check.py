# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\python\supermarket\check.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_checkwindow(object):
    def setupUi(self, checkwindow):
        checkwindow.setObjectName("checkwindow")
        checkwindow.resize(874, 600)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(checkwindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkWidget = QtWidgets.QTableWidget(checkwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.checkWidget.sizePolicy().hasHeightForWidth())
        self.checkWidget.setSizePolicy(sizePolicy)
        self.checkWidget.setAutoScrollMargin(16)
        self.checkWidget.setRowCount(0)
        self.checkWidget.setColumnCount(4)
        self.checkWidget.setObjectName("checkWidget")
        item = QtWidgets.QTableWidgetItem()
        self.checkWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkWidget.setHorizontalHeaderItem(3, item)
        self.checkWidget.horizontalHeader().setDefaultSectionSize(209)
        self.verticalLayout_3.addWidget(self.checkWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(checkwindow)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(checkwindow)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.check_btn = QtWidgets.QPushButton(checkwindow)
        self.check_btn.setObjectName("check_btn")
        self.verticalLayout_2.addWidget(self.check_btn)
        self.check_push = QtWidgets.QPushButton(checkwindow)
        self.check_push.setObjectName("check_push")
        self.verticalLayout_2.addWidget(self.check_push)
        self.check_backbtn = QtWidgets.QPushButton(checkwindow)
        self.check_backbtn.setObjectName("check_backbtn")
        self.verticalLayout_2.addWidget(self.check_backbtn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(checkwindow)
        self.check_backbtn.clicked.connect(checkwindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(checkwindow)

    def retranslateUi(self, checkwindow):
        _translate = QtCore.QCoreApplication.translate
        checkwindow.setWindowTitle(_translate("checkwindow", "check"))
        item = self.checkWidget.horizontalHeaderItem(0)
        item.setText(_translate("checkwindow", "商品"))
        item = self.checkWidget.horizontalHeaderItem(1)
        item.setText(_translate("checkwindow", "数量"))
        item = self.checkWidget.horizontalHeaderItem(2)
        item.setText(_translate("checkwindow", "进价"))
        item = self.checkWidget.horizontalHeaderItem(3)
        item.setText(_translate("checkwindow", "售价"))
        self.label.setText(_translate("checkwindow", "tips：先点击\"确认定价\"，再点击\"发布\"~"))
        self.label_2.setText(_translate("checkwindow", "售价上的数字代表原先的定价，若为0则表示还未定价"))
        self.check_btn.setText(_translate("checkwindow", "确认定价"))
        self.check_push.setText(_translate("checkwindow", "上架"))
        self.check_backbtn.setText(_translate("checkwindow", "返回"))