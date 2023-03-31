import sys, os, os.path
from stat import *
# Format: array_to_string vname_of_array vname_of_string separator
def array_to_string () 
{ 
    ((($# < 2) || ($# > 3))) && { 
        os.system('"" + FUNCNAME + ": usage: " + FUNCNAME + " arrayname stringname [separator]"')
        
        os.system('return 2')
    }
    
    os.system('local array=sys.argv[1] string=sys.argv[2]')
    
    ((3==$#)) && $3 = ? && os.system('local IFS="" + $ + "{3}" + $ + "{IFS}"')
    
    os.system('eval string="\"\${array[*]}\""')
    
    os.system('return 0')
}
