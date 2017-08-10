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
    parser.add_argument('--inst_synonym', action='store_true', default=False,
                        help=r"Setzt Flag für die Installation von Synonymen.")
    parser.add_argument('--inst_sequence', action='store_true', default=False,
                        help=r"Setzt Flag für die Installation von Sequenzen.")
    parser.add_argument('--inst_tab_save', action='store_true', default=False,
                        help=r"Setzt Flag für die Installation von Tab Save Tabellen.")
    parser.add_argument('--inst_tab', action='store_false', default=True,
                        help=r"Entfernt Flag für die Installation von Tab Tabellen.")
    parser.add_argument('--inst_view', action='store_false', default=True,
                        help=r"Entfernt Flag für die Installation von Views.")
    parser.add_argument('--inst_package', action='store_false', default=True,
                        help=r"Entfernt Flag für die Installation von Packages.")
    parser.add_argument('--inst_sql', action='store_false', default=True,
                        help=r"Entfernt Flag für die Installation von Sqls.")

    # Erweiterte Parameter, welche die Gui Initalisierung Regeln.
    parser.add_argument('--username', default=r"", help=r"Benutzername der Datenbank Verbindung.")
    parser.add_argument('--password', default=r"", help=r"Passwort der Datenbank Verbindung.")
    parser.add_argument('--connection', default=r"", help=r"Connection der Datenbank Verbindung.")
    parser.add_argument('--svnBasePath', default=r"", help=r"Schreibt Pfad in SVN Basis Pfad.")
    parser.add_argument('--svnKndPath', default=r"", help=r"Schreibt Pfad in SVN Kassen Pfad.")
    parser.add_argument('--installationPath', default=r"", help=r"Schreibt Pfad in Installation Pfad.")
    parser.add_argument('--global_defines_file', default=r"",
                        help=r"Pfad zu einem TAB seperierten File wo die Defines vordefiniert sind.")
    # jsonl_parameters ueberschreibt alle anderen Parameter.
    parser.add_argument('--jsonl_parameters', type=str, default=r'',
                        help=(r"Übergabe von allen Parameter in einem JSONL Format."
                               "Dieses Format überschreibt alle Parameter."))

    # Parameter welche eine blinde Installation ohne Gui zulassen. Dazu muss showGui Paramter zwingend False sein.
    parser.add_argument('--hideGui', action='store_true', default=False, help=r"Startet DB Installer ohne GUI.")
    parser.add_argument('--clean_installation_path', action='store_true', default=False,
                        help=r"Führt Aktion Installationspfad Bereinigen durch. Nur in Kombi-nation von Parameter –-hideGui oder --json_file_path.")
    parser.add_argument('--copy_all_data_to_installation', action='store_true', default=False,
                        help=r"Führt Aktion Dateien ab Pfade Laden durch. Nur in Kombination von Parameter -–hideGui oder --json_file_path.")
    parser.add_argument('--install_objects', action='store_true', default=False,
                        help=r"Führt Aktion Objekte installieren durch. Nur in Kombination von Parameter –-hideGui oder --json_file_path.")
    parser.add_argument('--json_file_path', default=r"",
                        help=(r"Übergabe eines Parameter Files in Jsonl Format."
                              "Zusammen mit den Argumenten für die Aktionen kann damit eine ganze Kette von "
                              "Arbeiten mit einem einzigen Aufruf erledigt werden. "
                              "Arbeiten in einem Jsonl File sind immer ohne Gui "
                              "und schreiben Debug Informationen auf die Konsole."))
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
    if len(args.json_file_path) > 0:
        globalInstaller.workJsonlFile(json_file_path=args.json_file_path,
                                      cleanInstallationPath=args.clean_installation_path,
                                      copy_all_data_to_installation=args.copy_all_data_to_installation,
                                      install_objects=args.install_objects)
    elif args.hideGui:
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
