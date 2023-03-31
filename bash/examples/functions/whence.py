import sys, os, os.path
from stat import *
#
# An almost-ksh compatible `whence' command.  This is as hairy as it is 
# because of the desire to exactly mimic ksh.
# 
# This depends somewhat on knowing the format of the output of the bash
# `builtin type' command.
#
# Chet Ramey
# chet@ins.CWRU.Edu
#
def whence () 
{ 
    os.system('local vflag= path=')
    
    if (len(sys.argv) == "0"  ):
        print("whence: argument expected")
        
        os.system('return 1')
    
    
        if ( "" + sys.argv[1] + "" == '-v'):
            vflag=1
            
            os.system('shift 1')
        elif ("" + sys.argv[1] + "" == '-*'):
            print("whence: bad option: " + sys.argv[1] + "")
            
            os.system('return 1')
        else:

    
    if (len(sys.argv) == "0"  ):
        print("whence: bad argument count")
        
        os.system('return 1')
    
    for cmd in ["" + $ + "@"]:
            if ( "" + vflag + ""  ):
            print(" os.popen('builtin type cmd | sed 1q').read() ")
        else:
            path= os.popen('builtin type -path cmd').read() 
            
            if ( "" + path + ""  ):
                print("path")
            else:
                
                    if ( "" + cmd + "" == '/*'):
                        if (-x "" + cmd + ""  ):
                            print("" + cmd + "")
                    else:
                        
                            elif ("" + $ + "(builtin type -type " + cmd + ")" == '""'):

                            else:
                                print("" + cmd + "")
    
    os.system('return 0')
}
