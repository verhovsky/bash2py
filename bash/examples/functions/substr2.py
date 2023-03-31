import sys, os, os.path
from stat import *
#
# substr -- a function to emulate the ancient ksh builtin
#
# -l == remove shortest from left
# -L == remove longest from left
# -r == remove shortest from right (the default)
# -R == remove longest from right
def substr () 
{ 
    os.system('local flag pat str')
    
    os.system('local usage="usage: substr -lLrR pat string or substr string pat"')
    
    os.system('local options="l:L:r:R:"')
    
    OPTIND=1
    
    while (os.system('getopts "" + options + "" c')):
        
            if ( "" + c + "" == 'l' or "" + c + "" == 'L' or "" + c + "" == 'r' or "" + c + "" == 'R'):
                flag="-" + c + ""
                
                pat="" + OPTARG + ""
            elif ("" + c + "" == ''?''):
                print("" + usage + "")
                
                os.system('return 1')
    
    if ("" + OPTIND + "" > 1  ):
        os.system('shift  OPTIND -1 ')
    
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
