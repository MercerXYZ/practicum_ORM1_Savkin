@echo off
if not exist "venv" python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt --quiet
python -m flask --debug run
pause