import sys, os, os.path
from stat import *
# this is a line editor using only /bin/sh, /bin/dd and /bin/rm
# /bin/rm is not really required, but it is nice to clean up temporary files
PATH=
dd=/bin/dd
rm=/bin/rm
# temporary files we might need
tmp=/tmp/silly.$$
ed=/tmp/ed.$$
os.system('trap "" + rm + " -f " + tmp + " " + tmp + ".1 " + tmp + ".2 " + tmp + ".3 " + tmp + ".4 " + tmp + ".5 " + tmp + ".6 " + ed + ".a " + ed + ".b " + ed + ".c; exit" 0 1 2 3')
# from now on, no more rm - the above trap is enough
os.system('unset rm')
# we do interesting things with IFS, but better save it...
saveIFS="" + IFS + ""
# in case "echo" is not a shell builtin...
def Echo () 
{ 
    
        if ( "" + sys.argv[1] + "" == '-n'):
            os.system('shift')
            
            os.system('dd of=tmp2> /dev/null ') <<EOF
$@
EOF

            IFS="+"
            
            os.system('set  os.popen('dd if=tmp bs=1 of=/dev/null skip=1 2>&1').read() ')
            
            IFS="" + saveIFS + ""
            
            os.system('dd if=tmp bs=1 count=sys.argv[1]2> /dev/null')
        else:
            os.system('dd2> /dev/null  <<EOF
$@
EOF
')
}
# this is used to generate garbage files
def true () 
{ 
    os.system('return 0')
}
def false () 
{ 
    os.system('return 1')
}
def zero () 
{ 
    ( os.system('trap 'go=false' 13')
    
    go=true
    
    while (os.system('go')):
        os.system('dd "if=" + sys.argv[0] + ""')
        
        
            if ( "" + $ + "?" == '0'):

            else:
                go=false ) 2> /dev/null
}
# arithmetic using dd!
# add variable n1 n2 n3...
# assigns n1+n2+n3+... to variable
def add () 
{ 
    result="" + sys.argv[1] + ""
    
    os.system('shift')
    
    os.system('dd if=/dev/null of=tmp bs=12> /dev/null')
    
    for n in ["" + $ + "@"]:
            
            if ( "" + n + "" == '0'):

            else:
                os.system('zero') | os.system('dd of=tmp.1 bs=1 "count=" + n + ""2> /dev/null')
                
                ( os.system('dd if=tmp')
                
                os.system('dd if=tmp.1') ) 2> /dev/null | os.system('dd of=tmp.22> /dev/null')
                
                os.system('dd if=tmp.2 of=tmp2> /dev/null')
    
    IFS="+"
    
    os.system('set  os.popen('dd if=tmp bs=1 of=/dev/null 2>&1').read() ')
    
    IFS="" + saveIFS + ""
    
    os.system('eval result='sys.argv[1]'')
}
# subtract variable n1 n2
# subtracts n2 from n1, assigns result to variable
def subtract () 
{ 
    result="" + sys.argv[1] + ""
    
    os.system('zero') | os.system('dd of=tmp bs=1 "count=" + sys.argv[2] + ""2> /dev/null')
    
    IFS="+"
    
    os.system('set  os.popen('dd if=tmp bs=1 of=/dev/null "skip=" + sys.argv[3] + "" 2>&1').read() ')
    
    IFS="" + saveIFS + ""
    
    
        if ( "" + sys.argv[1] + "" == 'dd*'):
            os.system('set 0')
    
    os.system('eval result='sys.argv[1]'')
}
# multiply variable n1 n2
# variable = n1 * n2
def multiply () 
{ 
    result="" + sys.argv[1] + ""
    
    os.system('zero') | os.system('dd "bs=" + sys.argv[2] + "" of=tmp "count=" + sys.argv[3] + ""2> /dev/null')
    
    IFS="+"
    
    os.system('set  os.popen('dd if=tmp bs=1 of=/dev/null 2>&1').read() ')
    
    IFS="" + saveIFS + ""
    
    os.system('eval result='sys.argv[1]'')
}
# divide variable n1 n2
# variable = int( n1 / n2 )
def divide () 
{ 
    result="" + sys.argv[1] + ""
    
    os.system('zero') | os.system('dd bs=1 of=tmp "count=" + sys.argv[2] + ""2> /dev/null')
    
    IFS="+"
    
    os.system('set  os.popen('dd if=tmp "bs=" + sys.argv[3] + "" of=/dev/null 2>&1').read() ')
    
    IFS="" + saveIFS + ""
    
    os.system('eval result='sys.argv[1]'')
}
# compare variable n1 n2 sets variable to lt if n1<n2, gt if n1>n2, eq if n1==n2
def compare () 
{ 
    res="" + sys.argv[1] + ""
    
    n1="" + sys.argv[2] + ""
    
    n2="" + sys.argv[3] + ""
    
    os.system('subtract somename "" + n1 + "" "" + n2 + ""')
    
    
        if ( "" + somename + "" == '0'):

        else:
            os.system('eval res=gt')
            
            os.system('return')
    
    os.system('subtract somename "" + n2 + "" "" + n1 + ""')
    
    
        if ( "" + somename + "" == '0'):

        else:
            os.system('eval res=lt')
            
            os.system('return')
    
    os.system('eval res=eq')
}
# lt n1 n2 returns true if n1 < n2
def lt () 
{ 
    n1="" + sys.argv[1] + ""
    
    n2="" + sys.argv[2] + ""
    
    os.system('subtract somename "" + n2 + "" "" + n1 + ""')
    
    
        if ( "" + somename + "" == '0'):
            os.system('return 1')
    
    os.system('return 0')
}
# le n1 n2 returns true if n1 <= n2
def le () 
{ 
    n1="" + sys.argv[1] + ""
    
    n2="" + sys.argv[2] + ""
    
    os.system('subtract somename "" + n1 + "" "" + n2 + ""')
    
    
        if ( "" + somename + "" == '0'):
            os.system('return 0')
    
    os.system('return 1')
}
# gt n1 n2 returns true if n1 > n2
def gt () 
{ 
    n1="" + sys.argv[1] + ""
    
    n2="" + sys.argv[2] + ""
    
    os.system('subtract somename "" + n1 + "" "" + n2 + ""')
    
    
        if ( "" + somename + "" == '0'):
            os.system('return 1')
    
    os.system('return 0')
}
# ge n1 n2 returns true if n1 >= n2
def ge () 
{ 
    n1="" + sys.argv[1] + ""
    
    n2="" + sys.argv[2] + ""
    
    os.system('subtract somename "" + n2 + "" "" + n1 + ""')
    
    
        if ( "" + somename + "" == '0'):
            os.system('return 0')
    
    os.system('return 1')
}
# useful functions for the line editor
# open a file - copy it to the buffers
def open () 
{ 
    file="" + sys.argv[1] + ""
    
    os.system('set  os.popen('dd "if=" + file + "" of=/dev/null 2>&1').read() ')
    
    
        if ( "" + sys.argv[1] + "" == 'dd*'):
            os.system('return 1')
    
    # copy the first line to $ed.c
    
    go=true
    
    len=0
    
    while (os.system('go')):
        
            if ( " os.popen('" + dd + " "if=file" bs=1 skip=" + len + " count=1 2>/dev/null').read() " == '?*'):
                go=true
            else:
                go=false
        
        os.system('add len 1 len')
    
    # now $len is the length of the first line (including newline)
    
    os.system('dd "if=" + file + "" bs=1 count=len of=ed.c2> /dev/null')
    
    os.system('dd "if=" + file + "" bs=1 skip=len of=ed.b2> /dev/null')
    
    os.system('dd if=/dev/null of=ed.a2> /dev/null')
    
    lineno=1
}
# save a file - copy the buffers to the file
def save () 
{ 
    # make a backup copy of the original
    
    os.system('dd "if=" + sys.argv[1] + "" "of=" + sys.argv[1] + ".bak"2> /dev/null')
    
    # and save
    
    ( os.system('dd if=ed.a')
    
    os.system('dd if=ed.c')
    
    os.system('dd if=ed.b') ) > "$1" 2> /dev/null
}
# replace n1 n2 bla replaces n2 chars of current line, starting n1-th
def replace () 
{ 
    os.system('dd if=ed.c of=tmp.1 bs=1 "count=" + sys.argv[1] + ""2> /dev/null')
    
    ( os.system('dd if=ed.c "skip=" + sys.argv[1] + "" bs=1') | os.system('dd of=tmp.2 bs=1 "skip=" + sys.argv[2] + ""') ) 2> /dev/null
    
    os.system('shift')
    
    os.system('shift')
    
    ( os.system('dd if=tmp.1')
    
    os.system('Echo -n "" + $ + "@"')
    
    os.system('dd if=tmp.2') ) > $tmp.3 2> /dev/null
    
    os.system('dd if=tmp.3 of=ed.c2> /dev/null')
}
# rstring n s bla
# replace the n-th occurence of s with bla
def rstring () 
{ 
    n="" + sys.argv[1] + ""
    
    os.system('shift')
    
    # first we have to find it - this is fun!
    
    # we have $tmp.4 => text before string, $tmp.5 => text after
    
    os.system('dd if=/dev/null of=tmp.42> /dev/null')
    
    os.system('dd if=ed.c of=tmp.52> /dev/null')
    
    string="" + sys.argv[1] + ""
    
    os.system('shift')
    
    os.system('dd of=tmp.62> /dev/null ') <<EOF
$@
EOF

    while (os.system(':')):
        
            if ( " os.popen('" + dd + " if=" + tmp + ".5 2>/dev/null').read() " == '$string*'):
                if (os.system('lt n 2') ):
                    # now we want to replace the string
                    
                    os.system('Echo -n "" + $ + "@"> $tmp.2')
                    
                    os.system('Echo -n "" + string + ""> $tmp.1')
                    
                    IFS="+"
                    
                    os.system('set  os.popen('dd bs=1 if=tmp.1 of=/dev/null 2>&1').read() ')
                    
                    IFS="" + saveIFS + ""
                    
                    slen=sys.argv[1]
                    
                    IFS="+"
                    
                    ( os.system('dd if=tmp.4')
                    
                    os.system('dd if=tmp.2')
                    
                    os.system('dd if=tmp.5 bs=1 skip=slen') ) 2> /dev/null > $tmp
                    
                    os.system('dd if=tmp of=ed.c2> /dev/null')
                    
                    os.system('return 0')
                else:
                    os.system('subtract n n 1')
                    
                    ( os.system('dd if=tmp.4')
                    
                    os.system('dd if=tmp.5 bs=1 count=1') ) > $tmp 2> /dev/null
                    
                    os.system('dd if=tmp of=tmp.42> /dev/null')
                    
                    # and remove it from $tmp.5
                    
                    os.system('dd if=tmp.5 of=tmp bs=1 skip=12> /dev/null')
                    
                    os.system('dd if=tmp of=tmp.52> /dev/null')
            elif (" os.popen('" + dd + " if=" + tmp + ".5 2>/dev/null').read() " == '?*'):
                # add one more byte...
                
                ( os.system('dd if=tmp.4')
                
                os.system('dd if=tmp.5 bs=1 count=1') ) > $tmp 2> /dev/null
                
                os.system('dd if=tmp of=tmp.42> /dev/null')
                
                # and remove it from $tmp.5
                
                os.system('dd if=tmp.5 of=tmp bs=1 skip=12> /dev/null')
                
                os.system('dd if=tmp of=tmp.52> /dev/null')
            else:
                # not found
                
                os.system('return 1')
}
# skip to next line
def next () 
{ 
    os.system('add l lineno 1')
    
    ( os.system('dd if=ed.a')
    
    os.system('dd if=ed.c') ) 2> /dev/null > $tmp.3
    
    os.system('dd if=ed.b of=tmp.42> /dev/null')
    
    os.system('open tmp.4')
    
    os.system('dd if=tmp.3 of=ed.a2> /dev/null')
    
    lineno=l
}
# delete current line
def delete () 
{ 
    l=lineno
    
    os.system('dd if=ed.a2> /dev/null > $tmp.1')
    
    os.system('dd if=ed.b of=tmp.22> /dev/null')
    
    os.system('open tmp.2')
    
    os.system('dd if=tmp.1 of=ed.a2> /dev/null')
    
    lineno=l
}
# insert before current line (without changing current)
def insert () 
{ 
    ( os.system('dd if=ed.a')
    
    os.system('Echo "" + $ + "@"') ) 2> /dev/null > $tmp.1
    
    os.system('dd if=tmp.1 of=ed.a2> /dev/null')
    
    os.system('add lineno lineno 1')
}
# previous line
def prev () 
{ 
    
        if ( "" + lineno + "" == '1'):

        else:
            os.system('subtract lineno lineno 1')
            
            # read last line of $ed.a
            
            IFS='+'
            
            os.system('set  os.popen('dd if=ed.a of=/dev/null bs=1 2>&1').read() ')
            
            IFS="" + saveIFS + ""
            
            size=sys.argv[1]
            
            # empty?
            
            
                elif ("" + size + "" == '0'):
                    os.system('return')
            
            os.system('subtract size size 1')
            
            # skip final newline
            
            
                if ( "" + size + "" == '0'):

                else:
                    os.system('subtract size1 size 1')
                    
                    
                        elif (" os.popen('" + dd + " if=" + ed + ".a bs=1 skip=" + size + " count=1 2>/dev/null').read() " == '?*'):

                        else:
                            size=size1
            
            go=true
            
            while (os.system('go')):
                
                    if ( "" + size + "" == '0'):
                        go=false
                    else:
                        
                            elif (" os.popen('" + dd + " if=" + ed + ".a bs=1 skip=" + size + " count=1 2>/dev/null').read() " == '?*'):
                                go=true
                                
                                os.system('subtract size size 1')
                            else:
                                go=false
                                
                                os.system('add size size 1')
            
            # now $size is the size of the first n-1 lines
            
            # add $ed.c to $ed.b
            
            ( os.system('dd if=ed.c')
            
            os.system('dd if=ed.b') ) 2> /dev/null > $tmp.5
            
            os.system('dd if=tmp.5 of=ed.b2> /dev/null')
            
            # move line to ed.c
            
            
                if ( "" + size + "" == '0'):
                    os.system('dd if=ed.a of=ed.c2> /dev/null')
                    
                    os.system('dd if=/dev/null of=tmp.52> /dev/null')
                else:
                    os.system('dd if=ed.a of=ed.c bs=1 skip=size2> /dev/null')
                    
                    os.system('dd if=ed.a of=tmp.5 bs=1 count=size2> /dev/null')
            
            # move rest to ed.a
            
            os.system('dd if=tmp.5 of=ed.a2> /dev/null')
}
# goes to a given line
def goto () 
{ 
    rl="" + sys.argv[1] + ""
    
    os.system('compare bla "" + rl + "" lineno')
    
    
        if ( "" + bla + "" == 'eq'):
            os.system('return')
        elif ("" + bla + "" == 'gt'):
            while (os.system('gt "" + rl + "" lineno')):
                os.system('next')
        elif ("" + bla + "" == 'lt'):
            while (os.system('lt "" + rl + "" lineno')):
                os.system('prev')
}
def lineout () 
{ 
    os.system('Echo -n "" + lineno + ": "')
    
    os.system('dd if=ed.c2> /dev/null')
}
state=closed
name=
autoprint=true
while (True):
    os.system('Echo -n '> '')
    cmd = raw_input()
    
        if ( "" + cmd + ":" + state + "" == 'open:open'):
            os.system('Echo "There is a file open already"')
        elif ("" + cmd + ":" + state + "" == 'open:*'):
            if (os.system('open "" + arg + ""') ):
                state=open
                name="" + arg + ""
                os.system('autoprint')
            else:
                os.system('Echo "Cannot open " + arg + ""')
        elif ("" + cmd + ":" + state + "" == 'new:open'):
            os.system('Echo "There is a file open already"')
        elif ("" + cmd + ":" + state + "" == 'new:*'):
            os.system('open "" + arg + ""')
            state=open
            name="" + arg + ""
            os.system('autoprint')
        elif ("" + cmd + ":" + state + "" == 'close:changed'):
            os.system('Echo "Use 'discard' or 'save'"')
        elif ("" + cmd + ":" + state + "" == 'close:closed'):
            os.system('Echo "Closed already"')
        elif ("" + cmd + ":" + state + "" == 'close:*'):
            state=closed
        elif ("" + cmd + ":" + state + "" == 'save:closed'):
            os.system('Echo "There isn't a file to save"')
        elif ("" + cmd + ":" + state + "" == 'save:*'):
            
                elif ("" + arg + "" == '?*'):
                    os.system('save "" + arg + ""')
                else:
                    os.system('save "" + name + ""')
            state=open
        if ( "" + arg + "" == 'discard:changed'):
            os.system('Echo "Your problem!"')
            state=closed
        elif ("" + arg + "" == 'discard:*'):
            state=closed
        elif ("" + arg + "" == 'print:closed'):
            os.system('Echo "No current file"')
        elif ("" + arg + "" == 'print:*'):
            os.system('lineout')
        elif ("" + arg + "" == 'goto:closed'):
            os.system('Echo "No current file"')
        elif ("" + arg + "" == 'goto:*'):
            os.system('goto "" + arg + ""')
            os.system('autoprint')
        elif ("" + arg + "" == 'next:closed'):
            os.system('Echo "No current file"')
        elif ("" + arg + "" == 'next:*'):
            os.system('next')
            os.system('autoprint')
        elif ("" + arg + "" == 'prev:closed'):
            os.system('Echo "No current file"')
        elif ("" + arg + "" == 'prev:*'):
            os.system('prev')
            os.system('autoprint')
        elif ("" + arg + "" == 'name:closed'):
            os.system('Echo "No current file"')
        elif ("" + arg + "" == 'name:*'):
            name="" + arg + ""
        elif ("" + arg + "" == 'replace:closed'):
            os.system('Echo "No current file"')
        elif ("" + arg + "" == 'replace:*'):
            if (os.system('rstring 1 arg') ):
                state=changed
                os.system('autoprint')
            else:
                os.system('Echo "Not found"')
        elif ("" + arg + "" == 'nreplace:closed'):
            os.system('Echo "No current file"')
        elif ("" + arg + "" == 'nreplace:*'):
            if (os.system('rstring arg') ):
                state=changed
                os.system('autoprint')
            else:
                os.system('Echo "Not found"')
        elif ("" + arg + "" == 'delete:closed'):
            os.system('Echo "No current file"')
        elif ("" + arg + "" == 'delete:*'):
            os.system('delete')
            state=changed
            os.system('autoprint')
        elif ("" + arg + "" == 'insert:closed'):
            os.system('Echo "No current file"')
        elif ("" + arg + "" == 'insert:*'):
            os.system('insert "" + arg + ""')
            os.system('prev')
            state=changed
            os.system('autoprint')
        elif ("" + arg + "" == 'quit:changed'):
            os.system('Echo "Use 'save' or 'discard'"')
        elif ("" + arg + "" == 'quit:*'):
            os.system('Echo "bye"')
            exit()
        elif ("" + arg + "" == 'autoprint:*'):
            autoprint="lineout"
        elif ("" + arg + "" == 'noprint:*'):
            autoprint=""
        elif ("" + arg + "" == ':*'):

        else:
            os.system('Echo "Command not understood"')
