import sys, os, os.path
from stat import *
#From: "Grigoriy Strokin" <grg@philol.msu.ru>
#Newsgroups: comp.unix.shell
#Subject: fast basename and dirname functions for BASH/SH
#Date: Sat, 27 Dec 1997 21:18:40 +0300
#
#Please send your comments to grg@philol.msu.ru
def basename () 
{ 
    os.system('local name="" + $ + "{1##*/}"')
    
    print("" + $ + "{name%" + sys.argv[2] + "}")
}
def dirname () 
{ 
    os.system('local dir="" + $ + "{1%" + $ + "{1##*/}}"')
    
    "" + $ + "{dir:=./}" != "/"  && dir="" + $ + "{dir%?}"
    
    print("" + dir + "")
}
# Two additional functions:
# 1) namename prints the basename without extension
# 2) ext prints extension of a file, including "."
def namename () 
{ 
    os.system('local name=${1##*/}')
    
    os.system('local name0="" + $ + "{name%.*}"')
    
    print("" + $ + "{name0:-" + name + "}")
}
def ext () 
{ 
    os.system('local name=${1##*/}')
    
    os.system('local name0="" + $ + "{name%.*}"')
    
    os.system('local ext=${name0:+${name#name0}}')
    
    print("" + $ + "{ext:-.}")
}
