# Alexander Carpio Mamani

import cv2
import numpy as np
import subprocess
import os
from PyQt5.QtCore import QThread
from dialogs import Dialogs

class RenderVideo(QThread):
        def __init__(self, photo=None, video=None, output=None):
                QThread.__init__(self)

                self.photo = photo
                self.video = video
                self.outputfile = output

        def run(self):
                try:
                        self.generate_video()
                        
                except Exception as e:
                        Dialogs.dialog(text=str(e))
                
        def create_video(self):
                cap = cv2.VideoCapture(self.video)
                width, height = int(cap.get(3)), int(cap.get(4))

                lower_green = np.array([0,80,0])   # threshold of filter coloer green
                upper_green = np.array([80,255,80])

                img = cv2.imread(self.photo)
                img = cv2.resize(img, (width,height))  # resize the image to the size of video.

                path = "video.mp4"

                codec = cv2.VideoWriter_fourcc(*"MP4V")
                out = cv2.VideoWriter(path, codec , 30, (width,height))

                while (True):
                        try:
                                ret, frame = cap.read()

                                if not ret:
                                        break

                                mask = cv2.inRange(frame.copy(), lower_green, upper_green)
                                        
                                frame[mask != 0] = [0, 0, 0]
                                        
                                image = img.copy()
                                image[mask==0] = [0,0,0]

                                final = image + frame
                                        
                                #cv2.imshow('video',final)
                                        
                                out.write(final)

                                #cv2.waitKey(1)
                                        
                        except Exception as e:
                                print('opencv: ',e)
                                break
                        
                cap.release()
                out.release()
                cv2.destroyAllWindows()
                
        def generate_video(self):
                self.create_video()
                
                videofile = os.path.join(os.path.dirname(__file__),"video.mp4")
                audiofile = os.path.join(os.path.dirname(__file__),"audio.mp3")
                
                subprocess.run(f"ffmpeg -i \"{self.video}\" -y \"{audiofile}\"")
                
                temporal = os.path.join(os.path.dirname(__file__),"temporal.mp4")
                codec = "copy"
                
                subprocess.run(f"ffmpeg -i \"{videofile}\" -i \"{audiofile}\" -c {codec} \"{temporal}\"")
                os.system(f'DEL /F /A \"{videofile}\"')
                os.system(f'DEL /F /A \"{audiofile}\"')
                
                subprocess.run(f"ffmpeg -i \"{temporal}\" -c:v libx264 -b:v 1.5M -c:a libvo_aacenc -b:a 128K -y \"{self.outputfile}\"")
                os.system(f'DEL /F /A \"{temporal}\"')


if __name__ == '__main__':
        print('...')
        
