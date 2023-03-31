import sys, os, os.path
from stat import *
#Newsgroups: comp.unix.admin,comp.unix.solaris,comp.unix.shell
#From: gwc@root.co.uk (Geoff Clare)
#Subject: Re: timeout -t <sec> <unix command> (Re: How to give rsh a shorter timeout?)
#Message-ID: <EoBxrs.223@root.co.uk>
#Date: Fri, 13 Feb 1998 18:23:52 GMT
#
# Conversion to bash v2 syntax done by Chet Ramey <chet@po.cwru.edu
# UNTESTED
#
prog=${0##*/}
usage="usage: " + prog + " [-signal] [timeout] [:interval] [+delay] [--] <command>"
SIG=-TERM
# default signal sent to the process when the timer expires
timeout=60
# default timeout
interval=15
# default interval between checks if the process is still alive
delay=2
# default delay between posting the given signal and
# destroying the process (kill -KILL)
while (os.system(':')):
    
        if ( sys.argv[1] == '--'):
            os.system('shift')
            break
        elif (sys.argv[1] == '-*'):
            SIG=sys.argv[1]
        elif (sys.argv[1] == '[0-9]*'):
            timeout=sys.argv[1]
        elif (sys.argv[1] == ':*'):
            EXPR='..\(.*\)'
            interval= os.popen('expr x"" + sys.argv[1] + "" : "" + EXPR + ""').read() 
        elif (sys.argv[1] == '+*'):
            EXPR='..\(.*\)'
            delay= os.popen('expr x"" + sys.argv[1] + "" : "" + EXPR + ""').read() 
        else:
            break
    os.system('shift')

    if ( $# == '0'):
        print("" + prog + ": " + usage + "")1>&2
        exit(2)
( for t in [timeout, delay]:
    while (((t > interval))):
        os.system('sleep interval')
        os.system('kill -0 $$') || exit()
        t=( t - interval )
    os.system('sleep t')
    os.system('kill SIG $$') && os.system('kill -0 $$') || exit()
    SIG=-KILL ) 2> /dev/null &
os.system('exec "" + $ + "@"')
