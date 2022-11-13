#**********************************************************************************
# content      = creates UI for Maya Tool Manager (MTM)
#
# version	   = 1.0.0
# date		   = 2022-10-13
#
# how to	   = create_ui()
# dependencies = PySide
# todos        = ...
# 
# license	   = ... (MIT)
# author	   = Enrico Vaccari <e.vaccari99@gmail.com>
#
# © ALL RIGHTS RESERVED
#**********************************************************************************


import os
import sys
import importlib as imp

import maya.cmds as cmds
# from Qt import QtWidgets, QtGui, QtCore, QtCompat

#**********************************************************************************
# VARIABLES
#**********************************************************************************


SCRIPTS_PATH = cmds.internalVar(usd=True)
MTM_PATH     = SCRIPTS_PATH + 'maya_tool_manager'

tools          = []
simple_tools   = []
ui_based_tools = []

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
# FUNCTIONS
#**********************************************************************************


def create_UI():
    
    # get tools list
    print('\n\nTOOLS LIST\n')
    tools = cf.list_tools(SCRIPTS_PATH)
    print(tools)
    print('\n')

    for tool_name in tools:
        # define object (tool) - Class Tool
        tool = cf.Tool(tool_name)
        
        # get tool path
        print('\n\n' + tool_name.upper() + ' (PATH)\n')
        tool_path = tool.path
        print('\n')

        # get tool content
        print('\n' + tool_name.upper() + ' (CONTENT)\n')
        tool_content = tool.content
        print(tool_content)
        print('\n')
 
        # validate (1) - checks if id directory exists
        print('\n' + tool_name.upper() + ' (ID_CHECK)\n')
        id_check = tc.id_check(tool_path)
        print(id_check)
        print('\n')

        # validate (2) - checks if main script exists
        print('\n' + tool_name.upper() + ' (MAIN_CHECK)\n')
        main_check = tc.main_script_check(tool_path)
        print(main_check)
        print('\n')

        # validate (3) - final check (id + main)
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

# #     for validated in checked_tools:
# #         # define object (tool) - subClass Validated
# #         checked_tool = cf.Validated(validated)

# #         # get tool type
# #         checked_tool.access_tool()

# #         # get tool type
# #         print('\n' + validated.upper() + ' (TYPE)\n')
# #         type = checked_tool.type
# #         print(type)
# #         print('\n')

# #         # classify tool
# #         print('\n' + validated.upper() + ' (CLASSIFIED)\n')
# #         checked_tool.classify()
# #         print('\n')

# #     print('\n\nSIMPLE_TOOLS\n')
# #     print(cf.simple_tools)
# #     print('\n')

# #     print('\n\nUI-BASED TOOLS\n')
# #     print(cf.ui_based_tools)
# #     print('\n')
    

create_UI()


