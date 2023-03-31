import sys, os, os.path
from stat import *
#Date: Wed, 31 Jan 2001 12:53:56 -0800
#From: Aaron Smith <aaron@mutex.org>
#To: freebsd-ports@freebsd.org
#Subject: useful bash completion function for pkg commands
#Message-ID: <20010131125356.G52003@gelatinous.com>
#hi all. i just wanted to share this bash completion function i wrote that
#completes package names for pkg_info and pkg_delete. i find this a great
#help when dealing with port management. programmed completion requires
#bash-2.04.
def _pkg_func () 
{ 
    os.system('local cur')
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    if ($cur == '-' ):
        if (${COMP_WORDS[0]} == 'pkg_info' ):
            COMPREPLY=(-a -c -d -D -i -k -r -R -p -L -q -I -m -v -e -l)
            
            os.system('return 0')
        else:
            if (${COMP_WORDS[0]} == 'pkg_delete' ):
                COMPREPLY=(-v -D -d -n -f -p)
                
                os.system('return 0')
    
    COMPREPLY=( os.popen('compgen -d /var/db/pkg/cur | sed sN/var/db/pkg/NNg').read() )
    
    os.system('return 0')
}
os.system('complete -F _pkg_func pkg_delete pkg_info')
