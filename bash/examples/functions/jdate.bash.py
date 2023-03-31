import sys, os, os.path
from stat import *
#From: damatex@CAM.ORG (Mario Boudreault)
#Newsgroups: comp.unix.shell
#Subject: JULIAN DATE CONVERSION SUB
#Date: 4 Aug 1995 10:23:28 -0400
#Message-ID: <3vtah0$jb3@ocean.CAM.ORG>
#For those using shells and who want to convert dates to a julian number
#here is a shell script (wihtout validation) that can be used as a base
#program for your shell scripts.
#Special thanks to Ed Ferguson@ti.com who sent me the algorithm to compute
#that date.
#
# MODIFIED BY CHET RAMEY TO CONVERT TO bash v2 SYNTAX
#
# cnvdate - Conversion de dates en julienne et vice et versa...
#
# Par : Mario Boudreault       Damatex Inc   Montreal, Canada
# Date: 2 Aout 1995
# Rev.:  2 Aout 1995
#
# Usage:
#          cvdate [-j] YYYMMDD		pour convertir en nbre de jours
#          cvdate -d {julian number}	pour convertir en AAAAMMJJ
#
def jul_date () 
{ 
    #
    
    # Separe ANNEE, MOIS et JOUR...
    
    #
    
    YEAR= os.popen('echo DATE | awk ' { print substr(sys.argv[0],1,4) } '').read() 
    
    MONTH= os.popen('echo DATE | awk ' { print substr(sys.argv[0],5,2) } '').read() 
    
    DAY= os.popen('echo DATE | awk ' { print substr(sys.argv[0],7,2) } '').read() 
    
    #
    
    # Execute la formule magique...
    
    #
    
    A=( DAY - 32075 + 1461 * ( YEAR + 4800 - ( 14 - MONTH ) / 12 )         	/ 4 + 367 * ( MONTH - 2 + ( 14 - MONTH ) / 12 * 12 ) / 12 - 		3 * ( ( YEAR + 4900 - ( 14 - MONTH ) / 12 ) / 100 ) / 4 )
    
    print("A")
}
def day_date () 
{ 
    TEMP1=( DATE + 68569 )
    
    TEMP2=( 4 * TEMP1 / 146097 )
    
    TEMP1=( TEMP1 - ( 146097 * TEMP2 + 3 ) / 4 )
    
    Y=( 4000 * ( TEMP1 + 1 ) / 1461001 )
    
    TEMP1=( TEMP1 - 1461 * Y / 4 + 31 )
    
    M=( 80 * TEMP1 / 2447 )
    
    D=( TEMP1 - 2447 * M / 80 )
    
    TEMP1=( M / 11 )
    
    M=( M + 2 - 12 * TEMP1 )
    
    Y=( 100 * ( TEMP2 - 49 ) + Y + TEMP1 )
    
    M= os.popen('echo M | awk ' { M=sys.argv[0] ; if ( length(sys.argv[0]) == 1 ) M="0"sys.argv[0] } END { print M } '').read() 
    
    D= os.popen('echo D | awk ' { D=sys.argv[0] ; if ( length(sys.argv[0]) == 1 ) D="0"sys.argv[0] } END { print D } '').read() 
    
    print("YMD")
}
# main()
if ($# == 1  ):
    DATE=sys.argv[1]
    os.system('jul_date')
else:
    if ("" + sys.argv[1] + "" == '-j'  ):
        DATE=sys.argv[2]
        os.system('jul_date')
    else:
        if ("" + sys.argv[1] + "" == '-d'  ):
            DATE=sys.argv[2]
            os.system('day_date')
#
# Termine
#
exit(0)
