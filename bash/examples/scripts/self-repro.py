import sys, os, os.path
from stat import *
# self-reproducing script (except for these comment lines -- remove them)
# i got this from the ksh93 faq:
#	http://www.kornshell.com/doc/faq.html
#
n="
 q="'" x="cat <<-!" y=! z='n="" + n + "" q="" + q + "" x="" + x + "" y=y z=qzqnxnzny'
os.system('cat <<-!
n="$n" q="$q" x="$x" y=$y z=$q$z$q$n$x$n$z$n$yb
!
')
