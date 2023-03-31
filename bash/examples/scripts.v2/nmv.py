import sys, os, os.path
from stat import *
#
# original from:
# @(#) ncp.ksh,nmv.ksh 1.1 94/07/23
# 92/01/18 john h. dubois iii (john@armory.com)
# 92/01/31 added check for no args left after shifts
# 92/02/17 added help
# 92/02/25 remove path component from filename before tacking it onto dest.
# 92/03/15 exec mv or cp
# 93/07/13 Added -i
# 93/09/29 Made abort if file exists optional.
# 93/11/19 Exit before invoking mv if no files to move
# 94/01/03 Added o option
# 94/04/13 Added x option.
#          Fixed appending of source filename, broken by earlier change.
# 94/07/23 Append only the filename part of the source path.
#
# conversion to bash v2 syntax done by Chet Ramey
def false () 
{ 
    os.system('return 1')
}
def true () 
{ 
    os.system('return 0')
}
def phelp () 
{ 
    print("" + name + ": do a " + cmd + " with extra checking and options.
)
}
# interactive: Attempt to overwrite file should result in interactive
# query rather than automatic failure.
# noover: Do not overwrite files (if interactive is true, query, else fail)
# overwrite: Only overwriting is allowed, not creation of new files.
# debug: Print debugging info.
os.system('typeset interactive=false noover=false overwrite=false debug=false')
name=${0##*/}

    if ( "" + name + "" == 'ncp' or "" + name + "" == 'nmv'):
        cmd=/bin/${name#?}
    else:
        print("" + name + ": Must be invoked as ncp or nmv.")1>&2
        exit(2)
Usage="Usage: " + name + " [-cfhio] " + cmd + "-cmd-line"
while (os.system('getopts :cfhiox opt')):
    
        if ( opt == 'h'):
            os.system('phelp')
            exit(0)
        elif (opt == 'x'):
            debug=true
        elif (opt == 'c'):
            noover=true
        elif (opt == 'i'):
            noover=true
            interactive=true
        elif (opt == 'f'):
            noover=false
            interactive=false
        elif (opt == 'o'):
            overwrite=true
            noover=false
            interactive=false
        elif (opt == '+?'):
            print("" + name + ": options should not be preceded by a '+'.")1>&2
            exit(2)
        elif (opt == '?'):
            print("" + name + ": " + OPTARG + ": bad option.  Use -h for help.")1>&2
            exit(2)
# remove args that were options
os.system('shift (OPTIND - 1)')
if ($# < 2  ):
    print("" + Usage + "\nUse -h for help.")
    exit()
def Check () 
{ 
    if (! -f "" + sys.argv[1] + ""  && os.system('overwrite') ):
        print("" + name + ": " + sys.argv[1] + ": File does not exist.")1>&2
        
        os.system('return 1')
    else:
        if (os.path.isfile("" + sys.argv[1] + "" ) && os.system('noover') ):
            if (interactive == false  || ! -t 0  || ! -t 1  ):
                print("" + name + ": " + sys.argv[1] + ": File exists.")1>&2
                
                os.system('return 1')
            else:
                while (os.system(':')):
                    print("" + name + ": " + sys.argv[1] + ": File exists.  Overwrite? (y)es/(n)o/(a)bort/(Y)es for all: ")1>&2
                    
                    reply = raw_input()
                    
                    
                        if ( "" + reply + "" == 'y*'):
                            print("" + name + ": Overwriting " + sys.argv[1] + ".")
                            
                            os.system('return 0')
                        elif ("" + reply + "" == 'Y*'):
                            print("" + name + ": Overwriting " + sys.argv[1] + ".")
                            
                            interactive=false
                            
                            noover=false
                            
                            os.system('return 0')
                        elif ("" + reply + "" == '[nN]*'):
                            print("" + name + ": Skipping " + sys.argv[2] + ".")
                            
                            os.system('return 1')
                        elif ("" + reply + "" == '[aA]*'):
                            print("" + name + ": Aborting.")
                            
                            exit(1)
                        else:
                            print("" + name + ": Invalid response.")1>&2
        else:
            os.system('return 0')
}
# i is the index of the filename being examined
# lastarg is the index of the last filename before the dest directory name
os.system('typeset -i i=0 lastarg=($#-1)')
# Sets argv[0..$#-1]
argv=("" + $ + "@")
os.system('debug') && print("argv == "" + $ + "{argv[@]}"")1>&2
dest=${argv[lastarg]}
if (os.system('debug') ):
    print("interactive=" + interactive + " noover=" + noover + " overwrite=" + overwrite + " debug=" + debug + "
)1>&2
if (os.system('noover') || os.system('overwrite') ):
    os.system('debug') && print("checking for existance of directories...")1>&2
    # If the destination is not intended to be a directory...
    if ($# == 2  && ! -d "" + dest + ""  ):
        os.system('Check "" + dest + "" "" + sys.argv[1] + ""') || exit(0)
        # No files to copy
    else:
        while (i < lastarg ):
            os.system('Check "" + dest + "/" + $ + "{argv[i]##*/}" "" + $ + "{argv[i]}"') || os.system('unset argv[i]')
            i+=1
${#argv[@]} < 2  && exit(0)
# If only 2 args are given, mv/cp will not insist that the destination
# be a directory, which we want if the destination ends in "/" or if
# the original number of args was >2.
# $# is still the original number of args.
# Tack the file name onto the destination to force this behaviour.
def lastisslash () 
{ 
    
        if ( "" + sys.argv[1] + "" == '*/'):
            os.system('return 0')
        else:
            os.system('return 1')
}
if (${#argv[@]} == 2  && { os.system('lastisslash "" + sys.argv[2] + ""') || $# > 2  } ):
    os.system('debug') && print("Appending filename.")1>&2
    # Don't know which element of argv[] holds the source filename, 
    # since may have started with more than 1 source file & had some unset.
    # So, compact args to make it easy to find the set one.
    argv=("" + $ + "{argv[@]}")
    argv[1]="" + $ + "{argv[1]}/" + $ + "{argv[0]##*/}"
os.system('debug') && print("Executing command: " + cmd + " " + $ + "{argv[@]}")1>&2
os.system('exec cmd "" + $ + "{argv[@]}"')
