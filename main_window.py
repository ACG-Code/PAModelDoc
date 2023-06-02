from PyQt5 import QtCore, QtGui, QtWidgets
from about_window import Ui_about_window
from help_window import Ui_help_window
from create_window import Ui_create_window
from update_window import Ui_update_window
from utilities import get_config
from utilities import retrieve_sections
import resources_rc

var = resources_rc


class AboutDialog(QtWidgets.QDialog, Ui_about_window):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)


class HelpDialog(QtWidgets.QDialog, Ui_help_window):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)


class CreateDialog(QtWidgets.QDialog, Ui_create_window):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)


class UpdateDialog(QtWidgets.QDialog, Ui_update_window):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 10, 331, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.cmb_config = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cmb_config.setObjectName("cmb_config")
        self.verticalLayout_2.addWidget(self.cmb_config)
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 761, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.le_user = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_user.setObjectName("le_user")
        self.gridLayout.addWidget(self.le_user, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.le_password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.le_password.setObjectName("le_password")
        self.gridLayout.addWidget(self.le_password, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 761, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.le_directory = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.le_directory.setObjectName("le_directory")
        self.gridLayout_2.addWidget(self.le_directory, 0, 0, 1, 1)
        self.btn_choose = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_choose.setObjectName("btn_choose")
        self.gridLayout_2.addWidget(self.btn_choose, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 761, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rad_all = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.rad_all.setObjectName("rad_all")
        self.gridLayout_3.addWidget(self.rad_all, 0, 0, 1, 1)
        self.cmb_elements = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cmb_elements.setObjectName("cmb_elements")
        self.gridLayout_3.addWidget(self.cmb_elements, 0, 2, 1, 1)
        self.rad_cubes = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.rad_cubes.setObjectName("rad_cubes")
        self.gridLayout_3.addWidget(self.rad_cubes, 0, 1, 1, 1)
        self.rad_dims = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.rad_dims.setObjectName("rad_dims")
        self.gridLayout_3.addWidget(self.rad_dims, 1, 0, 1, 1)
        self.rad_procs = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.rad_procs.setObjectName("rad_procs")
        self.gridLayout_3.addWidget(self.rad_procs, 1, 1, 1, 1)
        self.rad_security = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.rad_security.setObjectName("rad_security")
        self.gridLayout_3.addWidget(self.rad_security, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 50, 761, 80))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 1)
        self.btn_execute = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_execute.setFont(font)
        self.btn_execute.setObjectName("btn_execute")
        self.gridLayout_4.addWidget(self.btn_execute, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.actionCreate_Configuration = QtWidgets.QAction(main_window)
        self.actionCreate_Configuration.setObjectName("actionCreate_Configuration")
        self.actionUpdate_Configuration = QtWidgets.QAction(main_window)
        self.actionUpdate_Configuration.setObjectName("actionUpdate_Configuration")
        self.actionInstructions = QtWidgets.QAction(main_window)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionAbout = QtWidgets.QAction(main_window)
        self.actionAbout.setObjectName("actionAbout")
        self.menuSetup.addAction(self.actionCreate_Configuration)
        self.menuSetup.addAction(self.actionUpdate_Configuration)
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        self.actionAbout.triggered.connect(self.open_about)
        self.actionInstructions.triggered.connect(self.open_help)
        self.actionCreate_Configuration.triggered.connect(self.open_create)
        self.actionUpdate_Configuration.triggered.connect(self.open_update)
        sections = retrieve_sections()
        self.cmb_config.addItems(sections)
        self.btn_choose.clicked.connect(self.browse_dirs)
        self.cmb_elements.setEnabled(False)
        self.rad_all.clicked.connect(self.on_change)
        self.rad_dims.clicked.connect(self.on_change)
        self.rad_cubes.clicked.connect(self.on_change)
        self.rad_procs.clicked.connect(self.on_change)
        self.rad_security.clicked.connect(self.on_change)
        bools = ['', 'True', 'False']
        self.cmb_elements.addItems(bools)

    def open_about(self) -> None:
        dlg = AboutDialog()
        dlg.exec_()

    def open_help(self) -> None:
        dlg = HelpDialog()
        dlg.exec_()

    def open_create(self) -> None:
        dlg = CreateDialog()
        dlg.exec_()

    def open_update(self) -> None:
        dlg = UpdateDialog()
        dlg.exec_()

    def browse_dirs(self) -> None:
        _path = QtWidgets.QFileDialog.getExistingDirectory(None, "Choose Output Directory")
        self.le_directory.setText(_path)

    def on_change(self):
        if self.rad_all.isChecked():
            self.cmb_elements.setEnabled(True)
        elif self.rad_dims.isChecked():
            self.cmb_elements.setEnabled(True)
        else:
            self.cmb_elements.setEnabled(False)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "ACG Model Documenter"))
        self.groupBox.setTitle(_translate("main_window", "Configuration"))
        self.label.setText(_translate("main_window", "Choose Configuration"))
        self.label_2.setText(_translate("main_window", "Username"))
        self.label_3.setText(_translate("main_window", "Password"))
        self.groupBox_2.setTitle(_translate("main_window", "Options"))
        self.btn_choose.setText(_translate("main_window", "Choose Output Location"))
        self.rad_all.setText(_translate("main_window", "All"))
        self.rad_cubes.setText(_translate("main_window", "Cubes"))
        self.rad_dims.setText(_translate("main_window", "Dimensions"))
        self.rad_procs.setText(_translate("main_window", "Processes"))
        self.rad_security.setText(_translate("main_window", "Security"))
        self.groupBox_3.setTitle(_translate("main_window", "Execution"))
        self.btn_execute.setText(_translate("main_window", "Retrieve Documentation"))
        self.menuSetup.setTitle(_translate("main_window", "Setup"))
        self.menuHelp.setTitle(_translate("main_window", "Help"))
        self.actionCreate_Configuration.setText(_translate("main_window", "Create Configuration"))
        self.actionUpdate_Configuration.setText(_translate("main_window", "Update Configuration"))
        self.actionInstructions.setText(_translate("main_window", "Instructions"))
        self.actionAbout.setText(_translate("main_window", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
