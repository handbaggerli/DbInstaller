# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_LoginDialog import Ui_LoginDialog

from MyParameterModel import MyParameterModel
from MyTreeInfoModel import MyTreeInfoModel

#
# Main Windows class.
# Build by Generator and edited by hand.
#
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 879)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_SvnBasePath = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_SvnBasePath.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_SvnBasePath.setPlaceholderText("")
        self.lineEdit_SvnBasePath.setObjectName("lineEdit_SvnBasePath")
        self.verticalLayout_2.addWidget(self.lineEdit_SvnBasePath)
        self.lineEdit_SvnKndPath = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_SvnKndPath.setObjectName("lineEdit_SvnKndPath")
        self.verticalLayout_2.addWidget(self.lineEdit_SvnKndPath)
        self.lineEdit_InstallPath = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_InstallPath.setObjectName("lineEdit_InstallPath")
        self.verticalLayout_2.addWidget(self.lineEdit_InstallPath)
        self.lineEdit_DbLogin = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_DbLogin.setObjectName("lineEdit_DbLogin")
        self.verticalLayout_2.addWidget(self.lineEdit_DbLogin)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_BrowseSvnBase = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_BrowseSvnBase.setObjectName("pushButton_BrowseSvnBase")
        self.verticalLayout_3.addWidget(self.pushButton_BrowseSvnBase)
        self.pushButton_BrowseSvnKnd = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_BrowseSvnKnd.setObjectName("pushButton_BrowseSvnKnd")
        self.verticalLayout_3.addWidget(self.pushButton_BrowseSvnKnd)
        self.pushButton_BrowseInstall = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_BrowseInstall.setObjectName("pushButton_BrowseInstall")
        self.verticalLayout_3.addWidget(self.pushButton_BrowseInstall)
        self.pushButton_ConnectDB = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ConnectDB.setObjectName("pushButton_ConnectDB")
        self.verticalLayout_3.addWidget(self.pushButton_ConnectDB)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_Synonym = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Synonym.setObjectName("checkBox_Synonym")
        self.verticalLayout_5.addWidget(self.checkBox_Synonym)
        self.checkBox_Sequence = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Sequence.setObjectName("checkBox_Sequence")
        self.verticalLayout_5.addWidget(self.checkBox_Sequence)
        self.checkBox_SaveTable = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_SaveTable.setAcceptDrops(False)
        self.checkBox_SaveTable.setChecked(False)
        self.checkBox_SaveTable.setObjectName("checkBox_SaveTable")
        self.verticalLayout_5.addWidget(self.checkBox_SaveTable)
        self.checkBox_Table = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Table.setChecked(True)
        self.checkBox_Table.setObjectName("checkBox_Table")
        self.verticalLayout_5.addWidget(self.checkBox_Table)
        self.checkBox_View = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_View.setChecked(True)
        self.checkBox_View.setObjectName("checkBox_View")
        self.verticalLayout_5.addWidget(self.checkBox_View)
        self.checkBox_Package = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Package.setChecked(True)
        self.checkBox_Package.setObjectName("checkBox_Package")
        self.verticalLayout_5.addWidget(self.checkBox_Package)
        self.checkBox_Script = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_Script.setObjectName("checkBox_Script")
        self.verticalLayout_5.addWidget(self.checkBox_Script)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.tableView_Parameter = QtWidgets.QTableView(self.groupBox_2)
        self.tableView_Parameter.setObjectName("tableView_Parameter")
        self.horizontalLayout_3.addWidget(self.tableView_Parameter)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_CleanupSchema = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_CleanupSchema.setObjectName("pushButton_CleanupSchema")
        self.horizontalLayout_5.addWidget(self.pushButton_CleanupSchema)
        self.pushButton_LoadFromPath = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_LoadFromPath.setObjectName("pushButton_LoadFromPath")
        self.horizontalLayout_5.addWidget(self.pushButton_LoadFromPath)
        self.pushButton_CleanupPath = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_CleanupPath.setObjectName("pushButton_CleanupPath")
        self.horizontalLayout_5.addWidget(self.pushButton_CleanupPath)
        self.pushButton_CopyAndReplace = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_CopyAndReplace.setObjectName("pushButton_CopyAndReplace")
        self.horizontalLayout_5.addWidget(self.pushButton_CopyAndReplace)
        self.pushButton_InstallObjects = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_InstallObjects.setObjectName("pushButton_InstallObjects")
        self.horizontalLayout_5.addWidget(self.pushButton_InstallObjects)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.treeView_Info = QtWidgets.QTreeView(self.groupBox_4)
        self.treeView_Info.setObjectName("treeView_Info")
        self.verticalLayout_7.addWidget(self.treeView_Info)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuAktion = QtWidgets.QMenu(self.menuBar)
        self.menuAktion.setObjectName("menuAktion")
        self.menuInfo = QtWidgets.QMenu(self.menuBar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDB_Schema_Leeren = QtWidgets.QAction(MainWindow)
        self.actionDB_Schema_Leeren.setObjectName("actionDB_Schema_Leeren")
        self.actionDateien_ab_Pfade_Laden = QtWidgets.QAction(MainWindow)
        self.actionDateien_ab_Pfade_Laden.setObjectName("actionDateien_ab_Pfade_Laden")
        self.actionInstallationspfad_Bereinigen = QtWidgets.QAction(MainWindow)
        self.actionInstallationspfad_Bereinigen.setObjectName("actionInstallationspfad_Bereinigen")
        self.actionReplacments_ersetzen = QtWidgets.QAction(MainWindow)
        self.actionReplacments_ersetzen.setObjectName("actionReplacments_ersetzen")
        self.actionObjekte_Installieren = QtWidgets.QAction(MainWindow)
        self.actionObjekte_Installieren.setObjectName("actionObjekte_Installieren")
        self.actionParameter_in_Zwischenablage = QtWidgets.QAction(MainWindow)
        self.actionParameter_in_Zwischenablage.setObjectName("actionParameter_in_Zwischenablage")
        self.actionVersionshinweis = QtWidgets.QAction(MainWindow)
        self.actionVersionshinweis.setObjectName("actionVersionshinweis")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAktion.addAction(self.actionDB_Schema_Leeren)
        self.menuAktion.addSeparator()
        self.menuAktion.addAction(self.actionDateien_ab_Pfade_Laden)
        self.menuAktion.addAction(self.actionInstallationspfad_Bereinigen)
        self.menuAktion.addAction(self.actionReplacments_ersetzen)
        self.menuAktion.addSeparator()
        self.menuAktion.addAction(self.actionObjekte_Installieren)
        self.menuAktion.addSeparator()
        self.menuAktion.addAction(self.actionParameter_in_Zwischenablage)
        self.menuInfo.addAction(self.actionVersionshinweis)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAktion.menuAction())
        self.menuBar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #
        # User Objects, edited by hand
        #
        self.globalInstaller = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DB Installer"))
        self.groupBox.setTitle(_translate("MainWindow", "Globale Einstellungen"))
        self.label.setText(_translate("MainWindow", "SVN Basis Pfad:"))
        self.label_2.setText(_translate("MainWindow", "SVN Kassen Pfad:"))
        self.label_4.setText(_translate("MainWindow", "Installation Pfad:"))
        self.label_3.setText(_translate("MainWindow", "Datenbank Login"))
        self.pushButton_BrowseSvnBase.setToolTip(_translate("MainWindow", "Pfadauswahl für den SVN Basispfad."))
        self.pushButton_BrowseSvnBase.setText(_translate("MainWindow", "Browse"))
        self.pushButton_BrowseSvnKnd.setToolTip(_translate("MainWindow", "Pfadauswahl für den SVN Kassenpfad"))
        self.pushButton_BrowseSvnKnd.setText(_translate("MainWindow", "Browse"))
        self.pushButton_BrowseInstall.setToolTip(_translate("MainWindow", "Pfadauswahl für den Installationspfad."))
        self.pushButton_BrowseInstall.setText(_translate("MainWindow", "Browse"))
        self.pushButton_ConnectDB.setToolTip(_translate("MainWindow", "Erstellt Verbindung zur Datenbank."))
        self.pushButton_ConnectDB.setText(_translate("MainWindow", "Connect"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Installationsparameter"))
        self.checkBox_Synonym.setText(_translate("MainWindow", "Synonyme [syn]:"))
        self.checkBox_Sequence.setText(_translate("MainWindow", "Sequenzen [seq]:"))
        self.checkBox_SaveTable.setText(_translate("MainWindow", "Save Tabellen [tab_save]:"))
        self.checkBox_Table.setText(_translate("MainWindow", "Tabellen [tab];"))
        self.checkBox_View.setText(_translate("MainWindow", "Views [viw]:"))
        self.checkBox_Package.setText(_translate("MainWindow", "Packages [pks / pkb]:"))
        self.checkBox_Script.setText(_translate("MainWindow", "Scripts [sql]:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Aktionen"))
        self.pushButton_CleanupSchema.setToolTip(_translate("MainWindow",
                                                            "Es werden alle Datenbank Objekte ausser Synonyme im angemeldeten Schema gelöscht. "))
        self.pushButton_CleanupSchema.setText(_translate("MainWindow", "DB Schema Leeren"))
        self.pushButton_LoadFromPath.setToolTip(
            _translate("MainWindow", "Einlesen der Dateien von den veschiedenen Dateipfaden."))
        self.pushButton_LoadFromPath.setText(_translate("MainWindow", "Dateien ab Pfade Laden"))
        self.pushButton_CleanupPath.setToolTip(
            _translate("MainWindow", "Löscht alle Dateien im Installations Verzeichnis."))
        self.pushButton_CleanupPath.setText(_translate("MainWindow", "Installationspfad Bereinigen"))
        self.pushButton_CopyAndReplace.setToolTip(_translate("MainWindow",
                                                             "<html><head/><body><p>Kopieren von allen Dateien anhand der Hirarchie von den ausgewählten SVN Pfaden in das Installationsverzeichnis. In diesem Schritt werden alle Replacements vorgenommen.</p></body></html>"))
        self.pushButton_CopyAndReplace.setText(_translate("MainWindow", "Replacements ersetzen"))
        self.pushButton_InstallObjects.setText(_translate("MainWindow", "Objekte Installieren"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Dateien Log"))
        self.menuFile.setTitle(_translate("MainWindow", "Datei"))
        self.menuAktion.setTitle(_translate("MainWindow", "Aktionen"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDB_Schema_Leeren.setText(_translate("MainWindow", "DB Schema Leeren"))
        self.actionDateien_ab_Pfade_Laden.setText(_translate("MainWindow", "Dateien ab Pfade Laden"))
        self.actionInstallationspfad_Bereinigen.setText(_translate("MainWindow", "Installationspfad Bereinigen"))
        self.actionReplacments_ersetzen.setText(_translate("MainWindow", "Replacments ersetzen"))
        self.actionObjekte_Installieren.setText(_translate("MainWindow", "Objekte Installieren"))
        self.actionParameter_in_Zwischenablage.setText(_translate("MainWindow", "Parameter in Zwischenablage kopieren"))
        self.actionVersionshinweis.setText(_translate("MainWindow", "Versionshinweis"))

    ############################################################################################################################




    #
    # Connect user Signals to Slot. Edited by hand.
    #
    def connect_user_isgnals(self):
        self.pushButton_BrowseSvnBase.clicked.connect(self.__browseSvnBasePath)
        self.pushButton_BrowseSvnKnd.clicked.connect(self.__browseSvnKnd)
        self.pushButton_BrowseInstall.clicked.connect(self.__browseInstall)
        self.pushButton_ConnectDB.clicked.connect(self.__connectDB)
        self.pushButton_CleanupSchema.clicked.connect(self.__cleanupSchema)
        self.pushButton_LoadFromPath.clicked.connect(self.__loadFromPath)
        self.pushButton_CleanupPath.clicked.connect(self.__cleanupPath)
        self.pushButton_CopyAndReplace.clicked.connect(self.__copyAndReplace)
        self.pushButton_InstallObjects.clicked.connect(self.__installObjects)

        self.checkBox_Synonym.clicked.connect(self.__updateFlags)
        self.checkBox_Sequence.clicked.connect(self.__updateFlags)
        self.checkBox_SaveTable.clicked.connect(self.__updateFlags)
        self.checkBox_Table.clicked.connect(self.__updateFlags)
        self.checkBox_View.clicked.connect(self.__updateFlags)
        self.checkBox_Package.clicked.connect(self.__updateFlags)
        self.checkBox_Script.clicked.connect(self.__updateFlags)

        self.actionExit.triggered.connect(self.__exitAction)
        self.actionDB_Schema_Leeren.triggered.connect(self.__cleanupSchema)
        self.actionDateien_ab_Pfade_Laden.triggered.connect(self.__loadFromPath)
        self.actionInstallationspfad_Bereinigen.triggered.connect(self.__cleanupPath)
        self.actionObjekte_Installieren.triggered.connect(self.__installObjects)
        self.actionReplacments_ersetzen.triggered.connect(self.__copyAndReplace)
        self.actionParameter_in_Zwischenablage.triggered.connect(self.__copyParameter2Clipboard)
        self.actionVersionshinweis.triggered.connect(self.__versionInfo)

    #
    # Fills in user information.
    #
    def set_user_variables(self, globalInstaller):
        self.globalInstaller = globalInstaller
        if self.globalInstaller.getDbLogin().testConnection(printInfo=False):
            self.lineEdit_DbLogin.setText(self.globalInstaller.getDbLogin().getDisplayConnectionString())

        self.lineEdit_SvnBasePath.setText(self.globalInstaller.getSvnBasePath())
        self.lineEdit_SvnKndPath.setText(self.globalInstaller.getSvnKndPath())
        self.lineEdit_InstallPath.setText(self.globalInstaller.getInstallationPath())

        self.checkBox_Synonym.setChecked(self.globalInstaller.getFlagSynonym())
        self.checkBox_Sequence.setChecked(self.globalInstaller.getFlagSequence())
        self.checkBox_SaveTable.setChecked(self.globalInstaller.getFlagTabSave())
        self.checkBox_Table.setChecked(self.globalInstaller.getFlagTab())
        self.checkBox_View.setChecked(self.globalInstaller.getFlagView())
        self.checkBox_Package.setChecked(self.globalInstaller.getFlagPackage())
        self.checkBox_Script.setChecked(self.globalInstaller.getFlagSql())

        self.parameter_model = MyParameterModel(data=self.globalInstaller.getGlobalDefinesList())
        self.tableView_Parameter.setModel(self.parameter_model)
        self.treeInfoHeader = ("Object", "Description")
        self.treeView_Info_model = MyTreeInfoModel(headers=self.treeInfoHeader, installation_data=self.globalInstaller)
        self.treeView_Info.setModel(self.treeView_Info_model)

    #
    # Exit
    #
    def __exitAction(self):
        QtCore.QCoreApplication.instance().quit()

    #
    # Copy parameter to clip board
    #
    def __copyParameter2Clipboard(self):
        parameter = self.globalInstaller.dupParameter2String()
        QtWidgets.QApplication.clipboard().setText(parameter)

    #
    # Opens an Message Box
    #
    def __versionInfo(self):
        message_text = (
            "Das Programm DB Installer wurde mit vollständig in Python mit folgenden Komponenten ertellt.\n"
            "Python Version 3.5.3 Anaconda\n"
            "Zusätzliche wurden folgende Module über die Conda Umgebung installiert.\n"
            "cx_Oracle 6.0b2\n"
            "pip 9.0.1\n"
            "pycrypto 2.6.1\n"
            "pyqt 5.6.0\n"
            "qt 5.6.2\n"
            "setuptools 27.2.0\n"
            "chardet 3.0.4"
        )
        msg_info = QtWidgets.QMessageBox()
        msg_info.setWindowTitle("Versionshinweis")
        msg_info.setText(message_text)
        msg_info.setIcon(QtWidgets.QMessageBox.Information)
        msg_info.setWindowModality(QtCore.Qt.ApplicationModal)
        msg_info.exec_()

    #
    # Brows and set a path.
    #
    def __browseSvnBasePath(self):
        self.statusBar.showMessage("SVN Basispfad setzen.", 10000)
        initPath = os.getcwd()
        if len(self.globalInstaller.getSvnBasePath()) > 0:
            initPath = self.globalInstaller.getSvnBasePath()
        folder = QtWidgets.QFileDialog.getExistingDirectory(directory=initPath)
        if len(folder) > 0:
            self.lineEdit_SvnBasePath.setText(folder)
        else:
            self.lineEdit_SvnBasePath.setText("")
        self.globalInstaller.setSvnBasePath(self.lineEdit_SvnBasePath.text())

    #
    # Brows and set a path.
    #
    def __browseSvnKnd(self):
        self.statusBar.showMessage("SVN Kundenpfad setzen.", 10000)
        initPath = os.getcwd()
        if len(self.globalInstaller.getSvnBasePath()) > 0:
            initPath = self.globalInstaller.getSvnBasePath()
        if len(self.globalInstaller.getSvnKndPath()) > 0:
            initPath = self.globalInstaller.getSvnKndPath()
        folder = QtWidgets.QFileDialog.getExistingDirectory(directory=initPath)
        if len(folder) > 0:
            self.lineEdit_SvnKndPath.setText(folder)
        else:
            self.lineEdit_SvnKndPath.setText("")
        self.globalInstaller.setSvnKndPath(self.lineEdit_SvnKndPath.text())

    #
    # Brows and set a path.
    #
    def __browseInstall(self):
        self.statusBar.showMessage("Installationspfad setzen.", 10000)
        initPath = os.getcwd()
        if len(self.globalInstaller.getInstallationPath()) > 0:
            initPath = self.globalInstaller.getInstallationPath()
        folder = QtWidgets.QFileDialog.getExistingDirectory(directory=initPath)
        if len(folder) > 0:
            self.lineEdit_InstallPath.setText(folder)
        else:
            self.lineEdit_InstallPath.setText("")
        self.globalInstaller.setInstallationPath(self.lineEdit_InstallPath.text())
        self.__refreshTreeView()

    #
    # Open dialog for DB Connection and set connection
    #
    def __connectDB(self):
        loginShow = True
        self.statusBar.showMessage("Datenbank Verbindung setzen.", 10000)
        while loginShow:
            LoginDialog = QtWidgets.QDialog()
            LoginDialog.setWindowModality(QtCore.Qt.ApplicationModal)
            ui = Ui_LoginDialog()
            ui.setupUi(LoginDialog)
            result = LoginDialog.exec_()
            if result == QtWidgets.QDialog.Accepted:
                self.statusBar.showMessage("Datenbank Verbindung testen...", 10000)
                self.globalInstaller.getDbLogin().setUserName(userName=ui.lineEdit_Username.text())
                self.globalInstaller.getDbLogin().setPassword(passWord=ui.lineEdit_Password.text())
                self.globalInstaller.getDbLogin().setConnection(connection=ui.lineEdit_Connection.text())
                if self.globalInstaller.getDbLogin().testConnection(printInfo=False):
                    self.lineEdit_DbLogin.setText(self.globalInstaller.getDbLogin().getDisplayConnectionString())
                    self.statusBar.showMessage("Datenbank Verbindung OK.", 10000)
                    loginShow = False
                else:
                    self.statusBar.showMessage("Datenbank Verbindung fehlgeschlagen, Dialog wird neu angezeigt.", 10000)


            elif result == QtWidgets.QDialog.Rejected:
                loginShow = False

            LoginDialog.destroy()

    #
    # Opens a warning dialog and send drop all object command to GlobalInstaller
    #
    def __cleanupSchema(self):
        message_text = (
            "Achtung!\n"
            "Es werden alle DB Objekte ausser Synonyme und Datenbank Links gelöscht.\n"
            "Datenbank Info: {dbInfo}\n"
            "Fortfahren?"
        ).format(dbInfo=self.globalInstaller.getDbLogin().getDisplayConnectionString())
        msg_info = QtWidgets.QMessageBox()
        msg_info.setWindowTitle(r"Löschen der Datenbank Objekte")
        msg_info.setText(message_text)
        msg_info.setIcon(QtWidgets.QMessageBox.Warning)
        msg_info.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_info.setWindowModality(QtCore.Qt.ApplicationModal)
        retval = msg_info.exec_()
        if retval == QtWidgets.QMessageBox.Yes:
            self.statusBar.showMessage("Alle Datenbank Objekte werden gelöscht...")
            self.globalInstaller.cleanDatabase()
            self.statusBar.showMessage("Alle Datenbank Objekte gelöscht.", 10000)

    #
    # Send Load command to GlobalInstaller
    #
    def __loadFromPath(self):
        message = "Files werden ab den definierten Pfaden geladen analysiert..."
        self.statusBar.showMessage(message)
        self.globalInstaller.readInstallationObjectFromPath()
        self.parameter_model = MyParameterModel(data=self.globalInstaller.getGlobalDefinesList())
        self.tableView_Parameter.setModel(self.parameter_model)
        self.statusBar.showMessage(message, 5000)
        self.__refreshTreeView()

    #
    # Manuell Tree View Refresh
    #
    def __refreshTreeView(self):
        message = "Tree View wird neu aufgebaut..."
        self.statusBar.showMessage(message)
        self.treeView_Info_model = MyTreeInfoModel(headers=self.treeInfoHeader,
                                                   installation_data=self.globalInstaller)
        self.treeView_Info.setModel(self.treeView_Info_model)
        for col in range(self.treeView_Info_model.columnCount()):
            self.treeView_Info.resizeColumnToContents(col)
        message = "Tree View wird neu aufgebaut..."
        self.statusBar.showMessage(message, 5000)

    #
    # Send clean installation path command to GlobalInstaller
    #
    def __cleanupPath(self):
        self.statusBar.showMessage("Installations Pfad wird bereinigt...", 10000)
        self.globalInstaller.cleanInstallationPath()
        self.statusBar.showMessage("Installations Pfad Bereinigung abgeschlossen.", 10000)

    #
    # Send install command to GlobalInstaller
    # send identification object in loop
    #
    def __copyAndReplace(self):
        self.globalInstaller.copyGlobalDefinesList2Dic()
        message = "Installations Datei erstllen fuer {file_name}"
        for key in self.globalInstaller.getSynonymList():
            self.statusBar.showMessage(message.format(file_name=key))
            self.globalInstaller.copyData2InstallationPath(identification=key)
        for key in self.globalInstaller.getSequenceList():
            self.statusBar.showMessage(message.format(file_name=key))
            self.globalInstaller.copyData2InstallationPath(identification=key)
        for key in self.globalInstaller.getTabSaveList():
            self.statusBar.showMessage(message.format(file_name=key))
            self.globalInstaller.copyData2InstallationPath(identification=key)
        for key in self.globalInstaller.getTabList():
            self.statusBar.showMessage(message.format(file_name=key))
            self.globalInstaller.copyData2InstallationPath(identification=key)
        for key in self.globalInstaller.getViewList():
            self.statusBar.showMessage(message.format(file_name=key))
            self.globalInstaller.copyData2InstallationPath(identification=key)
        for key in self.globalInstaller.getPackageHeaderList():
            self.statusBar.showMessage(message.format(file_name=key))
            self.globalInstaller.copyData2InstallationPath(identification=key)
        for key in self.globalInstaller.getPackageBodyList():
            self.statusBar.showMessage(message.format(file_name=key))
            self.globalInstaller.copyData2InstallationPath(identification=key)
        for key in self.globalInstaller.getSqlList():
            self.statusBar.showMessage(message.format(file_name=key))
            self.globalInstaller.copyData2InstallationPath(identification=key)

        self.statusBar.showMessage("Alle Installations Dateien aufbereitet.", 10000)

    #
    # Build install Information
    #
    def __installObjects(self):
        message = "Objekt in DB installieren {objekt_name}."
        isBlindInstall = False
        if self.treeView_Info_model.rowCount() == 0:
            self.globalInstaller.buildInstallationObjectFromFileSystem()
            message = "Objekt in DB installieren Datei: {objekt_name}."
            isBlindInstall = True

        if self.globalInstaller.getFlagSynonym():
            for key in self.globalInstaller.getSynonymList():
                self.__installOneObject(isBlindInstall, key, message)
        if self.globalInstaller.getFlagSequence():
            for key in self.globalInstaller.getSequenceList():
                self.__installOneObject(isBlindInstall, key, message)
        if self.globalInstaller.getFlagTabSave():
            for key in self.globalInstaller.getTabSaveList():
                self.__installOneObject(isBlindInstall, key, message)
        if self.globalInstaller.getFlagTab():
            for key in self.globalInstaller.getTabList():
                self.__installOneObject(isBlindInstall, key, message)
        if self.globalInstaller.getFlagView():
            for key in self.globalInstaller.getViewList():
                self.__installOneObject(isBlindInstall, key, message)
        if self.globalInstaller.getFlagPackage():
            for key in self.globalInstaller.getPackageHeaderList():
                self.__installOneObject(isBlindInstall, key, message)
            for key in self.globalInstaller.getPackageBodyList():
                self.__installOneObject(isBlindInstall, key, message)
        if self.globalInstaller.getFlagSql():
            for key in self.globalInstaller.getSqlList():
                self.__installOneObject(isBlindInstall, key, message)

        self.statusBar.showMessage("Invalide DB Objekte kompilieren...")
        self.globalInstaller.compileSchema()
        self.statusBar.showMessage("Alle Objekte in DB Installiert.", 10000)
    #
    # Send One object to GlobalInstaller
    #
    def __installOneObject(self, isBlindInstall, key, message):
        self.statusBar.showMessage(message.format(objekt_name=key))
        if isBlindInstall:
            self.globalInstaller.installObject2DatabaseBlind(file_name=key)
        else:
            self.globalInstaller.installObject2Database(identification=key)
        QtCore.QCoreApplication.processEvents()

    #
    # Synchronaize check box flags with GlobalInstaller.
    #
    def __updateFlags(self):
        self.globalInstaller.setFlagSynonym(self.checkBox_Synonym.isChecked())
        self.globalInstaller.setFlagSequence(self.checkBox_Sequence.isChecked())
        self.globalInstaller.setFlagTabSave(self.checkBox_SaveTable.isChecked())
        self.globalInstaller.setFlagTab(self.checkBox_Table.isChecked())
        self.globalInstaller.setFlagView(self.checkBox_View.isChecked())
        self.globalInstaller.setFlagPackage(self.checkBox_Package.isChecked())
        self.globalInstaller.setFlagSql(self.checkBox_Script.isChecked())
