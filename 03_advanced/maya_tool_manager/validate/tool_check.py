#**********************************************************************************
# content		= checks if tool has id/tool_type/short_name
#               = writes out data in yaml file (temp)
#
# version		= 0.0.1
# date			= 27-10-2022
#
# how to		= id_check(tool_path)
#                 main_script_check(tool_path)
#                 check_sum(id_check, main_check)
#                 append_if_valid(tool_name, check_sum)
# 
# dependencies	= ...
# todos         = ...
# 
# license		= (e.g. MIT)
# author		= Enrico Vaccari <e.vaccari99@gmail.com>
#
# © ALL RIGHTS RESERVED
#**********************************************************************************

import os
import sys
import importlib as imp
# import webbrowser as wb 

import maya.cmds as cmds


#**********************************************************************************
# VARIABLES
#**********************************************************************************


SCRIPTS_PATH    = cmds.internalVar(usd=True)
MTM_PATH        = f'{SCRIPTS_PATH}maya_tool_manager'
UTILITIES_PATH  = f'{MTM_PATH}/utilities'
VAL_TOOLS_PATH  = f'{MTM_PATH}/validate/temp'
YAML_PATH       = f'{MTM_PATH}/lib/extern'

ID_TARGETS      = ['short_name', 'tool_type']

validated_tools = []

if UTILITIES_PATH not in sys.path:
    sys.path.append(UTILITIES_PATH)

import popup_functions as pf

try:
    imp.reload(pf)
except:
    reload(pf)

try:
    import yaml
except:
    if YAML_PATH not in sys.path:
        sys.path.append(YAML_PATH)
    import yaml

yaml_file = MTM_PATH + '/config/user_config.yml'
with open(yaml_file, 'r') as stream:
    user_config = yaml.safe_load(stream)

print(user_config['general_warning']['cancelButton'])


#**********************************************************************************
# FUNCTIONS
#**********************************************************************************


# VALIDATE (1) - id dir/tool_type/short_name
def id_check(tool_path):
    """ Checks if tool has id directory and whether it contains tool_type/short_name

    Args:
        tool_path (str): full tool path

    Returns:
        int: returns 0 if tool does NOT pass the check, 1 if it does 
    """   

    #******************************************************************************
    # INITIALIZATION
    id_path    = tool_path + '/id'
    tool_name  = os.path.splitext(os.path.basename(tool_path))[0]

    #******************************************************************************
    # checks if id directory for given tool exists
    if not os.path.isdir(id_path):
        title   = 'ID CHECK POPUP WINDOW (missing directory)'
        message = f'WAIT! The following tool: {tool_name} has currently no <id> directory. Do you want to create one? If not, this tool will be skipped.' 
        # put message into yaml and use .format to add tool name
        result  = pf.check_popup(title, message)
        
        if result == 'YES':
            os.mkdir(id_path)
        elif result == 'NO':
            return 0
        elif result == 'HELP':
            print('HELP')
            # wb.open('documentation_link')
            return 0
        
    #******************************************************************************
    # if id directory exists
    id_content = os.listdir(id_path)
    id_content = sorted(id_content)
    check_name = False
    check_type = False

    for file in id_content:
        # checks if short_name.txt file exist
        if ID_TARGETS[0] in file:
            check_name = True

        # checks if tool_type.txt file exist
        elif ID_TARGETS[1] in file:
            check_type = True
    
    #******************************************************************************
    # if tool_name does NOT exist (create one?)
    title   = 'ID CHECK POPUP WINDOW (missing file)'

    if check_name == False:
        message = f'WAIT! The following tool: {tool_name} has currently no <short_name.txt> file. Do you want to create one? If not, this tool will be skipped.' 
        result  = pf.check_popup(title, message)
        
        if result == 'YES':
            try:
                suffix = str(input('Insert tool short name (Example for Auto_Rigger: AuRi)'))
                file_name = f'short_name_{suffix}.txt'
                file_path = f'{id_path}/{file_name}'
                with open(file_path, 'w') as outfile:
                    pass
            except:
                print('No name specified')
                return 0
        elif result == 'NO':
            return 0
        elif result == 'HELP':
            print('HELP')
            # wb.open('documentation_link'')
            return 0
    
    #******************************************************************************
    # if tool_type does NOT exist (create one?)
    if check_type == False:
        message = f'WAIT! The following tool: {tool_name} has currently no <tool_type.txt> file. Do you want to create one? If not, this tool will be skipped.' 
        result  = pf.check_popup(title, message)
        
        if result == 'YES':
            title = 'TOOL TYPE WINDOW (choose)'
            message = f'What is the type of {tool_name}?'
            chosen_type = pf.type_popup(title, message)
            
            if chosen_type == 'SIMPLE':
                file_name = 'tool_type_simple.txt'
                file_path = f'{id_path}/{file_name}'
                with open(file_path, 'w') as outfile:
                    pass
            elif chosen_type == 'UI-BASED':
                file_name = 'tool_type_UI-based.txt'
                file_path = f'{id_path}/{file_name}'
                with open(file_path, 'w') as outfile:
                    pass

            elif chosen_type == 'CANCEL':
                return 0

        elif result == 'NO':
            return 0
        elif result == 'HELP':
            print('HELP')
            # wb.open('insert link of Wiki')
            return 0
    
    return 1

# VALIDATE (2) - main script
def main_script_check(tool_path):
    """
    Checks if too has id directory containing tool_type and short_name

    Args:
        tool_path (str): full tool path
        tool_content (List): file/directories contained in the tool

    Returns:
        int: returns 0 if tool does NOT pass the check, 1 if it does 
    """  

    #******************************************************************************
    # INIT
    check        = 1
    tool_name    = os.path.splitext(os.path.basename(tool_path))[0]
    tool_content = os.listdir(tool_path)
    
    #******************************************************************************
    # if main module does not exist
    if "main.py" not in tool_content:
        title   = 'MAIN SCRIPT WINDOW (missing file)'
        message = f'WAIT! The following tool: {tool_name} has currently no <main.py> file. Do you want to select a target file acting as a main? If not, this tool will be skipped' 
        result  = pf.check_popup(title, message)
        
        if result == 'YES':
            main_target = pf.browse_main_target()
            return 1
            # write out in yaml
        elif result == 'NO':
            return 0
        elif result == 'HELP':
            print('HELP')
            # wb.open('insert link of Wiki')
            return 0

    return 1

def check_sum(id_check, main_check):
    check_sum = id_check + main_check
    return check_sum

# VALIDATE (3) - append to validates
def append_if_valid(tool_name, check_sum):
    if check_sum == 2:
        validated_tools.append(tool_name)
    # else returns None
    return


#**********************************************************************************
# EXECUTION
#**********************************************************************************

# id_check(tool_path)
# main_script_check(tool_path)
# check_sum(id_check, main_check)
# append_if_valid(tool_name, check_sum)