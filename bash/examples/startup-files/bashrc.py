import sys, os, os.path
from stat import *

    if ( $- == '*i*'):

    else:
        os.system('return')
# bogus
if (os.path.isfile(/unix ) ):
    os.system('alias ls='/bin/ls -CF'')
else:
    os.system('alias ls='/bin/ls -F'')
os.system('alias ll='ls -l'')
os.system('alias dir='ls -ba'')
os.system('alias ss="ps -aux"')
os.system('alias dot='ls .[a-zA-Z0-9_]*'')
os.system('alias news="xterm -g 80x45 -e trn -e -S1 -N &"')
os.system('alias c="clear"')
os.system('alias m="more"')
os.system('alias j="jobs"')
# common misspellings
os.system('alias mroe=more')
os.system('alias pdw=pwd')
os.system('hash -p /usr/bin/mail mail')
if (-z "" + HOST + ""  ):
    os.environ['HOST'] = ${HOSTNAME}
HISTIGNORE="[   ]*:&:bg:fg"
def psgrep () 
{ 
    os.system('ps -aux') | os.system('grep sys.argv[1]') | os.system('grep -v grep')
}
#
# This is a little like `zap' from Kernighan and Pike
#
def pskill () 
{ 
    os.system('local pid')
    
    pid= os.popen('ps -ax | grep sys.argv[1] | grep -v grep | awk '{ print sys.argv[1] }'').read() 
    
    print("killing " + sys.argv[1] + " (process " + pid + ")...")
    
    os.system('kill -9 pid')
    
    print("slaughtered.")
}
def term () 
{ 
    TERM=sys.argv[1]
    
    os.environ[''] = FILE_TO_TRANSLATE
    
    os.system('tset')
}
def xtitle () 
{ 
    print("-e "\033]0;" + $ + "*\007"")
}
def cd () 
{ 
    os.system('builtin cd "" + $ + "@"') && os.system('xtitle HOST: PWD')
}
def bold () 
{ 
    os.system('tput smso')
}
def unbold () 
{ 
    os.system('tput rmso')
}
if (os.path.isfile(/unix ) ):
    def clear () 
    { 
        os.system('tput clear')
    }
def rot13 () 
{ 
    if ($# == 0  ):
        os.system('tr "[a-m][n-z][A-M][N-Z]" "[n-z][a-m][N-Z][A-M]"')
    else:
        os.system('tr "[a-m][n-z][A-M][N-Z]" "[n-z][a-m][N-Z][A-M]"< $1')
}
def watch () 
{ 
    if ($# != 1  ):
        os.system('tail -f nohup.out')
    else:
        os.system('tail -f sys.argv[1]')
}
#
#       Remote login passing all 8 bits (so meta key will work)
#
def rl () 
{ 
    os.system('rlogin $* -8')
}
def setenv () 
{ 
    if ($# != 2  ):
        print("setenv: Too few arguments")
    else:
        os.environ['$1'] = "$2"
}
def chmog () 
{ 
    if ($# != 4  ):
        print("usage: chmog mode owner group file")
        
        os.system('return 1')
    else:
        os.system('chmod sys.argv[1] sys.argv[4]')
        
        os.system('chown sys.argv[2] sys.argv[4]')
        
        os.system('chgrp sys.argv[3] sys.argv[4]')
}
