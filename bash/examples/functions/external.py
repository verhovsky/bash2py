import sys, os, os.path
from stat import *
# Contributed by Noah Friedman.
# To avoid using a function in bash, you can use the `builtin' or
# `command' builtins, but neither guarantees that you use an external
# program instead of a bash builtin if there's a builtin by that name.  So
# this function can be used like `command' except that it guarantees the
# program is external by first disabling any builtin by that name.  After
# the command is done executing, the state of the builtin is restored. 
def external () 
{ 
    os.system('local state=""')
    
    os.system('local exit_status')
    
    if (os.system('builtin_p "" + sys.argv[1] + ""') ):
        state="builtin"
        
        os.system('enable -n "" + sys.argv[1] + ""')
    
    os.system('command "" + $ + "@"')
    
    exit_status=$?
    
    if ("" + state + "" == "builtin"  ):
        os.system('enable "" + sys.argv[1] + ""')
    
    os.system('return ${exit_status}')
}
# What is does is tell you if a particular keyword is currently enabled as
# a shell builtin.  It does NOT tell you if invoking that keyword will
# necessarily run the builtin.  For that, do something like
#
#       test "$(builtin type -type [keyword])" = "builtin"
#
# Note also, that disabling a builtin with "enable -n" will make builtin_p
# return false, since the builtin is no longer available.
def builtin_p () 
{ 
    os.system('local word')
    
    os.system('set  os.popen('builtin type -all -type "" + sys.argv[1] + ""').read() ')
    
    for word in ["" + $ + "@"]:
            if ("" + $ + "{word}" == "builtin"  ):
            os.system('return 0')
    
    os.system('return 1')
}
