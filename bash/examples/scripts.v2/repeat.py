import sys, os, os.path
from stat import *
#
# original from:
# repeat: repeat a command.
# @(#) repeat.ksh 1.1 93/06/03
# 90/05 john h. dubois iii (john@armory.com)
# 90/11 added help
# 93/06/03 Added s, h, p, and v options
#
# conversion to bash v2 syntax done by Chet Ramey
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
    print("" + name + ": repeatedly execute a command line.
)
}
name=${0##*/}
Usage="Usage: repeat [-hpv] [-s <sec>] [[startcount]-][endcount] command [arg ...]"
os.system('typeset -i count=1 forever=0 sleep=0 print=0 verbose=0')
while (os.system('getopts :0123456789hpvs: opt')):
    
        if ( opt == 'h'):
            os.system('phelp')
            exit(0)
        elif (opt == 's'):
            sleep=OPTARG || exit(1)
        elif (opt == 'p'):
            print=1
        elif (opt == 'v'):
            verbose=1
        elif (opt == '[0-9]'):
            break
        elif (opt == '+?'):
            print("" + name + ": options should not be preceded by a '+'.")1>&2
            exit(2)
        elif (opt == '?'):
            print("" + name + ": " + OPTARG + ": bad option.  Use -h for help.")1>&2
            exit(2)
# remove args that were options
os.system('shift (OPTIND-1)')
if ($# < 2  ):
    print("" + Usage + "\nUse -h for help.")1>&2
    exit(2)

    if ( "" + sys.argv[1] + "" == '-[0-9]*-' or "" + sys.argv[1] + "" == '[0-9]*-'):
        # Start value only
        count=${1%-}
        forever=1
        end="-1"
    elif ("" + sys.argv[1] + "" == '-[0-9]*-[0-9]*' or "" + sys.argv[1] + "" == '[0-9]*-[0-9]*'):
        # Start and end value
        s=${1%-}
        end=${s##[0-9]*-}
        count=${s%-end}
    elif ("" + sys.argv[1] + "" == '-[0-9]*' or "" + sys.argv[1] + "" == '[0-9]*'):
        end=sys.argv[1]
        
            elif ("" + end + "" == '-\*'):
                count=-1
    if ( "" + end + "" == '-'):
        forever=1
        end="-1"
    else:
        print("" + name + ": bad count parameter: " + sys.argv[1] + "")1>&2
        exit(1)
os.system('shift')
-z "" + end + ""  && count < "" + end + ""  && increment=1 || increment=-1
os.system('istrue verbose') && print("start=" + count + " end=" + end + "")1>&2
# Need to do this here so that up to this point, -0 will keep the leading -
# and end will not be 0 if no value assigned
os.system('typeset -i end')
end+=increment
# make loop inclusive of original endcount
while (os.system('istrue forever') || count != end ):
    os.system('istrue print') && print("count")1>&2
    os.system('eval "" + $ + "@"')
    os.system('istrue sleep') && os.system('sleep sleep')
    count+=increment
