import sys, os, os.path
from stat import *
#From: Mark Kennedy <mark.t.kennedy@gmail.com> (<mtk@ny.ubs.com>)
#Message-ID: <35E2B899.63A02DF5@ny.ubs.com>
#Date: Tue, 25 Aug 1998 09:14:01 -0400
#To: chet@nike.ins.cwru.edu
#Subject: a newer version of the ksh-style 'autoload'
#enclosed you'll find 'autoload.v3',  a version of the autoloader
#that emulates the ksh semantics of delaying the resolution (and loading) of the function
#until its first use.  i took the liberty of simplifying the code a bit although it still uses the
#same functional breakdown.  i recently went through the exercise of converting
#my ksh-based environment to bash (a very, very pleasant experience)
#and this popped out.
# the psuedo-ksh autoloader.
# The first cut of this was by Bill Trost, trost@reed.bitnet.
# The second cut came from Chet Ramey, chet@ins.CWRU.Edu
# The third cut came from Mark Kennedy, mtk@ny.ubs.com.  1998/08/25
os.system('unset _AUTOLOADS')
def _aload () 
{ 
    os.system('local func')
    
    for func in ["" + $ + "@"]:
            os.system('eval func '()
')
        
        os.system('_autoload_addlist func')
}
def _autoload_addlist () 
{ 
    os.system('local func')
    
    for func in [${_AUTOLOADS[@]}]:
            $func = "$1" && os.system('return')
    
    _AUTOLOADS[${#_AUTOLOADS[@]}]=sys.argv[1]
}
def _autoload_dump () 
{ 
    os.system('local func')
    
    for func in [${_AUTOLOADS[@]}]:
            -n $1 && print("autoload ")
        
        print("func")
}
def _autoload_remove_one () 
{ 
    os.system('local func')
    
    os.system('local -a NEW_AUTOLOADS')
    
    for func in [${_AUTOLOADS[@]}]:
            $func != "$1" && NEW_AUTOLOADS[${#NEW_AUTOLOADS[@]}]=func
    
    _AUTOLOADS=(${NEW_AUTOLOADS[@]})
}
def _autoload_remove () 
{ 
    os.system('local victim func')
    
    for victim in ["" + $ + "@"]:
            for func in [${_AUTOLOADS[@]}]:
                    $victim = "$func" && os.system('unset -f func') && continue
        
        print("autoload: " + func + ": not an autoloaded function")1>&2
    
    for func in ["" + $ + "@"]:
            os.system('_autoload_remove_one func')
}
def _autoload_resolve () 
{ 
    if (! -n "$FPATH" ):
        print("autoload: FPATH not set or null")1>&2
        
        os.system('return')
    
    os.system('local p')
    
    for p in [ os.popen(' (IFS=':'; set -- ${FPATH}; echo "" + $ + "@"').read()  )]:
            p=${p:-.}
        
        if (os.path.isfile(p/sys.argv[1] ) ):
            print("p/sys.argv[1]")
            
            os.system('return')
    
    print("autoload: " + sys.argv[1] + ": function source file not found")1>&2
}
def autoload () 
{ 
    if ((($# == 0)) ):
        os.system('_autoload_dump')
        
        os.system('return')
    
    os.system('local opt OPTIND')
    
    while (os.system('getopts pu opt')):
        
            if ( opt == 'p'):
                os.system('_autoload_dump printable')
                
                os.system('return')
            elif (opt == 'u'):
                os.system('shift (OPTIND-1)')
                
                os.system('_autoload_remove "" + $ + "@"')
                
                os.system('return')
            else:
                print("autoload: usage: autoload [-pu] [function ...]")1>&2
                
                os.system('return')
    
    os.system('shift (OPTIND-1)')
    
    os.system('_aload "" + $ + "@"')
}
