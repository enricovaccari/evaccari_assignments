#**********************************************************************************
# content		= checks if tool has id/tool_type/short_name
#
# version		= 0.0.1
# date			= 27-10-2022
#
# how to		= id_check(tool_path, tool_content)
# dependencies	= ...
# todos         = ...
# 
# license		= (e.g. MIT)
# author		= Enrico Vaccari <e.vaccari99@gmail.com>
#
# © ALL RIGHTS RESERVED
#**********************************************************************************

#**********************************************************************************
# IMPORTS
#**********************************************************************************
# Python API
import os
import sys
import importlib as imp
import webbrowser as wb

# 3rd party API
import maya.cmds as cmds

#**********************************************************************************
# VARIABLES
#**********************************************************************************

# constants
SCRIPTS_PATH   = cmds.internalVar(usd=True)
MTM_PATH       = SCRIPTS_PATH + 'maya_tool_manager'
UTILITIES_PATH = MTM_PATH + '/utilities'
ID_TARGETS     = ['tool_type', 'short_name']


#variables
validated_tools = []

# print(SCRIPTS_PATH)
# print(MTM_PATH)
# print(UTILITIES_PATH)

# additional import
if UTILITIES_PATH not in sys.path:
    sys.path.append(UTILITIES_PATH)
import popup_functions

print(sys.path)

#**********************************************************************************
# FUNCTION DEFINITIONS
#**********************************************************************************

# VALIDATE (1) - id check/tool type/short name
def id_check(tool_path, tool_content):
    """
    Checks if too has id directory containing tool_type and short_name

    Args:
        tool_path (str): full tool path
        tool_content (List): file/directories contained in the tool

    Returns:
        int: returns 0 if tool does NOT pass the check, 1 if it does 
    """    
    check      = 1
    id_path    = tool_path + '/id'
    id_content = os.listdir(id_path)
    print(id_content)
    tool_name  = os.path.splitext(os.path.basename(tool_path))[0]

    # checks if id directory for given tool exists
    if not os.path.isdir(id_path):
        title   = 'ID CHECK POPUP WINDOW (missing directory)'
        message = r'WAIT! The following tool: "' + tool_name + '" has currently no id directory, therefore it will be skipped.' 
        result  = popup_functions.check_popup(title, message)
        if result == 'HELP':
            print('HELP')
            # wb.open('https://docs.google.com/document/d/1AHmaFD_qosOqqG81MAYirCgxqoIhbEo-aBSHvFlNBM4/edit?usp=sharing')
        check = 0
        return check

    check_type = 1
    check_name = 1
    
    for file in id_content:
        # checks if tool_type.txt file exist
        if ID_TARGETS[0] not in file:
            check_type = 0

        # checks if short_name.txt file exist
        if ID_TARGETS[1] not in file:
            check_name = 0

    if check_type == 0:
        title   = 'ID CHECK POPUP WINDOW (missing file)'
        message = r'WAIT! The following tool: "' + tool_name + '" has currently no tool_type.txt file, therefore it will be skipped.' 
        result  = popup_functions.check_popup(title, message)
        
        if result == 'HELP':
            print('HELP')
            # wb.open('https://docs.google.com/document/d/1AHmaFD_qosOqqG81MAYirCgxqoIhbEo-aBSHvFlNBM4/edit?usp=sharing')
    
    if check_name == 0:
        title   = 'ID CHECK POPUP WINDOW (missing file)'
        message = r'WAIT! The following tool: "' + tool_name + '" has currently no short_name.txt file, therefore it will be skipped.' 
        result  = popup_functions.check_popup(title, message)
        
        if result == 'HELP':
            print('HELP')
            # wb.open('https://docs.google.com/document/d/1AHmaFD_qosOqqG81MAYirCgxqoIhbEo-aBSHvFlNBM4/edit?usp=sharing')
    
    check = check_type * check_name
    
    return check

# VALIDATE (2) - main script
def main_script_check(tool_path, tool_content):
        """
    Checks if too has id directory containing tool_type and short_name

    Args:
        tool_path (str): full tool path
        tool_content (List): file/directories contained in the tool

    Returns:
        int: returns 0 if tool does NOT pass the check, 1 if it does 
    """  
    check      = 1
    tool_name  = os.path.splitext(os.path.basename(tool_path))[0]

    if "main.py" not in tool_content:
        title   = 'MAIN SCRIPT WINDOW (missing file)'
        message = r'WAIT! The following tool: "' + tool_name + '" has currently no main.py file, therefore it will be skipped.' 
        result  = popup_functions.check_popup(title, message)
        if result == 'HELP':
                print('HELP')
                # wb.open('https://docs.google.com/document/d/1AHmaFD_qosOqqG81MAYirCgxqoIhbEo-aBSHvFlNBM4/edit?usp=sharing')
        check = 0

    return check

def check_sum(id_check, main_check):
    check_sum = id_check + main_check
    return check_sum
# VALIDATE (3) - append to validates
def append_if_valid(tool_name, check_sum):
    if check_sum == 2:
        validated_tools.append(tool_name)
    return



id_check(SCRIPTS_PATH + 'evaccari_automatic_texture_plugger', [id])



