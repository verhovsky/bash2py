import sys, os, os.path
from stat import *
#
# Name: dirtree
# Programmer:
#            Hemant T. Shah
#            Life Insurance Data Processing
#            July 12 1994
#
# Description:
#  Print directory tree structure as follows:
#   |___Mail
#     |___scheduler
#     |___cics_scripts
#     |___tar_msdos
#     |___awk
#     |___attributes
#   |___tmp
#   |___News
#     |___dosscsi
#     |___FAQ_xterminal
#     |___shell_history.Z
#     |___FAQ_AIX
#     |___aix_ftp_site
#     |___hp_software
#   |___dnload
#     |___telnet.h
#     |___msdos
#     |___tnetd.tar.Z
#     |___aix
#     |___hp
#   |___xkey.c
#
# Conversion to bash v2 syntax done by Chet Ramey
#	- removed command substitutions calling `basename'
#
ProgramName=${0##*/}
Path="."
ShowAll=1
ShowDir=0
def ExpandDirectory () 
{ 
    os.system('local object')
    
    # Local variable
    
    os.chdir("$1")
    
    for object in [PWD/.??*, PWD/*]:
            if (S_ISDIR(os.stat(object ).st_mode)
        
        # It is a directory ):
            print("" + $ + "{indent}|___" + $ + "{object##*/}/")
            
            indent="" + $ + "{indent}!   "
            
            # Add to indentation
            
            if (-x object  ):
                os.system('ExpandDirectory object')
            
            indent=${indent%????}
            
            # Remove from indentation
        else:
            if (os.path.isfile(object ) ):
                if (((ShowAll == 1)) ):
                    print("" + $ + "{indent}|___" + $ + "{object##*/}")
}
def usage () 
{ 
    print("Usage: " + ProgramName + " [-h] [-f] [-d] [path] ")
    
    print("\t-h       ... display this help message.")
    
    print("\t-f path  ... shows all files and directories below path (default).")
    
    print("\t-d path  ... shows all directories only below path.")
}
