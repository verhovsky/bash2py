#! /usr/bin/env python
import sys,os
from stat import *
# if no args
if (('" ".join(sys.argv[1:])' not in globals()) ):
    # get the date as "hours(12) minutes" in a single call
    # make a bash array with it
    d=(os.popen("date \\\"+%I %M\\\"").read()+)
    # separate hours and minutes
    hour=str(d[0]#0)
    # remove leading 0 or values <10 will be interpreted as octal
    min=str(d[1]#0)
else:
    # get the arguments passed to the script
    hour=str(sys.argv[1])
    min=str(sys.argv[2])
plain=(🕐 🕑 🕒 🕓 🕔 🕕 🕖 🕗 🕘 🕙 🕚 🕛)
half=(🕜 🕝 🕞 🕟 🕠 🕡 🕢 🕣 🕤 🕥 🕦 🕧)
# array index starts at 0
hi=(hour-1)
if (min < 15 ):
    print(str(plain[$hi]))
elif (min < 45 ):
    print(str(half[$hi]))
else:
    print(str(plain[$((hi+1))]))
