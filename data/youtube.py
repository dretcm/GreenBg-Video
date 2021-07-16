# Alexander Carpio Mamani

import pytube
import subprocess
from PyQt5.QtCore import QThread
from data.dialogs import Dialogs
import os

class Download_YT(QThread):
    def __init__(self, url=None, resolution=None, outputfile=None):
        QThread.__init__(self)
        
        self.url = url
        self.resolution = resolution
        self.outputfile = outputfile

        self.path = os.path.dirname(os.path.abspath(__file__)) + '/processYT'

    def run(self):
        try:
            self.download_video()
        except Exception as e:
            print(str(e))
            Dialogs.dialog(text=str(e))

    def download_video(self):
        self.exist()
        
        video = pytube.YouTube(self.url)
        
        stream1 = video.streams.filter(resolution=self.resolution, only_video=True).first()
        stream1.download(output_path=self.path, filename='video')
        
        stream2 = video.streams.get_audio_only()
        stream2.download(output_path=self.path, filename='audio')    

        videofile = os.path.join(self.path,'video.mp4')
        audiofile = os.path.join(self.path, 'audio.mp4')
        temporal = os.path.join(self.outputfile,'temporal.mp4')
        
        subprocess.run(f"ffmpeg -i \"{videofile}\" -i \"{audiofile}\" -c copy -y \"{temporal}\"")

        file  = self.outputfile + '/' + stream2.default_filename
        os.rename(temporal, file)
        os.remove(videofile)
        os.remove(audiofile)
        
    def exist(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
