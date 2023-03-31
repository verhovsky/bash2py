import sys, os, os.path
from stat import *
##
# Destroy credentials
##
if (-z "" + $ + "{TERM_PROGRAM}"  ):
    # Don't run these commands if the shell is launched by Terminal,
    # even if it's a login shell.
    if (os.system('klist -s') ):
        os.system('kdestroy')
