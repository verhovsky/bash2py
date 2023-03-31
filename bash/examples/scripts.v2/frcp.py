import sys, os, os.path
from stat import *
#
# original from:
#
# @(#) frcp.ksh 2.2 93/11/14
# 92/06/29 john h. dubois iii (john@armory.com)
# 92/10/14 Cleaned up, improved, added -d and -r options
# 92/11/11 Made work with a dest of '.'
# 93/07/09 Added -l and -n options, & login as anonymous if no .netrc entry
# 93/11/14 Use either passwd or password in .netrc, since ftp does.
#
# conversion to bash v2 syntax by Chet Ramey
#
# frcp: ftp front end with rcp-like syntax.
# Note: requires any machine names given to be listed with
#       user and password in .netrc.  If not, anonymous FTP is
#	done.
#
# full path to ftp binary
if (-x /usr/bin/ftp  ):
    FTP=/usr/bin/ftp
else:
    if (-x /usr/ucb/ftp  ):
        FTP=/usr/ucb/ftp
    else:
        FTP=ftp
def istrue () 
{ 
    os.system('test 0 != "" + sys.argv[1] + ""')
}
def isfalse () 
{ 
    os.system('test 0 == "" + sys.argv[1] + ""')
}
# For each filename given, put the filename in filename[n]
# and the machine it is on in machine[n].
def SplitNames () 
{ 
    os.system('typeset file')
    
    os.system('typeset -i i=1')
    
    os.system('unset filename[*] machine[*]')
    
    for file in ["" + $ + "@"]:
            
            if ( "" + file + "" == '*:*'):
                machine[i]=${file%%:*}
            else:
                machine[i]=LocalMach
        
        filename[i]=${file#*:}
        
        i+=1
}
def verboseprint () 
{ 
    print("" + $ + "@")
    
    print("" + $ + "@")1>&2
}
def MakeDir () 
{ 
    OFS=IFS
    
    os.system('local IFS=/ dir component')
    
    
        if ( "" + sys.argv[1] + "" == '/*'):

        else:
            dir=.
    
    os.system('set -- sys.argv[1]')
    
    IFS=OFS
    
    for component in ["" + $ + "@"]:
            dir=dir/component
        
        if (! -d "" + dir + ""  ):
            if (os.system('mkdir "" + dir + ""') ):
                os.system(':')
            else:
                print("Could not make directory " + dir + ".")1>&2
                
                os.system('return 1')
    
    os.system('return 0')
}
def lastisdot () 
{ 
    
        if ( "" + sys.argv[1] + "" == '*/.' or "" + sys.argv[1] + "" == '*/..'):
            os.system('return 0')
        else:
            os.system('return 1')
}
# CopyFiles: issue ftp(TC) commands to copy files.
# Usage: CopyFiles [sourcemachine:]sourcepath ... [destmachine:]destpath
# Global vars:
# Uses LocalMach (should be name of local machine)
# Sets global arrs machine[]/filename[]
