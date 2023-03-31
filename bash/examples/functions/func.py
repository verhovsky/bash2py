import sys, os, os.path
from stat import *
#
# func -- print out definitions for functions named by arguments
#
# usage: func name [name ...]
#
# Chet Ramey
# chet@ins.CWRU.Edu
def func () 
{ 
    os.system('local status=0')
    
    if ($# == 0  ):
        print("usage: func name [name...]")1>&2
        
        os.system('return 1')
    
    for f in ["" + $ + "@"]:
            if ("" + $ + "(builtin type -type " + f + ")" != "function"  ):
            print("func: " + f + ": not a function")1>&2
            
            status=1
            
            # one failed
            
            continue
        
        os.system('builtin type f') | os.system('sed 1d')
    
    os.system('return status')
}
