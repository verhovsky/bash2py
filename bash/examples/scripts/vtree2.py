import sys, os, os.path
from stat import *
#
# vtree - make a tree printout of the specified directory, with disk usage
#	  in 1k blocks
#
# usage: vtree [-a] [dir]
#
# Original posted to Usenet sometime in February, 1996
# I believe that the original author is Brian S. Hiles <bsh29256@atc.fhda.edu>
#
def usage () 
{ 
    print("vtree: usage: vtree [-a] [dir]")1>&2
}
while (os.system('getopts a opt')):
    
        if ( "" + opt + "" == 'a'):
            andfiles=-a
        else:
            os.system('usage')
            exit(2)
os.system('shift (OPTIND - 1)')
os.environ['BLOCKSIZE'] = 1k
# 4.4 BSD systems need this
$# == 0  && os.system('set .')
while ($# > 0 ):
    os.chdir("$1") || { os.system('shift')
    $# > 1  && 1>&2
    continue }
    print("" + PWD + "")
    os.system('du andfiles') | os.system('sort -k 2f') | os.system('sed -e 's/\([^	]*\)	\(.*\)/\2  (\1)/' -e "s#^" + sys.argv[1] + "##" -e 's#[^/]*/\([^/]*\)$#|____\1#' -e 's#[^/]*/#|    #g'')
    $# > 1  && 
    os.system('shift')
