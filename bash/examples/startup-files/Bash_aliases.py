import sys, os, os.path
from stat import *
# Some useful aliases.
os.system('alias texclean='rm -f *.toc *.aux *.log *.cp *.fn *.tp *.vr *.pg *.ky'')
os.system('alias clean='echo -n "Really clean this directory?";
')
os.system('alias h='history'')
os.system('alias j="jobs -l"')
os.system('alias l="ls -l "')
os.system('alias ll="ls -l"')
os.system('alias ls="ls -F"')
os.system('alias pu="pushd"')
os.system('alias po="popd"')
#
# Csh compatability:
#
os.system('alias unsetenv=unset')
def setenv () 
{ 
    os.environ['$1'] = "$2"
}
# Function which adds an alias to the current shell and to
# the ~/.bash_aliases file.
def add-alias () 
{ 
    os.system('local name=sys.argv[1] value="" + sys.argv[2] + ""')
    
    print("alias name=\'value\'")>> ~/.bash_aliases
    
    os.system('eval alias name=\'value\'')
    
    os.system('alias name')
}
# "repeat" command.  Like:
#
#	repeat 10 echo foo
def repeat () 
{ 
    os.system('local count="" + sys.argv[1] + "" i')
    
    os.system('shift')
    
    for i in [ os.popen('seq 1 "" + count + ""').read() ]:
            os.system('eval "" + $ + "@"')
}
# Subfunction needed by `repeat'.
def seq () 
{ 
    os.system('local lower upper output')
    
    lower=sys.argv[1] upper=sys.argv[2]
    
    if (lower > upper  ):
        os.system('return')
    
    while (lower < upper ):
        print("" + lower + " ")
        
        lower=(lower + 1)
    
    print("" + lower + "")
}
