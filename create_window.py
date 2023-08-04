from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import resources_rc
from utilities import save_config, str_to_bool

# Next line to prevent removal of resources_rc during optimization
var = resources_rc


class UiCreateWindow(object):
    """
    Setup and display Setup...Create configuration window
    """

    def __init__(self):
        self.btnbox = None
        self.btn_save = None
        self.horizontalLayout = None
        self.layoutWidget1 = None
        self.le_port = None
        self.le_address = None
        self.label_4 = None
        self.label_7 = None
        self.cmb_ssl = None
        self.label_6 = None
        self.le_instance = None
        self.le_namespace = None
        self.label_5 = None
        self.cmb_cloud = None
        self.label_3 = None
        self.label_2 = None
        self.label_2 = None
        self.le_gateway = None
        self.label = None
        self.gridLayout = None
        self.layoutWidget = None

    def setup_ui(self, createwindow):
        createwindow.setObjectName("create_window")
        createwindow.resize(666, 538)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        createwindow.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(createwindow)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 641, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item, 10, 7, 1, 1)
        self.le_gateway = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_gateway.setObjectName("le_gateway")
        self.gridLayout.addWidget(self.le_gateway, 9, 4, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 5)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item1, 4, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.cmb_cloud = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_cloud.setObjectName("cmb_cloud")
        self.gridLayout.addWidget(self.cmb_cloud, 2, 1, 1, 1)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item2, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 7, 1, 1)
        self.le_namespace = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_namespace.setObjectName("le_namespace")
        self.gridLayout.addWidget(self.le_namespace, 9, 1, 1, 3)
        self.le_instance = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_instance.setObjectName("le_instance")
        self.gridLayout.addWidget(self.le_instance, 5, 3, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 1, 1, 3)
        self.cmb_ssl = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_ssl.setObjectName("cmb_ssl")
        self.gridLayout.addWidget(self.cmb_ssl, 5, 7, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 4, 1, 4)
        spacer_item4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item4, 10, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.le_address = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_address.setObjectName("le_address")
        self.gridLayout.addWidget(self.le_address, 2, 3, 1, 5)
        spacer_item6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item6, 3, 1, 1, 1)
        spacer_item5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item5, 2, 0, 3, 1)
        self.le_port = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_port.setObjectName("le_port")
        self.gridLayout.addWidget(self.le_port, 5, 1, 1, 1)
        spacer_item6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item6, 4, 2, 1, 1)
        spacer_item7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item7, 6, 1, 1, 1)
        spacer_item8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item8, 10, 5, 1, 1)
        spacer_item9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item9, 10, 1, 1, 1)
        spacer_item10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item10, 10, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(createwindow)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 490, 641, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btnbox = QtWidgets.QDialogButtonBox(self.layoutWidget1)
        self.btnbox.setOrientation(QtCore.Qt.Horizontal)
        self.btnbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.btnbox.setObjectName("btnbox")
        self.horizontalLayout.addWidget(self.btnbox)

        self.retranslate_ui(createwindow)
        self.btnbox.accepted.connect(createwindow.accept)  # type: ignore
        self.btnbox.rejected.connect(createwindow.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(createwindow)
        createwindow.setTabOrder(self.cmb_cloud, self.le_address)
        createwindow.setTabOrder(self.le_address, self.le_port)
        createwindow.setTabOrder(self.le_port, self.le_instance)
        createwindow.setTabOrder(self.le_instance, self.cmb_ssl)
        createwindow.setTabOrder(self.cmb_ssl, self.le_namespace)
        createwindow.setTabOrder(self.le_namespace, self.le_gateway)
        createwindow.setTabOrder(self.le_gateway, self.btn_save)
        bools = ['', 'True', 'False']
        self.cmb_cloud.addItems(bools)
        self.cmb_ssl.addItems(bools)
        self.btn_save.clicked.connect(self.save_config)
        QtCore.QMetaObject.connectSlotsByName(createwindow)
        createwindow.setTabOrder(self.cmb_cloud, self.le_address)
        createwindow.setTabOrder(self.le_address, self.le_port)
        createwindow.setTabOrder(self.le_port, self.le_instance)
        createwindow.setTabOrder(self.le_instance, self.cmb_ssl)
        createwindow.setTabOrder(self.cmb_ssl, self.le_namespace)
        createwindow.setTabOrder(self.le_namespace, self.le_gateway)
        createwindow.setTabOrder(self.le_gateway, self.btn_save)
        self.cmb_cloud.currentIndexChanged.connect(self.on_change)

    # noinspection PyUnusedLocal
    def save_config(self) -> None:
        _gateway = None
        _namespace = None
        _ssl = None
        _port = None
        _address = None
        _base_url = None
        _cloud = str_to_bool(self.cmb_cloud.currentText())
        try:
            _instance = self.le_instance.text()
            if _instance == '':
                raise ValueError("Instance name not supplied")
            if _cloud:
                _base = self.le_address.text()
                if _base == '':
                    raise ValueError("Base URL not supplied in address field")
                if _base.endswith('/'):
                    _base = _base[:-1]
                _base_url = _base + r'/tm1/api/' + _instance
            else:
                _address = self.le_address.text()
                if _address == '':
                    raise ValueError("Address was not supplied")
                _port = int(float(self.le_port.text() or None))
                if _port == 0:
                    raise ValueError('HTTPPortNumber not supplied')
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
            if str(v.args[0]['message']).__contains__('r'):
                v_msg = 'Invalid HTTPPortNumber'
            else:
                v_msg = str(v)
            msg.setText(v_msg)
            msg.exec_()
        except TypeError as t:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("HTTPPortNumber is invalid")
            msg.exec_()

    def reset_form(self) -> None:
        self.cmb_cloud.setCurrentText('')
        self.le_address.setText('')
        self.le_port.setText('')
        self.le_instance.setText('')
        self.cmb_ssl.setCurrentText('')
        self.le_gateway.setText('')
        self.le_namespace.setText('')

    def on_change(self, new_index) -> None:
        if new_index == 1:
            self.le_port.setEnabled(False)
            self.cmb_ssl.setEnabled(False)
            self.le_namespace.setEnabled(False)
            self.le_gateway.setEnabled(False)
        elif new_index == 2:
            self.le_port.setEnabled(True)
            self.cmb_ssl.setEnabled(True)
            self.le_namespace.setEnabled(True)
            self.le_gateway.setEnabled(True)

    def retranslate_ui(self, createwindow):
        _translate = QtCore.QCoreApplication.translate
        createwindow.setWindowTitle(_translate("create_window", "ACG Model Documenter - Create Configuration"))
        self.label.setText(_translate("create_window", "IBM Cloud"))
        self.label_2.setText(_translate("create_window", "Address"))
        self.label_3.setText(_translate("create_window", "HTTP Port Number"))
        self.label_5.setText(_translate("create_window", "SSL"))
        self.label_6.setText(_translate("create_window", "CAM Namespace ID"))
        self.label_7.setText(_translate("create_window", "SSO Gateway"))
        self.label_4.setText(_translate("create_window", "Instance Name"))
        self.btn_save.setText(_translate("create_window", "Save Configuration"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    create_window = QtWidgets.QDialog()
    ui = UiCreateWindow()
    ui.setup_ui(create_window)
    create_window.show()
    sys.exit(app.exec_())
