import sys, os, os.path
from stat import *
os.system('trap _notify CHLD')
NOTIFY_ALL=false
os.system('unset NOTIFY_LIST')
os.system('unalias false')
def false () 
{ 
    os.system('return 1')
}
def _notify () 
{ 
    os.system('local i j')
    
    os.system('local newlist=')
    
    if (os.system('NOTIFY_ALL') ):
        os.system('return')
        
        # let bash take care of this itself
    else:
        if (-z "" + NOTIFY_LIST + ""  ):
            os.system('return')
        else:
            os.system('set -- NOTIFY_LIST')
            
            for i in ["" + $ + "@"]:
                            j= os.popen('jobs -n %i').read() 
                
                if (-n "" + j + ""  ):
                    print("" + j + "")
                    
                    os.system('jobs -n %i> /dev/null')
                else:
                    newlist="newlist " + i + ""
            
            NOTIFY_LIST="" + newlist + ""
}
def notify () 
{ 
    os.system('local i j')
    
    if ($# == 0  ):
        NOTIFY_ALL=:
        
        os.system('set -b')
        
        os.system('return')
    else:
        for i in ["" + $ + "@"]:
                    # turn a valid job spec into a job number
            
            j= os.popen('jobs i').read() 
            
            
                if ( "" + j + "" == '[*'):
                    j=${j%%]*}
                    
                    j=${j#[}
                    
                    NOTIFY_LIST="" + NOTIFY_LIST + " " + j + ""
}
