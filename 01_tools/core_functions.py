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

# DCC Modules (Maya)
import maya.cmds as cmds 

#******************************************************************************
# 1) SECTION TITLE
#******************************************************************************

mc.commandPort(name="127.0.0.1:7002", stp="python", echoOutput=True)
mc.commandPort(name="127.0.0.1:7001", stp="mel", echoOutput=True)

b"python byte to string".decode("utf-8")
