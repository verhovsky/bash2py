import sys, os, os.path
from stat import *
# aref.bash --- pseudo-array manipulating routines
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created 1992-07-01
# Last modified: 1993-02-03
# Public domain
# Conversion to bash v2 syntax done by Chet Ramey
# Commentary:
# Code:
#:docstring aref:
# Usage: aref NAME INDEX
#
# In array NAME, access element INDEX (0-origin)
#:end docstring:
###;;;autoload
def aref () 
{ 
    os.system('local name="" + sys.argv[1] + ""')
    
    os.system('local index="" + sys.argv[2] + ""')
    
    os.system('set -- ${!name}')
    
    index > 1  && os.system('shift index')
    
    print("sys.argv[1]")
}
#:docstring string_aref:
# Usage: aref STRING INDEX
#
# Echo the INDEXth character in STRING (0-origin) on stdout. 
#:end docstring:
###;;;autoload
def string_aref () 
{ 
    os.system('local stuff=${1:sys.argv[2]}')
    
    print("${stuff:0:1}")
}
os.system('provide aref')
# aref.bash ends here
