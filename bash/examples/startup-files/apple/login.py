import sys, os, os.path
from stat import *
##
# Set path
##
os.environ['PATH'] = "${HOME}/${MACHTYPE}/bin:${HOME}/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
os.environ['MANPATH'] = "${HOME}/man:/usr/local/share/man:/usr/share/man"
##
# Read user's login
##
if (( os.system('-r ${bash_initdir}/login.mine') ) ):
    os.system('source ${bash_initdir}/login.mine')
