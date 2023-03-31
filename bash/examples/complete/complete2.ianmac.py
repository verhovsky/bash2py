import sys, os, os.path
from stat import *
#####
#From: ian@linuxcare.com (Ian Macdonald)
#Newsgroups: comp.unix.shell
#Subject: More bash 2.04 completions
#Date: 12 Aug 2000 09:53:40 GMT
#Organization: Linuxcare, Inc.
#Lines: 274
#Message-ID: <slrn8pa7l2.jgm.ian@lovelorn.linuxcare.com>
#Reply-To: ian@linuxcare.com
#####
# Turn on extended globbing
os.system('shopt -s extglob')
# cvs(1) completion
#
def _cvs () 
{ 
    os.system('local cur prev')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    if (COMP_CWORD == 1  || "" + $ + "{prev:0:1}" == "-"  ):
        COMPREPLY=($( compgen -W 'add admin checkout commit diff \

    else:
        COMPREPLY=( os.popen(' compgen -f cur ').read() )
    
    os.system('return 0')
}
os.system('complete -F _cvs cvs')
# rpm(8) completion. This isn't exhaustive yet, but still provides
# quite a lot of functionality.
# 
