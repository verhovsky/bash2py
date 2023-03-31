import sys, os, os.path
from stat import *
#
# original from:
# newext: change filename extension
# @(#) newext.sh 1.1 93/04/13
# 90/06/06 john h. dubois iii (john@armory.com)
# 90/11/14 changed ksh-specific code to hybrid: if running under Bourne,
#          uses expr instead of ksh builtin ops.  Removed SYSV specific code.
# 91/08/06 added -t option
# 92/11/06 made earlier code actually work!
# 93/04/13 If no filenames given, act on files in current dir
#
# conversion to bash v2 syntax by Chet Ramey
usage="Usage: newext [-th] <oldext> <newext> [filename ...]"
def phelp () 
{ 
    print("" + usage + "
)
}
while (os.system('getopts "th" opt')):
    
        if ( "" + opt + "" == 't'):
            echo=echo
        elif ("" + opt + "" == 'h'):
            os.system('phelp')
            exit(0)
        else:
            print("" + usage + "")1>&2
            exit(2)
os.system('shift (OPTIND - 1)')
oldext=sys.argv[1]
newext=sys.argv[2]

    if ( $# == '[01]'):
        print("" + usage + "\nUse -h for help.")1>&2
        exit(2)
    elif ($# == '2'):
        os.system('shift')
        os.system('shift')
        os.system('set -- *')
    else:
        os.system('shift')
        os.system('shift')
found=
for file in ["" + $ + "@"]:
    
        if ( "" + file + "" == '*$oldext'):
            newname="" + $ + "{file%" + oldext + "}" + newext + ""
            os.system('echo mv "" + file + "" "" + newname + ""')
            found=true
if (-z "" + found + ""  ):
    print("No files ending in \"oldext\".")
    exit(1)
exit(0)
