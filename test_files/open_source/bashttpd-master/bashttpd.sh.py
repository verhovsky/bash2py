#! /usr/bin/env python
import sys,os,subprocess
from stat import *
#
# A simple, configurable HTTP server written in bash.
#
# See LICENSE for licensing information.
#
# Original author: Avleen Vig, 2012
# Reworked by:     Josh Cartwright, 2012
def warn () :
    print("WARNING: "+str('"'+"\" \"".join(sys.argv[1:])+'"'))

"-r" "bashttpd.conf"  or { _rc = subprocess.Popen("cat",shell=True,stdout=file('bashttpd.conf','wb'),stdin=subprocess.PIPE)
_rc.communicate("""#
# bashttpd.conf - configuration for bashttpd
#
# The behavior of bashttpd is dictated by the evaluation
# of rules specified in this configuration file.  Each rule
# is evaluated until one is matched.  If no rule is matched,
# bashttpd will serve a 500 Internal Server Error.
#
# The format of the rules are:
#    on_uri_match REGEX command [args]
#    unconditionally command [args]
#
# on_uri_match:
#   On an incoming request, the URI is checked against the specified
#   (bash-supported extended) regular expression, and if encounters a match the
#   specified command is executed with the specified arguments.
#
#   For additional flexibility, on_uri_match will also pass the results of the
#   regular expression match, ${BASH_REMATCH[@]} as additional arguments to the
#   command.
#
# unconditionally:
#   Always serve via the specified command.  Useful for catchall rules.
#
# The following commands are available for use:
#
#   serve_file FILE
#     Statically serves a single file.
#
#   serve_dir_with_tree DIRECTORY
#     Statically serves the specified directory using 'tree'.  It must be
#     installed and in the PATH.
#
#   serve_dir_with_ls DIRECTORY
#     Statically serves the specified directory using 'ls -al'.
#
#   serve_dir  DIRECTORY
#     Statically serves a single directory listing.  Will use 'tree' if it is
#     installed and in the PATH, otherwise, 'ls -al'
#
#   serve_dir_or_file_from DIRECTORY
#     Serves either a directory listing (using serve_dir) or a file (using
#     serve_file).  Constructs local path by appending the specified root
#     directory, and the URI portion of the client request.
#
#   serve_static_string STRING
#     Serves the specified static string with Content-Type text/plain.
#
# Examples of rules:
#
# on_uri_match '^/issue$' serve_file "/etc/issue"
#
#   When a client's requested URI matches the string '/issue', serve them the
#   contents of /etc/issue
#
# on_uri_match 'root' serve_dir /
#
#   When a client's requested URI has the word 'root' in it, serve up
#   a directory listing of /
#
# DOCROOT=/var/www/html
# on_uri_match '/(.*)' serve_dir_or_file_from "$DOCROOT"
#   When any URI request is made, attempt to serve a directory listing
#   or file content based on the request URI, by mapping URI's to local
#   paths relative to the specified "$DOCROOT"
#

unconditionally serve_static_string 'Hello, world!  You can configure bashttpd by modifying bashttpd.conf.'

# More about commands:
#
# It is possible to somewhat easily write your own commands.  An example
# may help.  The following example will serve "Hello, $x!" whenever
# a client sends a request with the URI /say_hello_to/$x:
#
# serve_hello() {
#    add_response_header "Content-Type" "text/plain"
#    send_response_ok_exit <<< "Hello, $2!"
# }
# on_uri_match '^/say_hello_to/(.*)$' serve_hello
#
# Like mentioned before, the contents of ${BASH_REMATCH[@]} are passed
# to your command, so its possible to use regular expression groups
# to pull out info.
#
# With this example, when the requested URI is /say_hello_to/Josh, serve_hello
# is invoked with the arguments '/say_hello_to/Josh' 'Josh',
# (${BASH_REMATCH[0]} is always the full match)
""")
warn()
exit(1) }
def recv () :
    print("< "+str('"'+"\" \"".join(sys.argv[1:])+'"'))

def send () :
    print("> "+str('"'+"\" \"".join(sys.argv[1:])+'"'))
    print( r'%s\r\n' % (str(" ".join(sys.argv[1:]))) )
    

