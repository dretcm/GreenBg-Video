# Alexander Carpio Mamani

import sys, os
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QPushButton, QFileDialog, QTextEdit, QMessageBox, QProgressBar
from data.generate_meme import RenderMeme
from data.dialogs import Dialogs

class Interface_Meme(QWidget):
        def __init__(self):
                super().__init__()

                self.video = ''
                self.photo = ''
                
                self.initUI()

                #self.setWindowTitle('Dretcm GreenBg')
                self.resize(300,180)
                self.show()

        def initUI(self):
                
                bg = QLabel(self)
                bg.setGeometry(0,0,300,180)
                bg.setStyleSheet("background-image: url(data/data_meme/bg.png);")

                self.left = QTextEdit(self)
                self.left.setGeometry(10,10,135,100)
                self.left.setStyleSheet('font: 10pt "Arial";')

                self.right = QTextEdit(self)
                self.right.setGeometry(155,10,135,100)
                self.right.setStyleSheet('font: 10pt "Arial";')
                
                self.button = QPushButton("Go", self)
                self.button.setGeometry(240,120,50,30)
                self.button.setStyleSheet('font: 11pt "Arial";')
                
                self.size = QLineEdit(self)
                self.size.setStyleSheet('font: 12pt "Arial";')
                self.size.setGeometry(20,120,80,30)
                self.size.setPlaceholderText('size')
                self.size.setText("1")
                
                self.bold = QLineEdit(self)
                self.bold.setStyleSheet('font: 12pt "Arial";')
                self.bold.setGeometry(120,120,80,30)
                self.bold.setPlaceholderText('bold')
                self.bold.setText("2")

                self.bar = QProgressBar(self)
                self.bar.setGeometry(10,120,310,50)
                self.bar.setVisible(False)
                self.bar.setMaximum(0)
                self.bar.setMinimum(0)
                
                self.button.clicked.connect(self.start_process)
                
        def get_text(self, people):
                text = people.toPlainText() + "\n"
                new = []
                aux = ""
                for t in text:
                        if t == '\n':
                                new.append(aux)
                                aux = ""
                        else:
                                aux += t
                return new

        def start_process(self):
                try:
                        aea = self.left.toPlainText() + "\n"
                        
                        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
                        self.bar.setVisible(True)
                        
                        thin = self.get_text(self.left)
                        musculer = self.get_text(self.right)
                        
                        self.render = RenderMeme(thin=thin, musculer=musculer, output=folder, size=int(self.size.text()), bold=int(self.bold.text()))
                        self.render.finished.connect(self.finish)
                        self.render.start()
                        
                except Exception as e:
                        Dialogs.dialog(text=str(e))
                        self.finish()
                        
        def finish(self):
                self.bar.setVisible(False)
                
if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Interface_Meme()
        sys.exit(app.exec_())
        
