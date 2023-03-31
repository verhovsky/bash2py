import sys, os, os.path
from stat import *
# Who said shells can't use recursion?  Here is a factorial function.
# You call it with a number as an argument, and it returns the factorial
# of that number.
def fact () 
{ 
    os.system('local num=sys.argv[1]')
    
    if ("" + num + "" == 1  ):
        print("1")
        
        os.system('return')
    
    print("( num *  os.popen('fact $(( num - 1 ').read() ) ) )")
}
