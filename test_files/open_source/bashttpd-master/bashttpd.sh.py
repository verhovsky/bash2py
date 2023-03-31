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
    print("WARNING: " + str('"'+"\" \"".join(sys.argv[1:])+'"'))

"-r" "bashttpd.conf"  or { _rc = subprocess.call("cat",shell=True,stdout=file('bashttpd.conf','wb'),stdin=subprocess.PIPE)
_rc.communicate("#\n# bashttpd.conf - configuration for bashttpd\n#\n# The behavior of bashttpd is dictated by the evaluation\n# of rules specified in this configuration file.  Each rule\n# is evaluated until one is matched.  If no rule is matched,\n# bashttpd will serve a 500 Internal Server Error.\n#\n# The format of the rules are:\n#    on_uri_match REGEX command [args]\n#    unconditionally command [args]\n#\n# on_uri_match:\n#   On an incoming request, the URI is checked against the specified\n#   (bash-supported extended) regular expression, and if encounters a match the\n#   specified command is executed with the specified arguments.\n#\n#   For additional flexibility, on_uri_match will also pass the results of the\n#   regular expression match, " + str(BASH_REMATCH[@]) + " as additional arguments to the\n#   command.\n#\n# unconditionally:\n#   Always serve via the specified command.  Useful for catchall rules.\n#\n# The following commands are available for use:\n#\n#   serve_file FILE\n#     Statically serves a single file.\n#\n#   serve_dir_with_tree DIRECTORY\n#     Statically serves the specified directory using 'tree'.  It must be\n#     installed and in the PATH.\n#\n#   serve_dir_with_ls DIRECTORY\n#     Statically serves the specified directory using 'ls -al'.\n#\n#   serve_dir  DIRECTORY\n#     Statically serves a single directory listing.  Will use 'tree' if it is\n#     installed and in the PATH, otherwise, 'ls -al'\n#\n#   serve_dir_or_file_from DIRECTORY\n#     Serves either a directory listing (using serve_dir) or a file (using\n#     serve_file).  Constructs local path by appending the specified root\n#     directory, and the URI portion of the client request.\n#\n#   serve_static_string STRING\n#     Serves the specified static string with Content-Type text/plain.\n#\n# Examples of rules:\n#\n# on_uri_match '^/issue" + str() + "' serve_file \"/etc/issue\"\n#\n#   When a client's requested URI matches the string '/issue', serve them the\n#   contents of /etc/issue\n#\n# on_uri_match 'root' serve_dir /\n#\n#   When a client's requested URI has the word 'root' in it, serve up\n#   a directory listing of /\n#\n# DOCROOT=/var/www/html\n# on_uri_match '/(.*)' serve_dir_or_file_from \"" + str(DOCROOT) + "\"\n#   When any URI request is made, attempt to serve a directory listing\n#   or file content based on the request URI, by mapping URI's to local\n#   paths relative to the specified \"" + str(DOCROOT) + "\"\n#\n\nunconditionally serve_static_string 'Hello, world!  You can configure bashttpd by modifying bashttpd.conf.'\n\n# More about commands:\n#\n# It is possible to somewhat easily write your own commands.  An example\n# may help.  The following example will serve \"Hello, " + str(x) + "!\" whenever\n# a client sends a request with the URI /say_hello_to/" + str(x) + ":\n#\n# serve_hello() {\n#    add_response_header \"Content-Type\" \"text/plain\"\n#    send_response_ok_exit <<< \"Hello, " + str(sys.argv[2]) + "!\"\n# }\n# on_uri_match '^/say_hello_to/(.*)" + str() + "' serve_hello\n#\n# Like mentioned before, the contents of " + str(BASH_REMATCH[@]) + " are passed\n# to your command, so its possible to use regular expression groups\n# to pull out info.\n#\n# With this example, when the requested URI is /say_hello_to/Josh, serve_hello\n# is invoked with the arguments '/say_hello_to/Josh' 'Josh',\n# (" + str(BASH_REMATCH[0]) + " is always the full match)\n")
warn()
exit(1) }
def recv () :
    print("< " + str('"'+"\" \"".join(sys.argv[1:])+'"'))

