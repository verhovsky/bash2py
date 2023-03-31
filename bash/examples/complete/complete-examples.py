import sys, os, os.path
from stat import *
#
# Completion examples
#
#
# This encapsulates the default bash completion code
# call with the word to be completed as $1
#
# Since programmable completion does not use the bash default completions
# or the readline default of filename completion when the compspec does
# not generate any matches, this may be used as a `last resort' in a
# completion function to mimic the default bash completion behavior.
#
def _bash_def_completion () 
{ 
    os.system('local h t')
    
    COMPREPLY=()
    
    # command substitution
    
    if ("$1" == \$\(* ):
        t=${1#??}
        
        COMPREPLY=( os.popen('compgen -c -P '$(' t').read() )
    
    # variables with a leading `${'
    
    if (${#COMPREPLY[@]} == 0  && "$1" == \$\{* ):
        t=${1#??}
        
        COMPREPLY=( os.popen('compgen -v -P '${' -S '}' t').read() )
    
    # variables with a leading `$'
    
    if (${#COMPREPLY[@]} == 0  && "$1" == \$* ):
        t=${1#?}
        
        COMPREPLY=( os.popen('compgen -v -P '$' t ').read() )
    
    # username expansion
    
    if (${#COMPREPLY[@]} == 0  && "$1" == ~* && "$1" != */* ):
        t=${1#?}
        
        COMPREPLY=( os.popen(' compgen -u -P '~' t ').read() )
    
    # hostname
    
    if (${#COMPREPLY[@]} == 0  && "$1" == *@* ):
        h=${1%%@*}
        
        t=${1#*@}
        
        COMPREPLY=( os.popen(' compgen -A hostname -P "" + $ + "{h}@" t ').read() )
    
    # glob pattern
    
    if (${#COMPREPLY[@]} == 0  ):
        # sh-style glob pattern
        
        if ($1 == *[*?[]* ):
            COMPREPLY=( os.popen(' compgen -G "" + sys.argv[1] + "" ').read() )
            
            # ksh-style extended glob pattern - must be complete
        else:
            if (os.system('shopt -q extglob') && $1 == *[?*+\!@]\(*\)* ):
                COMPREPLY=( os.popen(' compgen -G "" + sys.argv[1] + "" ').read() )
    
    # final default is filename completion
    
    if (${#COMPREPLY[@]} == 0  ):
        COMPREPLY=( os.popen('compgen -f "" + sys.argv[1] + "" ').read() )
}
# 
# Return 1 if $1 appears to contain a redirection operator.  Handles backslash
# quoting (barely).
#
def _redir_op () 
{ 
    
        if ( "" + sys.argv[1] + "" == '*\\'[\<\>]'*'):
            os.system('return 1')
        elif ("" + sys.argv[1] + "" == '*[\<\>]*'):
            os.system('return 0')
        else:
            os.system('return 1')
}
# _redir_test tests the current word ($1) and the previous word ($2) for
# redirection operators and does filename completion on the current word
# if either one contains a redirection operator
def _redir_test () 
{ 
    if (os.system('_redir_op "" + sys.argv[1] + ""') ):
        COMPREPLY=( os.popen(' compgen -f "" + sys.argv[1] + "" ').read() )
        
        os.system('return 0')
    else:
        if (os.system('_redir_op "" + sys.argv[2] + ""') ):
            COMPREPLY=( os.popen(' compgen -f "" + sys.argv[1] + "" ').read() )
            
            os.system('return 0')
    
    os.system('return 1')
}
# optional, but without this you can't use extended glob patterns
os.system('shopt -s extglob')
#
# Easy ones for the shell builtins
#
# nothing for: alias, break, continue, dirs, echo, eval, exit, getopts,
# let, logout, popd, printf, pwd, return, shift, suspend, test, times,
# umask
#
os.system('complete -f -- . source')
os.system('complete -A enabled builtin')
os.system('complete -d cd')
# this isn't exactly right yet -- needs to skip shell functions and
# do $PATH lookup (or do compgen -c and filter out matches that also
# appear in compgen -A function)
os.system('complete -c command')
# could add -S '=', but that currently screws up because readline appends
# a space unconditionally
os.system('complete -v export local readonly')
os.system('complete -A helptopic help')
# currently same as builtins
os.system('complete -d pushd')
os.system('complete -A shopt shopt')
os.system('complete -c type')
os.system('complete -a unalias')
os.system('complete -v unset')
#
# Job control builtins: fg, bg, disown, kill, wait
# kill not done yet
#
os.system('complete -A stopped -P '%' bg')
os.system('complete -j -P '%' fg jobs disown')
# this is not quite right at this point
def _wait_func () 
{ 
    os.system('local cur')
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    
        if ( "" + cur + "" == '%*'):
            COMPREPLY=( os.popen('compgen -A running -P '%' ${cur#?} ').read() )
        elif ("" + cur + "" == '[0-9]*'):
            COMPREPLY=( os.popen('jobs -p | grep ^${cur}').read() )
        else:
            COMPREPLY=( os.popen('compgen -A running -P '%'').read()   os.popen('jobs -p').read() )
}
os.system('complete -F _wait_func wait')
#
# more complicated things, several as yet unimplemented
#
#complete -F _bind_func bind
def _declare_func () 
{ 
    os.system('local cur prev nflag opts')
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    COMPREPLY=()
    
    if (((COMP_CWORD <= 1)) || $cur == '-' ):
        COMPREPLY=(-a -f -F -i -p -r -t -x)
        
        os.system('return 0')
    
    if ($cur == '+' ):
        COMPREPLY=(+i +t +x)
        
        os.system('return 0')
    
    if ($prev == '-p' ):
        COMPREPLY=( os.popen('compgen -v cur').read() )
        
        os.system('return 0')
    
    os.system('return 1')
}
os.system('complete -F _declare_func declare typeset')
def _enable_func () 
{ 
    os.system('local cur prev nflag opts')
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    COMPREPLY=()
    
    if (((COMP_CWORD <= 1)) || $cur == '-' ):
        COMPREPLY=(-a -d -f -n -p -s)
        
        os.system('return 0')
    
    if ($prev == '-f' ):
        COMPREPLY=( os.popen(' compgen -f cur ').read() )
        
        os.system('return 0')
    
    for opts in ["" + $ + "{COMP_WORDS[@]}"]:
            if ($opts == -*n* ):
            nflag=1
    
    if (-z "" + nflag + ""  ):
        COMPREPLY=( os.popen(' compgen -A enabled cur ').read() )
    else:
        COMPREPLY=( os.popen(' compgen -A disabled cur ').read() )
    
    os.system('return 0')
}
os.system('complete -F _enable_func enable')
def _exec_func () 
{ 
    os.system('local cur prev')
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    if (((COMP_CWORD <= 1)) || $cur == '-' ):
        COMPREPLY=(-a -c -l)
        
        os.system('return 0')
    
    if ($prev != -*a* ):
        COMPREPLY=( os.popen(' compgen -c cur ').read() )
        
        os.system('return 0')
    
    os.system('return 1')
}
os.system('complete -F _exec_func exec')
def _fc_func () 
{ 
    os.system('local cur prev')
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    if (((COMP_CWORD <= 1)) || $cur == '-' ):
        COMPREPLY=(-e -n -l -r -s)
        
        os.system('return 0')
    
    if ($prev == -*e ):
        COMPREPLY=( os.popen('compgen -c cur').read() )
        
        os.system('return 0')
    
    os.system('return 1')
}
os.system('complete -F _fc_func fc')
def _hash_func () 
{ 
    os.system('local cur prev')
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    if (((COMP_CWORD <= 1)) || $cur == '-' ):
        COMPREPLY=(-p -r -t)
        
        os.system('return 0')
    
    if ($prev == '-p' ):
        COMPREPLY=( os.popen(' compgen -f cur ').read() )
        
        os.system('return 0')
    
    COMPREPLY=( os.popen(' compgen -c cur ').read() )
    
    os.system('return 0')
}
os.system('complete -F _hash_func hash')
def _history_func () 
{ 
    os.system('local cur prev')
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    COMPREPLY=()
    
    if (((COMP_CWORD <= 1)) || $cur == '-' ):
        COMPREPLY=(-a -c -d -n -r -w -p -s)
        
        os.system('return 0')
    
    if ($prev == -[anrw] ):
        COMPREPLY=( os.popen(' compgen -f cur ').read() )
    
    os.system('return 0')
}
os.system('complete -F _history_func history')
#complete -F _read_func read
def _set_func () 
{ 
    os.system('local cur prev')
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    COMPREPLY=()
    
    os.system('_redir_test "" + cur + "" "" + prev + ""') && os.system('return 0')
    
    if (((COMP_CWORD <= 1)) || $cur == '-' ):
        COMPREPLY=(-a -b -e -f -k -m -n -o -p -t -u -v -x -B -C -H -P --)
        
        os.system('return 0')
    
    if ($cur == '+' ):
        COMPREPLY=(+a +b +e +f +k +m +n +o +p +t +u +v +x +B +C +H +P)
        
        os.system('return 0')
    
    if ($prev == [+-]o ):
        COMPREPLY=( os.popen('compgen -A setopt cur').read() )
        
        os.system('return 0')
    
    os.system('return 1')
}
os.system('complete -F _set_func set')
def _trap_func () 
{ 
    os.system('local cur')
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    if (((COMP_CWORD <= 1)) || $cur == '-' ):
        COMPREPLY=(-l -p)
        
        os.system('return 0')
    
    COMPREPLY=( os.popen(' compgen -A signal ${cur}').read() )
    
    os.system('return 0')
}
os.system('complete -F _trap_func trap')
#
# meta-completion (completion for complete/compgen)
#
def _complete_meta_func () 
{ 
    os.system('local cur prev cmd')
    
    COMPREPLY=()
    
    cmd=sys.argv[1]
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    os.system('_redir_test "" + cur + "" "" + prev + ""') && os.system('return 0')
    
    if (((COMP_CWORD <= 1)) || "$cur" == '-' ):
        
            if ( "" + cmd + "" == 'complete'):
                COMPREPLY=(-a -b -c -d -e -f -j -k -s -v -u -r -p -A -G -W -P -S -X -F -C)
            elif ("" + cmd + "" == 'compgen'):
                COMPREPLY=(-a -b -c -d -e -f -j -k -s -v -u -A -G -W -P -S -X -F -C)
        
        os.system('return 0')
    
    if ($prev == -A ):
        COMPREPLY=(alias arrayvar binding builtin command directory disabled enabled export file 'function' helptopic hostname job keyword running service setopt shopt signal stopped variable)
        
        os.system('return 0')
    else:
        if ($prev == -F ):
            COMPREPLY=( os.popen(' compgen -A function cur ').read() )
        else:
            if ($prev == -C ):
                COMPREPLY=( os.popen(' compgen -c cur ').read() )
            else:
                COMPREPLY=( os.popen(' compgen -c cur ').read() )
    
    os.system('return 0')
}
os.system('complete -F _complete_meta_func complete compgen')
#
# some completions for shell reserved words
#
#complete -c -k time do if then else elif '{'
#
# external commands
#
os.system('complete -e printenv')
os.system('complete -c nohup exec nice eval trace truss strace sotruss gdb')
def _make_targets () 
{ 
    os.system('local mdef makef gcmd cur prev i')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    # if prev argument is -f, return possible filename completions.
    
    # we could be a little smarter here and return matches against
    
    # `makefile Makefile *.mk', whatever exists
    
    
        if ( "" + prev + "" == '-*f'):
            COMPREPLY=( os.popen('compgen -f cur ').read() )
            
            os.system('return 0')
    
    # if we want an option, return the possible posix options
    
    
        if ( "" + cur + "" == '-'):
            COMPREPLY=(-e -f -i -k -n -p -q -r -S -s -t)
            
            os.system('return 0')
    
    # make reads `makefile' before `Makefile'
    
    # GNU make reads `GNUmakefile' before all other makefiles, but we
    
    # check that we're completing `gmake' before checking for it
    
    if (os.path.isfile(GNUmakefile ) && ${COMP_WORDS[0]} == gmake  ):
        mdef=GNUmakefile
    else:
        if (os.path.isfile(makefile ) ):
            mdef=makefile
        else:
            if (os.path.isfile(Makefile ) ):
                mdef=Makefile
            else:
                mdef=*.mk
                
                # local convention
    
    # before we scan for targets, see if a makefile name was specified
    
    # with -f
    
    for ((i=0; i < ${#COMP_WORDS[@]}; i++))
    do
        if (${COMP_WORDS[i]} == -*f ):
            os.system('eval makef=${COMP_WORDS[i+1]}')
            
            # eval for tilde expansion
            
            break
    done
    
    -z "" + makef + ""  && makef=mdef
    
    # if we have a partial word to complete, restrict completions to
    
    # matches of that word
    
    if (-n "" + sys.argv[2] + ""  ):
        gcmd='grep "^" + sys.argv[2] + ""'
    else:
        gcmd=cat
    
    # if we don't want to use *.mk, we can take out the cat and use
    
    # test -f $makef and input redirection	
    
    COMPREPLY=( os.popen('cat makef 2>/dev/null | awk 'BEGIN {FS=":"} /^[^.# 	][^=]*:/ {print sys.argv[1]}' | tr -s ' ' '\012' | sort -u | eval gcmd ').read() )
}
os.system('complete -F _make_targets -X '+($*|*.[cho])' make gmake pmake')
def _umount_func () 
{ 
    COMPREPLY=( os.popen('mount | awk '{print sys.argv[1]}'').read() )
}
os.system('complete -F _umount_func umount')
def _configure_func () 
{ 
    
        if ( "" + sys.argv[2] + "" == '-*'):

        else:
            os.system('return')
    
    
        if ( "" + sys.argv[1] + "" == '\~*'):
            os.system('eval cmd=sys.argv[1]')
        else:
            cmd="" + sys.argv[1] + ""
    
    COMPREPLY=( os.popen('"" + cmd + "" --help | awk '{if (sys.argv[1] ~ /--.*/').read()  print sys.argv[1]}' | grep ^"" + sys.argv[2] + "" | sort -u))
}
os.system('complete -F _configure_func configure')
os.system('complete -W '"" + $ + "{GROUPS[@]}"' newgrp')
os.system('complete -f chown ln more cat')
os.system('complete -d mkdir rmdir')
os.system('complete -f strip')
os.system('complete -f -X '*.gz' gzip')
os.system('complete -f -X '*.bz2' bzip2')
os.system('complete -f -X '*.Z' compress')
os.system('complete -f -X '!*.+(gz|tgz|Gz)' gunzip gzcat zcat zmore')
os.system('complete -f -X '!*.Z' uncompress zmore zcat')
os.system('complete -f -X '!*.bz2' bunzip2 bzcat')
os.system('complete -f -X '!*.zip' unzip')
os.system('complete -f -X '!*.+(gif|jpg|jpeg|GIF|JPG|JPEG|bmp)' xv')
os.system('complete -f -X '!*.pl' perl perl5')
os.system('complete -A hostname rsh telnet rlogin ftp ping xping host traceroute nslookup')
os.system('complete -A hostname rxterm rxterm3 rxvt2')
os.system('complete -u su')
os.system('complete -g newgrp groupdel groupmod')
os.system('complete -f -X '!*.+(ps|PS)' gs gv ghostview psselect pswrap')
os.system('complete -f -X '!*.+(dvi|DVI)' dvips xdvi dviselect dvitype catdvi')
os.system('complete -f -X '!*.+(pdf|PDF)' acroread4')
os.system('complete -f -X '!*.texi*' makeinfo texi2dvi texi2html')
os.system('complete -f -X '!*.+(tex|TEX)' tex latex slitex')
os.system('complete -f -X '!*.+(mp3|MP3)' mpg123')
os.system('complete -f -X '!*.+(htm|html)' links w3m lynx')
#
# other possibilities, left as exercises
#
#complete -F _find_func find
#complete -F _man_func man
#complete -F _stty_func stty
