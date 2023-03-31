import sys, os, os.path
from stat import *
# y_or_n_p.bash
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created: 1992-06-18
# Last modified: 1993-03-01
# Public domain
# Conversion to bash v2 syntax done by Chet Ramey
# Commentary:
# Code:
#:docstring y_or_n_p:
# Usage: y_or_n_p QUERY
#
# Print QUERY on stderr, then read stdin for a y-or-n response.  Actually,
# user may type anything they like, but first character must be a `y', `n',
# `q', or `!', otherwise the question is repeated until such an answer is
# obtained.  
#
# If user typed `y', y_or_n_p returns 0.
#
# If user typed `n', y_or_n_p returns 1.
#
# If user typed `!', y_or_n_p returns 2.  This is an indication to the
#  caller that no more queries should be made.  Assume `y' for all the rest. 
#
# If user typed `q', y_or_n_p returns 3.  This is an indication to the
#  caller that no more queries should be made.  Assume `n' for all the rest.
#
#:end docstring:
###;;;autoload
def y_or_n_p () 
{ 
    os.system('local ans')
    
    ! -t 0  && os.system('return 1')
    
    while (-p = raw_input()):
        
            if ( "" + $ + "{ans}" == 'y*' or "" + $ + "{ans}" == 'Y*'):
                os.system('return 0')
            elif ("" + $ + "{ans}" == 'n*' or "" + $ + "{ans}" == 'N*'):
                os.system('return 1')
            elif ("" + $ + "{ans}" == '\!'):
                os.system('return 2')
            elif ("" + $ + "{ans}" == 'q*' or "" + $ + "{ans}" == 'Q*'):
                os.system('return 3')
            else:
                print("Please answer one of \ os.popen('y', \').read() n', \ os.popen('q', or \').read() "\!"'")1>&2
}
#:docstring yes_or_no_p:
# Usage: yes_or_no_p QUERY
#
# Like y_or_n_p, but require a full `yes', `no', `yes!', or `quit' response. 
#:end docstring:
###;;;autoload
def yes_or_no_p () 
{ 
    os.system('local ans')
    
    ! -t 0  && os.system('return 3')
    
    while (-p = raw_input()):
        ans="" + $ + "(echo " + $ + "{ans} | tr '[A-Z]' '[a-z]')"
        
        
            if ( "" + $ + "{ans}" == 'yes'):
                os.system('return 0')
            elif ("" + $ + "{ans}" == 'no'):
                os.system('return 1')
            elif ("" + $ + "{ans}" == 'yes\!'):
                os.system('return 2')
            elif ("" + $ + "{ans}" == 'quit'):
                os.system('return 3')
            else:
                print("Please answer \ os.popen('yes', \').read() no', \ os.popen('yes"\!"', or \').read() quit'")1>&2
}
os.system('provide y_or_n_p')
# y_or_n_p.bash ends here
