#**********************************************************************************
# content		= main script that runs the application
#
# version		= 0.0.1
# date			= 27-10-2022
#
# how to		= id_check(tool_path, tool_content)
# dependencies	= ...
# todos         = ...
# 
# license		= ...
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

#**********************************************************************************
#  VARIABLES
#**********************************************************************************

# constants
SCRIPTS_PATH = cmds.internalVar(usd=True)

# wip
