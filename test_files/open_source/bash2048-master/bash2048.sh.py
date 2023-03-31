#! /usr/bin/env python
import sys,os,subprocess
from stat import *
#important variables
_rc = subprocess.call(["declare","-ia","board"])
# array that keeps track of game status
_rc = subprocess.call(["declare","-i","pieces"])
# number of pieces present on board
_rc = subprocess.call(["declare","-i",score=0])
# score variable
_rc = subprocess.call(["declare","-i","flag_skip"])
# flag that prevents doing more than one operation on
# single field in one step
_rc = subprocess.call(["declare","-i","moves"])
# stores number of possible moves to determine if player lost 
# the game
_rc = subprocess.call(["declare",ESC=r''])
# escape byte
_rc = subprocess.call(["declare",header="Bash 2048 v1.1 (https://github.com/mydzor/bash2048)"])
#default config
_rc = subprocess.call(["declare","-i",board_size=4])
_rc = subprocess.call(["declare","-i",target=2048])
#for colorizing numbers
_rc = subprocess.call(["declare",and,"colors"])
colors[2]=33
# yellow text
colors[4]=32
# green text
colors[8]=34
# blue text
colors[16]=36
# cyan text
colors[32]=35
# purple text
colors[64]="33m\033[7"
# yellow background
colors[128]="32m\033[7"
# green background
colors[256]="34m\033[7"
# blue background
colors[512]="36m\033[7"
# cyan background
colors[1024]="35m\033[7"
# purple background
colors[2048]="31m\033[7"
# red background (won with default target)
_rc = subprocess.Popen("exec",shell=True,stdout=file('/dev/null','wb'))

# no logging by default
_rc = subprocess.call(["trap","end_game 0","INT"])
#handle INT signal
#simplified replacement of seq command
def _seq () :

    cur=1
    "max"
    inc=1
    
    if ( str(len(sys.argv)) == '1'):
        max=str(sys.argv[1])
    elif ( str(len(sys.argv)) == '2'):
        cur=str(sys.argv[1])
        max=str(sys.argv[2])
    elif ( str(len(sys.argv)) == '3'):
        cur=str(sys.argv[1])
        inc=str(sys.argv[2])
        max=str(sys.argv[3])
    while (_rc = subprocess.call(["test",str(max),>=,str(cur)])):
        print( str(cur)+" " )
        
        "cur+=inc"

# print currect status of the game, last added pieces are marked red
def print_board () :
    global header
    global pieces
    global target
    global score
    global index_max
    global board
    global colors
    global l

    _rc = subprocess.call(["clear"])
    print( str(header)+" pieces="+str(pieces)+" target="+str(target)+" score="+str(score)+"\n" )
    
    print( "Board status:\n" )
    
    print( "\n" )
    
    print( r'/------' )
    
    for l in [os.popen("_seq 1 "+index_max).read()]:
        print( r'|------' )
    
    print( r'\\\n' )
    
    for l in [os.popen("_seq 0 "+index_max).read()]:
        print( r'|' )
        
        for m in [os.popen("_seq 0 "+index_max).read()]:
            if (str(board[l*$board_size+m]) ):
                if (r'(last_added==(l*board_size+m))|(first_round==(l*board_size+m))' ):
                    print( r'\033[1m\033[31m %4d \033[0m|' % (str(board[l*$board_size+m])) )
                
                else:
                    print( "\033[1m\033["+str(colors[${board[l*$board_size+m]}])+"m %4d\033[0m |" % (str(board[l*$board_size+m])) )
                
                print( " %4d |" % (str(board[l*$board_size+m])) )
            
            else:
                print( r'      |' )
                
                print( r'      |' )
        
        l="="+str(index_max) or { 
            print( r'\n|------' )
            
            for l in [os.popen("_seq 1 "+index_max).read()]:
                print( r'|------' )
            
            print( r'|\n' )
            
            print( r'\n' )
            
        }
    print( r'\n\\------' )
    
    for l in [os.popen("_seq 1 "+index_max).read()]:
        print( r'|------' )
    
    print( r'/\n' )
    

