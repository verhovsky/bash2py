import sys, os, os.path
from stat import *
#   bash_completion - programmable completion functions for bash 3.x
#		      (backwards compatible with bash 2.05b)
#
#   $Id: bash_completion,v 1.872 2006/03/01 16:20:18 ianmacd Exp $
#
#   Copyright (C) Ian Macdonald <ian@caliban.org>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2, or (at your option)
#   any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
#   The latest version of this software can be obtained here:
#
#   http://www.caliban.org/bash/index.shtml#completion
#
#   RELEASE: 20060301
if ($- == *v* ):
    BASH_COMPLETION_ORIGINAL_V_VALUE="-v"
else:
    BASH_COMPLETION_ORIGINAL_V_VALUE="+v"
if (-n $BASH_COMPLETION_DEBUG ):
    os.system('set -v')
else:
    os.system('set +v')
# Alter the following to reflect the location of this file.
#
-n "" + BASH_COMPLETION + ""  || BASH_COMPLETION=/etc/bash_completion
-n "" + BASH_COMPLETION_DIR + ""  || BASH_COMPLETION_DIR=/etc/bash_completion.d
os.system('readonly BASH_COMPLETION BASH_COMPLETION_DIR')
# Set a couple of useful vars
#
UNAME= os.popen(' uname -s ').read() 
# strip OS type and version under Cygwin (e.g. CYGWIN_NT-5.1 => Cygwin)
UNAME=${UNAME/CYGWIN_*/Cygwin}
RELEASE= os.popen(' uname -r ').read() 
# features supported by bash 2.05 and higher
if (${BASH_VERSINFO[0]} == 2  && ${BASH_VERSINFO[1]} > 04 || ${BASH_VERSINFO[0]} > 2  ):
    os.system('declare -r bash205=BASH_VERSION2> /dev/null') || os.system(':')
    default="-o default"
    dirnames="-o dirnames"
    filenames="-o filenames"
# features supported by bash 2.05b and higher
if (${BASH_VERSINFO[0]} == 2  && ${BASH_VERSINFO[1]} = "05b" || ${BASH_VERSINFO[0]} > 2  ):
    os.system('declare -r bash205b=BASH_VERSION2> /dev/null') || os.system(':')
    nospace="-o nospace"
# features supported by bash 3.0 and higher
if (${BASH_VERSINFO[0]} > 2  ):
    os.system('declare -r bash3=BASH_VERSION2> /dev/null') || os.system(':')
    bashdefault="-o bashdefault"
    plusdirs="-o plusdirs"
