import sys, os, os.path
from stat import *
# string.bash --- bash emulation of string(3) library routines
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created: 1992-07-01
# Last modified: 1993-09-29
# Public domain
# Conversion to bash v2 syntax done by Chet Ramey
# Commentary:
# Code:
#:docstring strcat:
# Usage: strcat s1 s2
#
# Strcat appends the value of variable s2 to variable s1. 
#
# Example:
#    a="foo"
#    b="bar"
#    strcat a b
#    echo $a
#    => foobar
#
#:end docstring:
###;;;autoload
def strcat () 
{ 
    os.system('local s1_val s2_val')
    
    s1_val=${!1}
    
    # indirect variable expansion
    
    s2_val=${!2}
    
    os.system('eval "" + sys.argv[1] + ""=\'"" + $ + "{s1_val}" + $ + "{s2_val}"\'')
}
#:docstring strncat:
# Usage: strncat s1 s2 $n
# 
# Line strcat, but strncat appends a maximum of n characters from the value
# of variable s2.  It copies fewer if the value of variabl s2 is shorter
# than n characters.  Echoes result on stdout.
#
# Example:
#    a=foo
#    b=barbaz
#    strncat a b 3
#    echo $a
#    => foobar
#
#:end docstring:
###;;;autoload
def strncat () 
{ 
    os.system('local s1="" + sys.argv[1] + ""')
    
    os.system('local s2="" + sys.argv[2] + ""')
    
    os.system('local -i n="" + sys.argv[3] + ""')
    
    os.system('local s1_val s2_val')
    
    s1_val=${!s1}
    
    # indirect variable expansion
    
    s2_val=${!s2}
    
    if (${#s2_val} > ${n}  ):
        s2_val=${s2_val:0:n}
        
        # substring extraction
    
    os.system('eval "" + s1 + ""=\'"" + $ + "{s1_val}" + $ + "{s2_val}"\'')
}
#:docstring strcmp:
# Usage: strcmp $s1 $s2
#
# Strcmp compares its arguments and returns an integer less than, equal to,
# or greater than zero, depending on whether string s1 is lexicographically
# less than, equal to, or greater than string s2.
#:end docstring:
###;;;autoload
def strcmp () 
{ 
    "" + sys.argv[1] + "" == "" + sys.argv[2] + ""  && os.system('return 0')
    
    "" + $ + "{1}" '<' "" + $ + "{2}" > /dev/null && os.system('return -1')
    
    os.system('return 1')
}
#:docstring strncmp:
# Usage: strncmp $s1 $s2 $n
# 
# Like strcmp, but makes the comparison by examining a maximum of n
# characters (n less than or equal to zero yields equality).
#:end docstring:
###;;;autoload
def strncmp () 
{ 
    if (-z "" + $ + "{3}"  || "" + $ + "{3}" < "0"  ):
        os.system('return 0')
    
    if (${3} > ${#1}  && ${3} > ${#2}  ):
        os.system('strcmp "" + sys.argv[1] + "" "" + sys.argv[2] + ""')
        
        os.system('return $?')
    else:
        s1=${1:0:sys.argv[3]}
        
        s2=${2:0:sys.argv[3]}
        
        os.system('strcmp s1 s2')
        
        os.system('return $?')
}
#:docstring strlen:
# Usage: strlen s
#
# Strlen returns the number of characters in string literal s.
#:end docstring:
###;;;autoload
def strlen () 
{ 
    os.system('eval print "\" + $ + "{#" + $ + "{1}}"')
}
#:docstring strspn:
# Usage: strspn $s1 $s2
# 
# Strspn returns the length of the maximum initial segment of string s1,
# which consists entirely of characters from string s2.
#:end docstring:
###;;;autoload
def strspn () 
{ 
    # Unsetting IFS allows whitespace to be handled as normal chars. 
    
    os.system('local IFS=')
    
    os.system('local result="" + $ + "{1%%[!" + $ + "{2}]*}"')
    
    print("${#result}")
}
#:docstring strcspn:
# Usage: strcspn $s1 $s2
#
# Strcspn returns the length of the maximum initial segment of string s1,
# which consists entirely of characters not from string s2.
#:end docstring:
###;;;autoload
def strcspn () 
{ 
    # Unsetting IFS allows whitspace to be handled as normal chars. 
    
    os.system('local IFS=')
    
    os.system('local result="" + $ + "{1%%[" + $ + "{2}]*}"')
    
    print("${#result}")
}
#:docstring strstr:
# Usage: strstr s1 s2
# 
# Strstr echoes a substring starting at the first occurrence of string s2 in
# string s1, or nothing if s2 does not occur in the string.  If s2 points to
# a string of zero length, strstr echoes s1.
#:end docstring:
###;;;autoload
def strstr () 
{ 
    # if s2 points to a string of zero length, strstr echoes s1
    
    ${#2} == 0  && { 
        print("" + sys.argv[1] + "")
        
        os.system('return 0')
    }
    
    # strstr echoes nothing if s2 does not occur in s1
    
    
        if ( "" + sys.argv[1] + "" == '*$2*'):

        else:
            os.system('return 1')
    
    # use the pattern matching code to strip off the match and everything
    
    # following it
    
    first=${1/sys.argv[2]*/}
    
    # then strip off the first unmatched portion of the string
    
    print("" + $ + "{1##" + first + "}")
}
#:docstring strtok:
# Usage: strtok s1 s2
#
# Strtok considers the string s1 to consist of a sequence of zero or more
# text tokens separated by spans of one or more characters from the
# separator string s2.  The first call (with a non-empty string s1
# specified) echoes a string consisting of the first token on stdout. The
# function keeps track of its position in the string s1 between separate
# calls, so that subsequent calls made with the first argument an empty
# string will work through the string immediately following that token.  In
# this way subsequent calls will work through the string s1 until no tokens
# remain.  The separator string s2 may be different from call to call.
# When no token remains in s1, an empty value is echoed on stdout.
#:end docstring:
###;;;autoload
def strtok () 
{ 
    os.system(':')
}
#:docstring strtrunc:
# Usage: strtrunc $n $s1 {$s2} {$...}
#
# Used by many functions like strncmp to truncate arguments for comparison.
# Echoes the first n characters of each string s1 s2 ... on stdout. 
#:end docstring:
###;;;autoload
def strtrunc () 
{ 
    n=sys.argv[1]
    
    os.system('shift')
    
    for z in ["" + $ + "@"]:
            print("" + $ + "{z:0:" + n + "}")
}
os.system('provide string')
# string.bash ends here