# Generate new piece on the board
# inputs:
#         $board  - original state of the game board
#         $pieces - original number of pieces
# outputs:
#         $board  - new state of the game board
#         $pieces - new number of pieces
def generate_piece () :
    global pos
    global value
    global last_added

    while (True):
        pos="RANDOM%fields_total"
        "board["+str(pos)+"]" or { 
            value="RANDOM%10?2:4"
            "board["+str(pos)+"]="+str(value)
            last_added=str(pos)
            print( "Generated new piece with value "+str(value)+" at position ["+str(pos)+"]\n" )
            
            break
        }
    "pieces++"

# perform push operation between two pieces
# inputs:
#         $1 - push position, for horizontal push this is row, for vertical column
#         $2 - recipient piece, this will hold result if moving or joining
#         $3 - originator piece, after moving or joining this will be left empty
#         $4 - direction of push, can be either "up", "down", "left" or "right"
#         $5 - if anything is passed, do not perform the push, only update number 
#              of valid moves
#         $board - original state of the game board
# outputs:
#         $change    - indicates if the board was changed this round
#         $flag_skip - indicates that recipient piece cannot be modified further
#         $board     - new state of the game board
def push_pieces () :
    global board_size
    global board
    global first
    global second
    global change
    global flag_skip
    global target

    
    if ( str(sys.argv[4]) == '"up"'):
        "first="+str(sys.argv[2])+"*"+str(board_size)+"+"+str(sys.argv[1])
        "second=("+str(sys.argv[2])+"+"+str(sys.argv[3])+")*"+str(board_size)+"+"+str(sys.argv[1])
    elif ( str(sys.argv[4]) == '"down"'):
        "first=(index_max-"+str(sys.argv[2])+")*"+str(board_size)+"+"+str(sys.argv[1])
        "second=(index_max-"+str(sys.argv[2])+"-"+str(sys.argv[3])+")*"+str(board_size)+"+"+str(sys.argv[1])
    elif ( str(sys.argv[4]) == '"left"'):
        "first="+str(sys.argv[1])+"*"+str(board_size)+"+"+str(sys.argv[2])
        "second="+str(sys.argv[1])+"*"+str(board_size)+"+("+str(sys.argv[2])+"+"+str(sys.argv[3])+")"
    elif ( str(sys.argv[4]) == '"right"'):
        "first="+str(sys.argv[1])+"*"+str(board_size)+"+(index_max-"+str(sys.argv[2])+")"
        "second="+str(sys.argv[1])+"*"+str(board_size)+"+(index_max-"+str(sys.argv[2])+"-"+str(sys.argv[3])+")"
    str(board[$first]) or { 
        str(board[$second]) and { 
            if (_rc = subprocess.call(["test", not ,str(sys.argv[5])]) ):
                "board["+str(first)+"]="+str(board[$second])
                "board["+str(second)+"]=0"
                change=1
                print( "move piece with value "+str(board[$first])+" from ["+str(second)+"] to ["+str(first)+"]\n" )
            
            else:
                "moves++"
            return
        }
        return
    }
    str(board[$second]) and flag_skip=1
    str(board[$first])+"=="+str(board[second]) and { 
        if (_rc = subprocess.call(["test", not ,str(sys.argv[5])]) ):
            "board["+str(first)+"]*=2"
            "board["+str(first)+"]=="+str(target) and _rc = subprocess.call(["end_game",1])
            "board["+str(second)+"]=0"
            "pieces-=1"
            change=1
            "score+="+str(board[$first])
            print( "joined piece from ["+str(second)+"] with ["+str(first)+"], new value="+str(board[$first])+"\n" )
        
        else:
            "moves++"
    }

