:: --- WEEK 01 ASSIGNMENT - SHELL (02) - ENRICO VACCARI ---

@echo off
:: --- MAYA VERSION ---
set "MAYA_VERSION=2022"

:: --- PATH ---
set "PROJECT_ROOT=C:/Users/Vaccari/Desktop/Project_Test"
set "PIPELINEPATH=%PROJECT_ROOT%/dev"

:: --- PYTHONPATH ---
set "PYTHONPATH=%PROJECT_ROOT%/dev"

:: --- SHELF ---
set "MAYA_SHELF_PATH=%PIPELINEPATH%/shelf;%MAYA_SHELF_PATH%"

:: START MAYA
set "MAYA_DIR=C:/Program Files/Autodesk/Maya%MAYA_VERSION%"
set  "PATH=%MAYA_DIR%/bin"
start "" "%PATH%/maya.exe"