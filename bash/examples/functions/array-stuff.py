import sys, os, os.path
from stat import *
# usage: reverse arrayname
def reverse () 
{ 
    os.system('local -a R')
    
    os.system('local -i i')
    
    os.system('local rlen temp')
    
    # make r a copy of the array whose name is passed as an arg
    
    os.system('eval R=\( \"\" + $ + "\{" + sys.argv[1] + "\[@\]\}\" \)')
    
    # reverse R
    
    rlen=${#R[@]}
    
    for ((i=0; i < rlen/2; i++))
    do
        temp=${R[i]}
        
        R[i]=${R[rlen-i-1]}
        
        R[rlen-i-1]=temp
    done
    
    # and assign R back to array whose name is passed as an arg
    
    os.system('eval sys.argv[1]=\( \"\" + $ + "\{R\[@\]\}\" \)')
}
A=(1 2 3 4 5 6 7)
print("" + $ + "{A[@]}")
os.system('reverse A')
print("" + $ + "{A[@]}")
os.system('reverse A')
print("" + $ + "{A[@]}")
# unset last element of A
alen=${#A[@]}
os.system('unset A[alen-1]')
print("" + $ + "{A[@]}")
# ashift -- like shift, but for arrays
def ashift () 
{ 
    os.system('local -a R')
    
    os.system('local n')
    
    
        if ( $# == '1'):
            n=1
        elif ($# == '2'):
            n=sys.argv[2]
        else:
            print("" + FUNCNAME + ": usage: " + FUNCNAME + " array [count]")1>&2
            
            exit(2)
    
    # make r a copy of the array whose name is passed as an arg
    
    os.system('eval R=\( \"\" + $ + "\{" + sys.argv[1] + "\[@\]\}\" \)')
    
    # shift R
    
    R=("" + $ + "{R[@]:" + n + "}")
    
    # and assign R back to array whose name is passed as an arg
    
    os.system('eval sys.argv[1]=\( \"\" + $ + "\{R\[@\]\}\" \)')
}
os.system('ashift A 2')
print("" + $ + "{A[@]}")
os.system('ashift A')
print("" + $ + "{A[@]}")
os.system('ashift A 7')
print("" + $ + "{A[@]}")
# Sort the members of the array whose name is passed as the first non-option
# arg.  If -u is the first arg, remove duplicate array members.
def array_sort () 
{ 
    os.system('local -a R')
    
    os.system('local u')
    
    
        if ( "" + sys.argv[1] + "" == '-u'):
            u=-u
            
            os.system('shift')
    
    if ($# == 0  ):
        print("array_sort: argument expected")1>&2
        
        os.system('return 1')
    
    # make r a copy of the array whose name is passed as an arg
    
    os.system('eval R=\( \"\" + $ + "\{" + sys.argv[1] + "\[@\]\}\" \)')
    
    # sort R
    
    R=( os.popen(' printf "%s\n" "" + $ + "{A[@]}" | sort u').read() )
    
    # and assign R back to array whose name is passed as an arg
    
    os.system('eval sys.argv[1]=\( \"\" + $ + "\{R\[@\]\}\" \)')
    
    os.system('return 0')
}
A=(3 1 4 1 5 9 2 6 5 3 2)
os.system('array_sort A')
print("" + $ + "{A[@]}")
A=(3 1 4 1 5 9 2 6 5 3 2)
os.system('array_sort -u A')
print("" + $ + "{A[@]}")
