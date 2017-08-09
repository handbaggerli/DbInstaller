# -*- coding: utf-8 -*-

import GlobalInstaller

from PyQt5 import QtCore, QtGui
from MyTreeInfoItem import MyTreeInfoItem


##
## Implement the Abstract Table Model
## Holds the Tree Items as List of Object
##
class MyTreeInfoModel(QtCore.QAbstractItemModel):
    def __init__(self, headers, installation_data, parent=None):
        super(MyTreeInfoModel, self).__init__(parent=parent)

        rootData = [header for header in headers]
        self.rootItem = MyTreeInfoItem(rootData)  # Root Item beinhaltet den Header

        if len(installation_data.getInstallationObjects()) == 0:
            return

        # synonyme abfuellen
        if len(installation_data.getSynonymList()) > 0:
            self.__fillIn1LevelData(installation_data=installation_data, elementList=installation_data.getSynonymList(),
                                    value_text="Synonyme")

        # sequenzen abfuellen
        if len(installation_data.getSequenceList()) > 0:
            self.__fillIn1LevelData(installation_data=installation_data,
                                    elementList=installation_data.getSequenceList(), value_text="Sequenzen")

        # tab_saves abfuellen
        if len(installation_data.getTabSaveList()) > 0:
            self.__fillIn2LevelData(installation_data=installation_data, elementList=installation_data.getTabSaveList(),
                                    value_text="Save Tabellen")

        # tabs abfuellen
        if len(installation_data.getTabList()) > 0:
            self.__fillIn2LevelData(installation_data=installation_data, elementList=installation_data.getTabList(),
                                    value_text="Tabellen")

        # Views abfuellen
        if len(installation_data.getViewList()) > 0:
            self.__fillIn2LevelData(installation_data=installation_data, elementList=installation_data.getViewList(),
                                    value_text="Views")

        # Package headers abfuellen
        if len(installation_data.getPackageHeaderList()) > 0:
            self.__fillIn2LevelData(installation_data=installation_data,
                                    elementList=installation_data.getPackageHeaderList(), value_text="Package Headers")

        # Package bodies abfuellen
        if len(installation_data.getPackageBodyList()) > 0:
            self.__fillIn2LevelData(installation_data=installation_data,
                                    elementList=installation_data.getPackageBodyList(), value_text="Package Bodies")

        # Sqls abfuellen
        if len(installation_data.getSqlList()) > 0:
            self.__fillIn2LevelData(installation_data=installation_data, elementList=installation_data.getSqlList(),
                                    value_text="Scripts")

    #
    # Fill In Data with 2 levels of information.
    #
    def __fillIn2LevelData(self, installation_data, elementList, value_text):
        self.rootItem.insertChildren(position=self.rootItem.childCount(), count=1, columns=2)
        self.rootItem.child(row=self.rootItem.childCount() - 1).setData(column=0, value=value_text)
        self.rootItem.child(row=self.rootItem.childCount() - 1).setData(column=1,
                                                                        value="Total {value_text} [{count}]".format(
                                                                            value_text=value_text,
                                                                            count=len(
                                                                                elementList)))
        for element in elementList:
            for identification, installationObject in installation_data.getInstallationObjects():
                if element == identification:
                    parent = self.rootItem.child(row=self.rootItem.childCount() - 1)
                    parent.insertChildren(position=parent.childCount(), count=1, columns=2)
                    parent.child(row=parent.childCount() - 1).setData(column=0,
                                                                      value=installationObject.getDisplayName())
                    parent.child(row=parent.childCount() - 1).setData(column=1,

                                                                      value=installationObject.getSourcePath())
                    # Defines abfuellen
                    if len(installationObject.getLocalDefinesDic()) > 0:
                        subDefines = parent.child(row=parent.childCount() - 1)
                        subDefines.insertChildren(position=subDefines.childCount(), count=1, columns=2)
                        subDefines.child(row=subDefines.childCount() - 1).setData(column=0, value="Defines")
                        subDefines.child(row=subDefines.childCount() - 1).setData(column=1,
                                                                                  value="Total Defines [{count}]".format(
                                                                                      count=len(
                                                                                          installationObject.getLocalDefinesDic())))
                        for key, value in installationObject.getLocalDefinesDic().items():
                            subDefineKey = subDefines.child(row=subDefines.childCount() - 1)
                            subDefineKey.insertChildren(position=subDefineKey.childCount(), count=1, columns=2)
                            subDefineKey.child(row=subDefineKey.childCount() - 1).setData(column=0, value=key)
                            subDefineKey.child(row=subDefineKey.childCount() - 1).setData(column=1, value=value)

                    # Replacements abfuellen
                    if len(installationObject.getLocalReplacementDic()) > 0:
                        subReplaces = parent.child(row=parent.childCount() - 1)
                        subReplaces.insertChildren(position=subReplaces.childCount(), count=1, columns=2)
                        subReplaces.child(row=subReplaces.childCount() - 1).setData(column=0, value="Replacements")
                        subReplaces.child(row=subReplaces.childCount() - 1).setData(column=1,
                                                                                    value="Total Replacements [{count}]".format(
                                                                                        count=len(
                                                                                            installationObject.getLocalReplacementDic())))
                        for key, value in installationObject.getLocalReplacementDic().items():
                            subReplaceKey = subReplaces.child(row=subReplaces.childCount() - 1)
                            subReplaceKey.insertChildren(position=subReplaceKey.childCount(), count=1, columns=2)
                            subReplaceKey.child(row=subReplaceKey.childCount() - 1).setData(column=0, value=key)
                            subReplaceKey.child(row=subReplaceKey.childCount() - 1).setData(column=1, value=value)

    #
    # Fill In Data with 1 level of information.
    #
    def __fillIn1LevelData(self, installation_data, elementList, value_text):
        self.rootItem.insertChildren(position=self.rootItem.childCount(), count=1, columns=2)
        self.rootItem.child(row=self.rootItem.childCount() - 1).setData(column=0, value=value_text)
        self.rootItem.child(row=self.rootItem.childCount() - 1).setData(column=1,
                                                                        value="Total {value_text} [{count}]".format(
                                                                            value_text=value_text,
                                                                            count=len(
                                                                                elementList)))
        for element in elementList:
            for identification, installationObject in installation_data.getInstallationObjects():
                if element == identification:
                    parent = self.rootItem.child(row=self.rootItem.childCount() - 1)
                    parent.insertChildren(position=parent.childCount(), count=1, columns=2)
                    parent.child(row=parent.childCount() - 1).setData(column=0,
                                                                      value=installationObject.getDisplayName())
                    parent.child(row=parent.childCount() - 1).setData(column=1,
                                                                      value=installationObject.getSourcePath())

    #
    # Must by Implemented
    #
    def columnCount(self, parent=QtCore.QModelIndex()):
        return self.rootItem.columnCount()

    #
    # Must by Implemented
    #
    def data(self, index, role):
        if not index.isValid():
            return None

        if role != QtCore.Qt.DisplayRole and role != QtCore.Qt.EditRole:
            return None

        item = self.getItem(index)
        return item.data(index.column())

    #
    # Must by Implemented
    #
    def flags(self, index):
        if not index.isValid():
            return 0

        return QtCore.Qt.ItemIsEditable | super(MyTreeInfoModel, self).flags(index)

    #
    # Must by Implemented
    #
    def getItem(self, index):
        if index.isValid():
            item = index.internalPointer()
            if item:
                return item

        return self.rootItem

    #
    # Must by Implemented
    #
    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    #
    # Must by Implemented
    #
    def index(self, row, column, parent=QtCore.QModelIndex()):
        if parent.isValid() and parent.column() != 0:
            return QtCore.QModelIndex()

        parentItem = self.getItem(parent)
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    #
    # Must by Implemented
    #
    def insertColumns(self, position, columns, parent=QtCore.QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)
        success = self.rootItem.insertColumns(position, columns)
        self.endInsertColumns()

        return success

    #
    # Must by Implemented
    #
    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        parentItem = self.getItem(parent)
        self.beginInsertRows(parent, position, position + rows - 1)
        success = parentItem.insertChildren(position, rows,
                                            self.rootItem.columnCount())
        self.endInsertRows()

        return success

    #
    # Must by Implemented
    #
    def removeColumns(self, position, columns, parent=QtCore.QModelIndex()):
        self.beginRemoveColumns(parent, position, position + columns - 1)
        success = self.rootItem.removeColumns(position, columns)
        self.endRemoveColumns()

        if self.rootItem.columnCount() == 0:
            self.removeRows(0, self.rowCount())

        return success

    #
    # Must by Implemented
    #
    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        parentItem = self.getItem(parent)

        self.beginRemoveRows(parent, position, position + rows - 1)
        success = parentItem.removeChildren(position, rows)
        self.endRemoveRows()

        return success

    #
    # Must by Implemented
    #
    def rowCount(self, parent=QtCore.QModelIndex()):
        parentItem = self.getItem(parent)

        return parentItem.childCount()

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = self.getItem(index)
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QtCore.QModelIndex()

        return self.createIndex(parentItem.childNumber(), 0, parentItem)

    #
    # Must by Implemented
    #
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role != QtCore.Qt.EditRole:
            return False

        item = self.getItem(index)
        result = item.setData(index.column(), value)

        if result:
            self.dataChanged.emit(index, index)

        return result

    #
    # Must by Implemented
    #
    def setHeaderData(self, section, orientation, value, role=QtCore.Qt.EditRole):
        if role != QtCore.Qt.EditRole or orientation != QtCore.Qt.Horizontal:
            return False

        result = self.rootItem.setData(section, value)
        if result:
            self.headerDataChanged.emit(orientation, section, section)

        return result
