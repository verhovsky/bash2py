import sys, os, os.path
from stat import *
#
# shprof - a line profiler for shell scripts
#
# adapted from a similar program included in `The New KornShell' by
# Bolsky and Korn and posted to usenet by bsh20858@challenger.fhda.edu
#
# converted to bash v2 syntax by Chet Ramey
#
TMPFILE=${TMP:-/tmp}/shprof$$
os.system('trap 'rm -f TMPFILE' EXIT')
def errexit () 
{ 
    print("sys.argv[0]: "" + $ + "@"")1>&2
    
    exit(1)
}
# create script with profiling enabled
os.system('cat> $TMPFILE  <<-'_EOF_'
declare -a _line
_profend()
{
case "$1" in
/*|./*)	file="$1" ;;
*) file=$(type -path "$1") ;;
esac

echo "*** line profile for $file ***"
i=1;
while read -r && [ $i -le $NLINE ]; do
count=${_line[$i]}
if [ "$count" -gt 0 ]; then
echo "[$count] $i: $REPLY"
fi
i=$((i + 1))
done <$file
_EOF_
')
# make the profiling script remove itself after printing line stats
print("rm -f " + TMPFILE + "")>> $TMPFILE
os.system('cat>> $TMPFILE  <<-'_EOF_'
}
_command=$1
shift
i=1
NLINE=$(wc -l < "$_command")
while [ $i -le $NLINE ]; do
_line[$i]=0
i=$((i + 1))
done
unset i
trap "_profend ${_command}" EXIT
trap '_line[$LINENO]=$((${_line[$LINENO]} + 1))' DEBUG
LINENO=0
_EOF_
')

    if ( "" + sys.argv[1] + "" == '/*' or "" + sys.argv[1] + "" == './*'):
        file=sys.argv[1]
    else:
        file=(type -path "" + sys.argv[1] + "")
os.system('cat "" + $ + "{file-" + sys.argv[1] + "}">> $TMPFILE') || os.system('errexit "" + $ + "{1}: cannot open"')
os.system('chmod +x TMPFILE')
os.system('exec -a "" + file + "" TMPFILE "" + $ + "@"')
