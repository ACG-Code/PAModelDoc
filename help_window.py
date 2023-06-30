from PyQt5 import QtCore, QtGui, QtWidgets

import resources_rc
from base_settings import APP_NAME, APP_VERSION

# Next line to prevent removal of resources_rc during optimization
var = resources_rc


class UiHelpWindow(object):
    """
    Setup and display Help...Instructions screen
    """

    def __init__(self):
        self.le_instructions = None
        self.verticalLayout_2 = None
        self.verticalLayoutWidget_2 = None
        self.le_appname = None
        self.verticalLayout = None
        self.verticalLayoutWidget = None
        self.label_2 = None

    def setup_ui(self, helpwindow):
        helpwindow.setObjectName("help_window")
        helpwindow.resize(768, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        help_window.setWindowIcon(icon)
        self.label_2 = QtWidgets.QLabel(helpwindow)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 71))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(helpwindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 20, 641, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_appname = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.le_appname.setFont(font)
        self.le_appname.setObjectName("le_appname")
        self.verticalLayout.addWidget(self.le_appname)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(help_window)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 110, 741, 421))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_instructions = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.le_instructions.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.le_instructions.setObjectName("le_instructions")
        self.verticalLayout_2.addWidget(self.le_instructions)

        self.retranslate_ui(help_window)
        QtCore.QMetaObject.connectSlotsByName(help_window)
        self.le_appname.setText(f"{APP_NAME}\nVersion: {APP_VERSION}\n© 2023 Application Consulting Group")
        instructions = """
        <b>Options for CSV File:</b>
        <p style="margin-left: 25px;">
        -c:&lt;cube_name&gt;<br>
        -d:&lt;dimension_name&gt;<br>
        -v:&lt;cube_name&amp;view_name&gt;<br>
        -s:&lt;dimension_name&amp;public_subset_name&gt;<br>
        -p:&lt;process_name&gt;<br>
        </p>
        <p>&nbsp;</p>
        Order is important, cubes must be deleted before any dimensions used by the cube.  The "&lt; &gt;" signs 
        indicate proper names for items in the model, <br>and should not be included in the CSV file
        <p>&nbsp;</p><br>
        <b>Example:</b>
        <p style="margin-left: 25px;">
        -c:cube1<br>
        -c:cube2<br>
        -d:dimension1<br>
        -d:dimension2<br>
        -v:cube3&amp;View1<br>
        -s:dimension3&amp;subset1<br>
        -p:process1<br>
        </p>
        """
        self.le_instructions.setText(instructions)

    def retranslate_ui(self, helpwindow):
        _translate = QtCore.QCoreApplication.translate
        helpwindow.setWindowTitle(_translate("help_window", "ACG Model Documentor - Instructions"))
        self.label_2.setText(_translate("help_window",
                                        "<html><head/><body><p><img "
                                        "src=\"C:/Users/charvey/PycharmProjects/ACG-ModelDoc/PAModelDoc/acg_logo.jpg\"/></p"
                                        "></body></html>"))
        self.le_appname.setText(_translate("help_window", "TextLabel"))
        self.le_instructions.setText(_translate("help_window", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    help_window = QtWidgets.QDialog()
    ui = UiHelpWindow()
    ui.setup_ui(help_window)
    help_window.show()
    sys.exit(app.exec_())
