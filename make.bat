@echo off

set PROGNAME=cutter

echo.
echo Check Python version:
python --version
if %errorlevel% neq 0 (
	echo ERROR: Python platform not installed. Download a install python first.
	echo https://www.python.org/downloads/
	pause
	exit 1
)

echo.
echo Check PyInstaller version:
pyinstaller -v
if %errorlevel% neq 0 (
	echo ERROR: PyInstaller not found. Execute 'pip3 install pyinstaller' first.
	pause
	exit 1
)

echo.
mkdir build 1> nul 2> nul
cd build
pyinstaller --name=%PROGNAME% --log-level=INFO --onefile --console ..\main.py

echo.
pause
