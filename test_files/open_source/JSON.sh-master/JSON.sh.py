#! /usr/bin/env python
import sys,os,subprocess
from stat import *
def throw () :
    print(str(" ".join(sys.argv[1:])))
    exit(1)

BRIEF=0
LEAFONLY=0
PRUNE=0
def usage () :
    print()
    print("Usage: JSON.sh [-b] [-l] [-p] [-h]")
    print()
    print("-p - Prune empty. Exclude fields with empty values.")
    print("-l - Leaf only. Only show leaf nodes, which stops data duplication.")
    print("-b - Brief. Combines 'Leaf only' and 'Prune empty' options.")
    print("-h - This help text.")
    print()

def parse_options () :
    global BRIEF
    global LEAFONLY
    global PRUNE

    _rc = subprocess.call(["set",--,str('"'+"\" \"".join(sys.argv[1:])+'"')])
    ARGN=str(len(sys.argv))
    while (ARGN != 0 ):
        
        if ( str(sys.argv[1]) == '-h'):
            usage()
            exit(0)
        elif ( str(sys.argv[1]) == '-b'):
            BRIEF=1
            LEAFONLY=1
            PRUNE=1
        elif ( str(sys.argv[1]) == '-l'):
            LEAFONLY=1
        elif ( str(sys.argv[1]) == '-p'):
            PRUNE=1
        elif ( str(sys.argv[1]) == '?*'):
            print("ERROR: Unknown option.")
            usage()
            exit(0)
        _rc = subprocess.call(["shift",1])
        ARGN=(ARGN-1)

def awk_egrep () :
    global pattern

    pattern_string=str(sys.argv[1])
    _rc = subprocess.call(["gawk",r'{
        while ("+str(__file__)+") {
          start=match("+str(__file__)+", pattern);
          token=substr("+str(__file__)+", start, RLENGTH);
          print token;
          "+str(__file__)+"=substr("+str(__file__)+", start+RLENGTH);
        }
      }',pattern=str(pattern_string)])

def tokenize () :
    global 

    "GREP"
    "ESCAPE"
    "CHAR"
    if (print("test string") | _rc = subprocess.Popen("egrep" + " " + "-ao" + " " + "--color=never" + " " + "test",shell=True,stderr=file('/dev/null','wb'),stdout=file('/dev/null','wb'))
     ):
        GREP=r'egrep -ao --color=never'
    else:
        GREP=r'egrep -ao'
    if (print("test string") | _rc = subprocess.Popen("egrep" + " " + or + " " + "test",shell=True,stderr=file('/dev/null','wb'),stdout=file('/dev/null','wb'))
     ):
        ESCAPE=r'(\\[^u[:cntrl:]]|\\u[0-9a-fA-F]{4})'
        CHAR=r'[^[:cntrl:]"\\]'
    else:
        GREP="awk_egrep"
        ESCAPE=r'(\\\\[^u[:cntrl:]]|\\u[0-9a-fA-F]{4})'
        CHAR=r'[^[:cntrl:]"\\\\]'
    STRING="\""+str(CHAR)+"*("+str(ESCAPE)+""+str(CHAR)+"*)*\""
    NUMBER=r'-?(0|[1-9][0-9]*)([.][0-9]*)?([eE][+-]?[0-9]*)?'
    KEYWORD=r'null|false|true'
    SPACE=r'[[:space:]]+'
    _rc = subprocess.call([str(GREP),str(STRING)+"|"+str(NUMBER)+"|"+str(KEYWORD)+"|"+str(SPACE)+"|."]) | _rc = subprocess.call(["egrep","-v","^"+str(SPACE)+""+str()])

def parse_array () :
    global token
    global value
    global BRIEF

    index=0
    ary=r''
    -r = raw_input()
    
    if ( str(token) == '']''):
    
    else:
        while (_rc = subprocess.call([:])):
            _rc = subprocess.call(["parse_value",str(sys.argv[1]),str(index)])
            index=(index+1)
            ary=str(ary)+str(value)
            -r = raw_input()
            
            elif ( str(token) == '']''):
                break
            elif ( str(token) == '',''):
                ary=str(ary)+","
            else:
                throw()
            -r = raw_input()
    BRIEF == 0  and value=os.popen("printf '[%s]' \""+str(ary)+"\"").read() or value=
    _rc = subprocess.call([:])

def parse_object () :
    global token
    global value
    global BRIEF

    "key"
    obj=r''
    -r = raw_input()
    
    if ( str(token) == ''}''):
    
    else:
        while (_rc = subprocess.call([:])):
            
            elif ( str(token) == ''"'*'"''):
                key=str(token)
            else:
                throw()
            -r = raw_input()
            
            if ( str(token) == '':''):
            
            else:
                throw()
            -r = raw_input()
            _rc = subprocess.call(["parse_value",str(sys.argv[1]),str(key)])
            obj=str(obj)+""+str(key)+":"+str(value)
            -r = raw_input()
            
            if ( str(token) == ''}''):
                break
            elif ( str(token) == '',''):
                obj=str(obj)+","
            else:
                throw()
            -r = raw_input()
    BRIEF == 0  and value=os.popen("printf '{%s}' \""+str(obj)+"\"").read() or value=
    _rc = subprocess.call([:])

def parse_value () :
    global isleaf
    global isempty
    global print
    global token
    global value
    global LEAFONLY
    global PRUNE

    jpath=str(sys.argv[1])+""+str(sys.argv[2]) isleaf=0 isempty=0 print=0
    
    if ( str(token) == ''{''):
        parse_object()
    elif ( str(token) == ''[''):
        parse_array()
    elif ( str(token) == '''' or str(token) == '[!0-9]'):
        # At this point, the only valid single-character tokens are digits.
        throw()
    else:
        value=str(token)
        isleaf=1
        value == r'""'  and isempty=1
    value == r''  and return
    LEAFONLY == 0  and PRUNE == 0  and print=1
    LEAFONLY == 1  and isleaf == 1  and PRUNE == 0  and print=1
    LEAFONLY == 0  and PRUNE == 1  and isempty == 0  and print=1
    LEAFONLY == 1  and isleaf == 1  and PRUNE == 1  and isempty == 0  and print=1
    print == 1  and print( "[%s]\t%s\n" % (str(jpath), str(value)) )
    
    _rc = subprocess.call([:])

def parse () :
    global token

    -r = raw_input()
    parse_value()
    -r = raw_input()
    
    if ( str(token) == ''''):
    
    else:
        throw()

parse_options()
if (( __file__ == BASH_SOURCE  or ! (str(BASH_SOURCE)  != '') ) ):
    tokenize() | parse()
