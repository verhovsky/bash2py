import sys, os, os.path
from stat import *
# number.bash
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created: 1993-02-22
# Last modified: 1993-04-01
# Public domain
# Conversion to bash v2 syntax done by Chet Ramey
# Commentary:
# Code:
#:docstring number:
# Usage: number [number]
#
# Converts decimal integers to english notation.  Spaces and commas are
# optional.  Numbers 67 digits and larger will overflow this script.
#
# E.g: number 99,000,000,000,000,454
#      => ninety-nine quadrillion four hundred fifty-four
#
#:end docstring:
def number () 
{ 
    os.system('local result')
    
    os.system('local val1')
    
    os.system('local val2')
    
    os.system('local val3')
    
    os.system('local d1')
    
    os.system('local d2')
    
    os.system('local d3')
    
    
        if ( "" + $ + "*" == '*[!0-9,.]*'):
            print("number: invalid character in argument.")1>&2
            
            os.system('return 1')
        elif ("" + $ + "*" == '*.*'):
            print("number: fractions not supported (yet).")1>&2
            
            os.system('return 1')
    
    result=''
    
    os.system('eval set - "`echo " + $ + "{1+\"$@\"} | sed -n -e '
')
    
    while (os.system('test $# != 0')):
        os.system('eval `set - sys.argv[1]; 
')
        
        val1='' val2='' val3=''
        
        
            if ( "" + $ + "{d3}" == ''1''):
                val3='one'
            elif ("" + $ + "{d3}" == ''2''):
                val3='two'
            elif ("" + $ + "{d3}" == ''3''):
                val3='three'
            elif ("" + $ + "{d3}" == ''4''):
                val3='four'
            elif ("" + $ + "{d3}" == ''5''):
                val3='five'
            elif ("" + $ + "{d3}" == ''6''):
                val3='six'
            elif ("" + $ + "{d3}" == ''7''):
                val3='seven'
            elif ("" + $ + "{d3}" == ''8''):
                val3='eight'
            elif ("" + $ + "{d3}" == ''9''):
                val3='nine'
        
        
            if ( "" + $ + "{d2}" == ''1''):
                val2='teen'
            elif ("" + $ + "{d2}" == ''2''):
                val2='twenty'
            elif ("" + $ + "{d2}" == ''3''):
                val2='thirty'
            elif ("" + $ + "{d2}" == ''4''):
                val2='forty'
            elif ("" + $ + "{d2}" == ''5''):
                val2='fifty'
            elif ("" + $ + "{d2}" == ''6''):
                val2='sixty'
            elif ("" + $ + "{d2}" == ''7''):
                val2='seventy'
            elif ("" + $ + "{d2}" == ''8''):
                val2='eighty'
            elif ("" + $ + "{d2}" == ''9''):
                val2='ninety'
        
        
            if ( "" + $ + "{val2}" == ''teen''):
                val2=''
                
                
                    elif ("" + $ + "{d1}" == ''0''):
                        val1='ten'
                    elif ("" + $ + "{d1}" == ''1''):
                        val1='eleven'
                    elif ("" + $ + "{d1}" == ''2''):
                        val1='twelve'
                    elif ("" + $ + "{d1}" == ''3''):
                        val1='thirteen'
                    elif ("" + $ + "{d1}" == ''4''):
                        val1='fourteen'
                    elif ("" + $ + "{d1}" == ''5''):
                        val1='fifteen'
                    elif ("" + $ + "{d1}" == ''6''):
                        val1='sixteen'
                    elif ("" + $ + "{d1}" == ''7''):
                        val1='seventeen'
                    elif ("" + $ + "{d1}" == ''8''):
                        val1='eighteen'
                    elif ("" + $ + "{d1}" == ''9''):
                        val1='nineteen'
            if ( "" + $ + "{d1}" == '0'):
                os.system(':')
            else:
                if (os.system('test "." + $ + "{val2}" != '.'') && os.system('test "." + $ + "{d1}" != '.0'') ):
                    val2="" + $ + "{val2}-"
                
                
                    elif ("" + $ + "{d1}" == ''0''):
                        val2="" + $ + "{val2} "
                    elif ("" + $ + "{d1}" == ''1''):
                        val1='one'
                    elif ("" + $ + "{d1}" == ''2''):
                        val1='two'
                    elif ("" + $ + "{d1}" == ''3''):
                        val1='three'
                    elif ("" + $ + "{d1}" == ''4''):
                        val1='four'
                    elif ("" + $ + "{d1}" == ''5''):
                        val1='five'
                    elif ("" + $ + "{d1}" == ''6''):
                        val1='six'
                    elif ("" + $ + "{d1}" == ''7''):
                        val1='seven'
                    elif ("" + $ + "{d1}" == ''8''):
                        val1='eight'
                    elif ("" + $ + "{d1}" == ''9''):
                        val1='nine'
        
        if (os.system('test "." + $ + "{val3}" != '.'') ):
            result="" + $ + "{result}" + $ + "{val3} hundred "
        
        if (os.system('test "." + $ + "{val2}" != '.'') ):
            result="" + $ + "{result}" + $ + "{val2}"
        
        if (os.system('test "." + $ + "{val1}" != '.'') ):
            result="" + $ + "{result}" + $ + "{val1} "
        
        if (os.system('test "." + $ + "{d1}" + $ + "{d2}" + $ + "{d3}" != '.000'') ):
            
                if ( $# == '0' or $# == '1'):

                elif ($# == '2'):
                    result="" + $ + "{result}thousand "
                elif ($# == '3'):
                    result="" + $ + "{result}million "
                elif ($# == '4'):
                    result="" + $ + "{result}billion "
                elif ($# == '5'):
                    result="" + $ + "{result}trillion "
                elif ($# == '6'):
                    result="" + $ + "{result}quadrillion "
                elif ($# == '7'):
                    result="" + $ + "{result}quintillion "
                elif ($# == '8'):
                    result="" + $ + "{result}sextillion "
                elif ($# == '9'):
                    result="" + $ + "{result}septillion "
                elif ($# == '10'):
                    result="" + $ + "{result}octillion "
                elif ($# == '11'):
                    result="" + $ + "{result}nonillion "
                elif ($# == '12'):
                    result="" + $ + "{result}decillion "
                elif ($# == '13'):
                    result="" + $ + "{result}undecillion "
                elif ($# == '14'):
                    result="" + $ + "{result}duodecillion "
                elif ($# == '15'):
                    result="" + $ + "{result}tredecillion "
                elif ($# == '16'):
                    result="" + $ + "{result}quattuordecillion "
                elif ($# == '17'):
                    result="" + $ + "{result}quindecillion "
                elif ($# == '18'):
                    result="" + $ + "{result}sexdecillion "
                elif ($# == '19'):
                    result="" + $ + "{result}septendecillion "
                elif ($# == '20'):
                    result="" + $ + "{result}octodecillion "
                elif ($# == '21'):
                    result="" + $ + "{result}novemdecillion "
                elif ($# == '22'):
                    result="" + $ + "{result}vigintillion "
                else:
                    print("Error: number too large (66 digits max).")1>&2
                    
                    os.system('return 1')
        
        os.system('shift')
    
    os.system('set - ${result}')
    
    
        if ( "" + $ + "*" == ''''):
            os.system('set - 'zero'')
    
    print("${1+"" + $ + "@"}")
}
os.system('provide number')
# number.bash ends here
