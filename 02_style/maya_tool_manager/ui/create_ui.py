#**********************************************************************************
# content		= creates UI for Maya Tool Manager (MTM)
#
# version		= 0.0.1
# date			= 2022-10-13
#
# how to		= create_ui()
# dependencies	= PySide
# todos         = ...
# 
# license		= ... (MIT)
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

# 3rd party API
import maya.cmds as cmds
# from Qt import QtWidgets, QtGui, QtCore, QtCompat

#**********************************************************************************
# VARIABLES
#**********************************************************************************

# constants
SCRIPTS_PATH = cmds.internalVar(usd=True)
MTM_PATH     = SCRIPTS_PATH + 'maya_tool_manager'

# variables
tools          = []
simple_tools   = []
ui_based_tools = []

# additional import
if MTM_PATH not in sys.path:
    sys.path.append(MTM_PATH)

from core import core_functions as cf

try:
    imp.reload(cf)
except:
    reload(cf)

from validate import tool_check as tc

try:
    imp.reload(tc)
except:
    reload(tc)

#**********************************************************************************
# FUNCTION DEFINITIONS
#**********************************************************************************

# THIS IS A TEST (inside the UI in the buttons)

def create_UI():
    
    # get tools list
    print('\n\nTOOLS LIST\n')
    tools = cf.list_tools(SCRIPTS_PATH)
    print(tools)
    print('\n')

    for tool_name in tools:
        # get tool path
        print('\n\n' + tool_name.upper() + ' (PATH)\n')
        tool_path = cf.get_tool_path(tool_name)
        print(tool_path)
        print('\n')

        # get tool content
        print('\n' + tool_name.upper() + ' (CONTENT)\n')
        tool_content = cf.list_tool_content(tool_path)
        print(tool_content)
        print('\n')
 
        # validate (1) - id
        print('\n' + tool_name.upper() + ' (ID_CHECK)\n')
        id_check = tc.id_check(tool_path, tool_content)
        print(id_check)
        print('\n')

        # validate (2) - main script
        print('\n' + tool_name.upper() + ' (MAIN_CHECK)\n')
        main_check = tc.main_script_check(tool_path, tool_content)
        print(main_check)
        print('\n')

        # validate (3)
        print('\n' + tool_name.upper() + ' (SUM_CHECK)\n')
        check_sum = tc.check_sum(id_check, main_check)
        print(check_sum)
        print('\n')

        # append (if valid)
        tc.append_if_valid(tool_name, check_sum)

    print('\n\nVALIDATED TOOLS\n')
    checked_tools = tc.validated_tools
    print(checked_tools)
    print('\n\n')
    
# wip

#     for ...
#     # # VALIDATE CHECK

#         access_tool

# #     # identify tool path
# #     tool_type = cf.identify_tool_type(tool_path, tool_content)
# #     print('ID content: ' + str(id_content))

# #     # classify tool
# #     cf.classify_tool(tool_name, tool_type)

# # print(cf.simple_tools)
# # print(cf.ui_based_tools)     
        

    

# # print('Simple tools list:')
# # print(simple_tools)
# # print('\n')
# # print('UI-based tools list:')
# # print(ui_based_tools)
# #     # print(identify_tool_type(tool_content))

create_UI()