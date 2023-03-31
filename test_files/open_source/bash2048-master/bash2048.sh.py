#! /usr/bin/env python
import sys,os,subprocess,signal
from stat import *
#important variables
board=""

# array that keeps track of game status
pieces=""

# number of pieces present on board
score=0

# score variable
flag_skip=""

# flag that prevents doing more than one operation on
# single field in one step
moves=""

# stores number of possible moves to determine if player lost 
# the game
ESC="\x1b"

# escape byte
header="Bash 2048 v1.1 (https://github.com/mydzor/bash2048)"

#default config
board_size=4

target=2048

#for colorizing numbers
colors=""

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
_rc = subprocess.call("exec",shell=True,stdout=file('/dev/null','wb'))

# no logging by default
signal.signal(signal.SIGINT,"end_game 0")

#handle INT signal
#simplified replacement of seq command
def _seq () :

    cur=1
    
    
    inc=1
    
    
    if ( len(sys.argv) == '1'):
        max=sys.argv[1]
    elif ( len(sys.argv) == '2'):
        cur=sys.argv[1]
        max=sys.argv[2]
    elif ( len(sys.argv) == '3'):
        cur=sys.argv[1]
        inc=sys.argv[2]
        max=sys.argv[3]
    while (_rc = subprocess.call("test " + max + " -ge " + cur,shell=True)
    ):
        print( str(cur) + " " )
        
        cur="inc"

