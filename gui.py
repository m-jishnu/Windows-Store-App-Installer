# Form implementation generated from reading ui file 'Appinstaller.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainProgram(QtCore.QObject):
    def setupUi(self, MainProgram):
        MainProgram.setObjectName("MainProgram")
        MainProgram.setEnabled(True)
        MainProgram.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainProgram.sizePolicy().hasHeightForWidth())
        MainProgram.setSizePolicy(sizePolicy)
        MainProgram.setMinimumSize(QtCore.QSize(600, 400))
        MainProgram.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainProgram)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(60, 20, 531, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.Title.setObjectName("Title")
        self.imagetitle = QtWidgets.QLabel(self.centralwidget)
        self.imagetitle.setGeometry(QtCore.QRect(140, 10, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagetitle.sizePolicy().hasHeightForWidth())
        self.imagetitle.setSizePolicy(sizePolicy)
        self.imagetitle.setText("")
        self.imagetitle.setPixmap(QtGui.QPixmap("Images/installer_icon.png"))
        self.imagetitle.setScaledContents(True)
        self.imagetitle.setObjectName("imagetitle")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 100, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.Select_app_label = QtWidgets.QLabel(self.centralwidget)
        self.Select_app_label.setGeometry(QtCore.QRect(40, 90, 311, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Select_app_label.sizePolicy().hasHeightForWidth())
        self.Select_app_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Select_app_label.setFont(font)
        self.Select_app_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Select_app_label.setObjectName("Select_app_label")
        self.mainprogressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.mainprogressBar.setGeometry(QtCore.QRect(150, 190, 391, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainprogressBar.sizePolicy().hasHeightForWidth())
        self.mainprogressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.mainprogressBar.setFont(font)
        self.mainprogressBar.setProperty("value", 24)
        self.mainprogressBar.setTextVisible(False)
        self.mainprogressBar.setObjectName("mainprogressBar")
        self.currentprogressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.currentprogressBar.setGeometry(QtCore.QRect(150, 240, 391, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentprogressBar.sizePolicy().hasHeightForWidth())
        self.currentprogressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.currentprogressBar.setFont(font)
        self.currentprogressBar.setProperty("value", 24)
        self.currentprogressBar.setTextVisible(False)
        self.currentprogressBar.setObjectName("currentprogressBar")
        self.Main_bar = QtWidgets.QLabel(self.centralwidget)
        self.Main_bar.setGeometry(QtCore.QRect(0, 190, 141, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_bar.sizePolicy().hasHeightForWidth())
        self.Main_bar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Main_bar.setFont(font)
        self.Main_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Main_bar.setObjectName("Main_bar")
        self.Current_bar = QtWidgets.QLabel(self.centralwidget)
        self.Current_bar.setGeometry(QtCore.QRect(0, 240, 141, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Current_bar.sizePolicy().hasHeightForWidth())
        self.Current_bar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Current_bar.setFont(font)
        self.Current_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Current_bar.setObjectName("Current_bar")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(360, 100, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.stop_btn.setFont(font)
        self.stop_btn.setObjectName("stop_btn")
        self.Title.raise_()
        self.imagetitle.raise_()
        self.pushButton.raise_()
        self.Select_app_label.raise_()
        self.mainprogressBar.raise_()
        self.Main_bar.raise_()
        self.Current_bar.raise_()
        self.currentprogressBar.raise_()
        self.stop_btn.raise_()
        MainProgram.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainProgram)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainProgram.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainProgram)
        self.statusbar.setObjectName("statusbar")
        MainProgram.setStatusBar(self.statusbar)
        self.actionInstall_From_File = QtGui.QAction(MainProgram)
        self.actionInstall_From_File.setObjectName("actionInstall_From_File")
        self.actionDownload_From_Url = QtGui.QAction(MainProgram)
        self.actionDownload_From_Url.setObjectName("actionDownload_From_Url")
        self.actionclear_cache = QtGui.QAction(MainProgram)
        self.actionclear_cache.setObjectName("actionclear_cache")
        self.actionInstall_Driver_Chrome = QtGui.QAction(MainProgram)
        self.actionInstall_Driver_Chrome.setObjectName("actionInstall_Driver_Chrome")
        self.actionInstall_Chrome_Driver = QtGui.QAction(MainProgram)
        self.actionInstall_Chrome_Driver.setObjectName("actionInstall_Chrome_Driver")
        self.actionCheck_For_Updates = QtGui.QAction(MainProgram)
        self.actionCheck_For_Updates.setObjectName("actionCheck_For_Updates")
        self.actionAbout = QtGui.QAction(MainProgram)
        self.actionAbout.setStatusTip("")
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(MainProgram)
        self.actionHelp.setObjectName("actionHelp")
        self.actionOpen_Logs = QtGui.QAction(MainProgram)
        self.actionOpen_Logs.setObjectName("actionOpen_Logs")
        self.actionDownload_From_Url_2 = QtGui.QAction(MainProgram)
        self.actionDownload_From_Url_2.setObjectName("actionDownload_From_Url_2")
        self.actioninstall_From_File = QtGui.QAction(MainProgram)
        self.actioninstall_From_File.setObjectName("actioninstall_From_File")
        self.actionSet_Wait_Time = QtGui.QAction(MainProgram)
        self.actionSet_Wait_Time.setObjectName("actionSet_Wait_Time")
        self.menuOptions.addAction(self.actioninstall_From_File)
        self.menuOptions.addAction(self.actionclear_cache)
        self.menuAbout.addAction(self.actionCheck_For_Updates)
        self.menuAbout.addAction(self.actionOpen_Logs)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainProgram)
        QtCore.QMetaObject.connectSlotsByName(MainProgram)

    def retranslateUi(self, MainProgram):
        _translate = QtCore.QCoreApplication.translate
        MainProgram.setWindowTitle(_translate("MainProgram", "Alt App Installer"))
        self.Title.setText(_translate("MainProgram", "Alt App Installer"))
        self.pushButton.setText(_translate("MainProgram", "Choose App"))
        self.Select_app_label.setText(_translate("MainProgram", "Select App To Install:"))
        self.Main_bar.setText(_translate("MainProgram", "Main Progress:"))
        self.Current_bar.setText(_translate("MainProgram", "Current Progress:"))
        self.stop_btn.setText(_translate("MainProgram", "Stop"))
        self.menuOptions.setTitle(_translate("MainProgram", "Options"))
        self.menuAbout.setTitle(_translate("MainProgram", "Help"))
        self.actionInstall_From_File.setText(_translate("MainProgram", "Install From File"))
        self.actionInstall_From_File.setStatusTip(_translate("MainProgram", "Install App (appx,Msix) From Local File"))
        self.actionDownload_From_Url.setText(_translate("MainProgram", "Install From Url"))
        self.actionDownload_From_Url.setStatusTip(_translate("MainProgram", "Install from link given by user (link of the app from microsoft.com)"))
        self.actionclear_cache.setText(_translate("MainProgram", "Clear Cache"))
        self.actionclear_cache.setStatusTip(_translate("MainProgram", "Clear all files like [Downloads,logs.. etc]"))
        self.actionInstall_Driver_Chrome.setText(_translate("MainProgram", "Install Driver + Chrome"))
        self.actionInstall_Chrome_Driver.setText(_translate("MainProgram", "Install Chrome Driver"))
        self.actionInstall_Chrome_Driver.setStatusTip(_translate("MainProgram", "Download and install chrome driver"))
        self.actionCheck_For_Updates.setText(_translate("MainProgram", "Check For Updates"))
        self.actionCheck_For_Updates.setStatusTip(_translate("MainProgram", "Check For Updates"))
        self.actionAbout.setText(_translate("MainProgram", "About"))
        self.actionHelp.setText(_translate("MainProgram", "Help"))
        self.actionHelp.setStatusTip(_translate("MainProgram", "Get Help"))
        self.actionOpen_Logs.setText(_translate("MainProgram", "Open Logs"))
        self.actionOpen_Logs.setStatusTip(_translate("MainProgram", "Open log File"))
        self.actionDownload_From_Url_2.setText(_translate("MainProgram", "Download From Url"))
        self.actionDownload_From_Url_2.setStatusTip(_translate("MainProgram", "Download from link given by user (link of the app from microsoft.com)"))
        self.actioninstall_From_File.setText(_translate("MainProgram", "Install From File"))
        self.actioninstall_From_File.setStatusTip(_translate("MainProgram", "Install App (Appx,Msix..etc) From Local File "))
        self.actionSet_Wait_Time.setText(_translate("MainProgram", "Set Wait Time"))
        self.actionSet_Wait_Time.setStatusTip(_translate("MainProgram", "Set Wait Time ( Use If Slow Internet Speed,Default: 5)"))
