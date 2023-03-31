import sys, os, os.path
from stat import *
# Bourne Again SHell init file.
#
# Files you make look like rw-rw-r
os.system('umask 002')
# Don't make useless coredump files.  If you want a coredump,
# say "ulimit -c unlimited" and then cause a segmentation fault.
os.system('ulimit -c 0')
# Sometimes, there are lots of places that one can find tex inputs.
os.environ['TEXINPUTS'] = .:$HOME/bin:/usr/lib/tex/inputs:/usr/local/lib/tex/inputs
# Where's the Gnu stuff at?
GNU=/usr/gnu/bin
X11=/usr/bin/X11
UTIL_PATH=GNU:X11
STANDARD_PATH=/usr/local/bin:/usr/ucb:/bin:/usr/bin:/usr/etc:/etc:/usr/games
if (S_ISDIR(os.stat(HOME/bin/HOSTTYPE ).st_mode) ):
    MY_PATH=HOME/bin/HOSTTYPE
if (S_ISDIR(os.stat(HOME/bin ).st_mode) ):
    MY_PATH=MY_PATH:HOME/bin
if (S_ISDIR(os.stat(/usr/hosts ).st_mode) ):
    STANDARD_PATH=STANDARD_PATH:/usr/hosts
PATH=.:MY_PATH:UTIL_PATH:STANDARD_PATH
# If not running interactively, then return
if (-z "" + PS1 + ""  ):
    os.system('return')
# Set ignoreeof if you don't want EOF as the sole input to the shell to
# immediately signal a quit condition.  This only happens at the start
# of a line if the line is empty, and you haven't just deleted a character
# with C-d.  I turn this on in ~/.bash_profile so that only login shells
# have the right to be obnoxious.
# set -o ignoreeof
# Set auto_resume if you want to resume on "emacs", as well as on
# "%emacs".
auto_resume=exact
# Set notify if you want to be asynchronously notified about background
# job completion.
os.system('set -o notify')
# Make it so that failed `exec' commands don't flush this shell.
os.system('shopt -s execfail')
if (-z "" + LOGIN_SHELL + ""  ):
    PS1="\u@\h\" + $ + " "
HISTSIZE=256
MAILCHECK=60
# A couple of default aliases.
os.system('alias j='jobs -l'')
os.system('alias po=popd')
os.system('alias pu=pushd')
os.system('alias ls='ls -F'')
os.path.isfile(~/.bash_aliases ) && os.system('. ~/.bash_aliases')
