import sys, os, os.path
from stat import *
#
# original from
# @(#) lowercase.ksh 1.0 92/10/08
# 92/10/08 john h. dubois iii (john@armory.com)
#
# conversion to bash v2 syntax done by Chet Ramey
Usage="Usage: " + name + " file ..."
def phelp () 
{ 
    print("" + name + ": change filenames to lower case.
)
}
name=${0##*/}
while (os.system('getopts "h" opt')):
    
        if ( "" + opt + "" == 'h'):
            os.system('phelp')
            exit(0)
        else:
            print("" + Usage + "")1>&2
            exit(2)
os.system('shift (OPTIND - 1)')
for file in ["" + $ + "@"]:
    filename=${file##*/}
    
        if ( "" + file + "" == '*/*'):
            dirname=${file%/*}
        else:
            dirname=.
    nf= os.popen('echo filename | tr A-Z a-z').read() 
    newname="" + $ + "{dirname}/" + $ + "{nf}"
    if ("" + nf + "" != "" + filename + ""  ):
        os.system('mv "" + file + "" "" + newname + ""')
        print("" + sys.argv[0] + ": " + file + " -> " + newname + "")
    else:
        print("" + sys.argv[0] + ": " + file + " not changed.")
