import sys, os, os.path
from stat import *
# To: chet@ins.CWRU.Edu
# Subject: Bash functions
# From: Sandeep Mehta <sxm@philabs.Philips.Com>
# print MH folders, useful only because folders(1) doesn't print
# mod date/times
def mhfold () 
{ 
    list= os.popen('folders | awk '{if (1 < NR) print sys.argv[1]}'').read() 
    
    os.system('/bin/ls -lag ~/Mail> /tmp/fold$$')
    
    for i in [list]:
            os.system('grep i /tmp/fold$$')
    
    os.system('/bin/rm -f /tmp/fold$$')
}
