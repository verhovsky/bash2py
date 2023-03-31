import sys, os, os.path
from stat import *
#Newsgroups: comp.unix.shell
#From: gwc@root.co.uk (Geoff Clare)
#Subject: Re: Determining permissions on a file
#Message-ID: <Dr79nw.DtL@root.co.uk>
#Date: Fri, 10 May 1996 17:23:56 GMT
#Here's a bit of Korn shell that converts the symbolic permissions produced
#by "ls -l" into octal, using only shell builtins.  How to create a script
#combining this with an "ls -l" is left as an exercise...
#
#
# Converted to Bash v2 syntax by Chet Ramey <chet@po.cwru.edu>
#
# usage: showperm modestring
#
# example: showperm '-rwsr-x--x'
#
-z "" + sys.argv[1] + ""  && { print("showperm: usage: showperm modestring")1>&2
exit(2) }
tmode="" + sys.argv[1] + ""
os.system('typeset -i omode sbits')
os.system('typeset pmode')
# check for set-uid, etc. bits
sbits=0
