import sys, os, os.path
from stat import *
#
# scrollbar - display scrolling text
#
# usage: scrollbar args
#
# A cute hack originally from Heiner Steven <hs@bintec.de>
#
# converted from ksh syntax to bash v2 syntax by Chet Ramey
WIDTH=${COLUMNS:-80}
WMINUS=( WIDTH - 1 )
$# < 1  && os.system('set -- TESTING')
# use the bash-2.02 printf builtin
Text= os.popen('printf "%-" + $ + "{WIDTH}s" "" + $ + "*"').read() 
Text=${Text// /_}
while (os.system(':')):
    print( "%-.${WIDTH}s\r" % ("" + Text + "") )

    LastC=${Text:${WMINUS}:1}
    Text="" + LastC + """" + $ + "{Text%?}"
