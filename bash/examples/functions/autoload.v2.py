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
# usage: autoload [-pu] [func ...]
#
# options:
#	-p	print in a format that can be reused as input
#	-u	unset each function and remove it from the autoload list
#
# The first cut of this was by Bill Trost, trost@reed.edu
#
# Chet Ramey
# chet@ins.CWRU.Edu
os.system('unset _AUTOLOADS')
_aindex=0
#
# Declare a function ($1) to be autoloaded from a file ($2) when it is first
# called.  This defines a `temporary' function that will `.' the file 
# containg the real function definition, then execute that new definition with
# the arguments given to this `fake' function.  The autoload function defined
# by the file and the file itself *must* be named identically.
#
def _aload () 
{ 
    os.system('eval sys.argv[1] '() {  . 'sys.argv[2]' ; 'sys.argv[1]' "" + $ + "@" ; return $? ; }'')
    
    os.system('_autoload_addlist "" + sys.argv[1] + ""')
}
def _autoload_addlist () 
{ 
    os.system('local i=0')
    
    while (((i < _aindex))):
        
            if ( "" + $ + "{_AUTOLOADS[i]}" == '"$1"'):
                os.system('return 1')
        
        ((i += 1))
    
    _AUTOLOADS[_aindex]="" + sys.argv[1] + ""
    
    ((_aindex += 1))
    
    os.system('return 0')
}
def _autoload_dump () 
{ 
    os.system('local func')
    
    for func in [${_AUTOLOADS[@]}]:
            -n "" + sys.argv[1] + ""  && print("autoload ")
        
        print("" + func + "")
}
# Remove $1 from the list of autoloaded functions
def _autoload_remove_one () 
{ 
    os.system('local i=0 nnl=0')
    
    os.system('local -a nlist')
    
    while (((i < _aindex))):
        
            if ( "" + $ + "{_AUTOLOADS[i]}" == '"$1"'):

            else:
                nlist[nnl]="" + $ + "{_AUTOLOADS[i]}"
                
                ((nnl += 1))
        
        ((i += 1))
    
    os.system('unset _AUTOLOADS _aindex')
    
    os.system('eval _AUTOLOADS=(${nlist[@]})')
    
    _aindex=nnl
}
# Remove all function arguments from the list of autoloaded functions
def _autoload_remove () 
{ 
    os.system('local func i es=0')
    
    # first unset the autoloaded functions
    
    for func in ["" + $ + "@"]:
            i=0
        
        while (((i < _aindex))):
            
                if ( "" + $ + "{_AUTOLOADS[i]}" == '"$func"'):
                    os.system('unset -f func')
                    
                    break
            
            ((i += 1))
        
        if (((i == _aindex)) ):
            print("autoload: " + func + ": not an autoloaded function")1>&2
            
            es=1
    
    # then rebuild the list of autoloaded functions
    
    for func in ["" + $ + "@"]:
            os.system('_autoload_remove_one "" + func + ""')
    
    os.system('return es')
}
#
# Search $FPATH for a file the same name as the function given as $1, and
# autoload the function from that file.  There is no default $FPATH.
#
def autoload () 
{ 
    os.system('local -a fp')
    
    os.system('local _autoload_unset nfp i')
    
    if ((($# == 0)) ):
        os.system('_autoload_dump')
        
        os.system('return 0')
    
    OPTIND=1
    
    while (os.system('getopts pu opt')):
        
            if ( "" + opt + "" == 'p'):
                os.system('_autoload_dump printable')
                
                os.system('return 0')
            elif ("" + opt + "" == 'u'):
                _autoload_unset=y
            else:
                print("autoload: usage: autoload [-pu] [function ...]")1>&2
                
                os.system('return 1')
    
    os.system('shift ( OPTIND - 1 )')
    
    if (-n "" + _autoload_unset + ""  ):
        os.system('_autoload_remove "" + $ + "@"')
        
        os.system('return $?')
    
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
    
    # This turns $FPATH into an array, substituting `.' for `'
    
    #
    
    os.system('eval fp=($(
')
    
    nfp=${#fp[@]}
    
    for FUNC in ["" + $ + "@"]:
            i=0
        
        while (((i < nfp))):
            if (os.path.isfile(${fp[i]}/FUNC ) ):
                break
                
                # found it! 
            
            ((i += 1))
        
        if (((i == nfp)) ):
            print("autoload: " + FUNC + ": autoload function not found")1>&2
            
            es=1
            
            continue
        
        #		echo auto-loading $FUNC from ${fp[i]}/$FUNC
        
        os.system('_aload FUNC ${fp[i]}/FUNC')
        
        es=0
    
    os.system('return es')
}
