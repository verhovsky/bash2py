import sys, os, os.path
from stat import *
##
# Bourne Again Shell environment file
# Global environment setup
#
# Wilfredo Sanchez Jr. | tritan@mit.edu
# July 09, 1992
#
# MIT Project Athena
#
# ORIGINAL SOURCES: /usr/athena/lib/init/cshrc (ATHENA REL 7.3P)
##
os.environ['ENV_SET'] = "YES"
# avoid repeat
# File creation mask
os.system('umask 022')
# all files created are -rw-r--r--
##
# Load user environment
##
if (os.path.isfile(${bash_initdir}/environment.mine ) ):
    os.system('source ${bash_initdir}/environment.mine')
