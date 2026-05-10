@echo off
REM === Vai nella cartella in cui si trova questo script ===
cd /d "%~dp0"

REM === Prima sincronizza GitHub con il PC ===
git pull --rebase origin main

REM === Se il pull fallisce, prova a tenere la versione locale del glossario ===
IF ERRORLEVEL 1 (
    echo Conflitto rilevato. Tengo la versione locale di glossary.html...
    git checkout --ours glossary.html
    git add glossary.html
    git rebase --continue
)

REM === Genera glossary.html ===
python generate_glossary_html.py

REM === Aggiungi i file aggiornati ===
git add SonoVerse.xlsx glossary.html update_and_publish_glossary.bat

REM === Fai commit solo se necessario ===
git commit -m "Aggiorna Excel e HTML" || echo Nessuna modifica rilevante trovata

REM === Sincronizza di nuovo prima del push ===
git pull --rebase origin main

IF ERRORLEVEL 1 (
    echo Conflitto rilevato. Tengo la versione locale di glossary.html...
    git checkout --ours glossary.html
    git add glossary.html
    git rebase --continue
)

REM === Esegui push ===
git push origin main

REM === Apri glossario in locale ===
start glossary.html

pause