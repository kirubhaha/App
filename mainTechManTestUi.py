# Form implementation generated from reading ui file 'mainTechManTestUi.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from win32gui import GetWindowRect, GetForegroundWindow
screen_width = GetWindowRect(GetForegroundWindow())[2]
screen_height = GetWindowRect(GetForegroundWindow())[3]

class TechManTest_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.screen_width = screen_width
        self.screen_height = screen_height
        MainWindow.resize(self.screen_width, self.screen_height)
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet("QPushButton#logOutButton{\n"
"    background-color:#41436A;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#logOutButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#F64668;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#logOutButton:hover{\n"
"    background-color:#F64668;\n"
"}\n"
"QPushButton#newButton{\n"
"    background-color:#984063;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#newButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#26648E;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#newButton:hover{\n"
"    background-color:#26648E;\n"
"}\n"
"QPushButton#importButton{\n"
"    background-color:#984063;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#importButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#26648E;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#importButton:hover{\n"
"    background-color:#26648E;\n"
"}\n"
"QPushButton#templateButton{\n"
"    background-color:#984063;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#templateButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#26648E;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#templateButton:hover{\n"
"    background-color:#26648E;\n"
"}\n"
"QPushButton#exportButton{\n"
"    background-color:#984063;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#exportButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#26648E;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#exportButton:hover{\n"
"    background-color:#26648E;\n"
"}\n"
"QPushButton#viewSamplesButton{\n"
"    background-color:#984063;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#viewSamplesButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#26648E;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#viewSamplesButton:hover{\n"
"    background-color:#26648E;\n"
"}\n"
"QToolButton#searchButton{\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px;\n"
"}\n"
"QToolButton#searchButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QToolButton#reloadButton {\n"
"    background-color: #984063;\n"
"    color: rgba(255, 255, 255, 200);\n"
"    border-radius: 15px;\n"
"    padding-bottom: 6px;\n"
"}\n"
"QToolButton#reloadButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #26648E;\n"
"    background-position: calc(100% - 10px) center;\n"
"}\n"
"QToolButton#reloadButton:hover {\n"
"    background-color: #26648E;\n"
"}\n"
"QTableWidget#tableWidget {\n"
"    border-collapse: separate;\n"
"    border:none;\n"
"    min-width: 400px;\n"
"}\n"
"\n"
"QTableWidget#tableWidget QHeaderView::section:horizontal {\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #26648E;\n"
"    color: #ffffff;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QTableWidget#tableWidget QHeaderView::section:vertical {\n"
"    border-radius: 0px;\n"
"    padding-left: 5px;\n"
"}\n"
""
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.parGroupLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.parGroupLabel.setGeometry(QtCore.QRect(120, 20, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(28)
        font.setBold(True)
        self.parGroupLabel.setFont(font)
        self.parGroupLabel.setStyleSheet("color:rgba(255, 255, 255, 220);")
        self.parGroupLabel.setObjectName("parGroupLabel")
        self.descriptionLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.descriptionLabel.setGeometry(QtCore.QRect(120, 70, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(15)
        font.setBold(True)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setStyleSheet("color:rgba(255, 255, 255, 220);\n"
"")
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.containerLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.containerLabel.setEnabled(True)
        self.containerLabel.setGeometry(QtCore.QRect(0, -1, int(self.screen_width), int(self.screen_height*0.974)))
        self.containerLabel.setStyleSheet("background-color:rgb(255, 255, 255);\n""border: none;"
"")
        self.containerLabel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.containerLabel.setText("")
        self.containerLabel.setObjectName("containerLabel")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(1, 170, self.containerLabel.geometry().width()-5, self.containerLabel.geometry().height()-175))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setMaximumSize(QtCore.QSize(1920, 16777215))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        palette = self.tableWidget.palette()
        palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor('#e9eff3')) 
        palette.setColor(QtGui.QPalette.ColorRole.AlternateBase, QtGui.QColor('#d3e0e8'))
        palette.setColor(QtGui.QPalette.ColorRole.Highlight, QtGui.QColor('#92b1c6'))   
        self.tableWidget.setPalette(palette)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.DashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
        
        self.searchLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.searchLineEdit.setGeometry(QtCore.QRect(self.containerLabel.geometry().right()-271-10, 125, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        font.setBold(False)
        self.searchLineEdit.setFont(font)
        self.searchLineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-color:#984063;\n"
"border-radius:20px;\n"
"color:rgb(0, 0, 0);\n"
"padding-left:10px;")
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.searchButton = QtWidgets.QToolButton(parent=self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(self.searchLineEdit.geometry().right()-31-5, 125, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(13)
        font.setBold(True)
        self.searchButton.setFont(font)
        self.searchButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.searchButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.searchButton.setObjectName("searchButton")
        self.topLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.topLabel.setGeometry(QtCore.QRect(5, 10, int(self.screen_width*0.996)-2, 111))
        self.topLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #41436A , stop:1 #F64668);\n"
"border-radius: 20px;\n"
"")
        self.topLabel.setText("")
        self.topLabel.setObjectName("topLabel")
        self.logOutButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.logOutButton.setGeometry(QtCore.QRect(int(self.screen_width*0.915)-2, 45, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(True)
        self.logOutButton.setFont(font)
        self.logOutButton.setStyleSheet("")
        self.logOutButton.setObjectName("logOutButton")
        logOutButton_geometry = self.logOutButton.geometry()
        logOutButton_left = logOutButton_geometry.left()
        Label_x = logOutButton_left - 151 - 10
        
        self.newButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.newButton.setGeometry(QtCore.QRect(140, 125, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(True)
        self.newButton.setFont(font)
        self.newButton.setStyleSheet("")
        self.newButton.setObjectName("newButton")
        self.importButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.importButton.setGeometry(QtCore.QRect(200, 125, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(True)
        self.importButton.setFont(font)
        self.importButton.setStyleSheet("")
        self.importButton.setObjectName("importButton")
        self.testInfoLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.testInfoLabel.setGeometry(QtCore.QRect(25, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(18)
        font.setBold(True)
        self.testInfoLabel.setFont(font)
        self.testInfoLabel.setStyleSheet("color:#41436A;")
        self.testInfoLabel.setObjectName("testInfoLabel")
        self.reloadButton = QtWidgets.QToolButton(parent=self.centralwidget)
        self.reloadButton.setGeometry(QtCore.QRect(self.containerLabel.geometry().right()-271-10-31-10, 130, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(20)
        font.setBold(True)
        self.reloadButton.setFont(font)
        self.reloadButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.reloadButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.reloadButton.setObjectName("reloadButton")
        self.viewSamplesButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.viewSamplesButton.setGeometry(QtCore.QRect(460, 125, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(True)
        self.viewSamplesButton.setFont(font)
        self.viewSamplesButton.setStyleSheet("")
        self.viewSamplesButton.setObjectName("viewSamplesButton")
        self.roleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.roleLabel.setGeometry(QtCore.QRect(Label_x, 70, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        self.roleLabel.setFont(font)
        self.roleLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.roleLabel.setStyleSheet("color:rgba(255, 255, 255, 220);\n"
"")
        self.roleLabel.setText("")
        self.roleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.roleLabel.setObjectName("roleLabel")
        self.nameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(logOutButton_left - 151 - 100, 52, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(True)
        self.nameLabel.setFont(font)
        self.nameLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.nameLabel.setStyleSheet("color:rgba(255, 255, 255, 220);\n"
"")
        self.nameLabel.setText("")
        self.nameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.exportButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exportButton.setGeometry(QtCore.QRect(380, 125, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(True)
        self.exportButton.setFont(font)
        self.exportButton.setStyleSheet("")
        self.exportButton.setObjectName("exportButton")
        self.templateButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.templateButton.setGeometry(QtCore.QRect(280, 125, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        font.setBold(True)
        self.templateButton.setFont(font)
        self.templateButton.setStyleSheet("")
        self.templateButton.setObjectName("templateButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PAR Logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.containerLabel.raise_()
        self.topLabel.raise_()
        self.descriptionLabel.raise_()
        self.logOutButton.raise_()
        self.parGroupLabel.raise_()
        self.searchLineEdit.raise_()
        self.tableWidget.raise_()
        self.searchButton.raise_()
        self.newButton.raise_()
        self.importButton.raise_()
        self.testInfoLabel.raise_()
        self.reloadButton.raise_()
        self.viewSamplesButton.raise_()
        self.roleLabel.raise_()
        self.nameLabel.raise_()
        self.exportButton.raise_()
        self.templateButton.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.parGroupLabel.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.descriptionLabel.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.topLabel.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.containerLabel.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.logOutButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.newButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.importButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.templateButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.exportButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.viewSamplesButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.reloadButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parGroupLabel.setText(_translate("MainWindow", "PAR Group"))
        self.descriptionLabel.setText(_translate("MainWindow", "Life Science & Research Pvt. Ltd."))
        self.searchButton.setText(_translate("MainWindow", "🔍"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Test ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Test Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fee"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "GSTIN"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tax Rate"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Inclusive Of Tax"))
        self.searchLineEdit.setPlaceholderText(_translate("MainWindow", "Search by Name"))
        self.logOutButton.setText(_translate("MainWindow", "Log Out"))
        self.newButton.setText(_translate("MainWindow", "New"))
        self.importButton.setText(_translate("MainWindow", "Import"))
        self.testInfoLabel.setText(_translate("MainWindow", "Test Info"))
        self.reloadButton.setText(_translate("MainWindow", "⟳"))
        self.viewSamplesButton.setText(_translate("MainWindow", "View Samples"))
        self.exportButton.setText(_translate("MainWindow", "Export"))
        self.templateButton.setText(_translate("MainWindow", "Template"))
