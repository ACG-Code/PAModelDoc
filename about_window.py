from PyQt5 import QtCore, QtGui, QtWidgets

from base_settings import APP_NAME, APP_VERSION

LICENSE = """
Copyright (c) 2023 Application Consulting Group

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the 
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE.
"""


class UiAboutWindow(object):
    def __init__(self):
        self.lbl_license = None
        self.verticalLayout_2 = None
        self.verticalLayoutWidget_2 = None
        self.le_about = None
        self.verticalLayout = None
        self.verticalLayoutWidget = None
        self.label = None

    def setup_ui(self, aboutwindow):
        aboutwindow.setObjectName("about_window")
        aboutwindow.resize(700, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutwindow.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(aboutwindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 71))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(aboutwindow)
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
        self.le_about.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.le_about.setObjectName("le_about")
        self.verticalLayout.addWidget(self.le_about)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(aboutwindow)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 681, 351))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_license = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_license.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lbl_license.setObjectName("lbl_license")
        self.verticalLayout_2.addWidget(self.lbl_license)

        self.retranslate_ui(aboutwindow)
        QtCore.QMetaObject.connectSlotsByName(aboutwindow)
        self.lbl_license.setText(LICENSE)
        self.le_about.setText(f"{APP_NAME}\nVersion: {APP_VERSION}\n© 2023 Application Consulting Group, Inc.")

    def retranslate_ui(self, aboutwindow):
        _translate = QtCore.QCoreApplication.translate
        aboutwindow.setWindowTitle(_translate("about_window", "ACG Model Documentor - About"))
        self.label.setText(
            _translate("about_window", "<html><head/><body><p><img src=\"C:/Users/charvey/PycharmProjects/ACG"
                                       "-ModelDoc/PAModelDoc/acg_logo.jpg\"/></p></body></html>"))
        self.le_about.setText(_translate("about_window", "TextLabel"))
        self.lbl_license.setText(_translate("about_window", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    about_window = QtWidgets.QDialog()
    ui = UiAboutWindow()
    ui.setup_ui(about_window)
    about_window.show()
    sys.exit(app.exec_())
