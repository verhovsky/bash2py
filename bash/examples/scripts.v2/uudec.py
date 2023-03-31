import sys, os, os.path
from stat import *
os.system(':')
# @(#) uudec.sh 1.0 93/11/22
# 92/08/04 john@armory.com (John H. DuBois III)
# 93/11/22 Added help.
def isfalse () 
{ 
    os.system('test 0 == "" + sys.argv[1] + ""')
}
def phelp () 
{ 
    os.system('"" + name + ": process uuencoded files.
')
}
name=${0##*/}
os.system('typeset -i force=0')
while (os.system('getopts "hf" opt')):
    
        if ( "" + opt + "" == 'h'):
            os.system('phelp')
            exit(0)
        elif ("" + opt + "" == 'f'):
            force=1
        else:
            print("" + Usage + "")1>&2
            exit(2)
os.system('shift (OPTIND - 1)')
for file in ["" + $ + "@"]:
    print("" + file + "")
    while (b = raw_input() && "" + b + "" != begin ):
        os.system(':') < "$file"
    if ("" + b + "" == begin  ):
        if (os.path.isfile("" + filename + "" ) && os.system('isfalse force') ):
            print("Output file \"filename\" exists.  Not written.")
        else:
            os.system('uudecode "" + file + ""')
    else:
        print("No begin line.")
