import sys, os, os.path
from stat import *
# prompt.bash
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created: 1992-01-15
# Public domain
# $Id: prompt.bash,v 1.2 1994/10/18 16:34:35 friedman Exp $
# Commentary:
# Code:
#:docstring prompt:
# Usage: prompt [chars]
#
# Various preformatted prompt strings selected by argument.  For a
# list of available arguments and corresponding formats, do 
# `type prompt'. 
#:end docstring:
###;;;autoload
def prompt () 
{ 
    
        if ( "" + sys.argv[1] + "" == 'd'):
            PS1=' os.popen('dirs').read()  \$ '
        elif ("" + sys.argv[1] + "" == 'n'):
            PS1='\$ '
        elif ("" + sys.argv[1] + "" == 'hsw'):
            PS1='\h[SHLVL]: \w \$ '
        elif ("" + sys.argv[1] + "" == 'hw'):
            PS1='\h: \w \$ '
        elif ("" + sys.argv[1] + "" == 'sh'):
            PS1='[SHLVL] \h\$ '
        elif ("" + sys.argv[1] + "" == 'sw'):
            PS1='[SHLVL] \w \$ '
        elif ("" + sys.argv[1] + "" == 'uh'):
            PS1='\u@\h\$ '
        elif ("" + sys.argv[1] + "" == 'uhsHw'):
            PS1='\u@\h[SHLVL]:\#: \w \$ '
        elif ("" + sys.argv[1] + "" == 'uhsw'):
            PS1='\u@\h[SHLVL]: \w \$ '
        elif ("" + sys.argv[1] + "" == 'uhw'):
            PS1='\u@\h: \w \$ '
        elif ("" + sys.argv[1] + "" == 'uw'):
            PS1='(\u) \w \$ '
        elif ("" + sys.argv[1] + "" == 'w'):
            PS1='\w \$ '
}
os.system('provide prompt')
# prompt.bash ends here
