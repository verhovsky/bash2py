import sys, os, os.path
from stat import *
# Author: P@draigBrady.com
# V1.0  : Nov  3 2006
#
#  Execute a command with a timeout.
#  If the timeout occurs the exit status is 128
#
#  Note there is an asynchronous equivalent of this
#  script packaged with bash (under /usr/share/doc/ in my distro),
#  which I only noticed after writing this.
if (len(sys.argv) < "2"  ):
    print("Usage:    os.popen('basename " + sys.argv[0] + "').read()  timeout_in_seconds command")1>&2
    print("Example:  os.popen('basename " + sys.argv[0] + "').read()  2 sleep 3 || echo timeout")1>&2
    exit(1)
def cleanup () 
{ 
    os.system('kill %12> /dev/null')
    
    #kill sleep $timeout if running
    
    os.system('kill %22> /dev/null') && exit(128)
    
    #kill monitored job if running
}
os.system('set -m')
#enable job control
os.system('trap "cleanup" 17')
#cleanup after timeout or command
timeout=sys.argv[1] && os.system('shift')
#first param is timeout in seconds
os.system('sleep timeout') &
#start the timeout
os.system('"" + $ + "@"')
#start the job
