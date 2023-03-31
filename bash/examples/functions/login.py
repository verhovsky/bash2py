import sys, os, os.path
from stat import *
# replace the `login' and `newgrp' builtins in old bourne shells
def login () 
{ 
    os.system('exec login "" + $ + "@"')
}
def newgrp () 
{ 
    os.system('exec newgrp "" + $ + "@"')
}
