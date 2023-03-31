import sys, os, os.path
from stat import *
#
# replacements for test/[ that do arithmetic expansion on the operands to
# the arithmetic operators, like ksh.
#
def test () 
{ 
    os.system('local -i n1 n3')
    
    
        if ( len(sys.argv) == '3'):
            
                elif ("" + sys.argv[2] + "" == '-lt' or "" + sys.argv[2] + "" == '-gt' or "" + sys.argv[2] + "" == '-eq' or "" + sys.argv[2] + "" == '-ne' or "" + sys.argv[2] + "" == '-le' or "" + sys.argv[2] + "" == '-ge'):
                    n1=( sys.argv[1] )
                    
                    n3=( sys.argv[3] )
                    
                    os.system('builtin test "" + n1 + "" sys.argv[2] "" + n3 + ""')
                    
                    os.system('return $?')
                else:
                    os.system('builtin test "" + $ + "@"')
        else:
            os.system('builtin test "" + $ + "@"')
}
def [ () 
{ 
    os.system('local -i n1 n3')
    
    
        if ( len(sys.argv) == '4'):
            
                elif ("" + sys.argv[2] + "" == '-lt' or "" + sys.argv[2] + "" == '-gt' or "" + sys.argv[2] + "" == '-eq' or "" + sys.argv[2] + "" == '-ne' or "" + sys.argv[2] + "" == '-le' or "" + sys.argv[2] + "" == '-ge'):
                    n1=( sys.argv[1] )
                    
                    n3=( sys.argv[3] )
                    
                    os.system('builtin  "" + n1 + "" sys.argv[2] "" + n3 + "" ')
                    
                    os.system('return $?')
                else:
                    os.system('builtin  "" + $ + "@"')
        else:
            os.system('builtin  "" + $ + "@"')
}
q=7
q < 10 
print("$?")
q < 10 
print("$?")
