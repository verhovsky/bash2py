import sys, os, os.path
from stat import *
#
# zprintf - function that calls gawk to do printf for those systems that
#	    don't have a printf executable
#
# The format and arguments can have trailing commas, just like gawk
#
# example:
#	zprintf 'Eat %x %x and suck %x!\n' 57005 48879 64206
#
# Chet Ramey
# chet@po.cwru.edu
$# < 1  && { print("zprintf: usage: zprintf format [args ...]")1>&2
exit(2) }
fmt="" + $ + "{1%,}"
os.system('shift')
for a in ["" + $ + "@"]:
    args="" + args + ",\"${a%,}\""
os.system('gawk "BEGIN { printf \"fmt\" " + args + " }"')
