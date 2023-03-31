import sys, os, os.path
from stat import *
# Date: Fri, 11 Oct 91 11:22:36 edt
# From: friedman@gnu.ai.mit.edu
# To: bfox@gnu.ai.mit.edu
# A replacement for basename(1).  Not all the systems I use have this
# program.  Usage: basename [path] {extension}
def basename () 
{ 
    os.system('local path="" + sys.argv[1] + ""')
    
    os.system('local suffix="" + sys.argv[2] + ""')
    
    os.system('local tpath="" + $ + "{path%/}"')
    
    # Strip trailing '/' characters from path (unusual that this should
    
    # ever occur, but basename(1) seems to deal with it.)
    
    while ("" + $ + "{tpath}" != "" + $ + "{path}" ):
        tpath="" + $ + "{path}"
        
        path="" + $ + "{tpath%/}"
    
    path="" + $ + "{path##*/}"
    
    # Strip off pathname
    
    print("${path%${suffix}}")
    
    # Also strip off extension, if any.
}
