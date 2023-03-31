import sys, os, os.path
from stat import *
#
# cshtobash - convert csh aliases, environment variables, and variables to
#	      bash equivalents
#
# usage: cshtobash [filename]
#
# If filename is given, that file is sourced.  Note that csh always
# sources .cshrc.  To recreate your csh login environment, run
# `cshtobash ~/.login'.
#
# Inspired by (and some borrowed from) a similar program distributed with
# zsh-3.0.
#
# Chet Ramey
# chet@po.cwru.edu
#
os.system('trap 'rm -f TMPFILE1 TMPFILEa TMPFILEe TMPFILEv TMPFILEco TMPFILEci' 0 1 2 3 6 15')
{ TMPFILE1= os.popen('mktemp -t cb.1.XXXXXX').read()  && TMPFILEa= os.popen('mktemp -t cb.a.XXXXXX').read()  && TMPFILEe= os.popen('mktemp -t cb.e.XXXXXX').read()  && TMPFILEv= os.popen('mktemp -t cb.v.XXXXXX').read()  && TMPFILEco= os.popen('mktemp -t cshout.XXXXXX').read()  && TMPFILEci= os.popen('mktemp -t cshin.XXXXXX').read()  } || exit(1)
T='	'
SOURCE="" + $ + "{1:+source " + sys.argv[1] + "}"
os.system('cat > $TMPFILEci <<EOF
$SOURCE
alias >! $TMPFILEa
setenv >! $TMPFILEe
set >! $TMPFILEv
EOF
')
# give csh a minimal environment, similar to what login would provide
os.system('/usr/bin/env - USER=USER HOME=HOME PATH=/usr/bin:/bin:/usr/ucb:. TERM=TERM SHELL=SHELL /bin/csh -i< $TMPFILEci > $TMPFILEco 2>&1')
# First convert aliases
os.system('cat > $TMPFILE1 <<'EOF'
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
	*)	echo alias ${1}=\'$(echo "${2}" | sed "s:':'\\\\'':")\' ;;
	esac
}
EOF
')
os.system('sed "s/^\([a-zA-Z0-9_]*\)" + T + "\(.*\)" + $ + "/mkalias \1 '\2'/"< $TMPFILEa >> $TMPFILE1')
print("'# csh aliases'")

os.system('BASH TMPFILE1') | os.system('sed -e 's/\cwd/\PWD/g' -e 's/\term/\TERM/g' -e 's/\home/\HOME/g' -e 's/\user/\USER/g' -e 's/\prompt/\PS1/g'')
# Next, convert environment variables

print("'# csh environment variables'")

# Would be nice to deal with embedded newlines, e.g. in TERMCAP, but ...
os.system('sed -e '/^SHLVL/d' -e '/^PWD/d' -e "s/'/'"\\\\"''"/g -e "s/^\([A-Za-z0-9_]*=\)/export \1'/" -e "s/" + $ + "/'/"< $TMPFILEe')
# Finally, convert local variables

print("'# csh variables'")

os.system('sed -e 's/'"" + T + ""'/=/' -e "s/'/'"\\\\"''"/g -e '/^[A-Za-z0-9_]*=[^(]/{
< $TMPFILEv') | os.system('sed -e '/^argv=/d' -e '/^cwd=/d' -e '/^filec=/d' -e '/^status=/d' -e '/^verbose=/d' -e '/^term=/d' -e '/^home=/d' -e '/^path=/d' -e '/^user=/d' -e '/^shell=/d' -e '/^cdpath=/d' -e '/^mail=/d' -e '/^home=/s//HOME=/' -e '/^prompt=/s//PS1=/' -e '/^histfile=/s//HISTFILE=/' -e '/^history=/s//HISTSIZE=/' -e '/^savehist=$/s//HISTFILESIZE=${HISTSIZE-500}/' -e '/^savehist=/s//HISTFILESIZE=/' -e '/^ignoreeof=$/s/^.*$/set -o ignoreeof # ignoreeof/' -e '/^ignoreeof=/s//IGNOREEOF=/' -e '/^noclobber=/s/^.*$/set -C # noclobber/' -e '/^notify=/s/^.*$/set -b # notify/' -e '/^noglob=/s/^.*$/set -f # noglob/'')
# now some special csh variables converted to bash equivalents

print("'# special csh variables converted to bash equivalents'")

os.system('sed -e 's/'"" + T + ""'/=/'< $TMPFILEv') | os.system('grep "^cdpath="') | os.system('sed 's/(//
')
os.system('sed -e 's/'"" + T + ""'/=/'< $TMPFILEv') | os.system('grep "^mail="') | os.system('sed 's/(//
') | os.system('sed -e 's/MAILPATH=\([0-9][0-9][^:]*\)$/MAILCHECK=\1/' -e 's/MAILPATH=\([0-9][0-9][^:]*\):\(.*\)/MAILCHECK=\1 MAILPATH=\2/'')
exit(0)
