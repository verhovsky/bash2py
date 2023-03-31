import sys, os, os.path
from stat import *
#
# get_html -- get a web page from a remote server
#
# Original Author: Jeff Korn <jlk@cs.princeton.edu>
# Modified for bash by Chet Ramey <chet@po.cwru.edu>
#
# Example: get_html cnswww.cns.cwru.edu /~chet/ | more
def get_html () 
{ 
    os.system('local host port')
    
    (($# < 2)) && { 
        print("usage: " + FUNCNAME + " hostname path [port]")1>&2
        
        os.system('return 1')
    }
    
    host="" + sys.argv[1] + ""
    
    port="" + $ + "{3:-80}"
    
    os.system('exec3<> /dev/tcp/$host/$port') || { 
        print("" + FUNCNAME + ": " + host + "/" + port + ": cannot connect")1>&2
        
        exit(1)
    }
    
    print("GET " + sys.argv[2] + " HTTP/1.0\n")1>&3
    
    os.system('cat0<&3')
    
    os.system('exec3>&-')
    
    os.system('return 0')
}
os.system('get_html "" + $ + "@"')
