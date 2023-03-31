import sys, os, os.path
from stat import *
#
# original from:
# fman: new man program
# @(#) fman.ksh 1.5 94/04/16
# 91/07/03 john h. dubois iii (john@armory.com)
# 91/07/11 made it unpack man pages if neccessary
# 91/07/16 fixed test for whether man file pattern was expanded
# 92/01/21 made it read /etc/default/man to get section order,
#          and only display the first section found.
# 92/02/06 changed name to fman
# 92/02/07 fixed bug in notfound
# 92/02/13 incorporated changes from DOS version
# 92/03/11 changed to use MANPATH from environment if set,
#          and search all directories given in MANPATH
# 92/03/15 exec pager or man w/o forking
# 92/05/31 try using index if one exists
# 92/10/01 Added "See also <other sections>"
# 92/10/18 If PAGER is less, search for name of man page to make it easier
#          to find information in man pages for multiple items
# 92/11/11 Make it work for compressed files not listed in index;
#          deal with man pages listed in index that don't exist.
# 93/03/30 Fixed bug in MANPATH processing
# 93/06/17 Include paths in "See also:" message if they would be needed
#          to get to a man page.  Allow MANPATH spec on command line.
# 93/07/09 Added -h and -e options.
# 94/04/16 Added x option.
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
# Finds all sections that man page $1 is in and puts them in the the
# global array Sections[].  
# The filename of each page is put in FileNames[] with the same index.
# Global vars used:
# patharr[] MANPATH directories.
def FindSectionsInIndex () 
{ 
    os.system('typeset index indexes section mpath page=sys.argv[1]')
    
    os.system('typeset -i i=0 NIndex=0')
    
    for mpath in ["" + $ + "{patharr[@]}"]:
            if (-r mpath/index  ):
            indexes="" + indexes + " " + mpath + "/index"
            
            NIndex+=1
    
    -z "" + indexes + ""  && os.system('return')
    
    # Make grep give filename
    
    NIndex < 2  && indexes="" + indexes + " /dev/null"
    
    # set positional parameters to
    
    # indexfile:searchname pagename section ...
    
    # e.g.
    
    # /usr/man/index:FP_OFF Routines DOS
    
    os.system('set --  os.popen('grep "^" + page + "[ 	]" indexes').read() ')
    
    while ($# > 2 ):
        FileNames[i]=${1%%index*}catsys.argv[3]/sys.argv[2].sys.argv[3]
        
        Sections[i]=sys.argv[3]
        
        os.system('shift 3')
        
        i+=1
}
# Finds all sections that man page $1 is in by searching each man directory
# in the order given in patharr[],
# and puts them in the the global array Sections[].  
# The filename of each page is put in FileNames[] with the same index.
# Global vars used:
# patharr[] MANPATH directories.
def FindSectionsInDirs () 
{ 
    os.system('local page=sys.argv[1] mpath AllPaths Path')
    
    os.system('typeset -i i')
    
    for mpath in ["" + $ + "{patharr[@]}"]:
            AllPaths="" + AllPaths + " " + mpath + "/cat[0-9]*/" + page + ".* " + mpath + "/man[0-9]*/" + page + ".*"
    
    i=0
    
    for Path in [AllPaths]:
            os.system('istrue debug') && print("Path == Path")
        
        
            if ( "" + Path + "" == '*\*'):

            else:
                # Remove compressed-file suffix to make FileNames be the same
                
                # as it is when built by FindSectionsInIndex()
                
                FileNames[i]=${Path%.[zZ]}
                
                Path=${Path%/*}
                
                Sections[i]=${Path##*/*.}
                
                i+=1
}
# FindSection: display man page.
# Uses ordarr[] (built from $ORDER) to display the version of the man
# page that occurs first in $ORDER.
# Sections[] gives the sections that a man page was found in.
# If the global variable "exist" is set to 1, nothing is displayed;
# the function instead returns zero if a page is found, nonzero if not.
# The filename of each page is in FileNames[] with the same index.
# Global vars used:
# Sections[], FileNames[], ordarr[]
def FindSection () 
{ 
    os.system('typeset -i NumPages i foundsec')
    
    os.system('local section OtherSec filename NPAGER=PAGER POpt page=sys.argv[1] Pat')
    
    os.system('local PageFile')
    
    NumPages=${#Sections[*]}
    
    # Number of versions of man page found.
    
    os.system('isfalse NumPages') && os.system('return 1')
    
    
        if ( "" + PAGER + "" == '*less'):
            Popt="-p" + page + ""
    
    # For each section in ORDER, determine if any man page was found in
    
    # that section
    
    for section in ["" + $ + "{ordarr[@]}"]:
            i=0
        
        foundsec=0
        
        while (i < NumPages ):
            if ("" + $ + "{Sections[i]}" == section  ):
                # Found a man page from this section of ORDER
                
                filename=${FileNames[i]}
                
                if (-z "" + PageFile + ""  ):
                    PageFile=filename
                else:
                    if (os.system('istrue foundsec') ):
                        OtherSec="" + OtherSec + "" + page + "(" + $ + "{filename%/*/*} " + section + ") "
                    else:
                        OtherSec="" + OtherSec + "" + page + "(" + section + ") "
                
                foundsec=1
                
                os.system('istrue exist') && os.system('return')
            
            i+=1
    
    # No pages with the specified section found.
    
    -z "" + PageFile + ""  && os.system('return 1')
    
    # Return if all we want to know is whether the man page exists.
    
    "" + exist + "" == 1  && os.system('return 0')
    
    if (-z "" + OtherSec + ""  ):
        NPAGER="exec " + PAGER + ""
    
    if (-r PageFile  ):
        os.system('NPAGER POpt PageFile')
    else:
        if (-r PageFile.z  ):
            os.system('pcat PageFile.z') | os.system('NPAGER POpt')
        else:
            if (-r PageFile.Z  ):
                os.system('zcat PageFile.Z') | os.system('NPAGER POpt')
            else:
                if (os.path.isfile(PageFile.gz ) ):
                    os.system('gzip -dc PageFile.gz') | os.system('NPAGER POpt')
                else:
                    print("" + PageFile + ": cannot open.")1>&2
                    
                    OtherSec=
                    
                    os.system('unset Sections[i]')
                    
                    i+=1
                    
                    continue
    
    print("See also " + OtherSec + "")
    
    exit(0)
}
def phelp () 
{ 
    print("" + name + ": print man pages.
)
}
# main program
os.system('typeset -i exist=0 debug=0')
name=${0##*/}
Usage="Usage: " + name + " [-eh] [[manpath] section] command-name"
while (os.system('getopts :hex opt')):
    
        if ( opt == 'h'):
            os.system('phelp')
            exit(0)
        elif (opt == 'e'):
            exist=1
        elif (opt == 'x'):
            debug=1
        elif (opt == '+?'):
            print("" + name + ": options should not be preceded by a '+'.")1>&2
            exit(2)
        elif (opt == '?'):
            print("" + name + ": " + OPTARG + ": bad option.  Use -h for help.")1>&2
            exit(2)
# remove args that were options
os.system('shift (OPTIND-1)')
if ($# < 1  ):
    print("" + Usage + "\nUse -h for help.")1>&2
    exit()
P=PAGER
O=1:n:l:6:8:2:3:4:5:7:p:o
T=TERM
M=${MANPATH:-/usr/local/man:/usr/man}
os.path.isfile(/etc/default/man ) && os.system('. /etc/default/man')
-n "" + P + ""  && PAGER=P
-n "" + O + ""  && ORDER=O
-n "" + T + ""  && TERM=T
-n "" + M + ""  && MANPATH=M

    if ( $# == '0'):
        print("No man page specified.")
        exit(1)
    elif ($# == '1'):
        page=sys.argv[1]
    elif ($# == '2'):
        ORDER= os.popen('echo sys.argv[1] | tr a-z A-Z').read() 
        page=sys.argv[2]
    elif ($# == '3'):
        MANPATH=sys.argv[1]
        -n "" + sys.argv[2] + ""  && ORDER= os.popen('echo sys.argv[2] | tr a-z A-Z').read() 
        page=sys.argv[3]
    else:
        print("Too many arguments.")
        exit(1)
aargs=("" + $ + "@")
! -t 0  && PAGER=cat
OIFS=IFS
IFS=:
patharr=(MANPATH)
i=0
for d in [MANPATH]:
    for sec in [ORDER]:
            ordarr[i]=d/cat${sec}
        i+=1
        ordarr[i]=d/man${sec}
        i+=1
IFS=OIFS
os.system('istrue debug') && print("patharr == "" + $ + "{patharr[@]}"")
# if less or more is being used, remove multiple blank lines
os.environ['LESS'] = "-s $LESS"
os.environ['MORE'] = "-s $MORE"
# Try using index
os.system('FindSectionsInIndex "" + page + ""')
# Exit 0 if a page was found and we're just testing for existence.
os.system('FindSection "" + page + ""') && exit(0)
# Try searching directories
os.system('unset Sections[*]')
os.system('FindSectionsInDirs "" + page + ""')
os.system('FindSection "" + page + ""') && exit(0)
os.system('istrue exist') && exit(1)
# Try using man
# If using more or less, make man run faster by letting more or less compress
# multiple blank lines instead of rmb
#case "$PAGER" in
#esac
#cmd=(man $manopt -p$PAGER "${aargs[@]}")
os.environ[''] = FILE_TO_TRANSLATE
cmd=(man manopt "" + $ + "{aargs[@]}")
os.system('istrue debug') && print("" + name + ": running " + $ + "{cmd[*]}")1>&2
os.system('exec "" + $ + "{cmd[@]}"')
