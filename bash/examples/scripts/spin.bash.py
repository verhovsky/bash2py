import sys, os, os.path
from stat import *
#
# spin.bash -- provide a `spinning wheel' to show progress
#
# Chet Ramey
# chet@po.cwru.edu
#
bs=''
chars="|" + $ + "{bs} \\" + $ + "{bs} -" + $ + "{bs} /" + $ + "{bs}"
# Infinite loop for demo. purposes
while (os.system(':')):
    for letter in [chars]:
            print("${letter}")
exit(0)
