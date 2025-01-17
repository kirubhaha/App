# Form implementation generated from reading ui file 'detailsUi.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class DetailsUi_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.screen = QtWidgets.QApplication.primaryScreen()
        self.screen_geometry = self.screen.geometry()
        self.screen_width = self.screen_geometry.width()
        self.screen_height = self.screen_geometry.height()
        Form.resize(self.screen_width, self.screen_height)
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(5, 5, 581, 461))
        self.widget.setStyleSheet("QPushButton#saveButton{\n"
"    background-color:#41436A;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#saveButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#F64668;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#saveButton:hover{\n"
"    background-color:#F64668;\n"
"}\n"
"QPushButton#cancelButton{\n"
"    background-color:#41436A;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#cancelButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#F64668;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#cancelButton:hover{\n"
"    background-color:#F64668;\n"
"}\n"
"QComboBox {\n"
"            border: 1px solid #41436A;\n"
"            border-radius: 5px;\n"
"            padding-left: 4px;\n"
"            padding-right: 20px; \n"
"        }\n"
"        QComboBox::drop-down {\n"
"            subcontrol-origin: padding;\n"
"            subcontrol-position: top right;\n"
"            width: 25px;\n"
"            border-left: 1px solid #41436A;\n"
"            border-top-right-radius: 5px;\n"
"            border-bottom-right-radius: 5px;\n"
"            background: #41436A;\n"
"        }\n"
"        QComboBox::down-arrow {\n"
"            border: none;\n"
"            color: white;\n"
"            padding-right: 1px;\n"
"            width: 5px;\n"
"            height: 8px;\n"
"        }\n"
"        QComboBox:on {\n"
"            border: 1px solid #26648E;\n"
"        }\n"
"        QComboBox QListView {\n"
"            border: 1px solid #984063;\n"
"            border-radius: 4px;\n"
"            padding: 5px;\n"
"            background-color: #fff;\n"
"            outline: 0px;\n"
"        }\n"
"        QComboBox QListView::item {\n"
"            padding-left: 5px;\n"
"            background-color: #fff;\n"
"        }\n"
"        QComboBox QListView::item:hover {\n"
"            background-color: #96a4c5;\n"
"        }\n"
"        QComboBox QListView::item:selected {\n"
"            background-color: #96a4c5;\n"
"        }")
        self.widget.setObjectName("widget")
        self.passwordLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.passwordLineEdit.setGeometry(QtCore.QRect(300, 150, 235, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(False)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:#41436A;\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.passwordLineEdit.setText("")
        self.passwordLineEdit.setMaxLength(30)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.passwordLineEdit.setClearButtonEnabled(True)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.emailLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.emailLineEdit.setGeometry(QtCore.QRect(300, 80, 235, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(False)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:#41436A;\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.emailLineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhPreferLowercase|QtCore.Qt.InputMethodHint.ImhPreferUppercase|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.emailLineEdit.setText("")
        self.emailLineEdit.setMaxLength(30)
        self.emailLineEdit.setClearButtonEnabled(True)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.saveButton = QtWidgets.QPushButton(parent=self.widget)
        self.saveButton.setGeometry(QtCore.QRect(120, 370, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(True)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("")
        self.saveButton.setObjectName("saveButton")
        self.detailsLabel = QtWidgets.QLabel(parent=self.widget)
        self.detailsLabel.setGeometry(QtCore.QRect(20, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(18)
        font.setBold(True)
        self.detailsLabel.setFont(font)
        self.detailsLabel.setStyleSheet("color:#41436A;")
        self.detailsLabel.setObjectName("detailsLabel")
        self.nameLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.nameLineEdit.setGeometry(QtCore.QRect(40, 80, 235, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(False)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:#41436A;\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.nameLineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferLowercase|QtCore.Qt.InputMethodHint.ImhPreferUppercase)
        self.nameLineEdit.setClearButtonEnabled(True)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.districtLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.districtLineEdit.setGeometry(QtCore.QRect(40, 290, 235, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(False)
        self.districtLineEdit.setFont(font)
        self.districtLineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:#41436A;\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.districtLineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDate)
        self.districtLineEdit.setText("")
        self.districtLineEdit.setMaxLength(20)
        self.districtLineEdit.setReadOnly(False)
        self.districtLineEdit.setClearButtonEnabled(True)
        self.districtLineEdit.setObjectName("districtLineEdit")
        self.cancelButton = QtWidgets.QPushButton(parent=self.widget)
        self.cancelButton.setGeometry(QtCore.QRect(300, 370, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(True)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("")
        self.cancelButton.setObjectName("cancelButton")
        self.containerLabel = QtWidgets.QLabel(parent=self.widget)
        self.containerLabel.setGeometry(QtCore.QRect(0, 5, 578, 451))
        self.containerLabel.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border:3px solid #41436A;")
        self.containerLabel.setText("")
        self.containerLabel.setObjectName("containerLabel")
        self.phnoLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.phnoLineEdit.setGeometry(QtCore.QRect(40, 150, 235, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(False)
        self.phnoLineEdit.setFont(font)
        self.phnoLineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:#41436A;\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.phnoLineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.phnoLineEdit.setText("")
        self.phnoLineEdit.setMaxLength(15)
        self.phnoLineEdit.setClearButtonEnabled(True)
        self.phnoLineEdit.setObjectName("phnoLineEdit")
        self.addressLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.addressLineEdit.setGeometry(QtCore.QRect(40, 220, 495, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(False)
        self.addressLineEdit.setFont(font)
        self.addressLineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:#41436A;\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.addressLineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly|QtCore.Qt.InputMethodHint.ImhPreferLowercase|QtCore.Qt.InputMethodHint.ImhPreferUppercase)
        self.addressLineEdit.setText("")
        self.addressLineEdit.setMaxLength(80)
        self.addressLineEdit.setClearButtonEnabled(True)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.stateLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.stateLineEdit.setGeometry(QtCore.QRect(300, 290, 235, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(False)
        self.stateLineEdit.setFont(font)
        self.stateLineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:#41436A;\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;")
        self.stateLineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDate)
        self.stateLineEdit.setText("")
        self.stateLineEdit.setMaxLength(20)
        self.stateLineEdit.setReadOnly(False)
        self.stateLineEdit.setClearButtonEnabled(True)
        self.stateLineEdit.setObjectName("stateLineEdit")
        self.containerLabel.raise_()
        self.passwordLineEdit.raise_()
        self.emailLineEdit.raise_()
        self.saveButton.raise_()
        self.detailsLabel.raise_()
        self.nameLineEdit.raise_()
        self.districtLineEdit.raise_()
        self.cancelButton.raise_()
        self.phnoLineEdit.raise_()
        self.addressLineEdit.raise_()
        self.stateLineEdit.raise_()

        
        self.saveButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.cancelButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.passwordLineEdit.setPlaceholderText(_translate("Form", "Password*"))
        self.emailLineEdit.setPlaceholderText(_translate("Form", "Email*"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.detailsLabel.setText(_translate("Form", "Details"))
        self.nameLineEdit.setPlaceholderText(_translate("Form", "Name*"))
        self.districtLineEdit.setPlaceholderText(_translate("Form", "District*"))
        self.cancelButton.setText(_translate("Form", "Cancel"))
        self.phnoLineEdit.setPlaceholderText(_translate("Form", "Phone number*"))
        self.addressLineEdit.setPlaceholderText(_translate("Form", "Address*"))
        self.stateLineEdit.setPlaceholderText(_translate("Form", "State*"))
