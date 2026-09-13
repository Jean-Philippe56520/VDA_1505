@echo off
setlocal

cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo [INFO] Creation de l'environnement virtuel...
    py -m venv .venv
    if errorlevel 1 (
        echo [ERREUR] Impossible de creer l'environnement virtuel.
        pause
        exit /b 1
    )

    echo [INFO] Mise a jour de pip...
    call ".venv\Scripts\python.exe" -m pip install --upgrade pip
    if errorlevel 1 (
        echo [ERREUR] Echec de la mise a jour de pip.
        pause
        exit /b 1
    )
)

set "REQ_FILE=requirements.lock.txt"
if not exist "%REQ_FILE%" set "REQ_FILE=requirements.txt"

echo [INFO] Verification des dependances depuis %REQ_FILE%...
call ".venv\Scripts\python.exe" -m pip install -r "%REQ_FILE%"
if errorlevel 1 (
    echo [ERREUR] Echec de l'installation des dependances.
    pause
    exit /b 1
)

call ".venv\Scripts\python.exe" -m pip check
if errorlevel 1 (
    echo [ERREUR] Environnement Python incoherent.
    pause
    exit /b 1
)

echo [INFO] Lancement de Streamlit...
call ".venv\Scripts\python.exe" -m streamlit run app.py

pause
endlocal
