import sys, os, os.path
from stat import *
#
# The Bash script executes a command with a time-out.
# Based on the Bash documentation example.
#
# Upon time-out expiration SIGTERM (15) is sent to the process.  If the signal
# is blocked, then the subsequent SIGKILL (9) terminates it.
# Dmitry V Golovashkin (E-mail: dvg@ieee.org)
#
script_name="" + $ + "{0##*/}"
# Default values.
os.system('readonly param_timeout=5')
os.system('readonly param_interval=1')
os.system('readonly param_delay=1')
os.system('declare -i timeout=param_timeout')
os.system('declare -i interval=param_interval')
os.system('declare -i delay=param_delay')
blue="" + $ + "(tput setaf 4)"
bold_red="" + $ + "(tput bold; tput setaf 1)"
off="" + $ + "(tput sgr0)"
def print_usage () 
{ 
    os.system('cat') <<EOF

Synopsis:  $script_name [-t timeout] [-i interval] [-d delay] command

Executes the command with a time-out.  Upon time-out expiration SIGTERM (15) is
sent to the process.  If SIGTERM signal is blocked, then the subsequent SIGKILL
(9) terminates it.

$blue-t timeout$off
    Number of seconds to wait for command completion.
    Default value: $param_timeout seconds.  In some practical situations
    this value ${bold_red}must$off be increased (for instance -t 180) to allow
    the command to complete.

$blue-i interval$off
    Interval between checks if the process is still alive.
    Positive integer, default value: $param_interval seconds.
    Default value is OK for most situations.

$blue-d delay$off
    Delay between posting the SIGTERM signal and destroying the process by
    SIGKILL.  Default value: $param_delay seconds.
    Default value is OK for most situations.

As of today, Bash does not support floating point arithmetic (sleep does),
therefore all time values must be integers.
Dmitry Golovashkin (E-mail: dvg@ieee.org)
EOF

    exit(1)
    # No useful work was done.
}
# Options.
while (os.system('getopts ":t:i:d:" option')):
    
        if ( "" + option + "" == 't'):
            timeout=OPTARG
        elif ("" + option + "" == 'i'):
            interval=OPTARG
        elif ("" + option + "" == 'd'):
            delay=OPTARG
        else:
            os.system('print_usage')
os.system('shift (OPTIND - 1)')
# $# should be at least 1 (the command to execute), however it may be strictly
# greater than 1 if the command itself has options.
if ((($# == 0 || interval <= 0)) ):
    os.system('print_usage')
# kill -0 pid   Exit code indicates if a signal may be sent to "pid" process.
( ((t = timeout))
while (((t > 0))):
    os.system('sleep interval')
    os.system('kill -0 $$') || exit(0)
    ((t -= interval))
# Be nice, post SIGTERM first.
# The 'exit 0' below will be executed if any preceeding command fails.
os.system('kill -s SIGTERM $$') && os.system('kill -0 $$') || exit(0)
os.system('sleep delay')
os.system('kill -s SIGKILL $$') ) 2> /dev/null &
os.system('exec "" + $ + "@"')
