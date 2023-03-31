import sys, os, os.path
from stat import *
##
# Bash
# User preferences file
# Override these in rc.mine
#
# Wilfredo Sanchez Jr. | tritan@mit.edu
# July 09, 1992
#
# MIT Project Athena
##
if (-n "" + PS1 + ""  ):
    # Prompts
    PS1='[\h:\w] \u\$ '
    PS2=' -> '
    #PS3=
    #PS4=
    os.system('set -o emacs')
