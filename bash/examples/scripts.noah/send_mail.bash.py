import sys, os, os.path
from stat import *
# send_mail.bash
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created: 1992-07-02
# Public domain
# Commentary:
# TODO: implement Fcc headers (see emacs manual)
# Code:
#:docstring send_mail:
# Usage: send_mail
#
# This function serves as a simple replacement for sendmail as a client
# interface on those systems where it is not available.  It does assume
# that one can talk to an SMTP mailer on port 25 either on the local host
# or on the host specified by the MAILHOST environment variable.  If you
# have access to sendmail, it's better to use 'sendmail -t' instead of this
# script (which probably isn't as robust).
#
# Message is read from stdin, and headers are parsed to determine
# recipients.  
#:end docstring:
###;;;autoload
def send_mail () 
{ 
    # Need gawk, since several extensions are taken advantage of (like
    
    # IGNORECASE for regexps).
    
    os.system('local awk="" + $ + "{GAWK_LOCATION:-gawk}"')
    
    os.system('local DefaultFrom="" + $ + "{USER:-" + $ + "{LOGNAME}}"')
    
    os.system('local From')
    
    os.system('local To')
    
    os.system('local Cc')
    
    os.system('local Bcc')
    
    os.system('local tmpfile="/tmp/send_mail" + $ + "" + $ + ""')
    
    while (os.path.isfile("" + $ + "{tmpfile}" )):
        tmpfile="/tmp/send_mail" + $ + "{RANDOM}"
    
    # Lines consisting only of dots need one more dot appended.  SMTP
    
    # servers eat one of the dots (and if only 1 dot appears, it signifies
    
    # the end of the message).
    
    os.system('sed '/^\.\.*/s/^\(\.\.*\)$/\1./'> "${tmpfile}"')
    
    # Parse mail headers in message to extract recipients list. 
    
    # This doesn't affect what the user sees---it's only used to generate
    
    # the rcpt-to lines for SMTP. 
    
    os.system('eval $(${awk} -f - "" + $ + "{tmpfile}" <<- '__EOF__'
')
    
    # Not sure if an address is *required* after the HELO.. every sendmail
    
    # I tried talking to didn't seem to care.  Some sendmails don't care
    
    # if there's a HELO at all. 
    
    os.system('cat') <<-__EOF__ |
HELO
mail from: ${From:-${DefaultFrom}}
$(for name in ${To} ${Cc} ${Bcc} ; do
     echo "rcpt to: ${name}"
  done)
data
$(cat "${tmpfile}")
.
quit
__EOF__
  os.system('telnet ${MAILHOST:-localhost} 25> /dev/null 2>&1')
    
    os.system('rm -f "" + $ + "{tmpfile}"')
}
os.system('provide send_mail')
# send_mail.bash ends here
