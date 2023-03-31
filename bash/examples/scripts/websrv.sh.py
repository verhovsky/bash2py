import sys, os, os.path
from stat import *
#for instructions or updates go to:
#<A HREF="http://math.ucr.edu:8889/">This script's home page</A>
#email me questions or comments at:
#<A HREF="mailto:insom@math.ucr.edu">insom@math.ucr.edu</A>
#copyright chris ulrich; This software may be used or modified
#in any way so long as this notice remains intact.
#
# WWW server in sh
# Author: Chris Ulrich <chris@tinker.ucr.edu>
#
INDEX=index.html
date= os.popen('date').read() 
DOCHOME=/home/insom/web-docs
BINHOME=/home/insom/web-bin
LOGHOME=/home/insom/web-logs
LOGFILE=LOGHOME/access_log
#verbose=:
verbose=echo
os.system('exec2>> $LOGHOME/error_log')
def hheader () 
{ 
    print("HTTP/1.0 200 OK
)
}
def header () 
{ 
    print("Content-type: " + sys.argv[1] + "
)
}
def no_url () 
{ 
    os.system('header "text/plain"')
    
    print("No such url " + sys.argv[1] + "")
}
def send () 
{ 
    #case "$#" in 2) ;; *) echo eep! | mailx insom@math.ucr.edu  ; exit 3 ;; esac
    
    if (os.system('test -f "" + DOCHOME + "/" + sys.argv[2] + ""') ):
        os.system('header "" + sys.argv[1] + ""')
        
        os.system('cat "" + DOCHOME + "/" + sys.argv[2] + ""')
    else:
        os.system('no_url "" + sys.argv[2] + ""')
}
def LsToHTML () 
{ 
    if (os.system('test -f "" + DOCHOME + "/" + url + "/.title"') ):
        os.system('header "text/html; charset=US-ASCII"')
        
        print("<pre>")
        
        os.system('cat "" + DOCHOME + "/" + url + "/.title"')
        
        print("</pre>")
    else:
        if (os.system('test -f "" + DOCHOME + "/" + url + "/.title.html"') ):
            os.system('header "text/html; charset=US-ASCII"')
            
            os.system('cat "" + DOCHOME + "/" + url + "/.title.html"')
        else:
            os.system('header "text/html; charset=US-ASCII"')
    
    
        if ( "" + url + "" == '/'):

        else:
            url="" + url + "/"
    
    while (link = raw_input()):
        
            if ( link == '*.cgi'):

            else:
                print("<A HREF=\"urllink\">" + link + "</A> <BR>")
}
method = raw_input()
os.system('verbose "
>> $LOGFILE')
for hopeurl in [data]:
    url="" + $ + "{url}" + $ + "{url:+ }" + second + ""
    second="" + hopeurl + ""

    if ( "" + second + "" == '*[1-9].*'):
        inheader = raw_input()
        while (
            elif ("" + inheader + "" == '?' or "" + inheader + "" == ''''):
                False
            else:
                inheader = raw_input()):
            os.system(':')
        os.system('hheader')

    if ( "" + url + "" == '*..*'):
        os.system('no_url "" + url + ""')
        exit(1)
    elif ("" + url + "" == '*.txt' or "" + url + "" == '*.[ch]'):
        os.system('send "text/plain; charset=US-ASCII" "" + url + ""')
    elif ("" + url + "" == '*.html'):
        os.system('send "text/html; charset=US-ASCII" "" + url + ""')
    elif ("" + url + "" == '*.cgi'):
        if (os.system('test -x "" + DOCHOME + "/" + url + ""') ):
            message = raw_input()
            print("" + message + "") | os.system('"" + DOCHOME + "/" + url + ""')
        else:
            os.system('no_url "" + url + ""')
    elif ("" + url + "" == '*".cgi?"*'):
        oIFS="" + IFS + ""
        print("" + url + "") | { IFS='?' read url QUERY_STRING
        if (os.system('test -x "" + DOCHOME + "/" + url + ""') ):
            IFS="" + oIFS + ""
            os.environ[''] = FILE_TO_TRANSLATE
            os.system('"" + DOCHOME + "/" + url + ""')
        else:
            os.system('no_url "" + url + ""') }
    elif ("" + url + "" == '*.[Gg][Ii][Ff]'):
        os.system('send "image/gif" "" + url + ""')
    elif ("" + url + "" == '*.[Jj][Pp][Gg]' or "" + url + "" == '*.[Jj][Pp][Ee][Gg]'):
        os.system('send "image/jpeg" "" + url + ""')
    elif ("" + url + "" == '*.tbl'):
        os.system('header "text/html; charset=US-ASCII"')
        print("<pre>")
        os.system('test -f "" + DOCHOME + "/" + url + ""') && os.system('tbl< "$DOCHOME/$url"') | os.system('nroff') || os.system('no_url "" + url + ""')
        print("</pre>")
    elif ("" + url + "" == '*.nroff'):
        os.system('header "text/html; charset=US-ASCII"')
        print("<pre>")
        os.system('test -f "" + DOCHOME + "/" + url + ""') && os.system('nroff< "$DOCHOME/$url"') || os.system('no_url "" + url + ""')
        print("</pre>")
    elif ("" + url + "" == '*mp[23]'):
        if (os.system('test -f "" + DOCHOME + "/" + url + ""') ):
            os.system('header "application/mpstream"')
            print("+" + TCPLOCALIP + ":" + $ + "{MPSERVPORT:=9001}/" + url + "")
        else:
            os.system('no_url "" + url + ""')
    elif ("" + url + "" == '*.[0-9]' or "" + url + "" == '*.[0-9][a-z]'):
        os.system('header "text/html; charset=US-ASCII"')
        print("<pre>")
        if (os.system('test -f "" + DOCHOME + "/" + url + ""') ):
            #nroff -man  "$DOCHOME/$url" | $BINHOME/man2html
            print("perl at the moment is broken, so man2html doesn't work.  Sorry.")
            print("</pre>")
        else:
            os.system('no_url "" + url + ""')
    elif ("" + url + "" == '*.???' or "" + url + "" == '*.??'):
        os.system('send "unknown/data" "" + url + ""')
    elif ("" + url + "" == '*/'):
        if (os.system('test -d "" + DOCHOME + "/" + url + ""') ):
            os.system('ls "" + DOCHOME + "/" + url + ""') | os.system('LsToHTML')
    else:
        if (os.system('test -f "" + DOCHOME + "/" + url + ""') ):
            filetype = raw_input()< "$DOCHOME/$url"
            
                elif ("" + filetype + "" == '\#!/*/*' or "" + filetype + "" == '\#!?/*/*'):
                    os.system('header "text/plain; charset=US-ASCII"')
                    os.system('cat "" + DOCHOME + "/" + url + ""')
                elif ("" + filetype + "" == ''<!*>''):
                    os.system('header "text/html; charset=US-ASCII"')
                    os.system('cat "" + DOCHOME + "/" + url + ""')
                else:
                    os.system('header "text/html; charset=US-ASCII"')
                    print("<pre>")
                    os.system('cat "" + DOCHOME + "/" + url + ""')
                    print("</pre>")
        else:
            if (os.system('test -f "" + DOCHOME + "/" + url + "/" + INDEX + ""') ):
                os.system('header "text/html; charset=US-ASCII"')
                os.system('cat "" + DOCHOME + "/" + url + "/" + INDEX + ""')
            else:
                if (os.system('test -d "" + DOCHOME + "/" + url + ""') ):
                    os.system('ls "" + DOCHOME + "/" + url + ""') | os.system('LsToHTML')
                else:
                    os.system('no_url "" + url + ""')
