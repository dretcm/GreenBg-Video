# Alexander Carpio Mamani

import sys, os
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QFileDialog, QLineEdit, QMessageBox, QProgressBar
from data.generator import RenderVideo
from data.dialogs import Dialogs

class Background_app(QWidget):
        def __init__(self):
                super().__init__()

                self.video = ''
                self.photo = ''
                
                self.initUI()

                #self.setWindowTitle('Dretcm GreenBg')
                #self.resize(300,180)
                #self.show()

        def initUI(self):

                self.l1 = QLabel(self.photo,self)
                self.l1.setGeometry(70,20,200,20)
                self.l1.setStyleSheet('font: 11pt "Arial";')
                
                self.l2 = QLabel(self.video,self)
                self.l2.setGeometry(70,60,200,20)
                self.l2.setStyleSheet('font: 11pt "Arial";')

                self.b1 = QPushButton("Photo: ", self)
                self.b1.setStyleSheet('font: 75 11pt "Arial";')
                self.b1.setGeometry(10,20,50,20)
                
                self.b2 = QPushButton("Video: ", self)
                self.b2.setStyleSheet('font: 75 11pt "Arial";')
                self.b2.setGeometry(10,60,50,20)
                
                self.button = QPushButton("Go", self)
                self.button.setGeometry(90,120,50,30)
                self.button.setStyleSheet('font: 11pt "Arial";')
                
                self.entry = QLineEdit(self)
                self.entry.setGeometry(70,90,200,20)
                self.entry.setStyleSheet('font: 11pt "Arial";')
                self.entry.setPlaceholderText("outputfile")

                self.bar = QProgressBar(self)
                self.bar.setGeometry(60,120,180,30)
                self.bar.setVisible(False)
                self.bar.setMaximum(0)
                self.bar.setMinimum(0)

                self.button.clicked.connect(self.start_process)
                self.b1.clicked.connect(self.open_photo)
                self.b2.clicked.connect(self.open_video)

        def start_process(self):
                try:
                        if self.video == '' or self.photo == '':
                                raise Exception(" The video or the photo are empty")
                        
                        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
                        output = os.path.join(folder,self.entry.text()+'.mp4')
                        self.bar.setVisible(True)
                        
                        self.render = RenderVideo(photo=self.photo, video=self.video, output=output)
                        self.render.finished.connect(self.finish)
                        self.render.start()
                        
                except Exception as e:
                        Dialogs.dialog(text=str(e))
                        self.finish()
                        
        def finish(self):
                self.bar.setVisible(False)

        def open_photo(self):
                options = QFileDialog.Options()
                filename, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;", options=options)
                if filename:
                        self.l1.setText(str(os.path.basename(filename)))
                        self.photo = filename
                        
        def open_video(self):
                options = QFileDialog.Options()
                filename, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;", options=options)
                if filename:
                        self.l2.setText(str(os.path.basename(filename)))
                        self.video = filename
                
if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Background_app()
        sys.exit(app.exec_())
        
