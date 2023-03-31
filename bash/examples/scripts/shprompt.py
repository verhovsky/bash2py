import sys, os, os.path
from stat import *
#
# shprompt -- give a prompt and get an answer satisfying certain criteria
#
# shprompt [-dDfFsy] prompt
#	s = prompt for string
#	f = prompt for filename
#	F = prompt for full pathname to a file or directory
#	d = prompt for a directory name
#	D = prompt for a full pathname to a directory
#	y = prompt for y or n answer
#
# Chet Ramey
# chet@ins.CWRU.Edu
type=file
OPTS=dDfFsy
def succeed () 
{ 
    print("" + sys.argv[1] + "")
    
    exit(0)
}
while (os.system('getopts "" + OPTS + "" c')):
    
        if ( "" + c + "" == 's'):
            type=string
        elif ("" + c + "" == 'f'):
            type=file
        elif ("" + c + "" == 'F'):
            type=path
        elif ("" + c + "" == 'd'):
            type=dir
        elif ("" + c + "" == 'D'):
            type=dirpath
        elif ("" + c + "" == 'y'):
            type=yesno
        elif ("" + c + "" == '?'):
            print("usage: " + sys.argv[0] + " [-" + OPTS + "] prompt")1>&2
            exit(2)
if ("" + OPTIND + "" > 1  ):
    os.system('shift OPTIND - 1')
while (os.system(':')):
    
        if ( "" + type + "" == 'string'):
            print("" + sys.argv[1] + "")1>&2
            ans = raw_input() || exit(1)
            if (-n "" + ans + ""  ):
                os.system('succeed "" + ans + ""')
        elif ("" + type + "" == 'file' or "" + type + "" == 'path'):
            print("" + sys.argv[1] + "")1>&2
            ans = raw_input() || exit(1)
            #
            # use `fn' and eval so that bash will do tilde expansion for
            # me
            #
            os.system('eval fn="" + ans + ""')
            
                elif ("" + fn + "" == '/*'):
                    if (os.system('test -e "" + fn + ""') ):
                        os.system('succeed "" + fn + ""')
                    else:
                        print("" + sys.argv[0] + ": '" + fn + "' does not exist")1>&2
                else:
                    if ("" + type + "" == "path"  ):
                        print("" + sys.argv[0] + ": must give full pathname to file")1>&2
                    else:
                        if (os.system('test -e "" + fn + ""') ):
                            os.system('succeed "" + fn + ""')
                        else:
                            print("" + sys.argv[0] + ": '" + fn + "' does not exist")1>&2
        if ( "" + fn + "" == 'dir' or "" + fn + "" == 'dirpath'):
            print("" + sys.argv[1] + "")1>&2
            ans = raw_input() || exit(1)
            #
            # use `fn' and eval so that bash will do tilde expansion for
            # me
            #
            os.system('eval fn="" + ans + ""')
            
                elif ("" + fn + "" == '/*'):
                    if (os.system('test -d "" + fn + ""') ):
                        os.system('succeed "" + fn + ""')
                    else:
                        if (os.system('test -e "" + fn + ""') ):
                            print("" + sys.argv[0] + " '" + fn + "' is not a directory")1>&2
                        else:
                            print("" + sys.argv[0] + ": '" + fn + "' does not exist")1>&2
                else:
                    if ("" + type + "" == "dirpath"  ):
                        print("" + sys.argv[0] + ": must give full pathname to directory")1>&2
                    else:
                        if (os.system('test -d "" + fn + ""') ):
                            os.system('succeed "" + fn + ""')
                        else:
                            if (os.system('test -e "" + fn + ""') ):
                                print("" + sys.argv[0] + " '" + fn + "' is not a directory")1>&2
                            else:
                                print("" + sys.argv[0] + ": '" + fn + "' does not exist")1>&2
        if ( "" + fn + "" == 'yesno'):
            print("" + sys.argv[1] + "")1>&2
            ans = raw_input() || exit(1)
            
                elif ("" + ans + "" == 'y' or "" + ans + "" == 'Y' or "" + ans + "" == '[yY][eE][sS]'):
                    os.system('succeed "yes"')
                elif ("" + ans + "" == 'n' or "" + ans + "" == 'N' or "" + ans + "" == '[nN][oO]'):
                    os.system('succeed "no"')
                    exit(0)
                else:
                    print("" + sys.argv[0] + ": yes or no required")1>&2
exit(1)
