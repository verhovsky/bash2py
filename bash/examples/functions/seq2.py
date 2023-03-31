import sys, os, os.path
from stat import *
# Generate a sequence from m to n, m defaults to 1.
def seq () 
{ 
    os.system('declare -i lo hi i')
    
    # makes local
    
    os.system('local _SEQ INIT COMPARE STEP')
    
    
        if ( "" + sys.argv[1] + "" == '-r'):
            INIT='i=hi _SEQ=""' COMPARE='let "i >= " + lo + ""' STEP='let i-=1'
            
            os.system('shift')
        else:
            INIT='i=lo _SEQ=""' COMPARE='let "i <= " + hi + ""' STEP='let i+=1'
    
    
        if ( $# == '1'):
            lo=1 hi="" + sys.argv[1] + ""
        elif ($# == '2'):
            lo=sys.argv[1] hi=sys.argv[2]
        else:
            print("seq: usage: seq [-r] [low] high")1>&2
            
            os.system('return 2')
    
    # equivalent to the as-yet-unimplemented
    
    # for (( "$INIT" ; "$COMPARE" ; "$STEP" )); do _SEQ="${_SEQ}$i "; done
    
    os.system('eval "" + INIT + ""')
    
    while (os.system('eval "" + COMPARE + ""')):
        _SEQ="" + $ + "{_SEQ}" + i + " "
        
        os.system('eval "" + STEP + ""')
    
    print("" + $ + "{_SEQ# }")
    
    os.system('return 0')
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
