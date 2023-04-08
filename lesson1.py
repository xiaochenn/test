import os
import re
import datetime
import sys
import PyPDF2
import pypdfium2
from qtpy import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import  QApplication

class SearchWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件检索工具")
        self.setGeometry(100, 100, 600, 900)

        #检索目录及其文本框
        self.dir_label = QtWidgets.QLabel("检索目录", self)
        self.dir_label.setGeometry(50, 50, 80, 20)
        self.dir_lineedit = QtWidgets.QLineEdit(self)
        self.dir_lineedit.setGeometry(140, 50, 300, 20)

        #文件后缀及其文本框
        self.suffix_label = QtWidgets.QLabel("文件后缀", self)
        self.suffix_label.setGeometry(50, 90, 80, 20)
        self.suffix_lineedit = QtWidgets.QLineEdit(self)
        self.suffix_lineedit.setGeometry(140, 90, 300, 20)

        #关键词及其文本框
        self.keyword_label = QtWidgets.QLabel("关键词", self)
        self.keyword_label.setGeometry(50, 130, 80, 20)
        self.keyword_lineedit = QtWidgets.QLineEdit(self)
        self.keyword_lineedit.setGeometry(140, 130, 300, 20)

        self.filter_checkbox = QtWidgets.QCheckBox("仅检索创建于近5天的文件", self)
        self.filter_checkbox.setGeometry(50, 170, 300, 20)

        self.regex_checkbox = QtWidgets.QCheckBox("支持正则表达式检索", self)
        self.regex_checkbox.setGeometry(50, 200, 300, 20)

        self.pdf_checkbox = QtWidgets.QCheckBox("支持PDF文档检索", self)
        self.pdf_checkbox.setGeometry(50, 230, 300, 20)

        self.chinese_checkbox = QtWidgets.QCheckBox("支持中文检索", self)
        self.chinese_checkbox.setGeometry(50, 260, 300, 20)

        self.search_button = QtWidgets.QPushButton("搜索", self)
        self.search_button.setGeometry(460, 130, 80, 20)
        self.search_button.clicked.connect(self.search_files)

        self.result_label = QtWidgets.QLabel("搜索结果", self)
        self.result_label.setGeometry(50, 300, 80, 20)
        self.result_list = QtWidgets.QListWidget(self)
        self.result_list.setGeometry(50, 330, 500, 500)
        self.result_list.itemDoubleClicked.connect(self.open_file)

    def search_files(self):
        path = self.dir_lineedit.text()
        suffix = self.suffix_lineedit.text()
        keyword = self.keyword_lineedit.text()
        regex = self.regex_checkbox.isChecked()
        pdf = self.pdf_checkbox.isChecked()
        chinese = self.chinese_checkbox.isChecked()
        filter_date = self.filter_checkbox.isChecked()

        if not os.path.isdir(path):
            QtWidgets.QMessageBox.warning(self, "错误", "目录不存在！")
            return

        if not suffix.startswith("."):
            suffix = "." + suffix

        if filter_date:
            delta = datetime.timedelta(days=5)
            today = datetime.datetime.now()
            min_date = today - delta

        result = []
        for root, dirs, files in os.walk(path,topdown=True):
            for file in files:
                if file.endswith(suffix):
                    file_path = os.path.join(root, file)
                    if filter_date:       #判断时间要求
                        create_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                        if create_time < min_date:
                            continue
                    if pdf:
                        try:
                            with open(file_path,'rb') as f:
                                pdf_reader = pypdfium2.PdfDocument(f)
                                for i in range(len(pdf_reader)):
                                    page = pdf_reader.get_page(i).get_textpage().get_text_range()
                                if chinese:
                                    page = page.encode("utf-8", errors="ignore").decode("utf-8")
                                if regex:
                                    if re.search(keyword, page):
                                        result.append(file_path)
                                        break
                                else:
                                    if keyword in page:
                                        result.append(file_path)
                                        break
                        except:
                            pass
                    else:
                        try:
                            with open(file_path, "r", encoding="utf-8") as f:
                                content = f.read()
                                if chinese:
                                    page = page.encode("utf-8", errors="ignore").decode("utf-8")
                                if regex:
                                    if re.search(keyword, content):
                                        result.append(file_path)
                                else:
                                    if keyword in content:
                                        result.append(file_path)
                        except:
                            pass

        if not result:
            QtWidgets.QMessageBox.information(self, "搜索结果", "没有找到匹配的文件！")
        else:
            self.result_list.clear()
            for r in result:
                item = QtWidgets.QListWidgetItem(r)
                self.result_list.addItem(item)

    def open_file(self, item):
        os.startfile(item.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    app.exec_()

