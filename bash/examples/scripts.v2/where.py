import sys, os, os.path
from stat import *
#
# original from:
# @(#) where.ksh 1.1 94/07/11
# 91/01/12 john h. dubois iii (john@armory.com)
# 92/08/10 Only print executable *files*.
# 92/10/06 Print err msg if no match found.
# 92/11/27 Added implicit *
# 93/07/23 Print help only if -h is given.
# 94/01/01 Added -x option
# 94/07/11 Don't bother with eval
#
# conversion to bash v2 syntax done by Chet Ramey
name=${0##*/}
Usage="Usage: " + name + " [-hx] 'pattern' ..."
os.system('typeset -i exact=0')
def phelp () 
{ 
    print("" + name + ": find executable files in PATH that match patterns.
)
}
def istrue () 
{ 
    os.system('test 0 != "" + sys.argv[1] + ""')
}
def isfalse () 
{ 
    os.system('test 0 == "" + sys.argv[1] + ""')
}
while (os.system('getopts "xh" opt')):
    
        if ( "" + opt + "" == 'x'):
            exact=1
        elif ("" + opt + "" == 'h'):
            os.system('phelp')
            exit(0)
        else:
            print("" + Usage + "\nUse -h for help.")1>&2
            exit(2)
os.system('shift (OPTIND-1)')
os.system('set +f')
# make sure filename globbing is on
Args=("" + $ + "@")
# save args
OIFS=IFS
IFS=:
# Make PATH be split on :
Paths=(PATH)
IFS=OIFS
