import sys, os, os.path
from stat import *
# Date: Fri, 11 Oct 91 11:22:36 edt
# From: friedman@gnu.ai.mit.edu
# To: bfox@gnu.ai.mit.edu
# A replacement for dirname(1).  This one appears less often on some
# systems I use than basename(1), and I really depend on it for some
# things.  Usage: dirname [path]
def dirname () 
{ 
    os.system('local dir="" + sys.argv[1] + ""')
    
    os.system('local tdir="" + $ + "{dir%/}"')
    
    # Strip trailing '/' characters from dir (unusual that this should
    
    # ever occur, but dirname(1) seems to deal with it.)
    
    while ("" + $ + "{tdir}" != "" + $ + "{dir}" ):
        tdir="" + $ + "{dir}"
        
        dir="" + $ + "{tdir%/}"
    
    print("" + $ + "{dir%/*}")
}
