@echo off
title zcFlask
call .venv/Scripts/activate.bat

set FLASK_ENV=development
flask run -h 0.0.0.0 -p 8882
pause