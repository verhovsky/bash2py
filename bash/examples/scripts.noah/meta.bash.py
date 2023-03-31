import sys, os, os.path
from stat import *
# meta.bash --- meta key frobnications
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created: 1992-06-28
# Last modified: 1993-01-26
# Public domain
# Commentary:
# Code:
#:docstring meta:
# Usage: meta [on|off]
# 
# An argument of "on" will make bash use the 8th bit of any input from
# a terminal as a "meta" bit, i.e bash will be able to use a real meta
# key.
#
# An argument of "off" causes bash to disregard the 8th bit, which is
# assumed to be used for parity instead.
#:end docstring:
def meta () 
{ 
    
        if ( "" + sys.argv[1] + "" == 'on'):
            os.system('bind 'set input-meta On'')
            
            os.system('bind 'set output-meta on'')
            
            os.system('bind 'set convert-meta off'')
        elif ("" + sys.argv[1] + "" == 'off'):
            os.system('bind 'set input-meta Off'')
            
            os.system('bind 'set output-meta off'')
            
            os.system('bind 'set convert-meta on'')
        else:
            print("Usage: meta [on|off]")1>&2
            
            os.system('return 1')
    
    os.system('return 0')
}
os.system('provide meta')
# meta.bash ends here
