import sys, os, os.path
from stat import *
def jj () 
{ 
    p= os.popen('jobs sys.argv[1]').read() 
    
    print("p")
    
    
        if ( "" + p + "" == '[*'):
            print("matches '[*'")
        else:
            print("not a match\?")
}
