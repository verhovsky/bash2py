import sys, os, os.path
from stat import *
#
# ksh-like `cd': cd [-LP] [dir [change]]
#
def cd () 
{ 
    OPTIND=1
    
    while (os.system('getopts "LP" opt')):
        
            if ( opt == 'L' or opt == 'P'):
                CDOPTS="" + CDOPTS + " -" + opt + ""
            else:
                print("" + FUNCNAME + ": usage: " + FUNCNAME + " [-LP] [dir] [change]")1>&2
                
                os.system('return 2')
    
    os.system('shift ( OPTIND - 1 )')
    
    
        if ( $# == '0'):
            os.system('builtin cd CDOPTS "" + HOME + ""')
        elif ($# == '1'):
            os.system('builtin cd CDOPTS "" + $ + "@"')
        elif ($# == '2'):
            old="" + sys.argv[1] + "" new="" + sys.argv[2] + ""
            
            
                elif ("" + PWD + "" == '*$old*'):

                else:
                    print("" + $ + "{0##*/}: " + FUNCNAME + ": bad substitution")1>&2
                    
                    os.system('return 1')
            
            dir=${PWD//old/new}
            
            os.system('builtin cd CDOPTS "" + dir + ""') && print("" + PWD + "")
        else:
            print("" + $ + "{0##*/}: " + FUNCNAME + ": usage: " + FUNCNAME + " [-LP] [dir] [change]")1>&2
            
            os.system('return 2')
}
