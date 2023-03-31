import sys, os, os.path
from stat import *
#
#From: kaz@cafe.net (Kaz Kylheku)
#Newsgroups: comp.unix.shell
#Subject: Funky little bash script
#Message-ID: <6mspb9$ft2@espresso.cafe.net>
#Date: Thu, 25 Jun 1998 06:11:39 GMT
#Here is something I wrote a few years ago when I was bored one day.
#Warning: this contains control characters.
# Line input routine for GNU Bourne-Again Shell
# plus terminal-control primitives.
#
# by Kaz Kylheku
# June 1996, Vancouver, Canada
#
# Function to disable canonical input processing.
# Terminal modes are saved into variable "savetty"
#
#
def raw () 
{ 
    savetty= os.popen('stty -g').read() 
    
    os.system('stty -icanon -isig -echo -echok -echonl inlcr')
}
#
# Function to restore terminal settings from savetty variable
#
def restore () 
{ 
    os.system('stty savetty')
}
#
# Set terminal MIN and TIME values.
# If the input argument is a zero, set up terminal to wait for
# a keystroke indefinitely. If the argument is non-zero, set up
# an absolute timeout of that many tenths of a second. The inter-keystroke
# timer facility of the terminal driver is not exploited.
#
