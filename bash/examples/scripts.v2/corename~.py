import sys, os, os.path
from stat import *
#
# original from:
# @(#) corename.ksh 1.0 93/04/01
# 92/11/11 john h. dubois iii (john@armory.com)
# 92/02/16 Added help option.
# 92/02/22 Added cd to origdir to fix prob w/multiple relative paths.
# 93/04/01 Added check for whether file exists.
#
# conversion to bash v2 syntax done by Chet Ramey
# inspired by belal's equivalent utility
if ("" + sys.argv[1] + "" == -h  ):
    print("" + sys.argv[0] + ": print the names of executables that dumped core.
)
    exit(0)
$# == 0  && os.system('set core')
origdir=PWD
for i in ["" + $ + "@"]:
    os.chdir($origdir)
    file=${i##*/}
    dir=${i%file}
    -z "" + dir + ""  && dir=origdir/
    if (! -f dirfile  ):
        print("" + dir + "" + file + ": No such file.")
        continue
    if (! -r dirfile  ):
        print("" + dir + "" + file + ": Cannot open.")
        continue
    os.chdir($dir)
    # the adb output syntax is highly variable.  this works on SunOS 4.x
    os.system('set --  os.popen('adb file < /dev/null 2>&1 | sed 1q').read() ')
    name=${7#??}
    print("" + i + ": " + $ + "{name%??}")
