import sys, os, os.path
from stat import *
##
# Bourne Again Shell config file
#
# Wilfredo Sanchez Jr. | tritan@mit.edu
# July 09, 1992
#
# MIT Project Athena
#
# ORIGINAL SOURCES: /usr/athena/lib/init/cshrc (ATHENA REL 7.3P)
##
default_initdir=/usr/share/init
default_bash_initdir=${default_initdir}/bash
user_initdir=~/Library/init
user_bash_initdir=${user_initdir}/bash
if (-r ${user_bash_initdir}  ):
    initdir=${user_initdir}
    bash_initdir=${user_bash_initdir}
else:
    initdir=${default_initdir}
    bash_initdir=${default_bash_initdir}
# SET UP HOST-DEPENDANT VARIABLES, ETC.
host= os.popen('echo $(hostname').read()  | tr A-Z a-z)
user= os.popen('whoami').read() 
os.environ['HOST'] = ${host}
os.environ['USER'] = ${user}
# User ID
if (-z "" + $ + "{uid}"  ):
    uid= os.popen('id | cut -d = -f 2 | cut -d \( -f 1').read() 
# SET COMMAND SEARCH PATH AND MAN PATH
if (os.path.isfile(${bash_initdir}/path ) ):
    os.system('source ${bash_initdir}/path')
# ENVIRONMENT SETUP
if (-n "" + $ + "{PS1}"  ):
    interactive="YES"
if (-z "" + $ + "{ENV_SET}"  ):
    if (os.path.isfile(${default_bash_initdir}/environment ) ):
        #echo "Initializing environment..."
        os.system('source ${default_bash_initdir}/environment')
if (-r ${default_bash_initdir}/bash.defaults  ):
    os.system('source ${default_bash_initdir}/bash.defaults')
# DEFAULT LOGIN SOURCES
if (os.path.isfile(${bash_initdir}/rc.mine ) ):
    os.system('source ${bash_initdir}/rc.mine')
if ("" + $ + "{interactive}" == "YES"  ):
    # These aren't useful for non-interactive sessions
    if (os.path.isfile(${default_bash_initdir}/aliases ) ):
        os.system('source ${default_bash_initdir}/aliases')
