import sys, os, os.path
from stat import *
#
# xterm_title - print the contents of the xterm title bar
#
# Derived from http://www.clark.net/pub/dickey/xterm/xterm.faq.html#how2_title
#
P=${0##*/}
-z "" + DISPLAY + ""  && { print("" + $ + "{P}: not running X")1>&2
exit(1) }
if (-z "" + TERM + ""  || "" + TERM + "" != "xterm"  ):
    print("" + $ + "{P}: not running in an xterm")1>&2
    exit(1)
os.system('exec< /dev/tty')
old= os.popen('stty -g').read() 
os.system('stty raw -echo min 0 time ${1-10}')
print("\033[21t\c")> /dev/tty
IFS='' read -r a
os.system('stty old')
b=${a#???}
print("" + $ + "{b%??}")
exit(0)
