import sys, os, os.path
from stat import *
#From: kaz@cafe.net (Kaz Kylheku)
#Newsgroups: comp.unix.shell
#Subject: Why not roll your own @#$% find! (was: splitting directory off from filename)
#Message-ID: <6n1117$tp1@espresso.cafe.net>
#Date: Fri, 26 Jun 1998 20:47:34 GMT
# $1 = dirname, $2 = pattern, optional $3 = action
def xfind () 
{ 
    os.system('local x')
    
    os.system('local dir="" + sys.argv[1] + ""')
    
    # descend into specified directory
    
    os.system('builtin cd -L "" + sys.argv[1] + ""') || { 
        print("" + $ + "{FUNCNAME}: cannot change dir to " + sys.argv[1] + "")1>&2
        
        os.system('return 1')
    }
    
    #
    
    # default action is to print the filename
    
    #
    
    if (-n "" + sys.argv[3] + ""  ):
        action="" + sys.argv[3] + ""
    else:
        action='printf -- "%s\n"'
    
    # process ordinary files that match pattern
    
    for x in [sys.argv[2]]:
            if (os.path.isfile("" + x + "" ) ):
            os.system('eval "" + action + "" "" + x + ""')
    
    # now descend into subdirectories, avoiding symbolic links
    
    # and directories that start with a period.
    
    for x in [*]:
            if (S_ISDIR(os.stat("" + x + "" ).st_mode) && ! -L "" + x + ""  ):
            os.system('FUNCNAME "" + x + "" "" + sys.argv[2] + "" "" + action + ""')
    
    # finally, pop back up
    
    os.system('builtin cd -L ..')
}
#xfind "$@"
