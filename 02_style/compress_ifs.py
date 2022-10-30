#STYLE*****************************************************************************
# content		= assignment (Python Advanced)
#                 assigns color to curve(s)
#
# version		= 0.0.0
# date			= 2022-01-07
#
# how to		= set_color(['circle','circle1'], 8)
# dependencies	= ...
# todos         = ...
# 
# license		= (e.g. MIT)
# author		= Alexander Richter contact@alexanderrichtertd.com
#
#**********************************************************************************

#**********************************************************************************
# IMPORT
#**********************************************************************************

# Custom API
import maya.cmds as cmds

#**********************************************************************************
# FUNCTION DEFINITIONS
#**********************************************************************************

def set_color(ctrlList=None, color=None):
    """This function assigns a color to a set of curves

    Args:
        ctrlList (list): input list of curves. Defaults to None.
        color (int): input color value. Defaults to None.
    """    
    overrides = [4, 13, 25, 17, 17, 15, 6, 16]

    for ctrlName in ctrlList:
        ctrl_override = ctrlName + 'Shape.overrideEnabled'
        ctrl_color    = ctrlName + 'Shape.overrideColor'

        try:
            cmds.setAttr(ctrl_override, 1)
        except:
            pass

        try:
            cmds.setAttr(ctrl_color, overrides[color - 1])
        except:
            pass

# EXAMPLE
# set_color(['circle','circle1'], 8)