def apply_push () :
    global index_max
    global flag_skip
    global increment_max

    print( "\n\ninput: "+str(sys.argv[1])+" key\n" )
    
    for i in [os.popen("_seq 0 "+index_max).read()]:
        for j in [os.popen("_seq 0 "+index_max).read()]:
            flag_skip=0
            increment_max="index_max-j"
            for k in [os.popen("_seq 1 "+increment_max).read()]:
                "flag_skip" and break
                push_pieces()

def check_moves () :
    global moves

    moves=0
    apply_push()
    apply_push()
    apply_push()
    apply_push()

def key_react () :
    global change
    global REPLY
    global ESC

    change=0
    -d = raw_input()
    _rc = subprocess.call(["test",str(REPLY),==,str(ESC)]) and { 
        -d = raw_input()
        _rc = subprocess.call(["test",str(REPLY),==,"["]) and { 
            -d = raw_input()
            
            if ( str(REPLY) == 'A'):
                apply_push()
            elif ( str(REPLY) == 'B'):
                apply_push()
            elif ( str(REPLY) == 'C'):
                apply_push()
            elif ( str(REPLY) == 'D'):
                apply_push()
        }
    } or { 
        
        if ( str(REPLY) == 'k'):
            apply_push()
        elif ( str(REPLY) == 'j'):
            apply_push()
        elif ( str(REPLY) == 'l'):
            apply_push()
        elif ( str(REPLY) == 'h'):
            apply_push()
    }

def end_game () :
    global score
    global target

    print_board()
    print( "GAME OVER\n" )
    
    print( "Your score: "+str(score)+"\n" )
    
    _rc = subprocess.call(["stty",print])
    str(sys.argv[1]) and { 
        print( "Congratulations you have achieved "+str(target)+"\n" )
        
        exit(0)
    }
    print( "You have lost, better luck next time.\033[0m\n" )
    
    exit(0)

def help () :
    _rc = subprocess.Popen("cat",shell=True,stdin=subprocess.PIPE)
    _rc.communicate("""Usage: $1 [-b INTEGER] [-t INTEGER] [-l FILE] [-h]
    
      -b			specify game board size (sizes 3-9 allowed)
      -t			specify target score to win (needs to be power of 2)
      -l			log debug info into specified file
      -h			this help
    
    """)

#parse commandline options
while (_rc = subprocess.call(["getopts","b:t:l:h","opt"])):
    
    if ( str(opt) == 'b'):
        board_size=str(OPTARG)
        r'(board_size>=3)&(board_size<=9)' or { print( "Invalid board size, please choose size between 3 and 9\n" )
        
        exit(-1) }
    elif ( str(opt) == 't'):
        target=str(OPTARG)
        print( "obase=2;"+str(target)+"\n" )
         | _rc = subprocess.call(["bc"]) | _rc = subprocess.call(["grep","-e",r'^1[^1]*"+str()+"'])
        str(_rc) and { print( "Invalid target, has to be power of two\n" )
        
        exit(-1) }
    elif ( str(opt) == 'h'):
        help()
        exit(0)
    elif ( str(opt) == 'l'):
        _rc = subprocess.Popen("exec",shell=True,stdout=file('$OPTARG','wb'))
    
    elif ( str(opt) == '\?'):
        print( "Invalid option: -"+str(opt)+"\", try "+str(__file__)+" -h\n\"" )
        
        exit(1)
    elif ( str(opt) == ':'):
        print( "Option -"+str(opt)+"\" requires an argument, try "+str(__file__)+" -h\n\"" )
        
        exit(1)
#init board
fields_total="board_size*board_size"
index_max="board_size-1"
for i in [os.popen("_seq 0 "+fields_total).read()]:
    "board["+str(i)+"]=\"0\""
pieces=0
generate_piece()
first_round=str(last_added)
generate_piece()
while (True):
    print_board()
    key_react()
    "change" and generate_piece()
    first_round=-1
    pieces="=fields_total" and { check_moves()
    moves==0 and end_game() }
#lose the game
