# -*- coding: utf-8 -*-

import sys
from argparse import ArgumentParser

from DatabaseLogin import DatabaseLogin
from GlobalInstaller import GlobalInstaller

from PyQt5 import QtWidgets

from Ui_MainWindow import Ui_MainWindow

# import damit Installer funktioniert. auch wenn diese nicht hier benoetigt werden.

from PyQt5 import QtCore, QtGui
import cx_Oracle
import json
import base64

from Crypto.Cipher import AES


def get_parser():
    parser = ArgumentParser()
    # Parameter, welche die Gui Initalisierung Regeln.
    parser.add_argument('--inst_synonym', action='store_true', default=False)
    parser.add_argument('--inst_sequence', action='store_true', default=False)
    parser.add_argument('--inst_tab_save', action='store_true', default=False)
    parser.add_argument('--inst_tab', action='store_false', default=True)
    parser.add_argument('--inst_view', action='store_false', default=True)
    parser.add_argument('--inst_package', action='store_false', default=True)
    parser.add_argument('--inst_sql', action='store_false', default=True)

    # Erweiterte Parameter, welche die Gui Initalisierung Regeln.
    parser.add_argument('--username', default=r"")
    parser.add_argument('--password', default=r"")
    parser.add_argument('--connection', default=r"")
    parser.add_argument('--svnBasePath', default=r"")
    parser.add_argument('--svnKndPath', default=r"")
    parser.add_argument('--installationPath', default=r"")
    parser.add_argument('--global_defines_file', default=r"")
    # jsonl_parameters ueberschreibt in der Regel alle anderen Parameter.
    parser.add_argument('--jsonl_parameters', type=str, default=r'')

    # Parameter welche eine blinde Installation ohne Gui zulassen. Dazu muss showGui Paramter zwingend False sein.
    parser.add_argument('--showGui', default=True)
    parser.add_argument('--clean_installation_path', default=False)
    parser.add_argument('--copy_all_data_to_installation', default=False)
    parser.add_argument('--install_objects', default=False)
    return parser


#
# Main Programm. All starts at this point.
#
if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    dbLogin = DatabaseLogin(userName=args.username, passWord=args.password, connection=args.connection)
    dbLogin.testConnection(printInfo=False)
    globalInstaller = GlobalInstaller(dbLogin=dbLogin, svnBasePath=args.svnBasePath, svnKndPath=args.svnKndPath,
                                      installationPath=args.installationPath, flag_synonym=args.inst_synonym,
                                      flag_sequence=args.inst_sequence, flag_tab_save=args.inst_tab_save,
                                      flag_tab=args.inst_tab, flag_view=args.inst_view, flag_package=args.inst_package,
                                      flag_sql=args.inst_sql, global_defines_file=args.global_defines_file,
                                      jsonl_parameters=args.jsonl_parameters
                                      )

    if not args.showGui:
        # Calls function without gui.
        # used in command line only.
        if args.clean_installation_path:
            globalInstaller.cleanInstallationPath()
        if args.copy_all_data_to_installation:
            globalInstaller.readInstallationObjectFromPath()
            globalInstaller.copyAllData2InstallationPath()
        if args.install_objects:
            globalInstaller.installAllObjects2Database()
    else:
        # Default Obption starts Gui
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.connect_user_isgnals()
        ui.set_user_variables(globalInstaller=globalInstaller)
        MainWindow.show()
        sys.exit(app.exec_())
