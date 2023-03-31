import sys, os, os.path
from stat import *
# C-shell compatabilty package.
# setenv VAR VALUE
def setenv () 
{ 
    os.environ['$1'] = "$2"
}
def unsetenv () 
{ 
    os.system('unset sys.argv[1]')
}
# Can't write foreach yet.  Need pattern matching, and a few extras.
def foreach () 
{ 
    print("'Can'\''t do `foreach'\'' yet.  Type "help for".'")
}
# Make this work like csh's.  Special case "term" and "path".
#set () {
#}
def chdir () 
{ 
    os.system('builtin cd "" + $ + "@"')
}
# alias - convert csh alias commands to bash functions
# from Mohit Aron <aron@cs.rice.edu>
# posted to usenet as <4i5p17$bnu@larry.rice.edu>
