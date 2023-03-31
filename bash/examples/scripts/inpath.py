import sys, os, os.path
from stat import *
#
# Search $PATH for a file the same name as $1; return TRUE if found.
#
command=sys.argv[1]
-n "" + command + ""  || exit(1)
os.system('set `echo PATH | sed 's/^:/.:/
')
while ($# != 0 ):
    os.path.isfile(sys.argv[1]/command ) && exit(0)
    # test -x not universal
    os.system('shift')
exit(1)
