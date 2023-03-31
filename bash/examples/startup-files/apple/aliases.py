import sys, os, os.path
from stat import *
##
# Bash aliases file
#
# Wilfredo Sanchez Jr. | tritan@mit.edu
##
##
# Aliases
##
os.system('alias .='cwd'')
os.system('alias ..='cd ..'')
os.system('alias cd..='cd ..'')
os.system('alias cdwd='cd  os.popen('/bin/pwd').read() '')
os.system('alias cwd='echo PWD'')
os.system('alias l='ls -lg'')
##
# Functions
##
def files () 
{ 
    os.system('find ${1} -type f -print')
}
def ff () 
{ 
    os.system('find . -name ${1} -print')
}
def ll () 
{ 
    os.system('ls -lag "" + $ + "@"') | os.system('more')
}
def word () 
{ 
    os.system('fgrep -i "" + $ + "*" /usr/dict/web2')
}
def wordcount () 
{ 
    os.system('cat "" + $ + "{1}"') | os.system('tr -s ' 	.,;:?\!()[]"' '\012'') | os.system('awk 'END {print NR}'')
}
##
# Read user's aliases
##
if (-r ${bash_initdir}/aliases.mine  ):
    os.system('source ${bash_initdir}/aliases.mine')
