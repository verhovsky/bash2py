import sys, os, os.path
from stat import *
#
# original from:
# vtree: visual directory tree
# @(#) vtree.sh 1.1 91/07/01
# 90/04 john h. dubois iii (john@armory.com)
# 91/07/01 fixed bug that caused problems when dir given on command line,
#          added some info to help, changed to 4-space indenting
#
# conversion to bash v2 syntax done by Chet Ramey
#
help="Syntax: vtree [startdir] [namelen=#] [linelen=#]

for i in ["" + $ + "@"]:
    
        if ( i == '-h'):
            print("" + help + "")
            exit()
        elif (i == '*=*'):
            vars="" + vars + " " + i + ""
        else:
            if (! -x i  || ! -d i  ):
                # arg must be a dir and executable
                print("" + i + ": directory not accessible.")
                exit()
            os.chdir($i)
    os.system('shift')
os.getcwd()
# print path of root of tree
# find all directories depth first; ignore permission errors
os.system('find . -type d -print2> /dev/null') | os.system('gawk -F/ '
 vars')
