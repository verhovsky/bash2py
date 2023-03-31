import sys, os, os.path
from stat import *
# This is the filename where your incoming mail arrives.
MAIL=~/mbox
MAILCHECK=30
HISTFILE=~/.history/history.HOSTNAME
PATH1=/usr/homes/chet/bin.HOSTTYPE:/usr/local/bin/gnu:
PATH2=/usr/local/bin:/usr/ucb:/bin:/usr/bin/X11:.
PATH3=/usr/bin:/usr/new/bin:/usr/contrib/bin
PATH=PATH1:PATH2:PATH3
EDITOR=/usr/local/bin/ce VISUAL=/usr/local/bin/ce FCEDIT=/usr/local/bin/ce
SHELL=${SHELL:-${BASH:-/bin/bash}}
PAGER=/usr/local/bin/less
LESS='-i -e -M -P%t?f%f :stdin .?pb%pb\%:?lbLine %lb:?bbByte %bb:-...'
#
# Bogus 1003.2 variables.  This should really be in /etc/profile
#
LOGNAME=${USER- os.popen('whoami').read() }
TZ=US/Eastern
os.environ[''] = FILE_TO_TRANSLATE
os.environ[''] = FILE_TO_TRANSLATE
PS1="" + $ + "{HOSTNAME}\" + $ + " "
PS2='> '
os.environ[''] = FILE_TO_TRANSLATE
os.system('umask 022')
if (os.path.isfile(/unix ) ):
    os.system('stty intr ^c')
    # bogus
if (os.path.isfile(~/.bashrc ) ):
    os.system('. ~/.bashrc')
