import sys, os, os.path
from stat import *
# From: Seth Chaiklin <psykseth@aau.dk>
# To: chet@ins.CWRU.Edu
# Subject: bash functions (sorta)
#
# keep:
# usage: keep program
# declare the a program should be "kept".  i.e. try to fg a stopped one
# and only when that fails start a fresh program.
#
def keep () 
{ 
    
        if ( $# == '1' or $# == '2'):

        else:
            print("usage: keep [alias] program")1>&2
            
            os.system('return 1')
    
    # progname
    
    pn=${1##*/}
    
    # set up an alias for the kept program
    
    if ($# == 1  ):
        os.system('alias "" + pn + "=fg " + sys.argv[1] + " 2>/dev/null || " + sys.argv[1] + ""')
    else:
        os.system('alias "" + sys.argv[1] + "=fg " + sys.argv[2] + " 2>/dev/null || " + sys.argv[2] + ""')
}
#
# unkeep:
# usage: unkeep program
# unset the alias set up by the keep function
#
def unkeep () 
{ 
    if ($# != 1  ):
        print("usage: unkeep program")
        
        os.system('return 2')
    
    # unset the alias for the kept program
    
    os.system('unalias "" + $ + "{1##*/}"')
}
#
# kept:
# lists all kept programs in 'alias: program' form
#
def kept () 
{ 
    os.system('alias') | os.system('grep "fg.*2>"') | os.system('sed "s/alias \(.*\)='fg.*||\(.*\)'" + $ + "/\1:\2/"')
}
# some things that should be kept
#keep /usr/local/bin/emacs
#keep e ${EDITOR:-/usr/local/bin/emacs}
#keep edit ${EDITOR:-/usr/local/bin/emacs}
#keep /usr/local/bin/emm
