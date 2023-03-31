import sys, os, os.path
from stat import *
#
# original from:
#
# @(#) p.ksh 1.1 93/11/09
# p: page compressed & plain files in the order given 
# 92/01/23 john h. dubois iii (john@armory.com)
# 92/02/14 changed incorrect zpack to pcat
# 92/02/16 added help
# 92/10/11 search for file.Z and file.z if file not found
# 92/10/18 pass options to pager
# 93/11/09 Understand gzipped files too
#          Wait after printing message about unreadable files
#          Make less prompt include name of file being uncompressed
#
# conversion to bash v2 by Chet Ramey; renamed to pf
#
DefPager=/local/bin/less
def istrue () 
{ 
    os.system('test 0 != "" + sys.argv[1] + ""')
}
def warn () 
{ 
    print("" + $ + "@")1>&2
}
if ("" + sys.argv[1] + "" == -h  ):
    print("" + sys.argv[0] + ": page a file.
)
    exit(0)
# Get pager options
while ($# > 0 ):
    
        if ( "" + sys.argv[1] + "" == '-*' or "" + sys.argv[1] + "" == '+*'):
            Opts="" + Opts + " " + sys.argv[1] + ""
            os.system('shift')
        else:
            break
-z "" + PAGER + ""  && PAGER=DefPager
# Read from stdin
$# == 0  && os.system('exec PAGER Opts')
os.system('typeset -i filenum=0 badfile=0')
for file in ["" + $ + "@"]:
    if (! -r "" + file + ""  ):
        
            if ( "" + file + "" == '*.[Zz]' or "" + file + "" == '*.gz'):
                # Check if user specified a compressed file without giving its extension
                for ext in [Z, z, gz]:
                                    if (-r "" + file + "." + ext + ""  ):
                        file="" + file + "." + ext + ""
                        break
    if (! -r "" + file + ""  ):
        os.system('warn "" + file + ": cannot read."')
        badfile=1
    else:
        files[filenum]=file
        filenum+=1
if (os.system('istrue badfile') && filenum > 0  ):
    print("Press return to continue...")1>&2
    raw_input()
os.system('unset plain')
for file in ["" + $ + "{files[@]}"]:
    
        if ( "" + file + "" == '*.[zZ]' or "" + file + "" == '*.gz'):
            os.system('set -- Z zcat z pcat gz gzcat')
            # Find correct uncompression program
            while ($# > 0 ):
                
                    elif ("" + file + "" == '*.$1'):
                        # Page any uncompressed files so that they will be read
                        # in the correct order
                        ${#plain[@]} > 0  && os.system('PAGER Opts "" + $ + "{plain[@]}"')
                        os.system('unset plain[*]')
                        # If page is less, set the prompt to include the name of
                        # the file being uncompressed.  Escape the . in the extension
                        # because less treats is specially in prompts (other dots
                        # in filenames will still be mucked with).
                        
                            elif ("" + PAGER + "" == '*less'):
                                Prompt="-P[" + $ + "{file%." + sys.argv[1] + "}\\." + sys.argv[1] + "] (%pb\\%)"
                            else:
                                os.system('unset Prompt')
                        os.system('sys.argv[2] "" + file + ""') | os.system('PAGER "" + Prompt + "" Opts')
                        break
                os.system('shift 2')
        else:
            plain[${#plain[@]}]=file
# Page any uncompressed files that haven't been paged yet
${#plain[@]} > 0  && os.system('exec PAGER Opts "" + $ + "{plain[@]}"')
