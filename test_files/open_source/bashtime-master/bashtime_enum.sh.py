#! /usr/bin/env python
import sys,os
from stat import *
# This is bashtime.sh
# Copyright (c) 2013 Paul Scott-Murphy
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# if no args
if (('" ".join(sys.argv[1:])' not in globals()) ):
    # get the date as "hours(12) minutes" in a single call
    # make a bash array with it
    time=os.popen("date \\\"+%I%M\\\"").read()
else:
    # get the arguments passed to the script
    hour=str(sys.argv[1])
    min=str(sys.argv[2])
    time=str(hour)+""+str(min)
if (time < 115  ):
    print(r'🕐')
elif (time < 145  ):
    print(r'🕜')
elif (time < 215  ):
    print(r'🕑')
elif (time < 245  ):
    print(r'🕝')
elif (time < 315  ):
    print(r'🕒')
elif (time < 345  ):
    print(r'🕞')
elif (time < 415  ):
    print(r'🕓')
elif (time < 445  ):
    print(r'🕟')
elif (time < 515  ):
    print(r'🕔')
elif (time < 545  ):
    print(r'🕠')
elif (time < 615  ):
    print(r'🕕')
elif (time < 645  ):
    print(r'🕡')
elif (time < 715  ):
    print(r'🕖')
elif (time < 745  ):
    print(r'🕢')
elif (time < 815  ):
    print(r'🕗')
elif (time < 845  ):
    print(r'🕣')
elif (time < 915  ):
    print(r'🕘')
elif (time < 945  ):
    print(r'🕤')
elif (time < 1015  ):
    print(r'🕙')
elif (time < 1045  ):
    print(r'🕥')
elif (time < 1115  ):
    print(r'🕚')
elif (time < 1145  ):
    print(r'🕦')
elif (time < 1215  ):
    print(r'🕛')
elif (time < 1300  ):
    print(r'🕛')
else:
    print(r'⭕')
