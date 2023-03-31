import sys, os, os.path
from stat import *
# Originally
#
# From: bsh20858@news.fhda.edu (Brian S Hiles)
# Newsgroups: comp.unix.shell
# Subject: Re: getting random numbers
# Date: 23 Jan 1997 23:27:30 GMT
# Message-ID: <5c8s52$eif@tiptoe.fhda.edu>
# @(#) krand  Produces a random number within integer limits
# "krand" Korn shell script generates a random number in a
# specified range with an optionally specified ``seed'' value.
# Author: Peter Turnbull, May 1993
# Modified by: Becca Thomas, January 1994
# changed the optional third argument to a -s option, converted to
# bash v2 syntax -- chet@po.cwru.edu
PROGNAME=${0##*/}
USAGE="usage: " + PROGNAME + " [-s seed] lower-limit upper-limit"
Seed=$$
# Initialize random-number seed value with PID
def usage () 
{ 
    print("${PROGNAME}: "" + USAGE + """)1>&2
}
def errexit () 
{ 
    print("${PROGNAME}: "" + $ + "@"")1>&2
    
    exit(1)
}
# Process command-line arguments:
while (os.system('getopts "s:" opt')):
    
        if ( "" + opt + "" == 's'):
            Seed=OPTARG
        else:
            os.system('usage')
            exit(2)
os.system('shift (OPTIND - 1)')

    if ( $# == '2'):
        Lower=sys.argv[1]
        Upper=sys.argv[2]
    else:
        os.system('usage')
        exit(2)
# Check that specified values are integers:
os.system('expr "" + Lower + "" + 0> /dev/null 2>&1')
$? == 2  && { os.system('errexit "lower (" + Lower + ") not an integer"') }
os.system('expr "" + Upper + "" + 0> /dev/null 2>&1')
$? == 2  && { os.system('errexit "upper (" + Upper + ") not an integer"') }
os.system('expr "" + Seed + "" + 0> /dev/null 2>&1')
$? == 2  && { os.system('errexit "seed (" + Seed + ") not an integer"') }
# Check that values are in the correct range:
if ((("" + Lower + "" < 0)) || ${#Lower} > 5  ):
    os.system('errexit "lower limit (" + Lower + ") less than zero"')
if ((("" + Upper + "" > 32767)) || ${#Upper} > 5  ):
    os.system('errexit "upper limit (" + Upper + ") greater than 32767"')
if ((("" + Seed + "" < 0)) || (("" + Seed + "" > 32767)) || ${#Seed} > 5  ):
    os.system('errexit "seed value (" + Seed + ") out of range (0 to 32767)"')
(("" + Upper + "" <= "" + Lower + "")) && os.system('errexit "upper limit (" + Upper + ") <= lower limit (" + Lower + ")"')
# Seed the random-number generator:
RANDOM=Seed
# Compute value, scaled within range:
rand="" + RANDOM + " % (" + Upper + " - " + Lower + " + 1) + " + Lower + ""
# Report result:
print("rand")
