import sys, os, os.path
from stat import *
# To: chet@ins.CWRU.Edu
# Subject: Bash functions
# From: Sandeep Mehta <sxm@philabs.Philips.Com>
##########################################
#
# repeat - clone of C shell builtin `repeat'
#
# usage: repeat <count> <command>
#
# It has been tested inside other functions and in conditionals like 
# if [ "`repeat <count> <command>`" ]; then COMMANDS [ else COMMANDS ] fi
# Please send me fixes/enhancements.
# 
# Sandeep Mehta <sxm@philabs.Philips.Com>
##########################################
def repeat () 
{ 
    os.system('local rcount=sys.argv[1]')
    
    if ($# < 1  || -z "" + rcount + ""  ):
        print("usage: repeat <count> <command>")1>&2
        
        os.system('return 2')
    
    os.system('shift')
    
    os.system('local acmd=("" + $ + "@")')
    
    if (rcount < 0  ):
        print("count must be greater than 0")
        
        print("usage: repeat <count> <command>")1>&2
        
        os.system('return 2')
    
    st=0
    
    while (rcount > 0 ):
        os.system('eval "" + $ + "{acmd[@]}"')
        
        st=$?
        
        rcount=(rcount - 1)
    
    os.system('return st')
}
