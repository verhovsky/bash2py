import sys, os, os.path
from stat import *
#
# cdhist - cd replacement with a directory stack like pushd/popd
#
# usage: cd [-l] [-n] [-] [dir]
#
# options:
#	-l	print the cd directory stack, one entry per line
#	-	equivalent to $OLDPWD
#	-n	cd to nth directory in cd directory stack
#	-s	cd to first directory in stack matching (substring) `s'
#
# arguments:
#	dir	cd to dir and push dir onto the cd directory stack
#
# If the new directory is a directory in the stack and the options selected
# it (-n, -s), the new working directory is printed
#
# If the variable CDHISTFILE is set, the cd directory stack is loaded from
# and written to $CDHISTFILE every time `cd' is executed.
#
# Note: I got this off the net somewhere; I don't know the original author
#
# Chet Ramey
# chet@po.cwru.edu	
def _cd_print () 
{ 
    print("" + $ + "@")
}
def cd () 
{ 
    os.system('typeset -i cdlen i')
    
    os.system('typeset t')
    
    if ($# == 0  ):
        os.system('set -- HOME')
    
    if ( "" + CDHISTFILE + ""  && -r "" + CDHISTFILE + "" 
    
    # if directory history exists ):
        os.system('typeset CDHIST')
        
        i=-1
        
        while (-r = raw_input()
        
        # read directory history file):
            CDHIST[i=i+1]=t < $CDHISTFILE
    
    if ("" + $ + "{CDHIST[0]}" != "" + PWD + ""  && -n "" + PWD + ""  ):
        os.system('_cdins')
        
        # insert $PWD into cd history
    
    cdlen=${#CDHIST[*]}
    
    # number of elements in history
    
    
        if ( "" + $ + "@" == '-'):
            # cd to new dir
            
            if ("" + OLDPWD + "" == ""  && ((cdlen>1)) ):
                os.system(''_cdprint' ${CDHIST[1]}')
                
                os.system('builtin cd ${CDHIST[1]}')
                
                os.getcwd()
            else:
                os.system('builtin cd "" + $ + "@"')
                
                # pwd
        elif ("" + $ + "@" == '-l'):
            # _cdprint directory list
            
            ((i=cdlen))
            
            while ((((i=i-1)>=0))):
                num=i
                
                os.system(''_cdprint' "" + num + " " + $ + "{CDHIST[i]}"')
            
            os.system('return')
        elif ("" + $ + "@" == '-[0-9]' or "" + $ + "@" == '-[0-9][0-9]'):
            # cd to dir in list
            
            if ((((i=${1#-})<cdlen)) ):
                os.system(''_cdprint' ${CDHIST[i]}')
                
                os.system('builtin cd ${CDHIST[i]}')
                
                os.getcwd()
            else:
                os.system('builtin cd $@')
                
                # pwd
        elif ("" + $ + "@" == '-*'):
            # cd to matched dir in list
            
            t=${1#-}
            
            i=1
            
            while (((i<cdlen))):
                
                    elif (${CDHIST[i]} == '*$t*'):
                        os.system(''_cdprint' ${CDHIST[i]}')
                        
                        os.system('builtin cd ${CDHIST[i]}')
                        
                        os.getcwd()
                        
                        break
                
                ((i=i+1))
            
            if (((i>=cdlen)) ):
                os.system('builtin cd $@')
                
                # pwd
        else:
            # cd to new dir
            
            os.system('builtin cd $@')
            
            # pwd
    
    os.system('_cdins')
    
    # insert $PWD into cd history
    
    if ( "" + CDHISTFILE + ""  ):
        cdlen=${#CDHIST[*]}
        
        # number of elements in history
        
        i=0
        
        while (((i<cdlen))):
            print("${CDHIST[i]}")
            
            # update directory history
            
            ((i=i+1)) > $CDHISTFILE
}
