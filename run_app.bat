@echo off

set /p restart=refresh the environment(y/n)?

call conda activate base

if %restart%==y (goto pytube) else goto start

:start
call conda activate base
python main.py
call conda deactivate
goto finish

:pytube
echo refreshing pytube...
pip uninstall -y pytube
pip install pytube
goto start

:finish
pause
exit
