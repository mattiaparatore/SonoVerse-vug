@echo off
REM === Vai nella cartella in cui si trova questo script ===
cd /d "%~dp0"

REM === Genera glossary.html ===
python generate_glossary_html.py

REM === Aggiungi i file aggiornati ===
git add SonoVerse.xlsx glossary.html

REM === Fai commit solo se necessario ===
git commit -m "Aggiorna Excel e HTML" || echo ℹ️ Nessuna modifica rilevante trovata

REM === Esegui push ===
git push origin main

REM === Apri glossario in locale ===
start glossary.html
pause