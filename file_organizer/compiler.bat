@echo off
title compiler
echo compaling program...
python -m pip install pyinstaller
pyinstaller --onefile --icon=assets\app.ico main.py
cls
echo finish
echo Press to continue...
pause>nul