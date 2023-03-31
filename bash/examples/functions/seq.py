import sys, os, os.path
from stat import *
# Generate a sequence from m to n, m defaults to 1.
def seq () 
{ 
    os.system('declare -i lo hi i')
    
    # makes local
    
    os.system('local _SEQ')
    
    
        if ( $# == '1'):
            os.system('seq 1 "" + sys.argv[1] + ""')
            
            os.system('return $?')
        elif ($# == '2'):
            lo=sys.argv[1] hi=sys.argv[2]
            
            i=lo _SEQ=""
            
            while ("i <= hi"):
                _SEQ="" + $ + "{_SEQ}" + i + " "
                
                i+=1
            
            print("" + $ + "{_SEQ# }")
            
            os.system('return 0')
        else:
            print("seq: usage: seq [low] high")1>&2
            
            os.system('return 2')
}
# like the APL `iota' function (or at least how I remember it :-)
def iota () 
{ 
    
        if ( $# == '1'):
            os.system('seq 1 "" + sys.argv[1] + ""')
            
            os.system('return $?')
        else:
            print("iota: usage: iota high")1>&2
            
            os.system('return 2')
}
