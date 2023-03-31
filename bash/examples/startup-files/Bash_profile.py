import sys, os, os.path
from stat import *
# Startup file for bash login shells.
#
default_dir=/usr/local/lib/
if (-n "" + PS1 + ""  ):
    PS1='\u@\h(\#)\$ '
    IGNOREEOF=3
LOGIN_SHELL=true
# If the user has her own init file, then use that one, else use the
# canonical one.
if (os.path.isfile(~/.bashrc ) ):
    os.system('. ~/.bashrc')
else:
    if (os.path.isfile(${default_dir}Bashrc ) ):
        os.system('. ${default_dir}Bashrc')
