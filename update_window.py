from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import resources_rc
from utilities import str_to_bool, save_config, retrieve_sections, retrieve_section_for_update

# Next line to prevent removal of resources_rc during optimization
var = resources_rc


class UiUpdateWindow(object):
    def __init__(self):
        self.verticalLayoutWidget = None
        self.verticalLayout = None
        self.label = None
        self.cmb_config = None
        self.line = None
        self.gridLayoutWidget = None
        self.gridLayout = None
        self.label_7 = None
        self.label_6 = None
        self.cmb_ssl = None
        self.le_instance = None
        self.label_8 = None
        self.label_3 = None
        self.le_gateway = None
        self.cmb_cloud = None
        self.label_4 = None
        self.label_5 = None
        self.le_address = None
        self.le_namespace = None
        self.label_2 = None
        self.le_port = None
        self.widget = None
        self.horizontalLayout = None
        self.btn_save = None
        self.buttonBox = None

    def setup_ui(self, updatewindow):
        updatewindow.setObjectName("update_window")
        updatewindow.resize(776, 552)
        font = QtGui.QFont()
        font.setPointSize(10)
        updatewindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        updatewindow.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(updatewindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 20, 301, 49))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cmb_config = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmb_config.setObjectName("cmb_config")
        self.verticalLayout.addWidget(self.cmb_config)
        self.line = QtWidgets.QFrame(updatewindow)
        self.line.setGeometry(QtCore.QRect(10, 90, 761, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget = QtWidgets.QWidget(updatewindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 110, 751, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item, 2, 0, 1, 1)
        spacer_item1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item1, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item2, 0, 1, 1, 1)
        self.cmb_ssl = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cmb_ssl.setObjectName("cmb_ssl")
        self.gridLayout.addWidget(self.cmb_ssl, 4, 2, 1, 1)
        self.le_instance = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_instance.setObjectName("le_instance")
        self.gridLayout.addWidget(self.le_instance, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.le_gateway = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_gateway.setObjectName("le_gateway")
        self.gridLayout.addWidget(self.le_gateway, 7, 2, 1, 1)
        self.cmb_cloud = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cmb_cloud.setObjectName("cmb_cloud")
        self.gridLayout.addWidget(self.cmb_cloud, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.le_address = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_address.setObjectName("le_address")
        self.gridLayout.addWidget(self.le_address, 1, 2, 1, 1)
        self.le_namespace = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_namespace.setObjectName("le_namespace")
        self.gridLayout.addWidget(self.le_namespace, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.le_port = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_port.setObjectName("le_port")
        self.gridLayout.addWidget(self.le_port, 4, 0, 1, 1)
        spacer_item3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item3, 8, 0, 1, 1)
        self.widget = QtWidgets.QWidget(updatewindow)
        self.widget.setGeometry(QtCore.QRect(10, 510, 751, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(self.widget)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        sections = retrieve_sections()
        self.cmb_config.addItems(sections)
        bools = ['', 'True', 'False']
        self.cmb_cloud.addItems(bools)
        self.cmb_ssl.addItems(bools)
        self.reset_form()
        self.cmb_config.currentIndexChanged.connect(self.update_screen)
        self.cmb_cloud.currentIndexChanged.connect(self.on_change)
        self.btn_save.clicked.connect(self.save_config)
        self.retranslate_ui(updatewindow)
        self.buttonBox.accepted.connect(updatewindow.accept)  # type: ignore
        self.buttonBox.rejected.connect(updatewindow.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(updatewindow)

    def update_screen(self) -> None:
        section = retrieve_section_for_update(self.cmb_config.currentText())
        _cloud = str_to_bool(section['cloud'])
        if _cloud:
            self.cmb_cloud.setCurrentText(section['cloud'])
            self.le_address.setText(str(section['address'][:-(len(self.cmb_config.currentText()) + len('/tm1/api'))]))
            self.le_instance.setText(str(self.cmb_config.currentText()))
        else:
            self.cmb_cloud.setCurrentText(section['cloud'])
            self.le_address.setText(str(section['address']))
            self.le_port.setText(str(section['port']))
            self.le_instance.setText(str(self.cmb_config.currentText()))
            self.cmb_ssl.setCurrentText(str(section['ssl']))
            self.le_namespace.setText(str(section['namespace']))
            self.le_gateway.setText(str(section['gateway']))

    def on_change(self, new_index) -> None:
        if new_index == 1:
            self.le_port.setEnabled(False)
            self.cmb_ssl.setEnabled(False)
            self.le_gateway.setEnabled(False)
            self.le_namespace.setEnabled(False)
        else:
            self.le_port.setEnabled(True)
            self.cmb_ssl.setEnabled(True)
            self.le_namespace.setEnabled(True)
            self.le_gateway.setEnabled(True)

    def reset_form(self) -> None:
        self.cmb_cloud.setCurrentText('')
        self.le_address.setText('')
        self.le_port.setText('')
        self.le_instance.setText('')
        self.cmb_ssl.setCurrentText('')
        self.le_namespace.setText('')
        self.le_gateway.setText('')

    # noinspection PyUnusedLocal
    def save_config(self) -> None:
        _base_url = None
        _address = None
        _port = None
        _ssl = None
        _namespace = None
        _gateway = None
        try:
            _cloud = str_to_bool(self.cmb_cloud.currentText())
            _instance = self.le_instance.text()
            if _instance == '':
                raise ValueError("Instance name not supplied")
            if _cloud:
                _base = self.le_address.text()
                if _base == '':
                    raise ValueError("Base URL address not supplied in address field")
                if _base.endswith('/'):
                    _base = _base[:-1]
                _base_url = _base + '/tm1/api/' + _instance
            else:
                _address = self.le_address.text()
                if _address == '':
                    raise ValueError("Address not supplied")
                _port = int(self.le_port.text())
                if _port == 0:
                    raise ValueError("Invalid HTTPPortNumber supplied")
                _ssl = str_to_bool(self.cmb_ssl.currentText())
                _gateway = self.le_gateway.text()
                _namespace = self.le_namespace.text()
            if _cloud:
                _config = {
                    'cloud': True,
                    'address': _base_url
                }
            else:
                _config = {
                    'cloud': False,
                    'address': _address,
                    'port': _port,
                    'ssl': _ssl,
                    'namespace': _namespace,
                    'gateway': _gateway
                }
            save_config(instance=_instance, config=_config)
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Configuration Saved")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
            self.reset_form()
        except ValueError as v:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(v))
            msg.exec_()
        except TypeError as t:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("HTTPPortNumber is invalid")
            msg.exec_()

    def retranslate_ui(self, updatewindow):
        _translate = QtCore.QCoreApplication.translate
        updatewindow.setWindowTitle(_translate("update_window", "ACG Model Documenter - Update Configuration"))
        self.label.setText(_translate("update_window", "Choose Existing Configuration"))
        self.label_7.setText(_translate("update_window", "CAM Namespace ID"))
        self.label_6.setText(_translate("update_window", "Use SSL"))
        self.label_8.setText(_translate("update_window", "SSO Gateway"))
        self.label_3.setText(_translate("update_window", "Address"))
        self.label_4.setText(_translate("update_window", "HTTP Port Number"))
        self.label_5.setText(_translate("update_window", "Instance Name"))
        self.label_2.setText(_translate("update_window", "IBM Cloud"))
        self.btn_save.setText(_translate("update_window", "Save Configuration"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    update_window = QtWidgets.QDialog()
    ui = UiUpdateWindow()
    ui.setup_ui(update_window)
    update_window.show()
    sys.exit(app.exec_())
