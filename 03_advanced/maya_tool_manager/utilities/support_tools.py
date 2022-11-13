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
    YAML_PATH = f'{MTM_PATH}/lib/extern'
    if YAML_PATH not in sys.path:
        sys.path.append(YAML_PATH)
    import yaml


#**********************************************************************************
# FUNCTIONS
#**********************************************************************************

# decorator
def print_process(func):
    def wrapper(*args, **kwargs):
        
        print(f'\nSTART - {func.__name__}')
        start_time = time.time()
        
        if args: # if funct takes args
            func(args)
        else:
            func() # if funct takes no args

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'END - {round(elapsed_time, 1)}\n')
                        
    return wrapper
'''
def init_yaml(path):
   if not os.path.exists(path):
      user_data = []
      with open(path, 'w') as outfile:
         yaml.dump(user_data, outfile, default_flow_style=False, allow_unicode=True)

init_yaml(r'C:\Users\Vaccari\Documents\maya\2022\scripts\maya_tool_manager\validate\temp\test.yml')
'''

def display_loaded(dir_list):
    tools_number = len(dir_list)
    if tools_number == 0:
      title = ''
      pf.general_warning(title, message)
    else:
        return f'-{tools_number} Loaded'

def display_validated(dir_list):
    tools_number = len(dir_list)
    if tools_number == 0:
        return f'{SCRIPTS_PATH} is currently empty'
    else:
        return f'-{tools_number} Loaded'