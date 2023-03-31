import sys, os, os.path
from stat import *
#
# inet2hex - Internet address conversion, dotted-decimal to hex
#
def inet2hex () 
{ 
    os.system('local IFS')
    
    IFS=.
    
    os.system('set -- sys.argv[1]')
    
    if ((($# != 4)) ):
        print("inet2hex: incorrect input format: " + sys.argv[1] + "")1>&2
        
        print("inet2hex: usage: inet2hex XX.XX.XX.XX")1>&2
        
        os.system('return 2')
    
    print( "0x%02x%02x%02x%02x\n" % (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]) )

}
#
# hex2inet - Internet address conversion, hex to dotted-decimal
#
def hex2inet () 
{ 
    os.system('local x1 x2 x3 x4')
    
    os.system('local rev')
    
    OPTIND=1
    
    while (os.system('getopts "r" o')):
        
            if ( "" + o + "" == 'r'):
                rev=true
            else:
                print("hex2inet: usage: hex2inet [-r] [0x]XXXXXXXX")1>&2
                
                exit(2)
    
    os.system('shift ( OPTIND - 1 )')
    
    
        if ( "" + sys.argv[1] + "" == '0x*'):
            h=${1#??}
        else:
            h=sys.argv[1]
    
    if (((${#h} != 8)) ):
        print("hex2inet: " + h + " not in inet format")1>&2
        
        print("hex2inet: usage: hex2inet [0x]XXXXXXXX")1>&2
        
        os.system('return 2')
    
    x1=( 0x${h:0:2} )
    
    x2=( 0x${h:2:2} )
    
    x3=( 0x${h:4:2} )
    
    x4=( 0x${h:6:2} )
    
    if (-z "" + rev + ""  ):
        print( "%d.%d.%d.%d\n" % (x1, x2, x3, x4) )

    else:
        print( "%d.%d.%d.%d\n" % (x4, x3, x2, x1) )

    
    os.system('return 0')
}