# print currect status of the game, last added pieces are marked red
def print_board () :
    global header
    global pieces
    global target
    global score
    global index_max
    global board
    global board_size
    global colors
    global l

    _rc = subprocess.call(["clear"])
    print( str(header) + " pieces=" + str(pieces) + " target=" + str(target) + " score=" + str(score) + "\n" )
    
    print( "Board status:\n" )
    
    print( "\n" )
    
    print( "/------" )
    
    for l in [os.popen("_seq 1 "+str(index_max)).read()]:
        print( "|------" )
    
    print( "\\\\\\n" )
    
    for l in [os.popen("_seq 0 "+str(index_max)).read()]:
        print( "|" )
        
        for m in [os.popen("_seq 0 "+str(index_max)).read()]:
            if (board[l*board_size+m] ):
                if (("last_added"==("l"*"board_size+m"))|("first_round"==("l"*"board_size+m")) ):
                    print( "\\033[1m\\033[31m %4d \\033[0m|" % (board[l*board_size+m]) )
                
                else:
                    print( "\033[1m\033[" + str(colors[board[l*board_size+m]]) + "m %4d\033[0m |" % (board[l*board_size+m]) )
                
                print( " %4d |" % (board[l*board_size+m]) )
            
            else:
                print( "      |" )
                
                print( "      |" )
        
        l==index_max or { 
            print( "\\n|------" )
            
            for l in [os.popen("_seq 1 "+str(index_max)).read()]:
                print( "|------" )
            
            print( "|\\n" )
            
            print( "\\n" )
            
        }
    print( "\\n\\\\------" )
    
    for l in [os.popen("_seq 1 "+str(index_max)).read()]:
        print( "|------" )
    
    print( "/\\n" )
    

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
    global board
    global last_added

    while (True):
        pos="RANDOM"%"fields_total"
        "board"[pos] or { 
            value="RANDOM"%10?2:4
            board[pos]=value
            last_added=pos
            print( "Generated new piece with value " + str(value) + " at position [" + str(pos) + "]\n" )
            
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
    global first
    global board_size
    global second
    global board
    global change
    global flag_skip
    global target
    global pieces
    global score

    
    if ( sys.argv[4] == 'up'):
        first=sys.argv[2]*board_size+str(sys.argv[1])
        second=(str(sys.argv[2]) +  + str(sys.argv[3]))*str(board_size) +  + str(sys.argv[1])
    elif ( sys.argv[4] == 'down'):
        first=("index_max-" + str(sys.argv[2]))*str(board_size) +  + str(sys.argv[1])
        second=("index_max-" + str(sys.argv[2]) + "-" + str(sys.argv[3]))*str(board_size) +  + str(sys.argv[1])
    elif ( sys.argv[4] == 'left'):
        first=sys.argv[1]*board_size+str(sys.argv[2])
        second=sys.argv[1]*board_size+"(str(sys.argv[2]) +  + str(sys.argv[3]))
    elif ( sys.argv[4] == 'right'):
        first=sys.argv[1]*board_size+"("index_max-" + str(sys.argv[2]))
        second=sys.argv[1]*board_size+"("index_max-" + str(sys.argv[2]) + "-" + str(sys.argv[3]))
    board[first] or { 
        board[second] and { 
            if (_rc = subprocess.call("test -z " + sys.argv[5],shell=True)
             ):
                board[first]=board[second]
                board[second]=0
                change=1
                print( "move piece with value " + str(board[first]) + " from [" + str(second) + "] to [" + str(first) + "]\n" )
            
            else:
                "moves++"
            return
        }
        return
    }
    board[second] and flag_skip=1
    board[first]==board[second] and { 
        if (_rc = subprocess.call("test -z " + sys.argv[5],shell=True)
         ):
            "board"[first]*=2
            board[first]==target and _rc = subprocess.call(["end_game",1])
            board[second]=0
            pieces-=1
            change=1
            score=board[first]
            print( "joined piece from [" + str(second) + "] with [" + str(first) + "], new value=" + str(board[first]) + "\n" )
        
        else:
            "moves++"
    }

def apply_push () :
    global index_max
    global flag_skip
    global increment_max

    print( "\n\ninput: " + str(sys.argv[1]) + " key\n" )
    
    for i in [os.popen("_seq 0 "+str(index_max)).read()]:
        for j in [os.popen("_seq 0 "+str(index_max)).read()]:
            flag_skip=0
            increment_max="index_max-j"
            for k in [os.popen("_seq 1 "+str(increment_max)).read()]:
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
    raw_input()
    _rc = subprocess.call("test " + str(REPLY) + " " + = + " " + str(ESC),shell=True)
     and { 
        raw_input()
        _rc = subprocess.call("test " + str(REPLY) + " " + = + " [",shell=True)
         and { 
            raw_input()
            
            if ( REPLY == 'A'):
                apply_push()
            elif ( REPLY == 'B'):
                apply_push()
            elif ( REPLY == 'C'):
                apply_push()
            elif ( REPLY == 'D'):
                apply_push()
        }
    } or { 
        
        if ( REPLY == 'k'):
            apply_push()
        elif ( REPLY == 'j'):
            apply_push()
        elif ( REPLY == 'l'):
            apply_push()
        elif ( REPLY == 'h'):
            apply_push()
    }

def end_game () :
    global score
    global target

    print_board()
    print( "GAME OVER\n" )
    
    print( "Your score: " + str(score) + "\n" )
    
    _rc = subprocess.call(["stty","echo"])
    sys.argv[1] and { 
        print( "Congratulations you have achieved " + str(target) + "\n" )
        
        exit(0)
    }
    print( "You have lost, better luck next time.\033[0m\n" )
    
    exit(0)

def help () :
    _rc = subprocess.call("cat",shell=True,stdin=subprocess.PIPE)
    _rc.communicate("Usage: " + str(sys.argv[1]) + " [-b INTEGER] [-t INTEGER] [-l FILE] [-h]\n\n  -b			specify game board size (sizes 3-9 allowed)\n  -t			specify target score to win (needs to be power of 2)\n  -l			log debug info into specified file\n  -h			this help\n\n")

#parse commandline options
while (_rc = subprocess.call(["getopts","b:t:l:h","opt"])):
    
    if ( opt == 'b'):
        board_size=str(OPTARG)
        ("board_size">="3)&(board_size"<=9) or { print( "Invalid board size, please choose size between 3 and 9\n" )
        
        exit(-1) }
    elif ( opt == 't'):
        target=str(OPTARG)
        print( "obase=2;" + str(target) + "\n" )
         | _rc = subprocess.call(["bc"]) | _rc = subprocess.call(["grep","-e","^1[^1]*\$"])
        _rc and { print( "Invalid target, has to be power of two\n" )
        
        exit(-1) }
    elif ( opt == 'h'):
        help()
        exit(0)
    elif ( opt == 'l'):
        _rc = subprocess.call("exec",shell=True,stdout=file('$OPTARG','wb'))
    
    elif ( opt == '\?'):
        print( "Invalid option: -"opt", try " + str(__file__) + " -h\n" )
        
        exit(1)
    elif ( opt == ':'):
        print( "Option -"opt" requires an argument, try " + str(__file__) + " -h\n" )
        
        exit(1)
#init board
fields_total="board_size"*"board_size"
index_max="board_size-1"
for i in [os.popen("_seq 0 "+str(fields_total)).read()]:
    board[i]="0"
pieces=0
generate_piece()
first_round=last_added
generate_piece()
while (True):
    print_board()
    key_react()
    "change" and generate_piece()
    first_round=-1
    pieces=="fields_total" and { check_moves()
    moves==0 and end_game() }
#lose the game
