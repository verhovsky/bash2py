import sys, os, os.path
from stat import *
#
# original from:
# arc2tarz: convert arced file to tarred, compressed form.
# @(#) arc2tarz.ksh 1.0 92/02/16
# 91/03/28 john h. dubois iii (john@armory.com)
# 92/02/16 added -h option for help
#
# conversion to bash v2 syntax by Chet Ramey
os.system('unset ENV')
Usage="Usage: " + sys.argv[0] + " arcfile [-hcg] [ tarzfile ]"
def phelp () 
{ 
    print("" + Usage + "
)
}
compress=gzip
ext=gz
while (os.system('getopts "hcg" opt')):
    
        if ( "" + opt + "" == 'h'):
            os.system('phelp')
            exit(0)
        elif ("" + opt + "" == 'c'):
            compress=compress
            ext=Z
        elif ("" + opt + "" == 'g'):
            compress=gzip
            ext=gz
        else:
            print("" + Usage + "")1>&2
            exit(2)
os.system('shift (OPTIND - 1)')
if ($# == 0  ):
    os.system('phelp')
    exit(0)
-z "" + TMP + ""  && tmpdir=/tmp/arc2tarz.$$ || tmpdir=TMP/arc2tarz.$$

    if ( "" + sys.argv[1] + "" == '*.arc'):
        arcfile=sys.argv[1]
    else:
        arcfile=sys.argv[1].arc
if (! -f arcfile  || ! -r arcfile  ):
    print("Could not open arc file \"arcfile\".")
    exit(1)

    if ( "" + arcfile + "" == '/*'):

    else:
        arcfile=PWD/arcfile
basename=${arcfile%.arc}
basename=${basename##*/}
$# < 2  && tarzname=PWD/basename.tar.ext || tarzname=sys.argv[2]
os.system('trap 'rm -rf tmpdir tarzname' 1 2 3 6 15')
os.system('mkdir tmpdir')
os.chdir($tmpdir)
print("unarcing files...")
os.system('arc -ie arcfile')
# lowercase
for f in [*]:
    new= os.popen('echo f | tr A-Z a-z').read() 
    if ("" + f + "" != "" + new + ""  ):
        os.system('mv f new')
print("tarring/compressing files...")
os.system('tar cf - *') | os.system('compress> $tarzname')
os.chdir(-)
os.system('rm -rf tmpdir')
