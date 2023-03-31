import sys, os, os.path
from stat import *
# Sort the positional paramters.
# Make sure the positional parameters are passed as arguments to the function.
# If -u is the first arg, remove duplicate array members.
def sort_posparams () 
{ 
    os.system('local -a R')
    
    os.system('local u')
    
    
        if ( "" + sys.argv[1] + "" == '-u'):
            u=-u
            
            os.system('shift')
    
    # if you want the case of no positional parameters to return success,
    
    # remove the error message and return 0
    
    if ($# == 0  ):
        print("" + FUNCNAME + ": argument expected")1>&2
        
        os.system('return 1')
    
    # make R a copy of the positional parameters
    
    R=("" + $ + "{@}")
    
    # sort R.
    
    R=( os.popen(' printf "%s\n" "" + $ + "{R[@]}" | sort u').read() )
    
    print( "%s\n" % ("" + $ + "{R[@]}") )

    
    os.system('return 0')
}
# will print everything on separate lines
os.system('set -- 3 1 4 1 5 9 2 6 5 3 2')
os.system('sort_posparams "" + $ + "@"')
# sets without preserving quoted parameters
os.system('set --  os.popen(' sort_posparams "" + $ + "@" ').read() ')
print("" + $ + "@")
print("$#")
# sets preserving quoted parameters, beware pos params with embedded newlines
os.system('set -- 'a b' 'a c' 'x z'')
oifs=IFS
IFS='

os.system('set --  os.popen(' sort_posparams "" + $ + "@" ').read() ')
IFS="" + oifs + ""
print("" + $ + "@")
print("$#")
os.system('sort_posparams')
