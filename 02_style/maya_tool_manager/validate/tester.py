#******************************************************************************
# content		= ...
#
# version		= 0.0.0
# date			= 00/00/0000
#
# how to		= ...
# dependencies	= ...
# todos         = ...
# 
# license		= (e.g. MIT)
# author		= Enrico Vaccari <e.vaccari99@gmail.com>
#
# © ALL RIGHTS RESERVED
#******************************************************************************

#******************************************************************************
# 1) IMPORT MODULES
#******************************************************************************

# System Modules
import os
import sys

import maya.cmds as cmds
import webbrowser as wb


#******************************************************************************
# GLOBAL VARIABLES
#******************************************************************************

# constants
SCRIPTS_PATH = cmds.internalVar(usd=True)
TOOL_PATH = SCRIPTS_PATH + '/maya_tool_manager'
UTILITIES_PATH = TOOL_PATH + '/utilities'
ID_TARGETS = ['tool_type', 'short_name']

# print(SCRIPTS_PATH)
# print(TOOL_PATH)

# additional import
sys.path.append(UTILITIES_PATH)
import popup_functions

# #******************************************************************************
# # FUNCTION DEFINITIONS
# #******************************************************************************

def id_check(tool_path, tool_content):
    check      = 1 
    id_path    = tool_path + '/id'
    id_content = os.listdir(id_path)
    tool_name  = os.path.splitext(os.path.basename(tool_path))[0]

    # checks if id directory for given tool exists
    if not os.path.isdir(id_path):
        title   = 'ID CHECK POPUP WINDOW (missing directory)'
        message = r'WAIT! The following tool: "' + tool_name + '" has currently no id directory, therefore it will be skipped.' 
        result  = popup_functions.id_check_popup(title, message)
        if result == 'HELP':
            pass
            # wb.open('https://docs.google.com/document/d/1AHmaFD_qosOqqG81MAYirCgxqoIhbEo-aBSHvFlNBM4/edit?usp=sharing')
        check = 0

    # checks if tool_type.txt file exists
    for file in id_content:
        if ID_TARGETS[0] not in file:
            title   = 'ID CHECK POPUP WINDOW (missing file)'
            message = r'WAIT! The following tool: "' + tool_name + '" has currently no tool_type.txt file, therefore it will be skipped.' 
            result  = popup_functions.id_check_popup(title, message)
            if result == 'HELP':
                pass
                # wb.open('https://docs.google.com/document/d/1AHmaFD_qosOqqG81MAYirCgxqoIhbEo-aBSHvFlNBM4/edit?usp=sharing')
            check = 0

    # checks if short_name.txt file exists
    for file in id_content:
        if ID_TARGETS[1] not in file:
            title   = 'ID CHECK POPUP WINDOW (missing file)'
            message = r'WAIT! The following tool: "' + tool_name + '" has currently no short_name.txt file, therefore it will be skipped.' 
            result  = popup_functions.id_check_popup(title, message)
            if result == 'HELP':
                print('HELP')
                # wb.open('https://docs.google.com/document/d/1AHmaFD_qosOqqG81MAYirCgxqoIhbEo-aBSHvFlNBM4/edit?usp=sharing')
            check = 0
    
    return check
        
tool_path = 'C:/Users/Vaccari/Documents/maya/2022/scripts\evaccari_automatic_texture_plugger'
tool_content = os.listdir('C:/Users/Vaccari/Documents/maya/2022/scripts/evaccari_automatic_texture_plugger')
result = id_check(tool_path, tool_content)
print(result)

