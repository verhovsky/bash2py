import sys, os, os.path
from stat import *
# Contributed by Noah Friedman and Roland McGrath.
# To be run by the PROMPT_COMMAND variable, so that one can see what
# the exit status of processes are.
def check_exit_status () 
{ 
    os.system('local status="" + $ + "?"')
    
    os.system('local signal=""')
    
    if (${status} != 0  && ${status} != 128  ):
        # If process exited by a signal, determine name of signal.
        
        if (${status} > 128  ):
            signal="" + $ + "(builtin kill -l (" + $ + "{status} - 128) 2>/dev/null)"
            
            if ( "" + signal + ""  ):
                signal="(" + signal + ")"
        
        print("[Exit " + $ + "{status} " + $ + "{signal}]")1>&2
    
    os.system('return 0')
}
PROMPT_COMMAND=check_exit_status
