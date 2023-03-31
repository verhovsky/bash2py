import sys, os, os.path
from stat import *
#
# original from
# @(#) lowercase.ksh 1.0 92/10/08
# 92/10/08 john h. dubois iii (john@armory.com)
#
# conversion to bash v2 syntax done by Chet Ramey
def lowercase () 
{ 
    for file in ["" + $ + "@"]:
            os.path.isfile("" + file + "" ) || continue
        
        filename=${file##*/}
        
        
            if ( "" + file + "" == '*/*'):
                dirname=${file%/*}
            else:
                dirname=.
        
        nf= os.popen('echo filename | tr A-Z a-z').read() 
        
        newname="" + $ + "{dirname}/" + $ + "{nf}"
        
        if ("" + nf + "" != "" + filename + ""  ):
            os.system('mv "" + file + "" "" + newname + ""')
            
            print("lowercase: " + file + " -> " + newname + "")
        else:
            print("lowercase: " + file + " not changed.")
}
