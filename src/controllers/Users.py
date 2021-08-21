from src.controllers.Tables import Tables
from PySide6.QtWidgets import QTableWidgetItem
from PySide6 import QtWidgets
from PySide6.QtGui import Qt


class Users(Tables):
    """ this class is a Setup for a Table """

    def __init__(self, parent, table_name):
        super().__init__(parent, table_name)
        # which table to work on
        self.table = self.parent.ui.table_users


    def setup(self):
        # set sizes for Columns
        self.table.setColumnWidth(0, 80)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 100)
        # how to resize Columns 
        header = self.table.horizontalHeader()  
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)     
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Set up the view
        self.table.show()
        self.loadAll()

    def loadAll(self):
        """ load all Data from DB """
        if self.table:
            with self.db.connect() as cursor:
                result = cursor.execute('SELECT * FROM %s' % self.table_name)
                data = result.fetchall()
                # fill into table
                index = self.table.rowCount()
                for item in data:
                    index = self.insertItem(index, item)
                
                
    def insertItem(self, index, data):
        """ insert at index a Row with data data """ 
        self.table.setRowCount(index + 1)
        # Nummer
        item = QTableWidgetItem(str(index + 1))
        item.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(index, 0, item)
        
        self.table.setItem(index, 1, QTableWidgetItem(data[1]))
        self.table.setItem(index, 2, QTableWidgetItem(data[2]))
        self.table.setItem(index, 3, QTableWidgetItem(data[3]))
        return index + 1
