import sys, os, os.path
from stat import *
#
# whatis -- and implementation of the 10th Edition Unix sh builtin `whatis'
#	    command.
#
# usage: whatis arg [...]
#
# For each argument, whatis prints the associated value as a parameter,
# builtin, function, alias, or executable file as appropriate.  In each
# case, the value is printed in a form which would yield the same value
# if typed as input to the shell itself.
#
def whatis () 
{ 
    os.system('local wusage='usage: whatis arg [arg...]'')
    
    os.system('local fail=0')
    
    if ($# == 0  ):
        print("" + wusage + "")
        
        os.system('return 1')
    
    for arg in ["" + $ + "@"]:
            
            if (  os.popen('builtin type -type arg 2>/dev/null').read()  == '"alias"'):
                os.system('builtin alias "" + arg + ""')
            elif ( os.popen('builtin type -type arg 2>/dev/null').read()  == '"function"'):
                os.system('builtin type "" + arg + ""') | os.system('sed 1d')
            elif ( os.popen('builtin type -type arg 2>/dev/null').read()  == '"builtin"'):
                print("builtin "" + arg + """)
            elif ( os.popen('builtin type -type arg 2>/dev/null').read()  == '"file"'):
                os.system('builtin type -path "" + arg + ""')
            else:
                # OK, we could have a variable, or we could have nada
                
                if ("" + $ + "(eval echo \" + $ + "{" + arg + "+set})" == "set"  ):
                    # It is a variable, and it is set
                    
                    print("" + arg + "=")
                    
                    os.system('eval print '\"'\" + $ + "" + arg + "'\"'')
                else:
                    print("whatis: arg: not found")
                    
                    fail=1
    
    os.system('return fail')
}
