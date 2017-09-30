# -*- coding: utf-8 -*-
__author__ = 'U10938'

import os
import re
import urllib
from chardet import UniversalDetector

import GlobalInstaller


#
# Class for holding one Installation object.
# All copy and replacement process is done in this class.
#
class InstallationObject():
    def __init__(self, identification, svnBasePath, svnKndPath, installationPath, globalDefinesDic):

        self.identification = identification
        self.globalDefinesDic = globalDefinesDic
        self.type = self.identification.split('-')[0]
        self.fileName = self.identification.split('-')[1]
        self.fileNameWithExt = self.fileName + "." + self.type

        self.installationPath = self.__getInstallationPath(installationPath=installationPath)
        self.svnBasePath = self.__searchInPath(path=svnBasePath)
        self.svnKndPath = self.__searchInPath(path=svnKndPath)
        self.sourcePath = ""
        if len(self.svnKndPath) > 0:
            self.sourcePath = self.svnKndPath
        else:
            self.sourcePath = self.svnBasePath
        self.localDefinesDic = dict()
        self.localReplacementDic = dict()
        self.localReplacementDicData = dict()
        self.__findDefinesAndReplacementsInFile()
        self.__addLocalDefines2GlobalDefines()
        self.__searchReplacemntsFile(startPath=svnBasePath)
        self.__searchReplacemntsFile(startPath=svnKndPath)
        self.__loadReplacementsFromFile()

    def getIdentification(self):
        return self.identification

    def getFileName(self):
        return self.fileNameWithExt

    def getSourcePath(self):
        return self.sourcePath

    def getLocalDefinesDic(self):
        return self.localDefinesDic

    def getLocalReplacementDic(self):
        return self.localReplacementDic

    def getType(self):
        return self.type

    def getDisplayName(self):
        return self.fileName

    def getInstallationFile(self):
        return os.path.join(self.installationPath, self.fileNameWithExt)

    #
    # Reads the source file. Replaces the Replacements and writes the the destination path.
    #
    def copyData2InstallationPath(self):
        text = ""
        encoding = self.__detectEncoding()
        with open(os.path.join(self.sourcePath, self.fileNameWithExt), encoding=encoding) as fReader:
            text = fReader.read()

        # Zeilenweise auslesen, da Reguläre Expression im Code als Replacement erkannt werden könnten.
        lines = text.split("\n")
        text = ""
        for line in lines:
            if re.search(GlobalInstaller.GlobalInstaller.REGEX_VARIABLE_PATTERN, line):
                line = line.replace(r"/*{", r"{").replace(r"}*/", r"}")
                line = line.format(**self.localReplacementDicData)
            text += line + "\n"
        text = self.__replaceDefines(text=text)
        if not os.path.exists(self.installationPath):
            os.makedirs(self.installationPath)
        with open(os.path.join(self.installationPath, self.fileNameWithExt), mode="w+", encoding='utf-8') as fWriter:
            fWriter.write(text)

    #
    # Find the Encoding
    #
    def __detectEncoding(self):
        detector = UniversalDetector()
        detector.reset()
        with open(os.path.join(self.sourcePath, self.fileNameWithExt), 'rb') as fReader:
            text = fReader.readlines()

        for line in text:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']


    def __detectEncoding_file(self, filename):
        detector = UniversalDetector()
        detector.reset()
        with open(filename, 'rb') as fReader:
            text = fReader.readlines()

        for line in text:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']



    #
    # Defines in SQL has double .., replace it with single .
    #
    def __replaceDefines(self, text):
        for key, value in self.globalDefinesDic.items():
            text = text.replace(key + "..", key + ".")
            text = text.replace(key, value)
        return text

    #
    # Search if the file is the given path
    #
    def __searchInPath(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == self.fileNameWithExt:
                    return root
        return ""

    #
    # set the correct installation subfolder by type.
    #
    def __getInstallationPath(self, installationPath):
        if self.type == GlobalInstaller.GlobalInstaller.FILE_EXTENSION_SYNONYM:
            return os.path.join(installationPath, GlobalInstaller.GlobalInstaller.SUBDIR_SYNONYM)
        if self.type == GlobalInstaller.GlobalInstaller.FILE_EXTENSION_SEQUENCE:
            return os.path.join(installationPath, GlobalInstaller.GlobalInstaller.SUBDIR_SEQUENCE)
        if self.type == GlobalInstaller.GlobalInstaller.FILE_EXTENSION_TAB_SAVE:
            return os.path.join(installationPath, GlobalInstaller.GlobalInstaller.SUBDIR_TAB_SAVE)
        if self.type == GlobalInstaller.GlobalInstaller.FILE_EXTENSION_TABLE:
            return os.path.join(installationPath, GlobalInstaller.GlobalInstaller.SUBDIR_TABLE)
        if self.type == GlobalInstaller.GlobalInstaller.FILE_EXTENSION_VIEW:
            return os.path.join(installationPath, GlobalInstaller.GlobalInstaller.SUBDIR_VIEW)
        if self.type == GlobalInstaller.GlobalInstaller.FILE_EXTENSION_PACKAGE_HEADER:
            return os.path.join(installationPath, GlobalInstaller.GlobalInstaller.SUBDIR_PACKAGE_HEADER)
        if self.type == GlobalInstaller.GlobalInstaller.FILE_EXTENSION_PACKAGE_BODY:
            return os.path.join(installationPath, GlobalInstaller.GlobalInstaller.SUBDIR_PACKAGE_BODY)
        if self.type == GlobalInstaller.GlobalInstaller.FILE_EXTENSION_SQL:
            return os.path.join(installationPath, GlobalInstaller.GlobalInstaller.SUBDIR_SQL)
        return installationPath

    #
    # Search if defines or replacements in the file exists.
    #
    def __findDefinesAndReplacementsInFile(self):
        text = ""
        encoding = self.__detectEncoding()
        with open(os.path.join(self.sourcePath, self.fileNameWithExt), encoding=encoding) as fReader:
            text = fReader.read()
        matchDefins = re.findall(GlobalInstaller.GlobalInstaller.REGEX_DEFINE_PATTERN, text)
        matchReplacemet = re.findall(GlobalInstaller.GlobalInstaller.REGEX_VARIABLE_PATTERN, text)
        for define in matchDefins:
            self.localDefinesDic[define] = define[2:]
        for replace in matchReplacemet:
            self.localReplacementDic[replace] = ""

    #
    # Copy new local defines to the global define list
    #
    def __addLocalDefines2GlobalDefines(self):
        for key, value in self.localDefinesDic.items():
            if not key in self.globalDefinesDic:
                self.globalDefinesDic[key] = value

    #
    # Search for the replacemnt file.
    #
    def __searchReplacemntsFile(self, startPath):
        if len(startPath) > 0:
            for key, value in self.localReplacementDic.items():
                fileName = key.replace(r"/*{", "").replace(r"}*/", "")
                fileName += ".{extension}".format(
                    extension=GlobalInstaller.GlobalInstaller.FILE_EXTENSION_SQL_REPLACEMENT)
                for root, dirs, files in os.walk(startPath):
                    for file in files:
                        if file == fileName:
                            self.localReplacementDic[key] = os.path.join(root, file)

    #
    # Read the replacemnt text from the replacement file.
    #
    def __loadReplacementsFromFile(self):
        if len(self.localReplacementDic.items()):
            for key, value in self.localReplacementDic.items():
                # key Umschluesseln, damit format() Befehl funktioniert
                new_key = key.replace(r"/*{", "").replace(r"}*/", "")
                infoTextStart = " /* import von {0} */ \n".format(value)
                infoTextEnd = "\n/* ---- ENDE IMPORT ---- */\n"
                replaceText = "/* Replacement nicht vorhanden. */"
                if os.path.exists(value):
                    encoding = self.__detectEncoding_file(filename=value)
                    with open(value, encoding=encoding) as fReader:
                        replaceText = fReader.read()

                self.localReplacementDicData[new_key] = infoTextStart + replaceText + infoTextEnd
