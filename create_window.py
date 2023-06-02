from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import resources_rc
from utilities import save_config, str_to_bool

# Next line to prevent removal of resources_rc during optimization
var = resources_rc


class Ui_create_window(object):
    """
    Setup and display Setup...Create configuration window
    """
    def setupUi(self, create_window):
        create_window.setObjectName("create_window")
        create_window.resize(666, 538)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        create_window.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(create_window)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 641, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 7, 1, 1)
        self.le_gateway = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_gateway.setObjectName("le_gateway")
        self.gridLayout.addWidget(self.le_gateway, 9, 4, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.cmb_cloud = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_cloud.setObjectName("cmb_cloud")
        self.gridLayout.addWidget(self.cmb_cloud, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 10, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.le_address = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_address.setObjectName("le_address")
        self.gridLayout.addWidget(self.le_address, 2, 3, 1, 5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 0, 3, 1)
        self.le_port = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_port.setObjectName("le_port")
        self.gridLayout.addWidget(self.le_port, 5, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 4, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 6, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 10, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 10, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 10, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(create_window)
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
        self.btnbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnbox.setObjectName("btnbox")
        self.horizontalLayout.addWidget(self.btnbox)

        self.retranslateUi(create_window)
        self.btnbox.accepted.connect(create_window.accept) # type: ignore
        self.btnbox.rejected.connect(create_window.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(create_window)
        create_window.setTabOrder(self.cmb_cloud, self.le_address)
        create_window.setTabOrder(self.le_address, self.le_port)
        create_window.setTabOrder(self.le_port, self.le_instance)
        create_window.setTabOrder(self.le_instance, self.cmb_ssl)
        create_window.setTabOrder(self.cmb_ssl, self.le_namespace)
        create_window.setTabOrder(self.le_namespace, self.le_gateway)
        create_window.setTabOrder(self.le_gateway, self.btn_save)
        bools = ['', 'True', 'False']
        self.cmb_cloud.addItems(bools)
        self.cmb_ssl.addItems(bools)
        self.btn_save.clicked.connect(self.save_config)
        QtCore.QMetaObject.connectSlotsByName(create_window)
        create_window.setTabOrder(self.cmb_cloud, self.le_address)
        create_window.setTabOrder(self.le_address, self.le_port)
        create_window.setTabOrder(self.le_port, self.le_instance)
        create_window.setTabOrder(self.le_instance, self.cmb_ssl)
        create_window.setTabOrder(self.cmb_ssl, self.le_namespace)
        create_window.setTabOrder(self.le_namespace, self.le_gateway)
        create_window.setTabOrder(self.le_gateway, self.btn_save)
        self.cmb_cloud.currentIndexChanged.connect(self.on_change)

    def save_config(self) -> None:
        _cloud = str_to_bool(self.cmb_cloud.currentText())
        _instance = self.le_instance.text()
        if _cloud:
            _base = self.le_address.text()
            if _base.endswith('/'):
                _base = _base[:-1]
            _base_url = _base + r'/tm1/api/' + _instance
        else:
            _address = self.le_address.text()
            _port = int(self.le_port.text())
            _ssl = str_to_bool(self.cmb_ssl.currentText())
            _gateway = self.le_gateway.text()
            _namespace = self.le_namespace.text()
        if _cloud:
            _config = {
                'cloud': True,
                'base_url': _base_url
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

    def reset_form(self) -> None:
        self.cmb_cloud.setCurrentText('')
        self.le_address.setText('')
        self.le_port.setText('')
        self.le_instance.setText('')
        self.cmb_ssl.setCurrentText('')
        self.le_gateway.setText('')
        self.le_namespace.setText('')

    def on_change(self, newIndex) -> None:
        if newIndex == 1:
            self.le_port.setEnabled(False)
            self.cmb_ssl.setEnabled(False)
            self.le_namespace.setEnabled(False)
            self.le_gateway.setEnabled(False)
        elif newIndex == 2:
            self.le_port.setEnabled(True)
            self.cmb_ssl.setEnabled(True)
            self.le_namespace.setEnabled(True)
            self.le_gateway.setEnabled(True)

    def retranslateUi(self, create_window):
        _translate = QtCore.QCoreApplication.translate
        create_window.setWindowTitle(_translate("create_window", "ACG Model Cleanup - Create Configuration"))
        self.label.setText(_translate("create_window", "IBM Cloud"))
        self.label_2.setText(_translate("create_window", "Address"))
        self.label_3.setText(_translate("create_window", "HTTP Port Number"))
        self.label_5.setText(_translate("create_window", "SSL"))
        self.label_6.setText(_translate("create_window", "CAM Namespace ID"))
        self.label_7.setText(_translate("create_window", "SSO Gateway"))
        self.label_4.setText(_translate("create_window", "Instance Name"))
        self.btn_save.setText(_translate("create_window", "Save Configuration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_window = QtWidgets.QDialog()
    ui = Ui_create_window()
    ui.setupUi(create_window)
    create_window.show()
    sys.exit(app.exec_())
