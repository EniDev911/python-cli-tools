@echo off
title compiler

IF EXIST "main_.py" (

	echo compaling program...
	python -m pip install pyinstaller
	pyinstaller --onefile --icon=assets\app.ico main.py
	cls
	echo finish...

) ELSE (
	echo You must have a main.py file to compile.
)

echo Press to continue...
pause>nul
