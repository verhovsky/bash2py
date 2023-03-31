import sys, os, os.path
from stat import *
#
# pmtop - poor man's `top' for SunOS 4.x
#
CLEAR=clear
# could also be 'tput clear'
HEADER="USER       PID %CPU %MEM   SZ  RSS TT STAT START  TIME COMMAND"
if (-n "" + LINES + ""  ):
    SS=( LINES - 2 )
else:
    SS=20
while (os.system(':')):
    os.system('CLEAR')
    print("" + HEADER + "")
    os.system('ps -aux') | os.system('sort -nr -k 3') | os.system('sed ${SS}q')
    os.system('sleep 5')
exit(0)
