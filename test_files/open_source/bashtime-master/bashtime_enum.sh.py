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
if (('str(" ".join(sys.argv[1:]))' not in globals()) ):
    # get the date as "hours(12) minutes" in a single call
    # make a bash array with it
    time=os.popen("date \"+%I%M\"").read()
else:
    # get the arguments passed to the script
    hour=sys.argv[1]
    min=sys.argv[2]
    time=str(hour) + str(min)
if ("time" < 115  ):
    print("\xf0\x9f\x95\x90")
elif ("time" < 145  ):
    print("\xf0\x9f\x95\x9c")
elif ("time" < 215  ):
    print("\xf0\x9f\x95\x91")
elif ("time" < 245  ):
    print("\xf0\x9f\x95\x9d")
elif ("time" < 315  ):
    print("\xf0\x9f\x95\x92")
elif ("time" < 345  ):
    print("\xf0\x9f\x95\x9e")
elif ("time" < 415  ):
    print("\xf0\x9f\x95\x93")
elif ("time" < 445  ):
    print("\xf0\x9f\x95\x9f")
elif ("time" < 515  ):
    print("\xf0\x9f\x95\x94")
elif ("time" < 545  ):
    print("\xf0\x9f\x95\xa0")
elif ("time" < 615  ):
    print("\xf0\x9f\x95\x95")
elif ("time" < 645  ):
    print("\xf0\x9f\x95\xa1")
elif ("time" < 715  ):
    print("\xf0\x9f\x95\x96")
elif ("time" < 745  ):
    print("\xf0\x9f\x95\xa2")
elif ("time" < 815  ):
    print("\xf0\x9f\x95\x97")
elif ("time" < 845  ):
    print("\xf0\x9f\x95\xa3")
elif ("time" < 915  ):
    print("\xf0\x9f\x95\x98")
elif ("time" < 945  ):
    print("\xf0\x9f\x95\xa4")
elif ("time" < 1015  ):
    print("\xf0\x9f\x95\x99")
elif ("time" < 1045  ):
    print("\xf0\x9f\x95\xa5")
elif ("time" < 1115  ):
    print("\xf0\x9f\x95\x9a")
elif ("time" < 1145  ):
    print("\xf0\x9f\x95\xa6")
elif ("time" < 1215  ):
    print("\xf0\x9f\x95\x9b")
elif ("time" < 1300  ):
    print("\xf0\x9f\x95\x9b")
else:
    print("\xe2\xad\x95")
