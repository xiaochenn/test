import sys
from PyQt5.QtWidgets import  QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QDoubleSpinBox,QSpinBox,QWidget
from Ui_total import Ui_MainWindow
from Ui_buy import Ui_buywindow
from Ui_sold import Ui_soldwindow
from Ui_check import Ui_checkwindow


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menuAbout.triggered.connect(self.about)
        self.ui.Menu_Exit.triggered.connect(self.myclose)
    def open(self):
        self.show()

    def about(self):
        QMessageBox.information(self, "关于", "超市管理系统\t\t\t\t\n版本:1.0\n作者:潘奕臣\n学号:U202142540\n班级:计214", QMessageBox.Yes, QMessageBox.Yes)
    
    def myclose(self):
        replay = QMessageBox.question(self, "提示", "是否退出系统      ", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if replay == QMessageBox.Yes:
            self.close()

class buywindow(QWidget):          #购买商品界面
    def __init__(self):
        super().__init__()
        self.ui = Ui_buywindow()
        self.ui.setupUi(self)
        self.ui.buy_total_btn.clicked.connect(self.total)
        self.ui.buy_btn.clicked.connect(self.show_message)

    def show_message(self):
        if self.buy_item and  not 0 in self.buy_num and not 0 in self.buy_price:
            QMessageBox.information(self, "提示", "购买成功              ", QMessageBox.Yes, QMessageBox.Yes)
            self.buy_flag = 1
        elif 0 in self.buy_num or 0 in self.buy_price:
            QMessageBox.information(self, "提示", "价格和数量不能为0哦~           ", QMessageBox.Yes, QMessageBox.Yes)
        else:
            QMessageBox.information(self, "提示", "尚未购买，先点击结算哦~           ", QMessageBox.Yes, QMessageBox.Yes)

    def window_initial(self):            
        self.buy_item = []
        self.buy_price = []
        self.buy_num = []
        self.buy_total = 0.0
        self.buy_flag = 0
        for i in range(5):
            item_tmp = eval(''.join('self.ui.buy_lineEdit'+str(i)))
            item_tmp.setText('')
            price_tmp = eval(''.join('self.ui.buy_price'+str(i)))
            price_tmp.setValue(0)
            num_tmp = eval(''.join('self.ui.buy_num'+str(i)))
            num_tmp.setValue(0)
            total_tmp = eval(''.join('self.ui.buy_total'+str(i)))
            total_tmp.setText('0')
            self.ui.buy_total.setText('0')

    def open(self):
        self.window_initial()
        self.show()

    def total(self):              
        for i in range(5):
            item_tmp = eval(''.join('self.ui.buy_lineEdit'+str(i)))
            if item_tmp.text() == '':
                break
            else:
                self.buy_item.append(item_tmp.text())
                price_tmp = eval(''.join('self.ui.buy_price'+str(i)))
                self.buy_price.append(price_tmp.value())
                num_tmp = eval(''.join('self.ui.buy_num'+str(i)))
                self.buy_num.append(num_tmp.value())
                total_tmp = eval(''.join('self.ui.buy_total'+str(i)))
                total_tmp.setText(str(self.buy_price[i] * self.buy_num[i]))
                self.buy_total += self.buy_price[i] * self.buy_num[i]
        self.ui.buy_total.setText(str(self.buy_total))


class soldwindow(QWidget):              #卖出商品界面
    def __init__(self):
        super().__init__()
        self.ui = Ui_soldwindow()
        self.ui.setupUi(self)
        self.ui.sold_btn.clicked.connect(self.change)

    def change(self):
        for i in range(len(self.sold_item)):
            self.sold_num.append(self.ui.soldWidget.cellWidget(i,3).value())

    def window_initial(self):
        self.sold_item = []
        self.sold_price = []
        self.sold_num_total = []
        self.sold_num = []
        self.ui.soldWidget.clear()
        self.ui.soldWidget.setHorizontalHeaderLabels(['商品', '售价', '库存', '出售件数'])
        self.ui.soldWidget.setRowCount(0)

    def paint(self):
        for i in range(len(self.sold_item)):
            row = self.ui.soldWidget.rowCount()
            self.ui.soldWidget.insertRow(row)
            item_tmp = QTableWidgetItem(self.sold_item[i])
            num_tmp = QTableWidgetItem(str(self.sold_num_total[i]))
            price_tmp = QTableWidgetItem(str(self.sold_price[i]))
            sold_num_tmp = QSpinBox()
            self.ui.soldWidget.setItem(row, 0, item_tmp)
            self.ui.soldWidget.setItem(row, 1, price_tmp)
            self.ui.soldWidget.setItem(row, 2, num_tmp)
            self.ui.soldWidget.setCellWidget(row, 3, sold_num_tmp)

    def open(self,item,sold_price,num):
        self.window_initial()
        for i in range(len(item)):
            if sold_price[i] != 0 and num[i] != 0:
                self.sold_item.append(item[i])
                self.sold_price.append(sold_price[i])
                self.sold_num_total.append(num[i])
            else:
                continue
        self.paint()
        self.show()

class checkwindow(QWidget):             #定价界面
    def __init__(self):
        super().__init__()
        self.ui = Ui_checkwindow()
        self.ui.setupUi(self)
        self.ui.check_btn.clicked.connect(self.save)
        self.ui.check_push.clicked.connect(self.show_message)

    def paint(self):
        for i in range(len(self.check_item)):
            row = self.ui.checkWidget.rowCount()
            self.ui.checkWidget.insertRow(row)
            item_tmp = QTableWidgetItem(self.check_item[i])
            num_tmp = QTableWidgetItem(str(self.check_num[i]))
            price_tmp = QTableWidgetItem(str(self.check_price[i]))
            set_tmp = QDoubleSpinBox()
            try:
                set_tmp.setValue(self.check_set[i])
            except:
                pass
            self.ui.checkWidget.setItem(row, 0, item_tmp)
            self.ui.checkWidget.setItem(row, 1, num_tmp)
            self.ui.checkWidget.setItem(row, 2, price_tmp)
            self.ui.checkWidget.setCellWidget(row, 3, set_tmp)

    def save(self):
        for i in range(len(self.check_item)):
            self.check_set[i] = self.ui.checkWidget.cellWidget(i, 3).value()

    def window_initial(self):
        self.check_item = []
        self.check_price = []
        self.check_num = []
        self.check_set = []
        self.ui.checkWidget.clear()
        self.ui.checkWidget.setHorizontalHeaderLabels(['商品', '数量', '进价', '售价'])
        self.ui.checkWidget.setRowCount(0)

    def open(self,buy_item,buy_price,buy_num,sold_price):
        self.window_initial()
        self.check_item = buy_item
        self.check_price = buy_price
        self.check_num = buy_num
        self.check_set = sold_price + [0] * (len(self.check_item) - len(sold_price))
        self.paint()
        self.show()

    def show_message(self):
        for i in range(len(self.check_item)):
            if (self.ui.checkWidget.cellWidget(i, 3).value() == 0):
                QMessageBox.information(self, "提示", "还有商品没有定价哦~         ", QMessageBox.Yes, QMessageBox.Yes)
                break
        else:
            QMessageBox.information(self, "提示", "上架成功             ", QMessageBox.Yes, QMessageBox.Yes)
    
class control():
    def __init__(self):
        self.w1 = mainwindow()
        self.w2 = buywindow()
        self.w3 = soldwindow()
        self.w4 = checkwindow()
        self.item = []
        self.buy_price = []
        self.sold_price = []
        self.num = []

        #各个窗口跳转
        self.w1.ui.buy_btn.clicked.connect(self.w2.open)
        self.w1.ui.sold_btn.clicked.connect(lambda:self.w3.open(self.item,self.sold_price,self.num))
        self.w1.ui.check_btn.clicked.connect(lambda:self.w4.open(self.item,self.buy_price,self.num,self.sold_price))
        self.w2.ui.buy_back_btn.clicked.connect(self.w1.open)
        self.w4.ui.check_backbtn.clicked.connect(self.w1.open)
        self.w3.ui.sold_backbtn.clicked.connect(self.w1.open)

        #窗口数据传递
        self.w2.ui.buy_btn.clicked.connect(self.buy)  #进货
        self.w4.ui.check_push.clicked.connect(self.set) #定价
        self.w3.ui.sold_btn.clicked.connect(self.sold) #售出

    def buy(self): 
        for i in range(len(self.w2.buy_item)):
            if self.w2.buy_flag == 1:
                if self.w2.buy_item[i] in self.item:
                    self.num[self.item.index(self.w2.buy_item[i])] += self.w2.buy_num[i]
                else:
                    self.item.append(self.w2.buy_item[i])
                    self.buy_price.append(self.w2.buy_price[i])
                    self.num.append(self.w2.buy_num[i])
                    self.sold_price.append(0)

    def set(self):
        self.sold_price = self.w4.check_set

    def sold(self):
        for i in range(len(self.w3.sold_item)):
            if self.num[self.item.index(self.w3.sold_item[i])] >= self.w3.sold_num[i]:
                self.num[self.item.index(self.w3.sold_item[i])] -= self.w3.sold_num[i]
            else:
                QMessageBox.information(self.w3, "提示", " '{0}' 商品数量不足哦~         ".format(self.w3.sold_item[i]), QMessageBox.Yes, QMessageBox.Yes)
                break
        else:
            QMessageBox.information(self.w3, "提示", " '出售成功         ".format(self.w3.sold_item[i]), QMessageBox.Yes, QMessageBox.Yes)
        self.check()
        self.w3.close()
        self.w3.open(self.item,self.sold_price,self.num)

    def check(self):
        i = 0
        while (i < len(self.item)):
            if self.num[i] == 0:
                self.item.pop(i)
                self.buy_price.pop(i)
                self.num.pop(i)
                self.sold_price.pop(i)
            else:
                i += 1
                
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = control()
    w.w1.show()
    sys.exit(app.exec_())

