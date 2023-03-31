import sys, os, os.path
from stat import *
#
# .kshenv -- functions and aliases to provide the beginnings of a ksh 
#	     environment for bash.
#
# Chet Ramey
# chet@ins.CWRU.Edu
#
#
# These are definitions for the ksh compiled-in `exported aliases'.  There
# are others, but we already have substitutes for them: "history", "type",
# and "hash".
#
os.system('alias r="fc -s"')
os.system('alias functions="typeset -f"')
os.system('alias integer="typeset -i"')
os.system('alias nohup="nohup "')
os.system('alias command="command "')
os.system('alias stop="kill -s STOP"')
os.system('alias redirect="command exec"')
os.system('alias hist="fc"')
#
# An almost-ksh compatible `whence' command.  This is as hairy as it is 
# because of the desire to exactly mimic ksh (whose behavior was determined
# empirically).
# 
# This depends somewhat on knowing the format of the output of the bash
# `builtin type' command.
#
