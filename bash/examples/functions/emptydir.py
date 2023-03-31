import sys, os, os.path
from stat import *
#
#Derived from:
#
#From: damercer@mmm.com (Dan Mercer)
#Newsgroups: comp.unix.admin,comp.unix.shell,comp.unix.programmer,comp.sys.sun.admin
#Subject: Re: Command to find out if a directory is empty
#Date: 17 Aug 2000 14:35:56 GMT
#Message-ID: <8ngt8c$fmr$1@magnum.mmm.com>
# usage: emptydir [dirname] ;  default dirname is "."
def emptydir () 
{ 
    os.system('typeset file dir=${1:-.}')
    
    -d $dir || { 
        print("" + FUNCNAME + ": " + dir + " is not a directory")1>&2
        
        os.system('return 2')
    }
    
    for file in [dir/.*, dir/*]:
            
            if ( ${file#dir/} == '.' or ${file#dir/} == '..'):

            elif (${file#dir/} == '\*'):
                -e $file
                
                $?
                
                os.system('return')
            else:
                os.system('return 1')
}
