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

#******************************************************************************
# GLOBAL VARIABLES
#******************************************************************************

SCRIPT_PATH = cmds.internalVar(usd=True)


#******************************************************************************
# FUNCTION DEFINITIONS
#******************************************************************************

def list_tools(folder_path):
    """
    This function returns all the tools (directories) stored in the Maya 
    scripts directory in the form of a <list> 

    Args:
        folder_path (str): directory path target

    Returns:
        list: list of all the found items (files & directories)
    """    
    dir_list = os.listdir(folder_path)
    return dir_list

def list_tool_content(tool_path):
    """
    This function returns all the files/directories of a tool in the form
    of a <list> 

    Args:
        tool_path (str): directory path target (tool)

    Returns:
        list: list of all the found items (files & directories)
    """   
    tool_list = os.dirlist(tool_path)
    return tool_list

def access_tool(tool_name):
    sys.path.append(tool_path)


def identify_tool_type(tool_list):
    target_file = "_tool_type.py"
    tool_types = ['simple', 'UI-based', None]
    
    for item in tool_list:
        if _tool_type


# THIS IS A TEST







dir_list = list_tools(SCRIPT_PATH)
