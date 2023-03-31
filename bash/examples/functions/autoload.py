import sys, os, os.path
from stat import *
#
# An almost ksh-compatible `autoload'.  A function declared as `autoload' will
# be read in from a file the same name as the function found by searching the
# $FPATH (which works the same as $PATH), then that definition will be run.
#
# To do this without source support, we define a dummy function that, when
# executed, will load the file (thereby re-defining the function), then 
# execute that newly-redefined function with the original arguments.
#
# It's not identical to ksh because ksh apparently does lazy evaluation
# and looks for the file to load from only when the function is referenced.
# This one requires that the file exist when the function is declared as
# `autoload'.
#
# usage: autoload func [func...]
#
# The first cut of this was by Bill Trost, trost@reed.bitnet
#
# Chet Ramey
# chet@ins.CWRU.Edu
#
# Declare a function ($1) to be autoloaded from a file ($2) when it is first
# called.  This defines a `temporary' function that will `.' the file 
# containg the real function definition, then execute that new definition with
# the arguments given to this `fake' function.  The autoload function defined
# by the file and the file itself *must* be named identically.
#
def aload () 
{ 
    os.system('eval sys.argv[1] '() {  . 'sys.argv[2]' ; 'sys.argv[1]' "" + $ + "@" ; return $? ; }'')
}
#
# Search $FPATH for a file the same name as the function given as $1, and
# autoload the function from that file.  There is no default $FPATH.
#
def autoload () 
{ 
    #
    
    # Save the list of functions; we're going to blow away the arguments
    
    # in a second.  If any of the names contain white space, TFB.
    
    #
    
    os.system('local args="" + $ + "*"')
    
    #
    
    # This should, I think, list the functions marked as autoload and not
    
    # yet defined, but we don't have enough information to do that here.
    
    #
    
    if ($# == 0  ):
        print("usage: autoload function [function...]")1>&2
        
        os.system('return 1')
    
    #
    
    # If there is no $FPATH, there is no work to be done
    
    #
    
    if (-z "" + FPATH + ""  ):
        print("autoload: FPATH not set or null")1>&2
        
        os.system('return 1')
    
    #
    
    # This treats FPATH exactly like PATH: a null field anywhere in the
    
    # FPATH is treated the same as the current directory.
    
    #
    
    # The path splitting command is taken from Kernighan and Pike
    
    #
    
    #	fp=$(echo $FPATH | sed 's/^:/.:/
    
    #				s/::/:.:/g
    
    #				s/:$/:./
    
    #				s/:/ /g')
    
    # replaced with builtin mechanisms 2001 Oct 10
    
    fp=${FPATH/#:/.:}
    
    fp=${fp//::/:.:}
    
    fp=${fp/%:/:.}
    
    fp=${fp//:/ }
    
    for FUNC in [args]:
            #
        
        # We're blowing away the arguments to autoload here...
        
        # We have to; there are no arrays (well, there are, but
        
        # this doesn't use them yet).
        
        #
        
        os.system('set -- fp')
        
        while ($# != 0 ):
            if (os.path.isfile(sys.argv[1]/FUNC ) ):
                break
                
                # found it! 
            
            os.system('shift')
        
        if ($# == 0  ):
            print("" + FUNC + ": autoload function not found")1>&2
            
            continue
        
        #		echo auto-loading $FUNC from $1/$FUNC
        
        os.system('aload FUNC sys.argv[1]/FUNC')
    
    os.system('return 0')
}
