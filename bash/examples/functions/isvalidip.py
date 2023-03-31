import sys, os, os.path
from stat import *
# Thanks to Chris F. A. Johnson <c.f.a.johnson@rogers.com> for this one
def is_validip () 
{ 
    
        if ( "" + $ + "*" == '""' or "" + $ + "*" == '*[!0-9.]*' or "" + $ + "*" == '*[!0-9]'):
            os.system('return 1')
    
    os.system('local IFS=.')
    
    os.system('set -- $*')
    
    $# == 4  && ${1:-666} < 255  && ${2:-666} < 255  && ${3:-666} < 255  && ${4:-666} < 254 
}
