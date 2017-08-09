# -*- coding: utf-8 -*-
__author__ = 'U10938'

from PyQt5 import QtCore
from operator import itemgetter


class MyParameterModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        QtCore.QAbstractTableModel.__init__(self)
        self.headerdata = ["Paramter", "Value"]
        self.arraydata = data

    #
    # Function rowCount must be implemented
    #
    def rowCount(self, parent=QtCore.QModelIndex()):
        if len(self.arraydata) > 0:
            return len(self.arraydata)
        return 0

    #
    # Function columnCount must be implemented
    #
    def columnCount(self, parent=QtCore.QModelIndex()):
        if len(self.arraydata) > 0:
            return len(self.arraydata[0])
        return 0

    #
    # this is the initialisation of the header.
    #
    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.headerdata[section])
        return QtCore.QVariant()

    #
    # flags defines what with the item could be done
    #
    def flags(self, index: QtCore.QModelIndex):
        if index.column() == 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable  # only show data
        elif index.column() == 1:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable

    #
    # initialize the data for show on the grid.
    #
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        if not role == QtCore.Qt.DisplayRole:
            return None

        return QtCore.QVariant(self.arraydata[index.row()][index.column()])

    #
    # updates the data for each cell
    #
    def setData(self, index, value, role):
        if index.column() == 0:
            return False
        elif index.column() == 1:
            self.arraydata[index.row()][index.column()] = value
            return True

        return False

    #
    # Sorts the Data depending on the column
    #
    def sort(self, col, reverse):
        self.layoutAboutToBeChanged.emit()
        self.arraydata.sort(key=itemgetter(col), reverse=reverse)
        self.layoutChanged.emit()
