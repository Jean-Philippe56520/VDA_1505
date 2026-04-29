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

    echo [INFO] Installation des dependances...
    call ".venv\Scripts\python.exe" -m pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERREUR] Echec de l'installation des dependances.
        pause
        exit /b 1
    )
)

echo [INFO] Lancement de Streamlit...
call ".venv\Scripts\python.exe" -m streamlit run app.py

pause
endlocal