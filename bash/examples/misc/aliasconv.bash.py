import sys, os, os.path
from stat import *
#
# aliasconv.bash - convert csh aliases to bash aliases and functions
#
# usage: aliasconv.bash
#
# Chet Ramey
# chet@po.cwru.edu
#
os.system('trap 'rm -f TMPFILE' 0 1 2 3 6 15')
TMPFILE= os.popen('mktemp -t cb.XXXXXX').read()  || exit(1)
T='	'
os.system('cat > $TMPFILE <<'EOF'
mkalias ()
{
	case $2 in
	'')	echo alias ${1}="''" ;;
	*[
#\!]*)
		comm=$(echo $2 | sed  's/\!\*/"$\@"/g
				      s/\!:\([1-9]\)/"$\1"/g
			              s/
#/\#/g')
		echo $1 \(\) "{" command "$comm"  "; }"
		;;
	*)	echo alias ${1}=\'$(echo "${2}" | sed "s:':'\\\\'':g")\' ;;
	esac
}
EOF
')
# the first thing we want to do is to protect single quotes in the alias,
# since they whole thing is going to be surrounded by single quotes when
# passed to mkalias
os.system('sed -e "s:':\\'\\\'\\':" -e "s/^\([a-zA-Z0-9_-]*\)" + T + "\(.*\)" + $ + "/mkalias \1 '\2'/">> $TMPFILE')
os.system('BASH TMPFILE') | os.system('sed -e 's/\cwd/\PWD/g' -e 's/\term/\TERM/g' -e 's/\home/\HOME/g' -e 's/\user/\USER/g' -e 's/\prompt/\PS1/g'')
exit(0)
