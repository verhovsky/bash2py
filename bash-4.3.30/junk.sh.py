#! /usr/bin/env python
import os
class Bash2Py(object):
  __slots__ = ["val"]
  def __init__(self, value=''):
    self.val = value

FILE=Bash2Py("/some/file")
OPTION=Bash2Py(0)
#The statement below gets interpreted incorrectly. The '!' character never gets translated to 'not' and the '-x' is overlooked entirely, with the varaible being tested printed out twice.
#believe the desired output would be:
#if not(os.access(str(FILE.val),X_OK) )
if (not os.access(str(FILE.val),X_OK) ):
    print("File is not executable")
#The statement below also gets interpreted incorrectly. 
#believe the desired output would be:
#if (OPTION.val != "1")
if (str(OPTION.val) != "1" ):
    print("Option is disabled")
