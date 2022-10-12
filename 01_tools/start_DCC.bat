:: MAYA VERSION
set "MAYA_VERSION=2022"

:: --- PYTHONPATH ---
set "PROJECT_ROOT=C:/Users/Vaccari/Desktop/shell"
set "PYTHONPATH=%PROJECT_ROOT%"

:: START MAYA
set "MAYA_DIR=C:/Program Files/Autodesk/Maya%MAYA_VERSION%"
set  "PATH=%MAYA_DIR%/bin"
start "" "%PATH%/maya.exe"