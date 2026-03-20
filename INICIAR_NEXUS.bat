@echo off
title NEXUS AI - COMMAND CENTER
color 0a

echo ===================================================
echo    INICIALIZANDO NEXUS AI: OPERATIONAL SYSTEM
echo ===================================================

:: Inicia o dashboard em background
start /min cmd /c "python nexus_dashboard.py"
echo [OK] NEXUS Performance Dashboard: ONLINE

:: Inicia a Sentinela em primeiro plano
echo [OK] NEXUS Sentinel Core: EXECUTANDO...
python nexus_sentinel.py

pause