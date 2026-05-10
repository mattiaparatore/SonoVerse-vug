@echo off

REM === Vai nella cartella dello script ===
cd /d "%~dp0"

REM === Prima sincronizza con GitHub ===
git pull --rebase origin main

REM === Genera glossary.html ===
python generate_glossary_html.py

REM === Aggiungi file ===
git add SonoVerse.xlsx glossary.html

REM === Commit ===
git commit -m "Aggiorna glossary"

REM === Push ===
git push origin main

REM === Apri glossario locale ===
start glossary.html

pause