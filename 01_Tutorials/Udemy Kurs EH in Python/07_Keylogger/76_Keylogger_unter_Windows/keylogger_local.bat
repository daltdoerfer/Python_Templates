:: Diese Pragramm wurde von Denis Altdörfer geschrieben und wird dazu verwendet ein Python Skript in Windows zu starten
:: Achtung die Module müssen im Python Interpreter installiert sein

::Kommandozeilen nicht anzeigen
@echo off

::Hier werden die Laufwerke und Pfade gesetzt
set python_path="E:\Python38-64\pythonw.exe"
set script_exe="%cd%\keylogger_local.py"


echo Ausgabe zur Kontrolle:
echo PATH: %script_exe%
echo PATH: %python_path%


::--------------------------------------------------------
:: Funktion
::--------------------------------------------------------
echo.
echo %python_path% %script_exe% 
%python_path% %script_exe% 
echo. 

pause

