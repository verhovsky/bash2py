import sys, os, os.path
from stat import *
#####
#To: chet@po.cwru.edu, sarahmckenna@lucent.com
#Message-Id: <slrn8mqioc.msb.ian@lovelorn.linuxcare.com>
#Posted-To: comp.unix.shell, gnu.bash.bug
#Subject: bash 2.04 programmable completion examples
#Reply-To: ian@linuxcare.com, ian@caliban.org
#Summary: examples of programmable completion for bash 2.04
#Date: Thu, 13 Jul 2000 00:52:33 -0400 (EDT)
#From: ianmacd@linuxcare.com (Ian Macdonald)
#####
#########################################################################
# Turn on extended globbing
os.system('shopt -s extglob')
# A lot of the following one-liners were taken directly from the
# completion examples provided with the bash 2.04 source distribution
# Make directory commands see only directories
os.system('complete -d cd mkdir rmdir pushd')
# Make file commands see only files
os.system('complete -f cat less more chown ln strip')
os.system('complete -f -X '*.gz' gzip')
os.system('complete -f -X '*.Z' compress')
os.system('complete -f -X '!*.+(Z|gz|tgz|Gz)' gunzip zcat zmore')
os.system('complete -f -X '!*.Z' uncompress zmore zcat')
os.system('complete -f -X '!*.+(gif|jpg|jpeg|GIF|JPG|bmp)' ee xv')
os.system('complete -f -X '!*.+(ps|PS|ps.gz)' gv')
os.system('complete -f -X '!*.+(dvi|DVI)' dvips xdvi dviselect dvitype')
os.system('complete -f -X '!*.+(pdf|PDF)' acroread xpdf')
os.system('complete -f -X '!*.texi*' makeinfo texi2dvi texi2html')
os.system('complete -f -X '!*.+(tex|TEX)' tex latex slitex')
os.system('complete -f -X '!*.+(mp3|MP3)' mpg123')
# kill sees only signals
os.system('complete -A signal kill -P '%'')
# user commands see only users
os.system('complete -u finger su usermod userdel passwd')
# bg completes with stopped jobs
os.system('complete -A stopped -P '%' bg')
# other job commands
os.system('complete -j -P '%' fg jobs disown')
# network commands complete with hostname
os.system('complete -A hostname ssh rsh telnet rlogin ftp ping fping host traceroute nslookup')
# export and others complete with shell variables
os.system('complete -v export local readonly unset')
# set completes with set options
os.system('complete -A setopt set')
# shopt completes with shopt options
os.system('complete -A shopt shopt')
# helptopics
os.system('complete -A helptopic help')
# unalias completes with aliases
os.system('complete -a unalias')
# various commands complete with commands
os.system('complete -c command type nohup exec nice eval strace gdb')
# bind completes with readline bindings (make this more intelligent)
os.system('complete -A binding bind')
# Now we get to the meat of the file, the functions themselves. Some
# of these are works in progress. Most assume GNU versions of the
# tools in question and may require modifications for use on vanilla
# UNIX systems.
#
# A couple of functions may have non-portable, Linux specific code in
# them, but this will be noted where applicable
# GNU chown(1) completion. This should be expanded to allow the use of
# ':' as well as '.' as the user.group separator.
#
def _chown () 
{ 
    os.system('local cur prev user group')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    # do not attempt completion if we're specifying an option
    
    if ("" + $ + "{cur:0:1}" == "-"  ):
        os.system('return 0')
    
    # first parameter on line or first since an option?
    
    if (COMP_CWORD == 1  || "" + $ + "{prev:0:1}" == "-"  ):
        
            if ( "" + cur + "" == '[a-zA-Z]*.*'):
                user=${cur%.*}
                
                group=${cur#*.}
                
                COMPREPLY=($( awk 'BEGIN {FS=":"} \

                
                for ((i=0; i < ${#COMPREPLY[@]}; i++))
                do
                    COMPREPLY[i]=user.${COMPREPLY[i]}
                done
                
                os.system('return 0')
            else:
                COMPREPLY=( os.popen(' compgen -u cur -S '.' ').read() )
                
                os.system('return 0')
    else:
        COMPREPLY=( os.popen(' compgen -f cur ').read() )
    
    os.system('return 0')
}
os.system('complete -F _chown chown')
# umount(8) completion. This relies on the mount point being the third
# space-delimited field in the output of mount(8)
#
def _umount () 
{ 
    os.system('local cur')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    # could rewrite the cut | grep to be a sed command, but this is
    
    # clearer and doesn't result in much overhead
    
    COMPREPLY=( os.popen(' mount | cut -d' ' -f 3 | grep ^cur').read() )
    
    os.system('return 0')
}
os.system('complete -F _umount umount')
# GID completion. This will get a list of all valid group names from
# /etc/group and should work anywhere.
#
def _gid_func () 
{ 
    os.system('local cur')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    COMPREPLY=( os.popen(' awk 'BEGIN {FS=":"} {if (sys.argv[1] ~ /^'cur'/').read()  print sys.argv[1]}' 			   /etc/group ))
    
    os.system('return 0')
}
os.system('complete -F _gid_func groupdel groupmod')
# mount(8) completion. This will pull a list of possible mounts out of
# /etc/fstab, unless the word being completed contains a ':', which
# would indicate the specification of an NFS server. In that case, we
# query the server for a list of all available exports and complete on
# that instead.
#
def _mount () 
{ 
    os.system('local cur')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    
        if ( "" + cur + "" == '*:*'):
            COMPREPLY=( os.popen(' /usr/sbin/showmount -e --no-headers ${cur%%:*} |			       grep ^${cur#*:} | awk '{print sys.argv[1]}'').read() )
            
            os.system('return 0')
        else:
            COMPREPLY=( os.popen(' awk '{if (sys.argv[2] ~ /\//').read()  print sys.argv[2]}' /etc/fstab | 			       grep ^cur ))
            
            os.system('return 0')
}
os.system('complete -F _mount mount')
# Linux rmmod(1) completion. This completes on a list of all currently
# installed kernel modules.
#
def _rmmod () 
{ 
    os.system('local cur')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    COMPREPLY=( os.popen(' lsmod | awk '{if (NR != 1 && sys.argv[1] ~ /^'cur'/').read()  print sys.argv[1]}'))
    
    os.system('return 0')
}
os.system('complete -F _rmmod rmmod')
# Linux insmod(1) completion. This completes on a list of all
# available modules for the version of the kernel currently running.
#
def _insmod () 
{ 
    os.system('local cur modpath')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    modpath=/lib/modules/ os.popen('uname -r').read() 
    
    COMPREPLY=( os.popen(' ls -R modpath | sed -ne 's/^\('cur'.*\').read() \.o$/\1/p'))
    
    os.system('return 0')
}
os.system('complete -F _insmod insmod depmod modprobe')
# man(1) completion. This relies on the security enhanced version of
# GNU locate(1). UNIX variants having non-numeric man page sections
# other than l, m and n should add the appropriate sections to the
# first clause of the case statement.
#
# This is Linux specific, in that 'man <section> <page>' is the
# expected syntax. This allows one to do something like
# 'man 3 str<tab>' to obtain a list of all string handling syscalls on
# the system.
#
def _man () 
{ 
    os.system('local cur prev')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    
        if ( "" + prev + "" == '[0-9lmn]'):
            COMPREPLY=( os.popen(' slocate -ql 0 -r '/man/man'prev'/'cur | 		      sed -ne 's/^.*\/\('cur'[^.\/]*\').read() \..*$/\1/p' ))
            
            os.system('return 0')
        else:
            COMPREPLY=( os.popen(' slocate -ql 0 -r '/man/man./'cur | 		      sed -ne 's/^.*\/\('cur'[^.\/]*\').read() \..*$/\1/p' ))
            
            os.system('return 0')
}
os.system('complete -F _man man')
# Linux killall(1) completion. This wouldn't be much use on, say,
# Solaris, where killall does exactly that: kills ALL processes.
#
# This could be improved. For example, it currently doesn't take
# command line options into account
#
def _killall () 
{ 
    os.system('local cur prev')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    
        if ( "" + prev + "" == '-[A-Z0-9]*'):
            # get a list of processes (the first sed evaluation
            
            # takes care of swapped out processes, the second
            
            # takes care of getting the basename of the process)
            
            COMPREPLY=( os.popen(' ps ahx | awk '{if (sys.argv[5] ~ /^'cur'/').read()  print sys.argv[5]}' | 			       sed -e 's#[]\[]##g' -e 's#^.*/##' ))
            
            os.system('return 0')
    
    # first parameter can be either a signal or a process
    
    if (COMP_CWORD == 1  ):
        # standard signal completion is rather braindead, so we need
        
        # to hack around to get what we want here, which is to
        
        # complete on a dash, followed by the signal name minus
        
        # the SIG prefix
        
        COMPREPLY=( os.popen(' compgen -A signal SIG${cur#-} ').read() )
        
        for ((i=0; i < ${#COMPREPLY[@]}; i++))
        do
            COMPREPLY[i]=-${COMPREPLY[i]#SIG}
        done
    
    # get processes, adding to signals if applicable
    
    COMPREPLY=(${COMPREPLY[*]}  os.popen(' ps ahx | 		                       awk '{if (sys.argv[5] ~ /^'cur'/').read()  print sys.argv[5]}' | 				       sed -e 's#[]\[]##g' -e 's#^.*/##' ))
    
    os.system('return 0')
}
os.system('complete -F _killall killall')
# GNU find(1) completion. This makes heavy use of ksh style extended
# globs and contains Linux specific code for completing the parameter
# to the -fstype option.
#