UID == 0 and warn()
DATE=os.popen("date +\\\"%a, %d %b %Y %H:%M:%S %Z\\\"").read()
_rc = subprocess.call(["declare",and,RESPONSE_HEADERS=("Date: "+str(DATE)+" Expires: "+str(DATE)+" Server: Slash Bin Slash Bash"+)])
def add_response_header () :
    "RESPONSE_HEADERS+="+(str(sys.argv[1])+": "+str(sys.argv[2])+)

_rc = subprocess.call(["declare",and,HTTP_RESPONSE=([200]="OK "+[400]="Bad Request "+[403]="Forbidden "+[404]="Not Found "+[405]="Method Not Allowed "+[500]="Internal Server Error"+)])
def send_response () :
    global RESPONSE_HEADERS

    code=str(sys.argv[1])
    send()
    for i in [RESPONSE_HEADERS[@]]:
        send()
    send()
    while (-r = raw_input()):
        send()

def send_response_ok_exit () :
    send_response()
    exit(0)

def fail_with () :
    send_response()
    exit(1)

def serve_file () :

    file=str(sys.argv[1])
    -r = raw_input() and add_response_header()
    -r = raw_input() and add_response_header()
    send_response_ok_exit()

def serve_dir_with_tree () :
    global tree_vers
    global tree_opts

    dir=str(sys.argv[1]) "tree_vers" "tree_opts" "basehref" "x"
    add_response_header()
    # The --du option was added in 1.6.0.
    x = raw_input()
    tree_vers == "v1.6*" and tree_opts="--du"
    send_response_ok_exit()

def serve_dir_with_ls () :

    dir=str(sys.argv[1])
    add_response_header()
    send_response_ok_exit()

def serve_dir () :

    dir=str(sys.argv[1])
    # If `tree` is installed, use that for pretty output.
    _rc = subprocess.Popen("which" + " " + "tree",shell=True,stderr=file('/dev/null','wb'),stdout=file('/dev/null','wb'))
     and serve_dir_with_tree()
    serve_dir_with_ls()
    fail_with()

def serve_dir_or_file_from () :

    URL_PATH=str(sys.argv[1])+"/"+str(sys.argv[3])
    _rc = subprocess.call(["shift"])
    # sanitize URL_PATH
    URL_PATH=str(URL_PATH//[^a-zA-Z0-9_~\-\.\/]/)
    URL_PATH == "*..*" and fail_with()
    # Serve index file if exists in requested directory
    S_ISDIR(os.stat(URL_PATH).st_mode) and (os.path.isfile(URL_PATH+"/index.html") and S_ISREG(os.stat(URL_PATH+"/index.html").st_mode)) and -r URL_PATH+"/index.html" and URL_PATH=str(URL_PATH)+"/index.html"
    if ((os.path.isfile(URL_PATH) and S_ISREG(os.stat(URL_PATH).st_mode)) ):
        -r URL_PATH and serve_file() or fail_with()
    elif (S_ISDIR(os.stat(URL_PATH).st_mode) ):
        -x URL_PATH and serve_dir() or fail_with()
    fail_with()

def serve_static_string () :
    add_response_header()
    send_response_ok_exit()

def on_uri_match () :
    global REQUEST_URI
    global BASH_REMATCH

    regex=str(sys.argv[1])
    _rc = subprocess.call(["shift"])
    REQUEST_URI =~ regex and _rc = subprocess.call([str('"'+"\" \"".join(sys.argv[1:])+'"'),str(BASH_REMATCH[@])])

def unconditionally () :
    global REQUEST_URI

    _rc = subprocess.call([str('"'+"\" \"".join(sys.argv[1:])+'"'),str(REQUEST_URI)])

# Request-Line HTTP RFC 2616 $5.1
-r = raw_input() or fail_with()
# strip trailing CR if it exists
line=str(line%%'')
recv()
-r = raw_input()
(str(REQUEST_METHOD)  != '') and (str(REQUEST_URI)  != '') and (str(REQUEST_HTTP_VERSION)  != '') or fail_with()
# Only GET is supported at this time
REQUEST_METHOD == "GET"  or fail_with()
_rc = subprocess.call(["declare",and,"REQUEST_HEADERS"])
while (-r = raw_input()):
    line=str(line%%'')
    recv()
    # If we've reached the end of the headers, break.
    ('"$line"' not in globals()) and break
    "REQUEST_HEADERS+="+(str(line)+)
_rc = subprocess.call(["source","bashttpd.conf"])
fail_with()
