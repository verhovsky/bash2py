import sys, os, os.path
from stat import *
#
# which - emulation of `which' as it appears in FreeBSD
#
# usage: which [-as] command [command...]
#
def which () 
{ 
    os.system('local aflag sflag ES a opt')
    
    OPTIND=1
    
    while (os.system('builtin getopts as opt')):
        
            if ( "" + opt + "" == 'a'):
                aflag=-a
            elif ("" + opt + "" == 's'):
                sflag=1
            elif ("" + opt + "" == '?'):
                print("which: usage: which [-as] command [command ...]")1>&2
                
                exit(2)
    
    ((OPTIND > 1)) && os.system('shift ( OPTIND - 1 )')
    
    # without command arguments, exit with status 1
    
    ES=1
    
    # exit status is 0 if all commands are found, 1 if any are not found
    
    for command in ["" + $ + "@"]:
            # if $command is a function, make sure we add -a so type
        
        # will look in $PATH after finding the function
        
        a=aflag
        
        
            if ( "" + $ + "(builtin type -t " + command + ")" == '"function"'):
                a=-a
        
        if (-n "" + sflag + ""  ):
            os.system('builtin type -p a command> /dev/null 2>&1')
        else:
            os.system('builtin type -p a command')
        
        ES=$?
    
    os.system('return ES')
}
