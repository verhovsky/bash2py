#! /usr/bin/env python
import os
from stat import *
print(os.popen("date").read())
print( os.popen('ls -la').read() )
