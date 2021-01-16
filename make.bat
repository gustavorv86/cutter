@echo off

set PROGNAME=cutter

python --version
if %errorlevel% neq 0 (
	echo ERROR: Python platform not installed. Download a install python first.
	echo https://www.python.org/downloads/
	pause
	exit 1
)

pyinstaller -v
if %errorlevel% neq 0 (
	echo ERROR: PyInstaller not found. Execute 'pip3 install pyinstaller' first.
	pause
	exit 1
)

pyinstaller --name=%PROGNAME% --log-level=INFO --onefile --console __main__.py
pause

