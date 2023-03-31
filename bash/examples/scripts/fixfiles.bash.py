import sys, os, os.path
from stat import *
#
# From: c2a192@ugrad.cs.ubc.ca (Kazimir Kylheku)
# Newsgroups: comp.unix.shell,comp.os.linux.misc
# Subject: GNU Bash Script to fix filenames
# Date: 28 Mar 1996 14:54:43 -0800
# Organization: Computer Science, University of B.C., Vancouver, B.C., Canada
#
#This is a script which takes a list of directories, descends through each one
#and ``corrects'' filenames that:
#
#   -	contain filename globbing characters: * ? [ ]
#   -	quote characters: ' "
#   -	control characters: 0-31 (127 is not dealt with---oops)
#   -	- or + as the first character
#
# The GNU version of 'tr' is required. Also requires 'sed'.
#
# Script to process a given list of directories recursively
# and rename each file to something that is reasonable.
#
# The rules are:
#
# 1. replace each space, [, ], *, ", and ' character in the name with a
#    period.
# 2. replace each control character 1..31 with a printable character obtained
#    by adding 64 to the ascii value. ^A becomes A, ^B becomes B and so on.
# 3. replace a - or + occuring at the beginning of the name with a #
#
# 4. if the resulting name has been changed in any way, then
# 5.    if a file of the new name already exists, then
# 6.            add a . to the new name and goto step 5.
# 7. rename the old name to the new name
#
# written by Kaz Kylheku <kaz@cafe.net>
# March 1996
# Vancouver, Canada
#
# requires GNU 'bash', GNU 'tr', and some sort of 'sed' program.
#
# minimal conversion to bash v2 syntax done by Chet Ramey
def processfile () 
{ 
    new_name="`echo -n " + sys.argv[1] + " | tr '\173\175\052\077\042\047 ' '.......' |

    
    if ("" + new_name + "" != "" + sys.argv[1] + ""  ):
        while (os.path.isfile("" + new_name + "" )):
            new_name="" + $ + "{new_name}."
        
        print("changing \"" + sys.argv[1] + "\" to \"" + new_name + "\" in  os.popen('pwd').read() ")
        
        os.system('mv -- "" + sys.argv[1] + "" "" + new_name + ""')
}
def processdir () 
{ 
    os.system('set -f')
    
    os.system('local savepwd="" + PWD + ""')
    
    if (os.chdir("$1") ):
        os.system('set +f')
        
        for file in [*]:
                    os.system('set -f')
            
            if ("" + file + "" != "."  && "" + file + "" != ".."  ):
                if (-L "" + file + ""  ):
                    print("skipping symlink" file in  os.popen('pwd').read() )
                else:
                    if (S_ISDIR(os.stat("" + file + "" ).st_mode) ):
                        os.system('processdir "" + file + ""')
                    else:
                        if (os.path.isfile("" + file + "" ) ):
                            os.system('processfile "" + file + ""')
        
        os.chdir("$savepwd")
}
os.system('shopt -s nullglob dotglob')
if ($# == 0  ):
    print("" + sys.argv[0] + ": must specify a list of directories")1>&2
    print("" + sys.argv[0] + ": usage: " + sys.argv[0] + " directory [directory ...]")1>&2
    exit(2)
while ($# != 0 ):
    os.system('processdir "" + sys.argv[1] + ""')
    os.system('shift')
exit(0)
