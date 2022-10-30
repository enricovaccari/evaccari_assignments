import maya.cmds as cmds

def check_popup(title, message): # set them to None
   result = cmds.confirmDialog(t=title, m=message, b=['GOT IT!', 'CLOSE', 'HELP'], icn = 'warning', cb = 'CLOSE', ds = 'GOT IT!', ma='center', bgc = [0.80, 0.58, 0.00])
   return result

