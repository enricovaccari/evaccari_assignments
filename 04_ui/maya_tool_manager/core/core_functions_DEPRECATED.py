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

#**********************************************************************************
# IMPORTS
#**********************************************************************************

# Python API
import os
import sys
import importlib as imp

# 3rd party API
import maya.cmds as cmds

#******************************************************************************
# GLOBAL VARIABLES
#******************************************************************************

# constants
SCRIPTS_PATH = cmds.internalVar(usd=True)
TARGET       = "tool_type"

# variables
simple_tools  =  []
ui_based_tools = []


#******************************************************************************
# FUNCTIONS
#******************************************************************************


# LOAD ALL - tools list
def list_tools(folder_path): 
    """ Returns all the tools (directories) stored in the Maya scripts directory

    Args:
        folder_path (str): directory path target

    Returns:
        list: list of all the found items (files & directories)
    """    
    dir_list = os.listdir(folder_path)
    #  works with .encode so no need for raw strings
    
    exceptions = ["userSetup.py", 'maya_tool_manager']
    for exception in exceptions:
        if exception in dir_list:
            dir_list.remove(exception)
    
    return dir_list

# VALIDATE PREP - tool path
def get_tool_path(tool_name):
    tool_path = SCRIPTS_PATH + tool_name
    return tool_path

 # VALIDATE PREP - tool content
def list_tool_content(tool_path):
    """
    This function returns all the files/directories of a tool in the form
    of a <list> 

    Args:
        tool_path (str): directory path target (tool)

    Returns:
        list: list of all the found items (files & directories)
    """   
    tool_content = os.listdir(tool_path)
    return tool_content

# APPLY/CREATE - needs tool access for main
def access_tool(tool_path):
    if tool_path not in sys.path:
        sys.path.append(tool_path)
    # so that it doesn't append copies of the same path if already existing in sys.path
    print(sys.path)
    return

# DEFAULT CONFIGURATION
def identify_tool_type(tool_path, tool_content):
    id_path = tool_path + '/id'
    id_content = os.listdir(id_path)
    print('ID content: ' + str(id_content))
    
    for file in id_content:
        if TARGET in file:
            tool_type = file.replace('tool_type_', '')
            tool_type = tool_type.replace('.txt', '')
    
    return tool_type

def classify_tools(tool_name, tool_type):
    if tool_type == 'simple':
        simple_tools.append(tool_name)
    elif tool_type == 'UI-based':
        ui_based_tools.append(tool_name)




# THIS IS A TEST

# print(SCRIPTS_PATH)
# print('\n')
# tools = list_tools(SCRIPTS_PATH)
# print(tools)
# print('\n')
# for name in tools:
#     tool_path = get_tool_path(name) # maybe rename as tool_name but woud become same as parameter
#     print(tool_path)
#     print('\n')
#     tool_content = list_tool_content(tool_path)
#     print(tool_content)
#     print('\n')
#     access_tool(name)
#     tool_type = identify_tool_type(tool_content, tool_path)
#     if tool_type == TOOL_TYPES[0]:
#         simple_tools.append(tool_type)
#     if tool_type == TOOL_TYPES[1]:
#         ui_based_tools.append(tool_type)
        

    

# print('Simple tools list:')
# print(simple_tools)
# print('\n')
# print('UI-based tools list:')
# print(ui_based_tools)
#     # print(identify_tool_type(tool_content))

