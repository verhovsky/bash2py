import sys, os, os.path
from stat import *
#
# A function that works as a front end for both stty and the `bind'
# builtin, so the tty driver and readline see the same changes
#
#
# Convert between the stty ^H control character form and the readline \C-H
# form
#
def cvt () 
{ 
    print("" + $ + "@") | os.system('cat -v') | os.system('sed 's/\^/\\C-/'')
}
#
# stty front-end.  Parses the argument list and creates two command strings,
# one for stty, another for bind.
#
def fstty () 
{ 
    os.system('local cmd="" bargs=""')
    
    os.system('local e')
    
    while ($# > 0 ):
        
            if ( "" + sys.argv[1] + "" == '-a'):
                cmd="" + cmd + " everything"
            elif ("" + sys.argv[1] + "" == 'erase'):
                os.system('shift')
                
                e= os.popen('cvt "" + sys.argv[1] + ""').read() 
                
                cmd="" + cmd + " erase " + sys.argv[1] + ""
                
                bargs="" + bargs + " '\"e\": backward-delete-char'"
            elif ("" + sys.argv[1] + "" == 'kill'):
                os.system('shift')
                
                e= os.popen('cvt "" + sys.argv[1] + ""').read() 
                
                cmd="" + cmd + " kill " + sys.argv[1] + ""
                
                bargs="" + bargs + " '\"e\": unix-line-discard'"
            elif ("" + sys.argv[1] + "" == 'werase'):
                os.system('shift')
                
                e= os.popen('cvt "" + sys.argv[1] + ""').read() 
                
                cmd="" + cmd + " erase " + sys.argv[1] + ""
                
                bargs="" + bargs + " '\"e\": backward-kill-word'"
            elif ("" + sys.argv[1] + "" == 'lnext'):
                os.system('shift')
                
                e= os.popen('cvt "" + sys.argv[1] + ""').read() 
                
                cmd="" + cmd + " erase " + sys.argv[1] + ""
                
                bargs="" + bargs + " '\"e\": quoted-insert'"
            else:
                cmd="" + cmd + " " + sys.argv[1] + ""
        
        os.system('shift')
    
    os.system('command stty cmd')
    
    if (-n "" + bargs + ""  ):
        os.system('builtin bind bargs')
}
