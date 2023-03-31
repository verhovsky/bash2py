import sys, os, os.path
from stat import *
# @(#)precedence_test 1.0 91/07/24 Maarten Litmaath
# test of relative precedences for `&&' and `||' operators
print("\`Say' echos its argument. Its return value is of no interest.")

    if (  os.popen('echo -n').read()  == ''''):
        def Say () 
        { 
            print("" + $ + "*")
        }
    else:
        def Say () 
        { 
            print("" + $ + "*\c")
        }
print("\`Truth' echos its argument and returns a TRUE result.")
def Truth () 
{ 
    os.system('Say sys.argv[1]')
    
    os.system('return 0')
}
print("\`False' echos its argument and returns a FALSE result.")
def False () 
{ 
    os.system('Say sys.argv[1]')
    
    os.system('return 1')
}
print("")
cmd1='open test1 && test2 close || test3'
cmd2='test1 || open test2 && test3 close'
grouping_sh=
grouping_C='( )'
test3='Say 3'
for i in [1, 2]:
    os.system('eval proto=\cmdi')
    for test1 in ['Truth 1', 'False 1']:
            for test2 in ['Truth 2', 'False 2']:
                    for precedence in [sh, C]:
                            os.system('eval set x \grouping_precedence')
                os.system('shift')
                open=${1-' '}
                close=${2-' '}
                os.system('eval cmd=\""proto"\"')
                os.system('Say "" + cmd + "   output="')
                output= os.popen('eval "" + cmd + ""').read() 
                os.system('Say "" + output + ""')
                correct = raw_input() || { print("'Input fubar.  Abort.'")1>&2
                exit(1) }
                os.system('test "X" + output + "" == "X" + correct + ""') || print("   correct=" + correct + "")
                print("''")
            print("''")  <<EOF
12
12
123
123
13
13
13
13
13
1
13
1
123
123
12
12
EOF

