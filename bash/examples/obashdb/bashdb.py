import sys, os, os.path
from stat import *
# bashdb - Bash shell debugger
#
# Adapted from an idea in O'Reilly's `Learning the Korn Shell'
# Copyright (C) 1993-1994 O'Reilly and Associates, Inc.
# Copyright (C) 1998, 1999, 2001 Gary V. Vaughan <gvv@techie.com>>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# As a special exception to the GNU General Public License, if you
# distribute this file as part of a program that contains a
# configuration script generated by Autoconf, you may include it under
# the same distribution terms that you use for the rest of that program.
# NOTE:
#
# This program requires bash 2.x.
# If bash 2.x is installed as "bash2", you can invoke  bashdb like this:
#
#   DEBUG_SHELL=/bin/bash2 /bin/bash2 bashdb script.sh
# TODO:
#
# break [regexp]
# cond [break] [condition]
# tbreak [regexp|+lines]
# restart
# Variable watchpoints
# Instrument `source' and `.' files in $_potbelliedpig
# be cleverer about lines we allow breakpoints to be set on
# break [function_name]
print("'Bash Debugger version 1.2.4'")
os.environ['_dbname'] = ${0##*/}
if (os.system('test $# < 1') ):
    print("" + _dbname + ": Usage: " + _dbname + " filename")1>&2
    exit(1)
_guineapig=sys.argv[1]
if (os.system('test ! -r sys.argv[1]') ):
    print("" + _dbname + ": Cannot read file '" + _guineapig + "'.")1>&2
    exit(1)
os.system('shift')
__debug=${TMPDIR-/tmp}/bashdb.$$
os.system('sed -e '/^# bashdb - Bash shell debugger/,/^# -- DO NOT DELETE THIS LINE -- /d' "" + sys.argv[0] + ""> $__debug')
os.system('cat _guineapig>> $__debug')
os.system('exec ${DEBUG_SHELL-bash} __debug _guineapig "" + $ + "@"')
exit(1)
# -- DO NOT DELETE THIS LINE -- The program depends on it
#bashdb preamble
# $1 name of the original guinea pig script
__debug=sys.argv[0]
_guineapig=sys.argv[1]
__steptrap_calls=0
os.system('shift')
os.system('shopt -s extglob')
# turn on extglob so we can parse the debugger funcs
def _steptrap () 
{ 
    os.system('local i=0')
    
    _curline=sys.argv[1]
    
    if (((++__steptrap_calls > 1 && _curline == 1)) ):
        os.system('return')
    
    if (-n "" + _disps + ""  ):
        while (((i < ${#_disps[@]}))):
            if (-n "" + $ + "{_disps[" + i + "]}"  ):
                os.system('_msg "" + $ + "{_disps[" + i + "]}: \c"')
                
                os.system('eval _msg ${_disps[i]}')
            
            i=i+1
    
    if (((_trace)) ):
        os.system('_showline _curline')
    
    if (((_steps >= 0)) ):
        _steps="" + _steps + " - 1"
    
    if (os.system('_at_linenumbp') ):
        os.system('_msg "Reached breakpoint at line " + _curline + ""')
        
        os.system('_showline _curline')
        
        os.system('_cmdloop')
    else:
        if (-n "" + _brcond + ""  && os.system('eval _brcond') ):
            os.system('_msg "Break condition " + _brcond + " true at line " + _curline + ""')
            
            os.system('_showline _curline')
            
            os.system('_cmdloop')
        else:
            if (((_steps == 0)) ):
                # Assuming a real script will have the "#! /bin/sh" at line 1,
                
                # assume that when $_curline == 1 we are inside backticks.
                
                if (((! _trace)) ):
                    os.system('_msg "Stopped at line " + _curline + ""')
                    
                    os.system('_showline _curline')
                
                os.system('_cmdloop')
}
def _setbp () 
{ 
    os.system('local i f line _x')
    
    if (-z "" + sys.argv[1] + ""  ):
        os.system('_listbp')
        
        os.system('return')
    
    os.system('eval "" + _seteglob + ""')
    
    if ($1 == *(\+)[1-9]*([0-9]) ):
        
            if ( sys.argv[1] == '+*'):
                # normalize argument, then double it (+2 -> +2 + 2 = 4)
                
                _x=${1##*([!1-9])}
                
                # cut off non-numeric prefix
                
                _x=${x%%*([!0-9])}
                
                # cut off non-numeric suffix
                
                f=( sys.argv[1] + _x )
            else:
                f=( sys.argv[1] )
        
        # find the next valid line
        
        line="" + $ + "{_lines[" + f + "]}"
        
        while (os.system('_invalidbreakp f')):
            ((f++))
            
            line="" + $ + "{_lines[" + f + "]}"
        
        if (((f != sys.argv[1])) ):
            os.system('_msg "Line " + sys.argv[1] + " is not a valid breakpoint"')
        
        if (-n "" + $ + "{_lines[" + f + "]}"  ):
            _linebp[sys.argv[1]]=sys.argv[1]
            
            os.system('_msg "Breakpoint set at line " + f + ""')
        else:
            os.system('_msg "Breakpoints can only be set on executable lines"')
    else:
        os.system('_msg "Please specify a numeric line number"')
    
    os.system('eval "" + _resteglob + ""')
}
def _listbp () 
{ 
    os.system('local i')
    
    if (-n "" + _linebp + ""  ):
        os.system('_msg "Breakpoints:"')
        
        for i in [${_linebp[*]}]:
                    os.system('_showline i')
    else:
        os.system('_msg "No breakpoints have been set"')
}
def _clearbp () 
{ 
    os.system('local i')
    
    if (-z "" + sys.argv[1] + ""  ):
        -e = raw_input()
        
        
            if ( REPLY == '[yY]*'):
                os.system('unset _linebp[*]')
                
                os.system('_msg "All breakpoints have been cleared"')
        
        os.system('return 0')
    
    os.system('eval "" + _seteglob + ""')
    
    if ($1 == [1-9]*([0-9]) ):
        os.system('unset _linebp[sys.argv[1]]')
        
        os.system('_msg "Breakpoint cleared at line " + sys.argv[1] + ""')
    else:
        os.system('_msg "Please specify a numeric line number"')
    
    os.system('eval "" + _resteglob + ""')
}
def _setbc () 
{ 
    if ((($# > 0)) ):
        _brcond=$@
        
        os.system('_msg "Break when true: " + _brcond + ""')
    else:
        _brcond=
        
        os.system('_msg "Break condition cleared"')
}
def _setdisp () 
{ 
    if (-z "" + sys.argv[1] + ""  ):
        os.system('_listdisp')
    else:
        _disps[${#_disps[@]}]="" + sys.argv[1] + ""
        
        if (((${#_disps[@]} < 10)) ):
            os.system('_msg " " + $ + "{#_disps[@]}: " + sys.argv[1] + ""')
        else:
            os.system('_msg "" + $ + "{#_disps[@]}: " + sys.argv[1] + ""')
}
def _listdisp () 
{ 
    os.system('local i=0 j')
    
    if (-n "" + _disps + ""  ):
        while (((i < ${#_disps[@]}))):
            j=i+1
            
            if (((${#_disps[@]} < 10)) ):
                os.system('_msg " " + j + ": " + $ + "{_disps[" + i + "]}"')
            else:
                os.system('_msg "" + j + ": " + $ + "{_disps[" + i + "]}"')
            
            i=j
    else:
        os.system('_msg "No displays have been set"')
}
def _cleardisp () 
{ 
    if ((($# < 1)) ):
        -e = raw_input()
        
        
            if ( REPLY == '[Yy]*'):
                os.system('unset _disps[*]')
                
                os.system('_msg "All breakpoints have been cleared"')
        
        os.system('return 0')
    
    os.system('eval "" + _seteglob + ""')
    
    if ($1 == [1-9]*([0-9]) ):
        os.system('unset _disps[sys.argv[1]]')
        
        os.system('_msg "Display " + i + " has been cleared"')
    else:
        os.system('_listdisp')
        
        os.system('_msg "Please specify a numeric display number"')
    
    os.system('eval "" + _resteglob + ""')
}
# usage _ftrace -u funcname [funcname...]
def _ftrace () 
{ 
    os.system('local _opt=-t _tmsg="enabled" _func')
    
    if ($1 == -u ):
        _opt=+t
        
        _tmsg="disabled"
        
        os.system('shift')
    
    for _func in ["" + $ + "@"]:
            os.system('declare -f _opt _func')
        
        os.system('_msg "Tracing " + _tmsg + " for function " + _func + ""')
}
def _cmdloop () 
{ 
    os.system('local cmd args')
    
    while (-e = raw_input()):
        os.system('test -n "" + cmd + ""') && os.system('history -s "" + cmd + " " + args + ""')
        
        # save on history list
        
        os.system('test -n "" + cmd + ""') || { 
            os.system('set _lastcmd')
            
            cmd=sys.argv[1]
            
            os.system('shift')
            
            args=$*
        }
        
        if (-n "" + cmd + ""  ):
            
                if ( cmd == 'b' or cmd == 'br' or cmd == 'bre' or cmd == 'brea' or cmd == 'break'):
                    os.system('_setbp args')
                    
                    _lastcmd="break " + args + ""
                elif (cmd == 'co' or cmd == 'con'):
                    os.system('_msg "ambiguous command: '" + cmd + "', condition, continue?"')
                elif (cmd == 'cond' or cmd == 'condi' or cmd == 'condit' or cmd == 'conditi' or cmd == 'conditio' or cmd == 'condition'):
                    os.system('_setbc args')
                    
                    _lastcmd="condition " + args + ""
                elif (cmd == 'c' or cmd == 'cont' or cmd == 'conti' or cmd == 'contin' or cmd == 'continu' or cmd == 'continue'):
                    _lastcmd="continue"
                    
                    os.system('return')
                elif (cmd == 'd'):
                    os.system('_msg "ambiguous command: '" + cmd + "', delete, display?"')
                elif (cmd == 'de' or cmd == 'del' or cmd == 'dele' or cmd == 'delet' or cmd == 'delete'):
                    os.system('_clearbp args')
                    
                    _lastcmd="delete " + args + ""
                elif (cmd == 'di' or cmd == 'dis' or cmd == 'disp' or cmd == 'displ' or cmd == 'displa' or cmd == 'display'):
                    os.system('_setdisp args')
                    
                    _lastcmd="display " + args + ""
                elif (cmd == 'f' or cmd == 'ft' or cmd == 'ftr' or cmd == 'ftra' or cmd == 'ftrace'):
                    os.system('_ftrace args')
                    
                    _lastcmd="ftrace " + args + ""
                elif (cmd == '\?' or cmd == 'h' or cmd == 'he' or cmd == 'hel' or cmd == 'help'):
                    os.system('_menu')
                    
                    _lastcmd="help"
                elif (cmd == 'l' or cmd == 'li' or cmd == 'lis' or cmd == 'list'):
                    os.system('_displayscript args')
                    
                    # _lastcmd is set in the _displayscript function
                elif (cmd == 'p' or cmd == 'pr' or cmd == 'pri' or cmd == 'prin' or cmd == 'print'):
                    os.system('_examine args')
                    
                    _lastcmd="print " + args + ""
                elif (cmd == 'q' or cmd == 'qu' or cmd == 'qui' or cmd == 'quit'):
                    exit()
                elif (cmd == 's' or cmd == 'st' or cmd == 'ste' or cmd == 'step' or cmd == 'n' or cmd == 'ne' or cmd == 'nex' or cmd == 'next'):
                    _steps=${args:-1}
                    
                    _lastcmd="next " + args + ""
                    
                    os.system('return')
                elif (cmd == 't' or cmd == 'tr' or cmd == 'tra' or cmd == 'trac' or cmd == 'trace'):
                    os.system('_xtrace')
                elif (cmd == 'u' or cmd == 'un' or cmd == 'und' or cmd == 'undi' or cmd == 'undis' or cmd == 'undisp' or cmd == 'undispl' or cmd == 'undispla' or cmd == 'undisplay'):
                    os.system('_cleardisp args')
                    
                    _lastcmd="undisplay " + args + ""
                elif (cmd == '!*'):
                    os.system('eval ${cmd#!} args')
                    
                    _lastcmd="" + cmd + " " + args + ""
                else:
                    os.system('_msg "Invalid command: '" + cmd + "'"')
}
def _at_linenumbp () 
{ 
    -n ${_linebp[$_curline]}
}
def _invalidbreakp () 
{ 
    os.system('local line=${_lines[sys.argv[1]]}')
    
    # XXX - should use shell patterns
    
    if (os.system('test -z "" + line + ""') || os.system('expr "" + line + "" : '[ \t]*#.*'> /dev/null') || os.system('expr "" + line + "" : '[ \t]*;;[ \t]*$'> /dev/null') || os.system('expr "" + line + "" : '[ \t]*[^)]*)[ \t]*$'> /dev/null') || os.system('expr "" + line + "" : '[ \t]*;;[ \t]*#.**$'> /dev/null') || os.system('expr "" + line + "" : '[ \t]*[^)]*)[ \t]*;;[ \t]*$'> /dev/null') || os.system('expr "" + line + "" : '[ \t]*[^)]*)[ \t]*;;*[ \t]*#.*$'> /dev/null') ):
        os.system('return 0')
    
    os.system('return 1')
}
def _examine () 
{ 
    if (-n "" + $ + "*"  ):
        os.system('_msg "" + args + ": \c"')
        
        os.system('eval _msg args')
    else:
        os.system('_msg "Nothing to print"')
}
def _displayscript () 
{ 
    os.system('local i j start end bp cl')
    
    if ((($# == 1)) ):
        # list 5 lines on either side of $1
        
        if (sys.argv[1] == "%"  ):
            start=1
            
            end=${#_lines[@]}
        else:
            start=sys.argv[1]-5
            
            end=sys.argv[1]+5
    else:
        if ((($# > 1)) ):
            # list between start and end
            
            if (sys.argv[1] == "^"  ):
                start=1
            else:
                start=sys.argv[1]
            
            if (sys.argv[2] == "\" + $ + ""  ):
                end=${#_lines[@]}
            else:
                end=sys.argv[2]
        else:
            # list 5 lines on either side of current line
            
            start=_curline-5
            
            end=_curline+5
    
    # normalize start and end
    
    if (((start < 1)) ):
        start=1
    
    if (((end > ${#_lines[@]})) ):
        end=${#_lines[@]}
    
    cl=( end - start )
    
    if (((cl > ${LINES-24})) ):
        pager=${PAGER-more}
    else:
        pager=cat
    
    i=start
    
    ( while (((i <= end))):
        os.system('_showline i')
        
        i=i+1 ) 2>&1 | os.system('pager')
    
    # calculate the next block of lines
    
    start=( end + 1 )
    
    end=( start + 11 )
    
    if (((end > ${#_lines[@]})) ):
        end=${#_lines[@]}
    
    _lastcmd="list " + start + " " + end + ""
}
def _xtrace () 
{ 
    _trace="! " + _trace + ""
    
    if (((_trace)) ):
        os.system('_msg "Execution trace on"')
    else:
        os.system('_msg "Execution trace off"')
}
def _msg () 
{ 
    print("" + $ + "@")1>&2
}
def _showline () 
{ 
    os.system('local i=0 bp=' ' line=sys.argv[1] cl=' '')
    
    if (-n ${_linebp[$line]} ):
        bp='*'
    
    if (((_curline == line)) ):
        cl=">"
    
    if (((line < 100)) ):
        os.system('_msg "" + $ + "{_guineapig/*\//}:" + line + "   " + bp + " " + cl + "" + $ + "{_lines[" + line + "]}"')
    else:
        if (((line < 10)) ):
            os.system('_msg "" + $ + "{_guineapig/*\//}:" + line + "  " + bp + " " + cl + "" + $ + "{_lines[" + line + "]}"')
        else:
            if (((line > 0)) ):
                os.system('_msg "" + $ + "{_guineapig/*\//}:" + line + " " + bp + " " + cl + "" + $ + "{_lines[" + line + "]}"')
}
def _cleanup () 
{ 
    os.system('rm -f __debug _potbelliedpig2> /dev/null')
}
def _menu () 
{ 
    os.system('_msg 'bashdb commands:
')
}
os.system('shopt -u extglob')
HISTFILE=~/.bashdb_history
os.system('set -o history')
os.system('set +H')
# strings to save and restore the setting of `extglob' in debugger functions
# that need it
_seteglob='local __eopt=-u ; shopt -q extglob && __eopt=-s ; shopt -s extglob'
_resteglob='shopt __eopt extglob'
_linebp=()
_trace=0
_i=1
# Be careful about quoted newlines
_potbelliedpig=${TMPDIR-/tmp}/${_guineapig/*\//}.$$
os.system('sed 's,\\$,\\\\,' _guineapig> $_potbelliedpig')
os.system('_msg "Reading source from file: " + _guineapig + ""')
while (raw_input()):
    _lines[_i]=REPLY
    _i=_i+1 < $_potbelliedpig
os.system('trap _cleanup EXIT')
# Assuming a real script will have the "#! /bin/sh" at line 1,
# don't stop at line 1 on the first run
_steps=1
LINENO=-1
os.system('trap '_steptrap LINENO' DEBUG')
