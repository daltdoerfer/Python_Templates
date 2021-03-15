:: Diese Pragramm wurde von Denis Altdörfer geschrieben und wird dazu verwendet die Firmware des ESP8266 zu flashen

::Kommandozeilen nicht anzeigen
@echo off

::Hier werden die Laufwerke und Pfade gesetzt
set python_path="E:\Python38-64\python.exe"
set "decrypt_script_path=C:\Users\James\Desktop\Batch Dateien\Python Firefox Decrypt"
set decrypt_exe="%decrypt_script_path%\firefox_decrypt.py"
set dir_target_csv="C:\Users\James\Desktop"
e:
cd /d %python_path%

echo Ausgabe zur Kontrolle:
echo PATH: %decrypt_exe%
echo PATH: %python_path%


::Eingabe d für löschen und f für flashen
set /p eingabe=Enter [r] to show Password or [s] for save Password:


::Abfrage der Eingabe
if /i %eingabe%==y (
call :Read_Password
exit
)
if /i %eingabe%==n (
call :Abortion
exit
)


::--------------------------------------------------------
:: Funktion
::--------------------------------------------------------

:Read_Password
echo.
echo Read Password from Firefox and change format to CSV
::echo %cd%
echo %python_path% %decrypt_exe% -f csv
%python_path% %decrypt_exe% -f csv
echo

pause
::goto :EOF

:Abortion
echo.
echo Read Password from Firefox and save to CSV
echo %python_path% %decrypt_exe% -f csv > %dir_target_csv%
%python_path% %decrypt_exe% -f csv > %dir_target_csv%
echo

pause
::goto :EOF
