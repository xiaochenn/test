# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\python\supermarket\buy.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_buywindow(object):
    def setupUi(self, buywindow):
        buywindow.setObjectName("buywindow")
        buywindow.resize(745, 600)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(buywindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(buywindow)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 7, 1, 1)
        self.buy_lineEdit2 = QtWidgets.QLineEdit(buywindow)
        self.buy_lineEdit2.setObjectName("buy_lineEdit2")
        self.gridLayout.addWidget(self.buy_lineEdit2, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(buywindow)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 2, 1, 1)
        self.buy_lineEdit3 = QtWidgets.QLineEdit(buywindow)
        self.buy_lineEdit3.setObjectName("buy_lineEdit3")
        self.gridLayout.addWidget(self.buy_lineEdit3, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(buywindow)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(buywindow)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(buywindow)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 4, 1, 1)
        self.buy_num2 = QtWidgets.QSpinBox(buywindow)
        self.buy_num2.setObjectName("buy_num2")
        self.gridLayout.addWidget(self.buy_num2, 3, 6, 1, 1)
        self.buy_total0 = QtWidgets.QLabel(buywindow)
        self.buy_total0.setText("")
        self.buy_total0.setObjectName("buy_total0")
        self.gridLayout.addWidget(self.buy_total0, 1, 9, 1, 1)
        self.label = QtWidgets.QLabel(buywindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(buywindow)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 3, 1, 1)
        self.buy_num0 = QtWidgets.QSpinBox(buywindow)
        self.buy_num0.setProperty("value", 0)
        self.buy_num0.setObjectName("buy_num0")
        self.gridLayout.addWidget(self.buy_num0, 1, 6, 1, 1)
        self.buy_price2 = QtWidgets.QDoubleSpinBox(buywindow)
        self.buy_price2.setObjectName("buy_price2")
        self.gridLayout.addWidget(self.buy_price2, 3, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(buywindow)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 3, 4, 1, 1)
        self.buy_num4 = QtWidgets.QSpinBox(buywindow)
        self.buy_num4.setObjectName("buy_num4")
        self.gridLayout.addWidget(self.buy_num4, 5, 6, 1, 1)
        self.buy_lineEdit0 = QtWidgets.QLineEdit(buywindow)
        self.buy_lineEdit0.setObjectName("buy_lineEdit0")
        self.gridLayout.addWidget(self.buy_lineEdit0, 1, 1, 1, 1)
        self.buy_lineEdit4 = QtWidgets.QLineEdit(buywindow)
        self.buy_lineEdit4.setObjectName("buy_lineEdit4")
        self.gridLayout.addWidget(self.buy_lineEdit4, 5, 1, 1, 1)
        self.buy_total2 = QtWidgets.QLabel(buywindow)
        self.buy_total2.setText("")
        self.buy_total2.setObjectName("buy_total2")
        self.gridLayout.addWidget(self.buy_total2, 3, 9, 1, 1)
        self.label_8 = QtWidgets.QLabel(buywindow)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 10, 1, 1)
        self.buy_total4 = QtWidgets.QLabel(buywindow)
        self.buy_total4.setText("")
        self.buy_total4.setObjectName("buy_total4")
        self.gridLayout.addWidget(self.buy_total4, 5, 9, 1, 1)
        self.buy_price1 = QtWidgets.QDoubleSpinBox(buywindow)
        self.buy_price1.setObjectName("buy_price1")
        self.gridLayout.addWidget(self.buy_price1, 2, 3, 1, 1)
        self.buy_lineEdit1 = QtWidgets.QLineEdit(buywindow)
        self.buy_lineEdit1.setObjectName("buy_lineEdit1")
        self.gridLayout.addWidget(self.buy_lineEdit1, 2, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(buywindow)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 5, 4, 1, 1)
        self.buy_price4 = QtWidgets.QDoubleSpinBox(buywindow)
        self.buy_price4.setObjectName("buy_price4")
        self.gridLayout.addWidget(self.buy_price4, 5, 3, 1, 1)
        self.buy_num3 = QtWidgets.QSpinBox(buywindow)
        self.buy_num3.setObjectName("buy_num3")
        self.gridLayout.addWidget(self.buy_num3, 4, 6, 1, 1)
        self.buy_num1 = QtWidgets.QSpinBox(buywindow)
        self.buy_num1.setObjectName("buy_num1")
        self.gridLayout.addWidget(self.buy_num1, 2, 6, 1, 1)
        self.label_21 = QtWidgets.QLabel(buywindow)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 4, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(buywindow)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(buywindow)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(buywindow)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 9, 1, 1)
        self.buy_total3 = QtWidgets.QLabel(buywindow)
        self.buy_total3.setText("")
        self.buy_total3.setObjectName("buy_total3")
        self.gridLayout.addWidget(self.buy_total3, 4, 9, 1, 1)
        self.label_14 = QtWidgets.QLabel(buywindow)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)
        self.buy_price3 = QtWidgets.QDoubleSpinBox(buywindow)
        self.buy_price3.setObjectName("buy_price3")
        self.gridLayout.addWidget(self.buy_price3, 4, 3, 1, 1)
        self.buy_total1 = QtWidgets.QLabel(buywindow)
        self.buy_total1.setText("")
        self.buy_total1.setObjectName("buy_total1")
        self.gridLayout.addWidget(self.buy_total1, 2, 9, 1, 1)
        self.label_13 = QtWidgets.QLabel(buywindow)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 2, 1, 1)
        self.buy_price0 = QtWidgets.QDoubleSpinBox(buywindow)
        self.buy_price0.setObjectName("buy_price0")
        self.gridLayout.addWidget(self.buy_price0, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(buywindow)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(buywindow)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(buywindow)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(buywindow)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 7, 1, 1)
        self.label_23 = QtWidgets.QLabel(buywindow)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 2, 7, 1, 1)
        self.label_24 = QtWidgets.QLabel(buywindow)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 3, 7, 1, 1)
        self.label_25 = QtWidgets.QLabel(buywindow)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 4, 7, 1, 1)
        self.label_26 = QtWidgets.QLabel(buywindow)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 5, 7, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buy_total_btn = QtWidgets.QPushButton(buywindow)
        self.buy_total_btn.setObjectName("buy_total_btn")
        self.horizontalLayout_2.addWidget(self.buy_total_btn)
        self.buy_total = QtWidgets.QLabel(buywindow)
        self.buy_total.setObjectName("buy_total")
        self.horizontalLayout_2.addWidget(self.buy_total)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buy_btn = QtWidgets.QPushButton(buywindow)
        self.buy_btn.setObjectName("buy_btn")
        self.verticalLayout.addWidget(self.buy_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(buywindow)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.buy_back_btn = QtWidgets.QPushButton(buywindow)
        self.buy_back_btn.setObjectName("buy_back_btn")
        self.horizontalLayout.addWidget(self.buy_back_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(buywindow)
        self.buy_back_btn.clicked.connect(buywindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(buywindow)

    def retranslateUi(self, buywindow):
        _translate = QtCore.QCoreApplication.translate
        buywindow.setWindowTitle(_translate("buywindow", "购入"))
        self.label_3.setText(_translate("buywindow", "数量      "))
        self.label.setText(_translate("buywindow", "     商品名称"))
        self.label_12.setText(_translate("buywindow", "价格    "))
        self.label_5.setText(_translate("buywindow", "单个总价"))
        self.buy_total_btn.setText(_translate("buywindow", "结算"))
        self.buy_total.setText(_translate("buywindow", "0"))
        self.buy_btn.setText(_translate("buywindow", "购入"))
        self.label_6.setText(_translate("buywindow", "tips:先点击结算再购入"))
        self.buy_back_btn.setText(_translate("buywindow", "返回"))