# Turn on extended globbing and programmable completion
os.system('shopt -s extglob progcomp')
# A lot of the following one-liners were taken directly from the
# completion examples provided with the bash 2.04 source distribution
# Make directory commands see only directories
os.system('complete -d pushd')
# The following section lists completions that are redefined later
# Do NOT break these over multiple lines.
#
# START exclude -- do NOT remove this line
os.system('complete -f -X '!*.?(t)bz?(2)' bunzip2 bzcat bzcmp bzdiff bzegrep bzfgrep bzgrep')
os.system('complete -f -X '!*.@(zip|ZIP|jar|JAR|exe|EXE|pk3|war|wsz|ear|zargo|xpi|sxw|ott)' unzip zipinfo')
os.system('complete -f -X '*.Z' compress znew')
os.system('complete -f -X '!*.@(Z|gz|tgz|Gz|dz)' gunzip zcmp zdiff zcat zegrep zfgrep zgrep zless zmore')
os.system('complete -f -X '!*.Z' uncompress')
os.system('complete -f -X '!*.@(gif|jp?(e)g|miff|tif?(f)|pn[gm]|p[bgp]m|bmp|xpm|ico|xwd|tga|pcx|GIF|JP?(E)G|MIFF|TIF?(F)|PN[GM]|P[BGP]M|BMP|XPM|ICO|XWD|TGA|PCX)' ee display')
os.system('complete -f -X '!*.@(gif|jp?(e)g|tif?(f)|png|p[bgp]m|bmp|x[bp]m|rle|rgb|pcx|fits|pm|GIF|JPG|JP?(E)G|TIF?(F)|PNG|P[BGP]M|BMP|X[BP]M|RLE|RGB|PCX|FITS|PM)' xv qiv')
os.system('complete -f -X '!*.@(@(?(e)ps|?(E)PS|pdf|PDF)?(.gz|.GZ|.bz2|.BZ2|.Z))' gv ggv kghostview')
os.system('complete -f -X '!*.@(dvi|DVI)?(.@(gz|Z|bz2))' xdvi')
os.system('complete -f -X '!*.@(dvi|DVI)?(.@(gz|bz2))' kdvi')
os.system('complete -f -X '!*.@(dvi|DVI)' dvips dviselect dvitype dvipdf advi dvipdfm dvipdfmx')
os.system('complete -f -X '!*.@(pdf|PDF)' acroread gpdf xpdf')
os.system('complete -f -X '!*.@(?(e)ps|?(E)PS|pdf|PDF)' kpdf')
os.system('complete -f -X '!*.@(@(?(e)ps|?(E)PS|pdf|PDF)?(.gz|.GZ)|cb(r|z)|CB(R|Z)|djv?(u)|DJV?(U)||dvi|DVI|gif|jp?(e)g|miff|tif?(f)|pn[gm]|p[bgp]m|bmp|xpm|ico|xwd|tga|pcx|GIF|JP?(E)G|MIFF|TIF?(F)|PN[GM]|P[BGP]M|BMP|XPM|ICO|XWD|TGA|PCX)' evince')
os.system('complete -f -X '!*.@(?(e)ps|?(E)PS)' ps2pdf')
os.system('complete -f -X '!*.texi*' makeinfo texi2html')
os.system('complete -f -X '!*.@(?(la)tex|?(LA)TEX|texi|TEXI|dtx|DTX|ins|INS)' tex latex slitex jadetex pdfjadetex pdftex pdflatex texi2dvi')
os.system('complete -f -X '!*.@(mp3|MP3)' mpg123 mpg321 madplay')
os.system('complete -f -X '!*.@(mp?(e)g|MP?(E)G|wma|avi|AVI|asf|vob|VOB|bin|dat|divx|DIVX|vcd|ps|pes|fli|flv|FLV|viv|rm|ram|yuv|mov|MOV|qt|QT|wmv|mp3|MP3|m4v|M4V|ogg|OGG|ogm|OGM|mp4|MP4|wav|WAV|asx|ASX|mng|MNG|srt)' xine aaxine fbxine kaffeine')
os.system('complete -f -X '!*.@(avi|asf|wmv)' aviplay')
os.system('complete -f -X '!*.@(rm?(j)|ra?(m)|smi?(l))' realplay')
os.system('complete -f -X '!*.@(mpg|mpeg|avi|mov|qt)' xanim')
os.system('complete -f -X '!*.@(ogg|OGG|m3u|flac|spx)' ogg123')
os.system('complete -f -X '!*.@(mp3|MP3|ogg|OGG|pls|m3u)' gqmpeg freeamp')
os.system('complete -f -X '!*.fig' xfig')
os.system('complete -f -X '!*.@(mid?(i)|MID?(I))' playmidi')
os.system('complete -f -X '!*.@(mid?(i)|MID?(I)|rmi|RMI|rcp|RCP|[gr]36|[GR]36|g18|G18|mod|MOD|xm|XM|it|IT|x3m|X3M)' timidity')
os.system('complete -f -X '*.@(o|so|so.!(conf)|a|rpm|gif|GIF|jp?(e)g|JP?(E)G|mp3|MP3|mp?(e)g|MPG|avi|AVI|asf|ASF|ogg|OGG|class|CLASS)' vi vim gvim rvim view rview rgvim rgview gview')
os.system('complete -f -X '*.@(o|so|so.!(conf)|a|rpm|gif|GIF|jp?(e)g|JP?(E)G|mp3|MP3|mp?(e)g|MPG|avi|AVI|asf|ASF|ogg|OGG|class|CLASS)' emacs')
os.system('complete -f -X '!*.@(exe|EXE|com|COM|scr|SCR|exe.so)' wine')
os.system('complete -f -X '!*.@(zip|ZIP|z|Z|gz|GZ|tgz|TGZ)' bzme')
os.system('complete -f -X '!*.@(?([xX]|[sS])[hH][tT][mM]?([lL]))' netscape mozilla lynx opera galeon curl dillo elinks amaya')
os.system('complete -f -X '!*.@(sxw|stw|sxg|sgl|doc|dot|rtf|txt|htm|html|odt|ott|odm)' oowriter')
os.system('complete -f -X '!*.@(sxi|sti|pps|ppt|pot|odp|otp)' ooimpress')
os.system('complete -f -X '!*.@(sxc|stc|xls|xlw|xlt|csv|ods|ots)' oocalc')
os.system('complete -f -X '!*.@(sxd|std|sda|sdd|odg|otg)' oodraw')
os.system('complete -f -X '!*.@(sxm|smf|mml|odf)' oomath')
os.system('complete -f -X '!*.odb' oobase')
os.system('complete -f -X '!*.rpm' rpm2cpio')
# FINISH exclude -- do not remove this line
# start of section containing compspecs that can be handled within bash
# user commands see only users
os.system('complete -u su usermod userdel passwd chage write chfn groups slay w sux')
# group commands see only groups
-n "" + bash205 + ""  && os.system('complete -g groupmod groupdel newgrp2> /dev/null')
# bg completes with stopped jobs
os.system('complete -A stopped -P '%' bg')
# other job commands
os.system('complete -j -P '%' fg jobs disown')
# readonly and unset complete with shell variables
os.system('complete -v readonly unset')
# set completes with set options
os.system('complete -A setopt set')
# shopt completes with shopt options
os.system('complete -A shopt shopt')
# helptopics
os.system('complete -A helptopic help')
# unalias completes with aliases
os.system('complete -a unalias')
# bind completes with readline bindings (make this more intelligent)
os.system('complete -A binding bind')
# type and which complete on commands
os.system('complete -c command type which')
# builtin completes on builtins
os.system('complete -b builtin')
# start of section containing completion functions called by other functions
# This function checks whether we have a given program on the system.
# No need for bulky functions in memory if we don't.
#
def have () 
{ 
    os.system('unset -v have')
    
    PATH=PATH:/sbin:/usr/sbin:/usr/local/sbin type sys.argv[1]&>/dev/null && have="yes"
}
# use GNU sed if we have it, since its extensions are still used in our code
#
UNAME != Linux  && os.system('have gsed') && os.system('alias sed=gsed')
# This function checks whether a given readline variable
# is `on'.
#
def _rl_enabled () 
{ 
    "$( bind -v )" = *$1+([[:space:]])on*
}
# This function shell-quotes the argument
def quote () 
{ 
    print("\'${1//\'/\'\\\'\'}\'")
    
    #'# Help vim syntax highlighting
}
# This function quotes the argument in a way so that readline dequoting
# results in the original argument
def quote_readline () 
{ 
    os.system('local t="" + $ + "{1//\\/\\\\}"')
    
    print("\'${t//\'/\'\\\'\'}\'")
    
    #'# Help vim syntax highlighting
}
# This function shell-dequotes the argument
def dequote () 
{ 
    os.system('eval print "" + sys.argv[1] + ""')
}
# Get the word to complete
# This is nicer than ${COMP_WORDS[$COMP_CWORD]}, since it handles cases
# where the user is completing in the middle of a word.
# (For example, if the line is "ls foobar",
# and the cursor is here -------->   ^
# it will complete just "foo", not "foobar", which is what the user wants.)
def _get_cword () 
{ 
    if ("${#COMP_WORDS[COMP_CWORD]}" -eq 0 || "$COMP_POINT" == "${#COMP_LINE}" ):
        print("" + $ + "{COMP_WORDS[COMP_CWORD]}")
    else:
        os.system('local i')
        
        os.system('local cur="" + COMP_LINE + ""')
        
        os.system('local index="" + COMP_POINT + ""')
        
        for ((i = 0; i <= COMP_CWORD; ++i))
        do
            while ("${#cur}" -ge ${#COMP_WORDS[i]} && "${cur:0:${#COMP_WORDS[i]}}" != "${COMP_WORDS[i]}"):
                cur="" + $ + "{cur:1}"
                
                index="( index - 1 )"
            
            if ("$i" -lt "$COMP_CWORD" ):
                os.system('local old_size="" + $ + "{#cur}"')
                
                cur="" + $ + "{cur#" + $ + "{COMP_WORDS[i]}}"
                
                os.system('local new_size="" + $ + "{#cur}"')
                
                index="( index - old_size + new_size )"
        done
        
        if ("${COMP_WORDS[COMP_CWORD]:0:${#cur}}" != "$cur" ):
            # We messed up! At least return the whole word so things keep working
            
            print("" + $ + "{COMP_WORDS[COMP_CWORD]}")
        else:
            print("" + $ + "{cur:0:" + index + "}")
}
# This function performs file and directory completion. It's better than
# simply using 'compgen -f', because it honours spaces in filenames.
# If passed -d, it completes only on directories. If passed anything else,
# it's assumed to be a file glob to complete on.
#
def _filedir () 
{ 
    os.system('local IFS='	
 xspec')
    
    os.system('_expand') || os.system('return 0')
    
    os.system('local toks=() tmp')
    
    while (-r = raw_input()):
        -n $tmp && toks[${#toks[@]}]=tmp < <( compgen -d -- "$(quote_readline "$cur")" )
    
    if ("$1" != -d ):
        xspec=${1:+"!*." + sys.argv[1] + ""}
        
        while (-r = raw_input()):
            -n $tmp && toks[${#toks[@]}]=tmp < <( compgen -f -X "$xspec" -- "$(quote_readline "$cur")" )
    
    COMPREPLY=("" + $ + "{COMPREPLY[@]}" "" + $ + "{toks[@]}")
}
# This function completes on signal names
#
def _signals () 
{ 
    os.system('local i')
    
    # standard signal completion is rather braindead, so we need
    
    # to hack around to get what we want here, which is to
    
    # complete on a dash, followed by the signal name minus
    
    # the SIG prefix
    
    COMPREPLY=( os.popen(' compgen -A signal SIG${cur#-} ').read() )
    
    for ((i=0; i < ${#COMPREPLY[@]}; i++))
    do
        COMPREPLY[i]=-${COMPREPLY[i]#SIG}
    done
}
# This function completes on configured network interfaces
#
def _configured_interfaces () 
{ 
    if (os.path.isfile(/etc/debian_version ) ):
        # Debian system
        
        COMPREPLY=( os.popen(' sed -ne 's|^iface \([^ ]\+\').read() .*$|\1|p' 			       /etc/network/interfaces ))
    else:
        if (os.path.isfile(/etc/SuSE-release ) ):
            # SuSE system
            
            COMPREPLY=( os.popen(' command ls 			/etc/sysconfig/network/ifcfg-* | 			sed -ne 's|.*ifcfg-\('cur'.*\').read() |\1|p' ))
        else:
            if (os.path.isfile(/etc/pld-release ) ):
                # PLD Linux
                
                COMPREPLY=( os.popen(' command ls -B 			/etc/sysconfig/interfaces | 			sed -ne 's|.*ifcfg-\('cur'.*\').read() |\1|p' ))
            else:
                # Assume Red Hat
                
                COMPREPLY=( os.popen(' command ls 			/etc/sysconfig/network-scripts/ifcfg-* | 			sed -ne 's|.*ifcfg-\('cur'.*\').read() |\1|p' ))
}
# This function completes on all available network interfaces
# -a: restrict to active interfaces only
# -w: restrict to wireless interfaces only
#
def _available_interfaces () 
{ 
    os.system('local cmd')
    
    if ("" + $ + "{1:-}" == -w  ):
        cmd="iwconfig"
    else:
        if ("" + $ + "{1:-}" == -a  ):
            cmd="ifconfig"
        else:
            cmd="ifconfig -a"
    
    COMPREPLY=( os.popen(' eval cmd 2>/dev/null | 		sed -ne 's|^\('cur'[^[:space:][:punct:]]\{1,\}\').read() .*$|\1|p'))
}
# This function expands tildes in pathnames
#
def _expand () 
{ 
    # FIXME: Why was this here?
    
    # [ "$cur" != "${cur%\\}" ] && cur="$cur\\"
    
    # expand ~username type directory specifications
    
    if ("$cur" == \~*/* ):
        os.system('eval cur=cur')
    else:
        if ("$cur" == \~* ):
            cur=${cur#\~}
            
            COMPREPLY=( os.popen(' compgen -P '~' -u cur ').read() )
            
            os.system('return ${#COMPREPLY[@]}')
}
# This function completes on process IDs.
# AIX and Solaris ps prefers X/Open syntax.
UNAME == SunOS -o UNAME == AIX  && def _pids () 
{ 
    COMPREPLY=( os.popen(' compgen -W '$( command ps -efo pid | sed 1d ').read() ' -- cur ))
} || def _pids () 
{ 
    COMPREPLY=( os.popen(' compgen -W '$( command ps axo pid | sed 1d ').read() ' -- cur ))
}
# This function completes on process group IDs.
# AIX and SunOS prefer X/Open, all else should be BSD.
UNAME == SunOS -o UNAME == AIX  && def _pgids () 
{ 
    COMPREPLY=( os.popen(' compgen -W '$( command ps -efo pgid | sed 1d ').read() ' -- cur ))
} || def _pgids () 
{ 
    COMPREPLY=( os.popen(' compgen -W '$( command ps axo pgid | sed 1d ').read() ' -- cur ))
}
# This function completes on user IDs
#
def _uids () 
{ 
    if (os.system('type getent&>/dev/null') ):
        COMPREPLY=( os.popen(' getent passwd | 			    awk -F: '{if (sys.argv[3] ~ /^'cur'/').read()  print sys.argv[3]}' ))
    else:
        if (os.system('type perl&>/dev/null') ):
            COMPREPLY=( os.popen(' compgen -W '$( perl -e '"'"'while ((uid').read()  = (getpwent)[2]) { print uid . "\n" }'"'"' )' -- cur ))
        else:
            # make do with /etc/passwd
            
            COMPREPLY=( os.popen(' awk 'BEGIN {FS=":"} {if (sys.argv[3] ~ /^'cur'/').read()  print sys.argv[3]}'			    /etc/passwd ))
}
# This function completes on group IDs
#
def _gids () 
{ 
    if (os.system('type getent&>/dev/null') ):
        COMPREPLY=( os.popen(' getent group | 			    awk -F: '{if (sys.argv[3] ~ /^'cur'/').read()  print sys.argv[3]}' ))
    else:
        if (os.system('type perl&>/dev/null') ):
            COMPREPLY=( os.popen(' compgen -W '$( perl -e '"'"'while ((gid').read()  = (getgrent)[2]) { print gid . "\n" }'"'"' )' -- cur ))
        else:
            # make do with /etc/group
            
            COMPREPLY=( os.popen(' awk 'BEGIN {FS=":"} {if (sys.argv[3] ~ /^'cur'/').read()  print sys.argv[3]}'			    /etc/group ))
}
# This function completes on services
#
def _services () 
{ 
    os.system('local sysvdir famdir')
    
    S_ISDIR(os.stat(/etc/rc.d/init.d ).st_mode) && sysvdir=/etc/rc.d/init.d || sysvdir=/etc/init.d
    
    famdir=/etc/xinetd.d
    
    COMPREPLY=( os.popen(' builtin echo sysvdir/!(*.rpmsave|*.rpmorig|*~|functions').read() ))
    
    if (S_ISDIR(os.stat(famdir ).st_mode) ):
        COMPREPLY=("" + $ + "{COMPREPLY[@]}"  os.popen(' builtin echo famdir/!(*.rpmsave|*.rpmorig|*~').read() ))
    
    COMPREPLY=( os.popen(' compgen -W '${COMPREPLY[@]#@(sysvdir|famdir').read() /}' -- cur ))
}
# This function complete on modules
#
def _modules () 
{ 
    os.system('local modpath')
    
    modpath=/lib/modules/sys.argv[1]
    
    COMPREPLY=( os.popen(' command ls -R modpath | 			sed -ne 's/^\('cur'.*\').read() \.k\?o\(\|.gz\)$/\1/p'))
}
# this function complete on user:group format
#
def _usergroup () 
{ 
    os.system('local IFS='
')
    
    cur=${cur//\\\\ / }
    
    if ($cur = *@(\\:|.)* && -n "" + bash205 + ""  ):
        user=${cur%%*([^:.])}
        
        COMPREPLY=( os.popen('compgen -P ${user/\\\\} -g -- ${cur##*[.:]}').read() )
    else:
        if ($cur = *:* && -n "" + bash205 + ""  ):
            COMPREPLY=( os.popen(' compgen -g -- ${cur##*[.:]} ').read() )
        else:
            COMPREPLY=( os.popen(' compgen -S : -u -- cur ').read() )
}
# this function count the number of mandatory args
#
def _count_args () 
{ 
    args=1
    
    for ((i=1; i < COMP_CWORD; i++))
    do
        if ("${COMP_WORDS[i]}" != -* ):
            args=(args+1)
    done
}
# start of section containing completion functions for bash built-ins
# bash alias completion
#
def _alias () 
{ 
    os.system('local cur')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    
        if ( "" + COMP_LINE + "" == '*[^=]'):
            COMPREPLY=( os.popen(' compgen -A alias -S '=' -- cur ').read() )
        elif ("" + COMP_LINE + "" == '*='):
            COMPREPLY=("" + $ + "( alias " + $ + "{cur%=} 2>/dev/null | 			     sed -e 's|^alias '" + cur + "'\(.*\)" + $ + "|\1|' )")
}
os.system('complete -F _alias nospace alias')
# bash export completion
#
def _export () 
{ 
    os.system('local cur')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    
        if ( "" + COMP_LINE + "" == '*=\$*'):
            COMPREPLY=( os.popen(' compgen -v -P '$' -- ${cur#*=\$} ').read() )
        elif ("" + COMP_LINE + "" == '*[^=]'):
            COMPREPLY=( os.popen(' compgen -v -S '=' -- cur ').read() )
        elif ("" + COMP_LINE + "" == '*='):
            COMPREPLY=("" + $ + "( eval echo -n \"$ os.popen('echo ${cur%=}').read() \" |

}
os.system('complete -F _export default nospace export')
# bash shell function completion
#
def _function () 
{ 
    os.system('local cur prev')
    
    COMPREPLY=()
    
    cur= os.popen('_get_cword').read() 
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    if ($1 == @(declare|typeset) ):
        if ("" + prev + "" == -f  ):
            COMPREPLY=( os.popen(' compgen -A function -- cur ').read() )
        else:
            if ("$cur" == -* ):
                COMPREPLY=( os.popen(' compgen -W '-a -f -F -i -r -x -p' -- 				       cur ').read() )
    else:
        if (COMP_CWORD == 1  ):
            COMPREPLY=( os.popen(' compgen -A function -- cur ').read() )
        else:
            COMPREPLY=("() " + $ + "( type -- " + $ + "{COMP_WORDS[1]} | sed -e 1,2d )")
}
os.system('complete -F _function function declare typeset')
# bash complete completion
#
