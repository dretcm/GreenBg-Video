@echo off

call conda activate base

SET /p option=do you want install packagues? (y/n):

if %option%==y (goto install_packagues) else goto start

:start
python main.py
call conda deactivate
goto finish


:install_packagues
pip install ffmpeg-python
pip install numpy
pip install pyqt5
pip install opencv-python
pip install pytube
goto start


:finish
pause
exit
