@echo off

:: Finds the absolute path of the script
set SCRIPT_DIR=%~dp0
set PROJECT_ROOT=%SCRIPT_DIR%..\..

:: Hook paths
set HOOKS_SRC=%PROJECT_ROOT%\scripts\git-hooks\hooks
set HOOKS_DEST=%PROJECT_ROOT%\.git\hooks

:: Creates the .git\hooks folder if it does not exist
if not exist "%HOOKS_DEST%" mkdir "%HOOKS_DEST%"

:: Copy batch hooks
copy "%HOOKS_SRC%\*.bat" "%HOOKS_DEST%\"

:: Copy shell hooks (if Git Bash is used)
copy "%HOOKS_SRC%\*" "%HOOKS_DEST%\"

echo Done.
