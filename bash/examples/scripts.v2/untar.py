import sys, os, os.path
from stat import *
#
# original from:
# @(#) untar.ksh 1.0 93/11/10
# 92/10/08 john h. dubois iii (john@armory.com)
# 92/10/31 make it actually work if archive isn't in current dir!
# 93/11/10 Added pack and gzip archive support
#
# conversion to bash v2 syntax done by Chet Ramey
def phelp () 
{ 
    print("" + name + ": extract tar archives into directories, uncompressing if neccessary.
)
}
if ($# == 0  ):
    os.system('phelp')
    exit(1)
name=${0##/}
OWD=PWD
for file in ["" + $ + "@"]:
    os.chdir($OWD)
    
        if ( "" + file + "" == '*.tar.Z'):
            ArchiveName=${file%%.tar.Z} zcat=zcat
        elif ("" + file + "" == '*.tar.z'):
            ArchiveName=${file%%.tar.z} zcat=pcat
        elif ("" + file + "" == '*.tar.gz'):
            ArchiveName=${file%%.tar.gz} zcat=gzcat
        else:
            ArchiveName=file
            for ext in ["", .Z, .z, .gz]:
                            if (os.path.isfile("" + file + ".tar" + ext + "" ) ):
                    file="" + file + ".tar" + ext + ""
                    break
            if (! -f "" + file + ""  ):
                print("" + file + ": cannot find archive.")1>&2
                continue
    if (! -r "" + file + ""  ):
        print("" + file + ": cannot read.")1>&2
        continue
    DirName=${ArchiveName##*/}
    S_ISDIR(os.stat("" + DirName + "" ).st_mode) || { os.system('mkdir "" + DirName + ""') || { print("" + DirName + ": could not make archive directory.")1>&2
    continue } }
    os.chdir($DirName) || { print("" + name + ": cannot cd to " + DirName + "")1>&2
    continue }
    
        if ( "" + file + "" == '/*'):

        else:
            file=OWD/file
    print("Extracting archive " + file + " into directory " + DirName + "...")
    
        if ( "" + file + "" == '*.tar.Z' or "" + file + "" == '*.tar.z' or "" + file + "" == '*.tar.gz'):
            os.system('zcat file') | os.system('tar xvf -')
        elif ("" + file + "" == '*.tar'):
            os.system('tar xvf file')
    print("Done extracting archive " + file + " into directory " + DirName + ".")
