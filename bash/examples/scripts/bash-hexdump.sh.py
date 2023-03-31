import sys, os, os.path
from stat import *
#From: "dennis" <dennis@netstrata.com>
#To: <bash-maintainers@gnu.org>
#Subject: New example script: bash-hexdump
#Date: Mon, 4 Jan 2010 22:48:19 -0700
#Message-ID: <6dbec42d$64fcdbd2$4a32cf2d$@com>
#I've written a script that functions like "hexdump -C" or "hd". If you'd 
#like to include it in a future distribution of example Bash scripts, I have 
#included it here: 
# bash-hexdump# pure Bash, no externals
# by Dennis Williamson - 2010-01-04
# in response to 
os.system('http://stackoverflow.com/questions/2003803/show-hexadecimal-numbers-of-a-file')
# usage: bash-hexdump file
saveIFS="" + IFS + ""
IFS=""
# disables interpretation of \t, \n and space
saveLANG="" + LANG + ""
LANG=C
# allows characters > 0x7F
bytecount=0
valcount=0
print( "%08x  " % (bytecount) )

while (-d = raw_input()
# -d '' allows newlines, -r allows \):
    ((bytecount++))
    # for information about the apostrophe in this printf command, see
    #  http://www.opengroup.org/onlinepubs/009695399/utilities/printf.html
    print( -v % (val, "%02x", "'" + char + "") )

    print("" + val + " ")
    ((valcount++))
    if ("$val" < 20 or "$val" > 7e ):
        string+="."
        # show unprintable characters as a dot
    else:
        string+=char
    if (((bytecount % 8 == 0))
    # add a space down the middle ):
        print(" ")
    if (((bytecount % 16 == 0))
    # print 16 values per line ):
        print("|" + string + "|")
        string=''
        valcount=0
        print( "%08x  " % (bytecount) )
 < "$1"
if ("$string" != ""
# if the last line wasn't full, pad it out ):
    length=${#string}
    if (((length > 7)) ):
        ((length--))
    ((length += (16 - valcount) * 3 + 4))
    print( "%${length}s\n" % ("|" + string + "|") )

    print( "%08x  " % (bytecount) )


LANG="" + saveLANG + ""
IFS="" + saveIFS + ""
exit(0)
