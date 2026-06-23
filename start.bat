@echo off
echo ========================================
echo Pink Lightning Set List Generator
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
	echo Creating virtual environment...
	python -m venv venv
	echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
if not exist "venv\Lib\site-packages\flask\" (
	echo Installing dependencies...
	pip install -r requirements.txt
	echo.
)

REM Initialize database
if not exist "pinklightning.db" (
	echo Initializing database...
	python init_db.py
	echo.
)

REM Start the app
echo Starting Pink Lightning Set List Generator...
echo.
echo Open your browser to: http://localhost:5000
echo Login: pinklightning / gottohave100
echo.
echo Press CTRL+C to stop the server
echo.
python app.py
