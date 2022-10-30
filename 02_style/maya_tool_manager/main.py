#******************************************************************************
# content         = identifies all the existing applications in the "scripts"
#                   of your installed Maya package
#
# creation date   = 13/10/2022 
#
# author          = Enrico Vaccari <e.vaccari99@gmail.com>
#
# © ALL RIGHTS RESERVED
#******************************************************************************

#******************************************************************************
# 1) IMPORT MODULES
#******************************************************************************



# System Modules
import os
import sys



# DCC Modules (Maya)
import maya.cmds as cmds 

import importlib as imp



#******************************************************************************
# GLOBAL VARIABLES
#******************************************************************************

# constants
SCRIPTS_PATH = cmds.internalVar(usd=True)

os.chdir(SCRIPTS_PATH)
print(os.getcwd())

# # THIS IS A TEST

# print(SCRIPTS_PATH)
# print('\n')
# tools = core_functions.list_tools(SCRIPTS_PATH)
# print(tools)
# print('\n')

# # for name in tools:
# #     tool_path = get_tool_path(name) # maybe rename as tool_name but woud become same as parameter
# #     print(tool_path)
# #     print('\n')
# #     tool_content = list_tool_content(tool_path)
# #     print(tool_content)
# #     print('\n')
# #     access_tool(name)
# #     tool_type = identify_tool_type(tool_content, tool_path)
# #     if tool_type == TOOL_TYPES[0]:
# #         simple_tools.append(tool_type)
# #     if tool_type == TOOL_TYPES[1]:
# #         ui_based_tools.append(tool_type)
        

    

# # print('Simple tools list:')
# # print(simple_tools)
# # print('\n')
# # print('UI-based tools list:')
# # print(ui_based_tools)
# #     # print(identify_tool_type(tool_content))

# '''