def send () :
    print("> " + str('"'+"\" \"".join(sys.argv[1:])+'"'))
    print( "%s\\r\\n" % (str(" ".join(sys.argv[1:]))) )
    

UID == 0 and warn()
DATE=os.popen("date +\"%a, %d %b %Y %H:%M:%S %Z\"").read()
RESPONSE_HEADERS=("Date: " + str(DATE) "Expires: " + str(DATE) "Server: Slash Bin Slash Bash")

def add_response_header () :
    global RESPONSE_HEADERS

    RESPONSE_HEADERS=(str(sys.argv[1]) + ": " + str(sys.argv[2]))

HTTP_RESPONSE=([200]="OK" [400]="Bad Request" [403]="Forbidden" [404]="Not Found" [405]="Method Not Allowed" [500]="Internal Server Error")

def send_response () :
    global RESPONSE_HEADERS

    code=sys.argv[1]
    
    send()
    for i in [str(RESPONSE_HEADERS[@])]:
        send()
    send()
    while (line = raw_input()):
        send()

def send_response_ok_exit () :
    send_response()
    exit(0)

def fail_with () :
    send_response()
    exit(1)

def serve_file () :

    file=sys.argv[1]
    
    CONTENT_TYPE = raw_input() and add_response_header()
    CONTENT_LENGTH = raw_input() and add_response_header()
    send_response_ok_exit()

def serve_dir_with_tree () :

    dir=str(sys.argv[1])
    
    add_response_header()
    # The --du option was added in 1.6.0.
    x = raw_input()
    tree_vers == "v1.6"* and tree_opts="--du"
    send_response_ok_exit()

def serve_dir_with_ls () :

    dir=sys.argv[1]
    
    add_response_header()
    send_response_ok_exit()

def serve_dir () :

    dir=sys.argv[1]
    
    # If `tree` is installed, use that for pretty output.
    _rc = subprocess.call("which tree",shell=True,stderr=file('/dev/null','wb'),stdout=file('/dev/null','wb'))
     and serve_dir_with_tree()
    serve_dir_with_ls()
    fail_with()

def serve_dir_or_file_from () :

    URL_PATH=str(sys.argv[1]) + "/" + str(sys.argv[3])
    
    _rc = subprocess.call(["shift"])
    # sanitize URL_PATH
    URL_PATH=URL_PATH//[^a-zA-Z0-9_~\-\.\/]/
    URL_PATH == *".."* and fail_with()
    # Serve index file if exists in requested directory
    S_ISDIR(os.stat(URL_PATH).st_mode) and (os.path.isfile(str(URL_PATH) + "/index.html") and S_ISREG(os.stat(str(URL_PATH) + "/index.html").st_mode)) and -r str(URL_PATH) + "/index.html" and URL_PATH=str(URL_PATH) + "/index.html"
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

    regex=sys.argv[1]
    
    _rc = subprocess.call(["shift"])
    REQUEST_URI =~ regex and _rc = subprocess.call([str('"'+"\" \"".join(sys.argv[1:])+'"'),str(BASH_REMATCH[@])])

def unconditionally () :
    global REQUEST_URI

    _rc = subprocess.call([str('"'+"\" \"".join(sys.argv[1:])+'"'),str(REQUEST_URI)])

# Request-Line HTTP RFC 2616 $5.1
line = raw_input() or fail_with()
# strip trailing CR if it exists
line=line%%"\r"
recv()
REQUEST_METHOD = raw_input()
(str(REQUEST_METHOD)  != '') and (str(REQUEST_URI)  != '') and (str(REQUEST_HTTP_VERSION)  != '') or fail_with()
# Only GET is supported at this time
"REQUEST_METHOD" == ""GET""  or fail_with()
REQUEST_HEADERS=""

while (line = raw_input()):
    line=line%%"\r"
    recv()
    # If we've reached the end of the headers, break.
    ('"$line"' not in globals()) and break
    REQUEST_HEADERS=(line)
_rc = subprocess.call(["source","bashttpd.conf"])
fail_with()
