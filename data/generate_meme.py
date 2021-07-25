import cv2
import subprocess
import os
from PyQt5.QtCore import QThread
from data.dialogs import Dialogs

class RenderMeme(QThread):
        def __init__(self, thin=["..."], musculer=["..."], output="", bold=2, size=1):
                QThread.__init__(self)

                self.output = output
                self.thin = thin
                self.musculer = musculer

                self.size = size
                self.bold = bold

        def run(self):
                try:
                        self.record_meme()
                        
                except Exception as e:
                        Dialogs.dialog(text=str(e))
                        pass
                
        def put_text(self, words, image, separate = 30, x=10):
                y = separate
                img = image
                for text in words:
                        img = cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, self.size, (0,0,0), self.bold, cv2.LINE_AA)
                        y += separate
                return img

        def record_meme(self, video="data/data_meme/vs.mp4", audio="data/data_meme/vs.mp3", path = "data/data_meme/vs_tempo.mp4"):
                cap = cv2.VideoCapture(video)
                font = cv2.FONT_HERSHEY_SIMPLEX
                
                width, height = int(cap.get(3)), int(cap.get(4))
                
                codec = cv2.VideoWriter_fourcc(*"MP4V")
                out = cv2.VideoWriter(path, codec , 30.0, (width, height))
                                         
                while (True):
                        ret, frame = cap.read()

                        if not ret:
                                break

                        img = cv2.line(frame, (360,0), (360,720), (0,0,0), 2)
                        img = cv2.rectangle(img, (0,0), (720,720), (0,0,0), 2)
                        
                        img = self.put_text(self.thin, img)
                        img = self.put_text(self.musculer, frame, x= 370)
                                
                        out.write(img)
                        
                        if cv2.waitKey(1) == ord('q'):
                                break

                out.release()
                cap.release()
                cv2.destroyAllWindows()

                self.output = os.path.join(self.output, "output.mp4")
                subprocess.run(f"ffmpeg -i \"{path}\" -i \"{audio}\" -c:v libx264 -b:v 1.5M -c:a libvo_aacenc -b:a 128K -y \"{self.output}\"")
                os.remove(path)
                
if __name__ == "__main__":
        thin = ["Gustavo diciendo que", "tenia lag y se ganaba"]
        musculer = ["Diego mandando", "surrender"]
        a = RenderMeme(thin=thin, musculer=musculer,output=r'C:/Users/USUARIO/Desktop/')
        a.record_meme()
