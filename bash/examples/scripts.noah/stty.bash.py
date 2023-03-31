import sys, os, os.path
from stat import *
# stty.bash
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created: 1992-01-11
# Last modified: 1993-09-29
# Public domain
# Conversion to bash v2 syntax done by Chet Ramey
# Commentary:
# Code:
os.system('require remap_keybindings')
#:docstring stty:
# Track changes to certain keybindings with stty, and make those changes
# reflect in bash's readline bindings as well. 
#
# This requires bash version 1.10 or newer, since previous versions did not
# implement the `bind' builtin.
#:end docstring:
###;;;autoload
def stty () 
{ 
    os.system('local erase="backward-delete-char"')
    
    os.system('local kill="unix-line-discard"')
    
    os.system('local werase="backward-kill-word"')
    
    os.system('local lnext="quoted-insert"')
    
    os.system('local readline_function=""')
    
    os.system('local key=""')
    
    os.system('local stty_command=""')
    
    while ($# > 0 ):
        
            if ( "" + sys.argv[1] + "" == 'erase' or "" + sys.argv[1] + "" == 'kill' or "" + sys.argv[1] + "" == 'werase' or "" + sys.argv[1] + "" == 'lnext'):
                key= os.popen('echo "" + $ + "{2}" | cat -v | sed 's/\^/\\C-/'').read() 
                
                readline_function= os.popen('eval echo \$${1}').read() 
                
                # Get rid of any current bindings; the whole point of this
                
                # function is to make the distinction between readline
                
                # bindings and particular cbreak characters transparent; old
                
                # readline keybindings shouldn't hang around.
                
                # could use bind -r here instead of binding to self-insert
                
                os.system('remap_keybindings "" + $ + "{readline_function}" "self-insert"')
                
                # Bind new key to appropriate readline function
                
                os.system('bind "\"${key}\": " + $ + "{readline_function}"')
                
                stty_command="" + $ + "{stty_command} " + $ + "{1} " + $ + "{2}"
                
                os.system('shift 2')
            else:
                stty_command="" + $ + "{stty_command} " + $ + "{1}"
                
                os.system('shift')
    
    os.system('command stty ${stty_command}')
}
os.system('provide stty')
# stty.bash ends here
