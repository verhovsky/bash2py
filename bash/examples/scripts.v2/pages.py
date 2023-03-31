import sys, os, os.path
from stat import *
#
# original from:
# @(#) pages.sh 1.0 92/09/26
# 92/09/05 John H. DuBois III (jhdiii@armory.com)
# 92/09/26 Added help
#
# conversion to bash v2 syntax by Chet Ramey
Usage="" + sys.argv[0] + " [-h] [-n lines/page] page-ranges [file ...]"
def usage () 
{ 
    print("" + Usage + "")1>&2
}
def phelp () 
{ 
    print("" + sys.argv[0] + ": print selected pages.
)
}
while (os.system('getopts "n:h" opt')):
    
        if ( "" + opt + "" == 'n'):
            LinesPerPage=OPTARG
        elif ("" + opt + "" == 'h'):
            os.system('phelp')
            exit(0)
        else:
            os.system('usage')
            exit(2)
os.system('shift (OPTIND - 1)')
if ($# == 0  ):
    print("sys.argv[0]: no page ranges given.")1>&2
    os.system('usage')
    exit(1)
PageList=sys.argv[1]
os.system('shift')
os.system('gawk "
 "" + $ + "@"')
