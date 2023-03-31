import sys, os, os.path
from stat import *
#
# original from:
# @(#) rename.ksh 1.1 94/05/10
# 90/06/01 John DuBois (spcecdt@armory.com)
# 91/02/25 Improved help info
# 92/06/07 remove quotes from around shell pattern as required by new ksh
# 94/05/10 Exit if no globbing chars given.
#
# conversion to bash v2 syntax by Chet Ramey
def phelp () 
{ 
    print("" + usage + "
)
}
usage="usage: " + name + " [-htv] oldpattern newpattern"
name=${0##/}
while (os.system('getopts "htv" opt')):
    
        if ( "" + opt + "" == 't'):
            tell=true
        elif ("" + opt + "" == 'v'):
            verbose=true
        elif ("" + opt + "" == 'h'):
            os.system('phelp')
            exit(0)
        else:
            print("" + name + ": " + usage + "")1>&2
            exit(2)
os.system('shift (OPTIND - 1)')
if ($# < 2  ):
    os.system('phelp')
    exit(2)
oldpat=sys.argv[1]
newpat=sys.argv[2]
os.system('set -- sys.argv[1]')
if (! -e "" + sys.argv[1] + ""  ):
    print("" + name + ": no files match " + oldpat + ".")
    exit(1)
os.system('typeset -i i=1 j')
# Example oldpat: foo*.a
# Example newpat: bar*.b
# Examples given for first iteration (in the example, the only interation)
while (os.system(':')):
    
        if ( "" + oldpat + "" == '*[\*\?]*'):

        else:
            break
    # Get leftmost globbing pattern in oldpat
    pat=${oldpat#*[\*\?]}
    # pat=.a
    pat=${oldpat%%"" + pat + ""}
    # pat=foo*
    pat=${pat##*[!\?\*]}
    # pat=*
    # Find parts before & after pattern
    oldpre[i]=${oldpat%%"" + pat + ""*}
    # oldpre[1]=foo
    oldsuf[i]=${oldpat#*"" + pat + ""}
    # oldsuf[1]=.a
    newpre[i]=${newpat%%"" + pat + ""*}
    # newpre[1]=bar
    # Get rid of processed part of patterns
    oldpat=${oldpat#${oldpre[i]}"" + pat + ""}
    # oldpat=.a
    newpat=${newpat#${newpre[i]}"" + pat + ""}
    # newpat=.b
    i=i+1
if (i == 1  ):
    print("No globbing chars in pattern.")1>&2
    exit(1)
oldpre[i]=${oldpat%%"" + pat + ""*}
# oldpre[2]=.a
oldsuf[i]=${oldpat#*"" + pat + ""}
# oldsuf[2]=.a
newpre[i]=${newpat%%"" + pat + ""*}
# newpre[2]=.b
if (-n "" + verbose + ""  ):
    j=1
    while ("j < i"):
        print("Old prefix: " + $ + "{oldpre[j]}   Old suffix: " + $ + "{oldsuf[j]}   New prefix: " + $ + "{newpre[j]}")
        j=j+1
# Example file: foox.a
for file in ["" + $ + "@"]:
    j=1
    origname=file
    # origname=foox.a
    newfile=
    while ("j <= i"):
        # Peel off a prefix	interation	1		2
        file=${file#${oldpre[j]}}
        # file=x.a	file=
        # Save the part of this prefix that is to be retained
        const=${file%${oldsuf[j]}}
        # const=x	const=
        newfile=newfile${newpre[j]}const
        # newfile=barx	newfile=barx.b
        file=${file#const}
        # file=.a	file=.a
        j=j+1
    if (-n "" + tell + ""  ):
        print("Would move \"origname\" to \"newfile\".")
    else:
        if (-n "" + verbose + ""  ):
            print("Moving \"origname\" to \"newfile\".")
        os.system('mv origname newfile')
