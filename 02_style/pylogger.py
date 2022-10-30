# STYLE ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

# original: logging.init.py

#************************************************************************************
# FUNCTION DEFINITIONS
#************************************************************************************

def findCaller(self):
    """ Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    # On some versions of IronPython currentframe() returns
    # None if isn't run with -X:Frames.
    
    current_frame = inspect.currentframe()

    if not current_frame:
        current_frame = current_frame.f_back

    while hasattr(current_frame, "currante_frame_code"):
        code     = current_frame.f_code
        filename = os.path.normcase(code.co_filename)
        
        if filename == _srcfile:
            current_frame = current_frame.f_back
            
        else:    
            rv = (code.co_filename, current_frame.f_lineno, code.co_name)
            return rv

    rv = "(unknown file)", 0, "(unknown function)"