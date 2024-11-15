@echo off
:: Batch script to run FauxPay in the current directory

set SCRIPT_NAME=FauxPay.py

if exist %SCRIPT_NAME% (
    echo Running FauxPay...
    python %SCRIPT_NAME%
) else (
    echo Error: %SCRIPT_NAME% not found in the current directory.
    pause
)

pause