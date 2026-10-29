@echo off
setlocal
cd /d "%~dp0\.."
set "ROOT=%CD%"

echo Starting Namma Trip Karnataka...

if not exist "%ROOT%\.venv\Scripts\python.exe" (
    echo ERROR: Python virtual environment not found.
    pause
    exit /b 1
)

start "Namma Trip Backend" /D "%ROOT%" "%ROOT%\.venv\Scripts\python.exe" -m uvicorn backend.main:app --host 127.0.0.1 --port 8000

start "Namma Trip Frontend" /D "%ROOT%\frontend" "%ROOT%\.venv\Scripts\python.exe" -m http.server 5500

timeout /t 3 /nobreak >nul
start "" "http://127.0.0.1:5500"

endlocal
