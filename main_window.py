import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtWidgets import QMessageBox, QProgressBar, QVBoxLayout, QWidget
from TM1py.Exceptions import TM1pyNotAdminException, TM1pyException

import resources_rc
from about_window import UiAboutWindow
from base_settings import APP_NAME
from create_window import UiCreateWindow
from help_window import UiHelpWindow
from pamodel import get_docs
from update_window import UiUpdateWindow
from utilities import retrieve_sections, get_config

var = resources_rc


class AboutDialog(QtWidgets.QDialog, UiAboutWindow):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setup_ui(self)


class HelpDialog(QtWidgets.QDialog, UiHelpWindow):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setup_ui(self)


class CreateDialog(QtWidgets.QDialog, UiCreateWindow):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setup_ui(self)


class UpdateDialog(QtWidgets.QDialog, UiUpdateWindow):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setup_ui(self)


class UiMainWindow(object):
    def __init__(self):
        self.actionAbout = None
        self.actionInstructions = None
        self.actionUpdate_Configuration = None
        self.actionCreate_Configuration = None
        self.statusbar = None
        self.menuHelp = None
        self.menuSetup = None
        self.menubar = None
        self.groupBox_3 = None
        self.centralwidget = None
        self.verticalLayoutWidget = None
        self.verticalLayout = None
        self.groupBox = None
        self.verticalLayoutWidget_2 = None
        self.verticalLayout_2 = None
        self.label = None
        self.cmb_config = None
        self.gridLayoutWidget = None
        self.gridLayout = None
        self.le_user = None
        self.label_2 = None
        self.le_password = None
        self.label_3 = None
        self.groupBox_2 = None
        self.gridLayoutWidget_2 = None
        self.le_directory = None
        self.gridLayout_2 = None
        self.btn_choose = None
        self.gridLayoutWidget_3 = None
        self.rad_all = None
        self.gridLayout_3 = None
        self.rad_cubes = None
        self.rad_dims = None
        self.rad_procs = None
        self.rad_security = None
        self.gridLayoutWidget_4 = None
        self.btn_execute = None
        self.gridLayout_4 = None
        self.check_elem = None
        self.completed = None
        self.popup = None
        self.progress_bar = QProgressBar()

    def setup_ui(self, mainwindow):
        mainwindow.setObjectName("main_window")
        mainwindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainwindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
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
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item, 0, 1, 1, 1)
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
        self.check_elem = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.check_elem.setObjectName("check_elem")
        self.gridLayout_3.addWidget(self.check_elem, 0, 2, 1, 1)
        self.check_elem.setText("Enable Element Count")
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
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacer_item1, 0, 0, 1, 1)
        self.btn_execute = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_execute.setFont(font)
        self.btn_execute.setObjectName("btn_execute")
        self.gridLayout_4.addWidget(self.btn_execute, 0, 1, 1, 1)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacer_item2, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.actionCreate_Configuration = QtWidgets.QAction(mainwindow)
        self.actionCreate_Configuration.setObjectName("actionCreate_Configuration")
        self.actionUpdate_Configuration = QtWidgets.QAction(mainwindow)
        self.actionUpdate_Configuration.setObjectName("actionUpdate_Configuration")
        self.actionInstructions = QtWidgets.QAction(mainwindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionAbout = QtWidgets.QAction(mainwindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuSetup.addAction(self.actionCreate_Configuration)
        self.menuSetup.addAction(self.actionUpdate_Configuration)
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.statusbar.showMessage("Ready")

        self.retranslate_ui(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)
        self.actionAbout.triggered.connect(self.open_about)
        self.actionInstructions.triggered.connect(self.open_help)
        self.actionCreate_Configuration.triggered.connect(self.open_create)
        self.actionUpdate_Configuration.triggered.connect(self.open_update)
        sections = retrieve_sections()
        self.cmb_config.addItems(sections)
        self.btn_choose.clicked.connect(self.browse_dirs)
        self.check_elem.setEnabled(False)
        self.rad_all.clicked.connect(self.on_change)
        self.rad_dims.clicked.connect(self.on_change)
        self.rad_cubes.clicked.connect(self.on_change)
        self.rad_procs.clicked.connect(self.on_change)
        self.rad_security.clicked.connect(self.on_change)
        self.btn_execute.clicked.connect(self.retrieve_doc)
        self.statusbar.addPermanentWidget(self.progress_bar)
        self.progress_bar.hide()

    @staticmethod
    def open_about() -> None:
        dlg = AboutDialog()
        dlg.exec_()

    @staticmethod
    def open_help() -> None:
        dlg = HelpDialog()
        dlg.exec_()

    def open_create(self) -> None:
        dlg = CreateDialog()
        dlg.exec_()
        self.cmb_config.clear()
        sections = retrieve_sections()
        self.cmb_config.addItems(sections)

    def open_update(self) -> None:
        dlg = UpdateDialog()
        dlg.exec_()
        self.cmb_config.clear()
        self.cmb_config.addItems(retrieve_sections())

    def browse_dirs(self) -> None:
        _path = QtWidgets.QFileDialog.getExistingDirectory(None, "Choose Output Directory")
        self.le_directory.setText(_path)

    def on_change(self):
        if self.rad_all.isChecked():
            self.check_elem.setEnabled(True)
        elif self.rad_dims.isChecked():
            self.check_elem.setEnabled(True)
        else:
            self.check_elem.setEnabled(False)

    def retrieve_doc(self) -> None:
        _method = {}
        try:
            if self.cmb_config.currentText() == '':
                raise ValueError("No Configuration Selected")
            section = get_config(self.cmb_config.currentText())
            if self.le_user.text() == '':
                raise ValueError("No Username Provided")
            _output_dir = self.le_directory.text()
            if _output_dir == '':
                raise ValueError("No directory specified")
            _user = self.le_user.text()
            _password = self.le_password.text()
            section['user'] = _user
            section['password'] = _password
            section['session_context'] = APP_NAME
            if not self.rad_all.isChecked() and not self.rad_dims.isChecked() and self.rad_cubes.isChecked() \
                    and self.rad_procs.isChecked() and not self.rad_security.isChecked():
                raise ValueError("No Options Selected")
            if self.rad_all.isChecked():
                _method['retrieve'] = 'all'
                if self.check_elem.isChecked():
                    _method['elements'] = True
                else:
                    _method['elements'] = False
            elif self.rad_dims.isChecked():
                _method['retrieve'] = 'dimensions'
                if self.check_elem.isChecked():
                    _method['elements'] = True
                else:
                    _method['elements'] = False
            elif self.rad_cubes.isChecked():
                _method['retrieve'] = 'cubes'
            elif self.rad_procs.isChecked():
                _method['retrieve'] = 'processes'
            elif self.rad_security.isChecked():
                _method['retrieve'] = 'security'
            self.statusbar.showMessage("Retrieving Information - Please wait...")
            QtWidgets.QApplication.processEvents()
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            get_docs(server=str(self.cmb_config.currentText()), instance=section, output_dir=_output_dir, **_method)
            QtWidgets.QApplication.restoreOverrideCursor()
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Retrieval Complete")
            msg.exec_()
            self.statusbar.showMessage("Ready")
        except ValueError as e:
            self.statusbar.showMessage(str(e))
        except TM1pyNotAdminException:
            self.statusbar.showMessage("User must be admin in PA")
        except TM1pyException as t:
            self.statusbar.showMessage(str(t))

    def retranslate_ui(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("main_window", "ACG Model Documenter"))
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
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
