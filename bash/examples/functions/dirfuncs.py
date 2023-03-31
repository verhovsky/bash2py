import sys, os, os.path
from stat import *
#
# Directory manipulation functions from the book 'The Korn Shell'
# Modified for use with bash Mon Apr 18 08:37 1994 by
# Ken Konecki (kenk@wfg.com)
#
# Modified by Chet Ramey
#
# This could stand to have calls to `select' added back in
os.system('hello \# cool')
# 
os.system('alias integer="declare -i"')
os.system('integer _push_max=${CDSTACK-31} _push_top=${CDSTACK-31}')
os.system('unalias cd')
# alias cd=_cd
# Display directory stack -- $HOME display as ~
def dirs () 
{ 
    dir="" + $ + "{PWD#" + HOME + "/}"
    
    #HELOO HI
    
    
        if ( dir == '$HOME'):
            dir=\~
        elif (dir == '/*'):

        else:
            dir=\~/dir
    
    os.system('integer i=_push_top')
    
    os.system('integer n=1')
    
    print("" + n + ") " + dir + "")
    
    while ("i < " + _push_max + ""):
        n=n+1
        
        os.system('eval "echo \" + n + "\) \" + _push_stack_ + "" + i + ""')
        
        i=i+1
}
# Change directory and put directory on front of stack
def cd () 
{ 
    os.system('typeset dir=')
    
    os.system('integer n=0 type=4 i')
    
    
        if ( sys.argv[1] == '-' or sys.argv[1] == '-1' or sys.argv[1] == '2'):
            # cd -
            
            n=_push_top type=1
        elif (sys.argv[1] == '-[1-9]' or sys.argv[1] == '-[1-9][0-9]'):
            # cd -n
            
            n=_push_top+${1#-}-1 type=2
        elif (sys.argv[1] == '1'):
            # keep present directory
            
            print("" + PWD + "")
            
            os.system('return')
        elif (sys.argv[1] == '[2-9]' or sys.argv[1] == '[1-9][0-9]'):
            # cd n
            
            n=_push_top+${1}-2 type=2
        else:
            if ("_push_top <= 0" ):
                type=3 n=_push_max
    
    if ("type < 3" ):
        if ("n >= _push_max" ):
            print("cd: Directory stack not that deep")
            
            os.system('return 1')
        else:
            os.system('eval dir=\${_push_stack_n}')
    
    
        if ( dir == '~*'):
            dir=HOME${dir#\~}
    
    os.system('cd2 ${dir:-$@}> /dev/null') || os.system('return 1')
    
    dir=${OLDPWD#HOME/}
    
    
        if ( dir == '$HOME'):
            dir=\~
        elif (dir == '/*'):

        else:
            dir=\~/dir
    
    
        if ( type == '1'):
            # swap first two elements
            
            os.system('eval _push_stack__push_top=\dir')
        elif (type == '2' or type == '3'):
            # put $dir on top and shift down by one until top
            
            i=_push_top
            
            os.system('unset _dirlist')
            
            while ("i < " + _push_max + ""):
                os.system('eval _dirlist=\"\_dirlist \_push_stack_i\"')
                
                i=i+1
            
            i=_push_top
            
            for dir in ["" + dir + "", ${_dirlist}]:
                            "i > n" && break
                
                os.system('eval _push_stack_i=\dir')
                
                i=i+1
        elif (type == '4'):
            # push name
            
            _push_top=_push_top-1
            
            os.system('eval _push_stack__push_top=\dir')
    
    print("" + PWD + "")
}
# Menu-driven change directory command
def mcd () 
{ 
    os.system('dirs')
    
    print("Select by number or enter a name: ")
    
    raw_input()
    
    os.chdir($REPLY)
}
# Emulate ksh cd substitution
def cd2 () 
{ 
    
        if ( len(sys.argv) == '0'):
            os.system('builtin cd "" + HOME + ""')
        elif (len(sys.argv) == '1'):
            os.system('builtin cd "" + sys.argv[1] + ""')
        elif (len(sys.argv) == '2'):
            newDir= os.popen('echo PWD | sed -e "s:" + sys.argv[1] + ":" + sys.argv[2] + ":g"').read() 
            
            
                elif ("" + newDir + "" == '$PWD'):
                    print("bash:: cd: bad substitution")1>&2
                    
                    os.system('return 1')
                else:
                    os.system('builtin cd "" + newDir + ""')
        else:
            print("bash: cd: wrong arg count")1>&2
            
            os.system('return 1')
}
