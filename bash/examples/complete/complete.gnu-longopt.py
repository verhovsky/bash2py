import sys, os, os.path
from stat import *
#
# Originally from:
#
#Message-ID: <3B13EC65.179451AE@wanadoo.fr>
#Date: Tue, 29 May 2001 20:37:25 +0200
#From: Manu Rouat <emmanuel.rouat@wanadoo.fr>
#Subject: [bash] Universal command options completion?
#
#
#In the recent versions of bash (after 2.04) programmable 
#completion is available. A useful completion function
#is , for a particular command, to enumerate all flags
#that can be used in the command. Now, most GNU unix 
#commands have so-called 'long options' for example:
#
#ls --color=always --no-group --size
#
#and these are all listed when you issue a '--help' flag.
#So the idea is to use that, then parse the output of the
#'--help' and reinject this to compgen. The basis of the 
#following 'universal' completion funtion was the _configure_func'
#written by Ian McDonnald (or is it Chet Ramey ?)
#A dedicated function will always be better, but this is quite
#convenient. I chose to use 'long options' because they are
#easy to parse and explicit too (it's the point I guess...)
#Lots of room for improvement !
def _longopt_func () 
{ 
    
        if ( "" + sys.argv[2] + "" == '-*'):

        else:
            os.system('return')
    
    
        if ( "" + sys.argv[1] + "" == '\~*'):
            os.system('eval cmd=sys.argv[1]')
        else:
            cmd="" + sys.argv[1] + ""
    
    COMPREPLY=( os.popen('"" + cmd + "" --help | sed  -e '/--/!d' -e 's/.*--\([^ ]*\').read() .*/--\1/'| grep ^"" + sys.argv[2] + "" |sort -u))
}
os.system('complete -o default -F _longopt_func ldd wget bash id info')
# some examples that work
