import sys, os, os.path
from stat import *
print( os.popen('date').read() )
print( os.popen('ls -la').read() )
