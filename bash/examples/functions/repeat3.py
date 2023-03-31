import sys, os, os.path
from stat import *
# From psamuels@jake.niar.twsu.edu (Peter Samuelson)
# posted to usenet, Message-ID: <6rtp8j$2a0$1@jake.niar.twsu.edu>
def repeat () 
{ 
    os.system('local i max')
    
    # note that you can use \$i in the command string
    
    max=sys.argv[1]
    
    os.system('shift')
    
    i=1
    
    while (((i <= max))):
        os.system('eval "" + $ + "@"')
        
        ((i = i + 1))
}
