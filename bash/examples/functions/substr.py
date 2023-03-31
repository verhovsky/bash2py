import sys, os, os.path
from stat import *
#
# substr -- a function to emulate the ancient ksh builtin
#
#
# -l == shortest from left
# -L == longest from left
# -r == shortest from right (the default)
# -R == longest from right
def substr () 
{ 
    os.system('local flag pat str')
    
    os.system('local usage="usage: substr -lLrR pat string or substr string pat"')
    
    
        if ( "" + sys.argv[1] + "" == '-l' or "" + sys.argv[1] + "" == '-L' or "" + sys.argv[1] + "" == '-r' or "" + sys.argv[1] + "" == '-R'):
            flag="" + sys.argv[1] + ""
            
            pat="" + sys.argv[2] + ""
            
            os.system('shift 2')
        elif ("" + sys.argv[1] + "" == '-*'):
            print("substr: unknown option: " + sys.argv[1] + "")
            
            print("" + usage + "")
            
            os.system('return 1')
        else:
            flag="-r"
            
            pat="" + sys.argv[2] + ""
    
    if (len(sys.argv) == 0  || len(sys.argv) > 2  ):
        print("substr: bad argument count")
        
        os.system('return 2')
    
    str="" + sys.argv[1] + ""
    
    #
    
    # We don't want -f, but we don't want to turn it back on if
    
    # we didn't have it already
    
    #
    
    
        if ( "" + $ + "-" == '"*f*"'):

        else:
            fng=1
            
            os.system('set -f')
    
    
        if ( "" + flag + "" == '-l'):
            str="" + $ + "{str#" + pat + "}"
            
            # substr -l pat string
        elif ("" + flag + "" == '-L'):
            str="" + $ + "{str##" + pat + "}"
            
            # substr -L pat string
        elif ("" + flag + "" == '-r'):
            str="" + $ + "{str%" + pat + "}"
            
            # substr -r pat string
        elif ("" + flag + "" == '-R'):
            str="" + $ + "{str%%" + pat + "}"
            
            # substr -R pat string
        else:
            str="" + $ + "{str%" + sys.argv[2] + "}"
            
            # substr string pat
    
    print("" + str + "")
    
    #
    
    # If we had file name generation when we started, re-enable it
    
    #
    
    if ("" + fng + "" == "1"  ):
        os.system('set +f')
}
