import sys, os, os.path
from stat import *
# bash_version.bash --- get major and minor components of bash version number
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created: 1993-01-26
# Last modified: 1993-01-26
# Public domain
# Converted to bash v2 syntax by Chet Ramey
# Commentary:
# Code:
#:docstring bash_version:
# Usage: bash_version {major|minor}
#
# Echo the major or minor number of this version of bash on stdout, or
# just echo $BASH_VERSION if no argument is given. 
#:end docstring:
###;;;autoload
def bash_version () 
{ 
    os.system('local major minor')
    
    
        if ( "" + sys.argv[1] + "" == 'major'):
            print("" + $ + "{BASH_VERSION/.*/}")
        elif ("" + sys.argv[1] + "" == 'minor'):
            major="" + $ + "{BASH_VERSION/.*/}"
            
            minor="" + $ + "{BASH_VERSION#" + $ + "{major}.}"
            
            print("" + $ + "{minor%%.*}")
        elif ("" + sys.argv[1] + "" == 'patchlevel'):
            minor="" + $ + "{BASH_VERSION#*.*.}"
            
            print("" + $ + "{minor%(*}")
        elif ("" + sys.argv[1] + "" == 'version'):
            minor=${BASH_VERSION/#*.*./}
            
            print("${BASH_VERSION/%.minor/}")
        elif ("" + sys.argv[1] + "" == 'release'):
            print("${BASH_VERSION%(*}")
        elif ("" + sys.argv[1] + "" == 'build'):
            minor="" + $ + "{BASH_VERSION#*.*.*(}"
            
            print("${minor%)}")
        else:
            print("" + $ + "{BASH_VERSION}")
}
os.system('provide bash_version')
# bash_version.bash ends here
