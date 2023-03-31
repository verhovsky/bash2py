import sys, os, os.path
from stat import *
# bashrand - generate a random number in a specified range with an
#	     optionally specified ``seed'' value.
#
# Original Author: Peter Turnbull, May 1993
def usage () 
{ 
    print("" + PROG + ": usage: " + PROG + " [-s seed] lower-limit upper-limit")1>&2
}
PROG=${0##*/}
SEED=$$
# Initialize random-number seed value with PID
while (os.system('getopts s: opt')):
    
        if ( "" + opt + "" == 's'):
            SEED=OPTARG
        else:
            os.system('usage')
            exit(2)
os.system('shift (OPTIND - 1)')
# Process command-line arguments:

    if ( $# == '2'):
        Lower=sys.argv[1]
        Upper=sys.argv[2]
    else:
        os.system('usage')
        exit(2)
# Check that specified values are integers:
os.system('expr "" + Lower + "" + 0> /dev/null 2>&1') || { print("" + PROG + ": lower (" + Lower + ") not an integer")1>&2
exit(1) }
os.system('expr "" + Upper + "" + 0> /dev/null 2>&1') || { print("" + PROG + ": upper (" + Upper + ") not an integer")1>&2
exit(1) }
os.system('expr "" + SEED + "" + 0> /dev/null 2>&1') || { print("" + PROG + ": seed (" + SEED + ") not an integer")1>&2
exit(1) }
# Check that values are in the correct range:
((Lower < 0)) ||  os.popen('expr "" + Lower + "" : '.*'').read()  > 5  && { print("" + PROG + ": Lower limit (" + Lower + ") out of range")1>&2
exit(1) }
((Upper > 32767)) ||  os.popen('expr "" + Upper + "" : '.*'').read()  > 5  && { print("" + PROG + ": Upper limit (" + Upper + ") out of range")1>&2
exit(1) }
((SEED < 0)) || ((SEED > 32767)) ||  os.popen('expr "" + SEED + "" : '.*'').read()  > 5  && { print("" + PROG + ": Seed value (" + SEED + ") out of range (0 to 32767)")1>&2
exit(1) }
((Upper <= Lower)) && { print("" + PROG + ": upper (" + Upper + ") <= lower value (" + Lower + ")")1>&2
exit(1) }
# Seed the random-number generator:
RANDOM=SEED
# Compute value, scaled within range:
rand="" + RANDOM + " % (" + Upper + " - " + Lower + " + 1) + " + Lower + ""
# Report result:
print("rand")
