from abc import abstractmethod

class Tables:
    """ abstract class for CRUD OPerations on QTableWidgets """
    @abstractmethod
    def __init__(self, parent, table_name):
        """ 
        :param parent: must have, 
        db Object which provides DB Connection
        ui Object which is the GUI
        :param table_name: Name of the Table inside DB
        """
        self.parent = parent
        self.table_name = table_name
        self.ui = self.parent.ui
        self.db = self.parent.db
    
    @abstractmethod
    def loadAll(self):
        pass