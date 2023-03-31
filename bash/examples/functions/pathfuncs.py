import sys, os, os.path
from stat import *
#From: "Simon J. Gerraty" <sjg@zen.void.oz.au>
#Message-Id: <199510091130.VAA01188@zen.void.oz.au>
#Subject: Re: a shell idea?
#Date: Mon, 09 Oct 1995 21:30:20 +1000
# NAME:
#	add_path.sh - add dir to path
#
# DESCRIPTION:
#	These functions originated in /etc/profile and ksh.kshrc, but
#	are more useful in a separate file.
#
# SEE ALSO:
#	/etc/profile
#
# AUTHOR:
#	Simon J. Gerraty <sjg@zen.void.oz.au>
#	@(#)Copyright (c) 1991 Simon J. Gerraty
#
#	This file is provided in the hope that it will
#	be of use.  There is absolutely NO WARRANTY.
#	Permission to copy, redistribute or otherwise
#	use this file is hereby granted provided that
#	the above copyright notice and this notice are
#	left intact.
# is $1 missing from $2 (or PATH) ?
def no_path () 
{ 
    os.system('eval "case :\" + $ + "" + $ + "{2-PATH}: in *:" + sys.argv[1] + ":*) return 1;; *) return 0;; esac"')
}
# if $1 exists and is not in path, append it
def add_path () 
{ 
    S_ISDIR(os.stat(${1:-.} ).st_mode) && os.system('no_path $*') && os.system('eval ${2:-PATH}="\" + $ + "" + $ + "{2:-PATH}:" + sys.argv[1] + ""')
}
# if $1 exists and is not in path, prepend it
def pre_path () 
{ 
    S_ISDIR(os.stat(${1:-.} ).st_mode) && os.system('no_path $*') && os.system('eval ${2:-PATH}="" + sys.argv[1] + ":\" + $ + "" + $ + "{2:-PATH}"')
}
# if $1 is in path, remove it
def del_path () 
{ 
    os.system('no_path $*') || os.system('eval ${2:-PATH}=`eval echo :'$'${2:-PATH}: |
')
}
