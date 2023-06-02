from PyQt5 import QtCore, QtGui, QtWidgets
from base_settings import APP_NAME, APP_VERSION

LICENSE = """
Copyright (c) 2023 Application Consulting Group

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom 
the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE.
"""


class Ui_about_window(object):
    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(700, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        about_window.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(about_window)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 71))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(about_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 10, 581, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_about = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.le_about.setFont(font)
        self.le_about.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_about.setObjectName("le_about")
        self.verticalLayout.addWidget(self.le_about)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(about_window)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 681, 351))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_license = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_license.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_license.setObjectName("lbl_license")
        self.verticalLayout_2.addWidget(self.lbl_license)

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)
        self.lbl_license.setText(LICENSE)
        self.le_about.setText(f"{APP_NAME}\nVersion: {APP_VERSION}\n© 2023 Application Consulting Group, Inc.")

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "ACG Model Cleanup - About"))
        self.label.setText(_translate("about_window", "<html><head/><body><p><img src=\":/acg_logo.jpg\"/></p></body></html>"))
        self.le_about.setText(_translate("about_window", "TextLabel"))
        self.lbl_license.setText(_translate("about_window", "TextLabel"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about_window = QtWidgets.QDialog()
    ui = Ui_about_window()
    ui.setupUi(about_window)
    about_window.show()
    sys.exit(app.exec_())
