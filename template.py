import sys

from pathlib import Path
import os
from src.config.LoggerConfiguration import configure_logging
from ui_main import Ui_MainWindow
from src.ui_Functions import ui_Functions
from ui_dialog import Ui_Dialog
from ui_error import Ui_Error
from PySide6.QtWidgets import QMainWindow, QApplication
import logging
from PySide6 import QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.logger = logging.getLogger('MainWindow')
        self.ui = Ui_MainWindow()
        self.rootDir = Path(__file__).parent

        # UI Stuff
        self.ui.setupUi(self)
        self.ui_functions = ui_Functions(self, self.ui)
        self.ui_functions.setWindowTitle("MainWindow")
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.rootDir, 'App.ico')))

        # Connectors
        self.ui.btn_close.clicked.connect(self.window_close)
        self.ui.btn_max.clicked.connect(self.ui_functions.maximize_restore)
        self.ui.btn_min.clicked.connect(self.showMinimized)

        # ?? in progress
        self.dialog = Ui_Dialog()
        self.error = Ui_Error()

        # dialogexec("Heading", "Message", "icon", "Button1name", "button2name")
        # errorexec("Message", "icon", "buttonname")
        

    def dialogexec(self, heading, message, icon, btn1, btn2):
        self.dialog.dialogConstrict(self.dialog, heading, message, icon, btn1, btn2)
        self.dialog.exec_()

    def errorexec(self, heading, icon, btnOk):
        self.error.errorConstrict(self.error, heading, icon, btnOk)
        self.error.exec_()

    def closeEvent(self, event):
        """ catch the closing Event """
        print("X is clicked: I'm now closing ...")
        
    def window_close(self):
        """ exit the app """
        app.quit()
     
    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    configure_logging()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
