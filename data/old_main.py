# Alexander Carpio Mamani

import sys
from PyQt5.QtWidgets import (QWidget, QApplication,QTabWidget)
from interface_youtube import InterfaceDownloader
from interface_generator import Background_app
from interface_meme import Interface_Meme
from dialogs import Dialogs

class Interface(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
                
        self.setWindowTitle('Dretcm BG')
        self.resize(313,203)

        self.show()

    def initUI(self):
        try:
            tab1 = Background_app()
            tab2 = Interface_Meme()
            tab3 = InterfaceDownloader()

            tabs = QTabWidget(self)
            tabs.setStyleSheet('font: 10pt "Arial";')
            tabs.addTab(tab1,'Bg green')
            tabs.addTab(tab2,'Meme')
            tabs.addTab(tab3,'Downloader')
            
            tabs.setGeometry(5,3,303,197)
        except Exception as e:
            Dialogs.dialog(text=str(e))

                
if __name__=='__main__':
    app = QApplication(sys.argv)
    aux = Interface()
    sys.exit(app.exec_())
