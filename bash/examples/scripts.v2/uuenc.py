import sys, os, os.path
from stat import *
#
# original from:
# @(#) uuenc.ksh 1.0 93/09/18
# 93/09/18 john h. dubois iii (john@armory.com)
#
# conversion to bash v2 syntax by Chet Ramey
def istrue () 
{ 
    os.system('test 0 != "" + sys.argv[1] + ""')
}
def isfalse () 
{ 
    os.system('test 0 == "" + sys.argv[1] + ""')
}
def phelp () 
{ 
    print("" + name + ": uuencode files.
)
}
name=${0##*/}
Usage="Usage: " + name + " [-hf] <filename> ..."
os.system('typeset -i force=0')
SUF=uu
while (os.system('getopts :hf opt')):
    
        if ( opt == 'h'):
            os.system('phelp')
            exit(0)
        elif (opt == 'f'):
            force=1
        elif (opt == '+?'):
            print("" + name + ": options should not be preceded by a '+'.")1>&2
            exit(2)
        elif (opt == '?'):
            print("" + name + ": " + OPTARG + ": bad option.  Use -h for help.")1>&2
            exit(2)
# remove args that were options
os.system('shift (OPTIND - 1)')
if ($# < 1  ):
    print("" + Usage + "\nUse -h for help.")1>&2
    exit()
for file in ["" + $ + "@"]:
    tail=${file##*/}
    out="" + tail + "." + $ + "{SUF}"
    if (os.system('isfalse force') && -a "" + out + ""  ):
        print("" + name + ": " + out + ": file exists.  Use -f to overwrite.")1>&2
    else:
        os.system('uuencode file tail> $out')
