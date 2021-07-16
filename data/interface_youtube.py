# Alexander Carpio Mamani

from data.youtube import Download_YT
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QProgressBar, QLineEdit, QComboBox, QPushButton, QFileDialog
import sys
from data.dialogs import Dialogs

class InterfaceDownloader(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
                
##        self.setWindowTitle('go dmp3')
##        self.resize(300,170)
##
##        self.show()
        
    def initUI(self):
        
        self.box = QComboBox(self)
        self.box.setGeometry(20,50,200,20)
        items = ['mp4-1080p','mp4-720p', 'mp4-480p', 'mp4-360p']
        for i in items:
            self.box.addItem(i)
        self.box.setStyleSheet('font: 75 11pt "Arial";')

        self.entry = QLineEdit(self)
        self.entry.setGeometry(20,20,200,20)
        self.entry.setPlaceholderText("url o link de youtube")
        self.entry.setStyleSheet('font: 75 11pt "Arial";')

        self.button = QPushButton('Go',self)
        self.button.setStyleSheet('font: 75 11pt "Arial";')
        self.button.setGeometry(50,80,80,30)
        self.button.clicked.connect(self.go_process)

        self.bar = QProgressBar(self)
        self.bar.setGeometry(60,120,200,40)
        self.bar.setVisible(False)
        self.bar.setMaximum(0)
        self.bar.setMinimum(0)

    def go_process(self):
        try:
            option = str(self.box.currentText())
            folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            
            self.button.setEnabled(False)
            self.bar.setVisible(True)
            
            self.yt = Download_YT(url=self.entry.text(), resolution= option[4:], outputfile=folder)
            self.yt.finished.connect(self.finish)
            self.yt.start()
            
        except Exception as e:
            Dialogs.dialog(text=str(e))
            self.finish()

    def finish(self):
        self.bar.setVisible(False)
        self.button.setEnabled(True)
        self.entry.clear()
        del self.yt

    def dialog(title='Error!', text = 'There was a mistake.', icon=QMessageBox.Warning):
        msgBox = QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Yt = InterfaceDownloader()
    sys.exit(app.exec_())
    
