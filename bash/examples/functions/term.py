import sys, os, os.path
from stat import *
#
# term -- a shell function to set the terminal type interactively or not.
#
def term () 
{ 
    os.system('local t')
    
    if ($# != 0  ):
        os.system('eval  os.popen('tset -sQ sys.argv[1]').read() ')
    else:
        # interactive
        
        if (-z "" + TERM + ""  ):
            TERM="unknown"
        
        
            if ( "" + TERM + "" == 'network' or "" + TERM + "" == 'dialup' or "" + TERM + "" == 'unknown' or "" + TERM + "" == 'lat'):
                TERM=unknown
            else:
                os.system('eval  os.popen('tset -sQ').read() ')
        
        while ("" + TERM + "" == "unknown" ):
            print("Terminal type: ")
            
            t = raw_input()
            
            if (-n "" + t + ""  ):
                os.system('eval  os.popen('tset -sQ t').read() ')
}
