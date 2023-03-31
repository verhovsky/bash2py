import sys, os, os.path
from stat import *
#	ash -- "Adventure shell"
#	last edit:	86/04/21	D A Gwyn
#	SCCS ID:	@(#)ash.sh	1.4
OPATH=PATH
def ask () 
{ 
    print("" + $ + "@" '[y/n] ')
    
    ans = raw_input()
    
    
        if ( "" + ans + "" == 'y*' or "" + ans + "" == 'Y*'):
            os.system('return 0')
        else:
            os.system('return 1')
}
CAT=${PAGER:-more}
def ash_inst () 
{ 
    os.system('cat <<-EOF

                Instructions for the Adventure shell

Welcome to the Adventure shell!  In this exploration of the UNIX file
system, I will act as your eyes and hands.  As you move around, I will
describe whatever is visible and will carry out your commands.  The
general form of a command is
        Verb Object Extra_stuff.
Most commands pay no attention to the "Extra_stuff", and many do not
need an "Object".  A typical command is
        get all
which picks up all files in the current "room" (directory).  You can
find out what you are carrying by typing the command
        inventory
The command "help" results in a full description of all commands that I
understand.  To quit the Adventure shell, type
        quit

There are UNIX monsters lurking in the background.  These are also
known as "commands with arguments".

Good luck!
EOF
')
}
def ash_help () 
{ 
    print("I understand the following commands (synonyms in parentheses):")
    
    print("")
    
    print("change OBJECT to NEW_NAME       changes the name of the object")
    
    print("clone OBJECT as NEW_NAME        duplicates the object")
    
    print("drop OBJECTS                    leaves the objects in the room")
    
    print("enter (go) PASSAGE              takes the labeled passage")
    
    print("examine OBJECTS                 describes the objects in detail")
    
    print("feed OBJECT to MONSTER          stuffs the object into a UNIX monster")
    
    print("get (take) OBJECTS              picks up the specified objects")
    
    print("gripe (bug)                     report a problem with the Adventure shell")
    
    print("help                            prints this summary")
    
    print("inventory (i)                   tells what you are carrying")
    
    print("kill (destroy) OBJECTS          destroys the objects")
    
    print("look (l)                        describes the room, including hidden objects")
    
    print("open (read) OBJECT              shows the contents of an object")
    
    print("quit (exit)                     leaves the Adventure shell")
    
    print("resurrect OBJECTS               attempts to restore dead objects")
    
    print("steal OBJECT from MONSTER       obtains the object from a UNIX monster")
    
    print("throw OBJECT at daemon          feeds the object to the printer daemon")
    
    print("up                              takes the overhead passage")
    
    print("wake MONSTER                    awakens a UNIX monster")
    
    print("where (w)                       tells you where you are")
    
    print("xyzzy                           moves you to your home")
}
MAINT=chet@ins.cwru.edu
PATH=/usr/ucb:/bin:/usr/bin:/usr/local/bin:.
os.environ[''] = FILE_TO_TRANSLATE
os.system('trap 'echo Ouch!' 2 3')
#trap '' 18			# disable Berkeley job control
#ash_lk(){ echo " $1 " | fgrep " $2 " >&- 2>&-; }
def ash_lk () 
{ 
    print(" " + sys.argv[1] + " ") | os.system('fgrep -q " " + sys.argv[2] + " "> /dev/null 2>&1')
}
def ash_pr () 
{ 
    print("$*") | os.system('tr ' ' '\012'') | os.system('pr -5 -t -w75 -l ( $# + 4 ) / 5 ')
}
def ash_rm () 
{ 
    print(" " + sys.argv[1] + " ") | os.system('sed -e "s/ " + sys.argv[2] + " / /" -e 's/^ //' -e 's/ $//'')
}
# enable history, bang history expansion, and emacs editing
os.system('set -o history')
os.system('set -o histexpand')
os.system('set -o emacs')
os.chdir(os.path.expanduser('~'))
LIM=.limbo
# $HOME/$LIM contains "destroyed" objects
os.system('mkdir LIM') || { print("ash: cannot mkdir " + LIM + ": exiting")
exit(1) }
KNAP=.knapsack
# $HOME/$KNAP contains objects being "carried"
if (! -d KNAP  ):
    os.system('mkdir KNAP> /dev/null 2>&1')
    if ($? == 0  ):
        print("'You found a discarded empty knapsack.'")
    else:
        print("'You have no knapsack to carry things in.'")
        exit(1)
else:
    print("'One moment while I peek in your old knapsack...'")
kn= os.popen('echo \').read() ls -a KNAP | sed -e '/^\.$/d' -e '/^\.\.$/d'\ os.popen('').read() 
if (os.system('ask 'Welcome to the Adventure shell!  Do you need instructions?'') ):
    os.system('ash_inst')
    print("'Type a newline to continue: '")
    raw_input()
wiz=false
cha=false
prev=LIM
while (os.system(':')):
    room= os.popen('pwd').read() 
    if (room != prev  ):
        if (room == HOME  ):
            print("'You are in your own home.'")
        else:
            print("You have entered " + room + ".")
        exs=
        obs=
        hexs=
        hobs=
        f=false
        for i in [ os.popen('ls -a').read() ]:
                    
                if ( i == '.' or i == '..'):

                elif (i == '.*'):
                    if (os.path.isfile(i ) ):
                        hobs="" + hobs + " " + i + ""
                    else:
                        if (S_ISDIR(os.stat(i ).st_mode) ):
                            hexs="" + hexs + " " + i + ""
                        else:
                            f=true
                else:
                    if (os.path.isfile(i ) ):
                        obs="" + obs + " " + i + ""
                    else:
                        if (S_ISDIR(os.stat(i ).st_mode) ):
                            exs="" + exs + " " + i + ""
                        else:
                            f=true
        if ( "" + obs + ""  ):
            print("'This room contains:'")
            os.system('ash_pr obs')
        else:
            print("'The room looks empty.'")
        if ( "" + exs + ""  ):
            print("'There are exits labeled:'")
            os.system('ash_pr exs')
            print("'as well as a passage overhead.'")
        else:
            print("'There is a passage overhead.'")
        if (os.system('sh -c f') ):
            print("'There are shadowy figures in the corner.'")
        prev=room
    -e = raw_input()
    # prompt is '-advsh> '
    if ($? != 0  ):
        verb=quit
        # EOF
    
        if ( verb == 'change'):
            if ( "" + obj + ""  ):
                if (os.system('ash_lk "" + obs + " " + hobs + "" "" + obj + ""') ):
                    os.system('set -- x')
                    
                        elif ("" + sys.argv[1] + "" == 'to'):
                            if ( "" + sys.argv[2] + ""  ):
                                if (os.path.isfile(sys.argv[2] ) ):
                                    print("You must destroy " + sys.argv[2] + " first.")
                                    os.system('set --')
                                if ( "" + sys.argv[2] + ""  ):
                                    if (os.system('mv obj sys.argv[2]')
                                    # >&- 2>&- ):
                                        print("The " + obj + " shimmers and turns into " + sys.argv[2] + ".")
                                        obs= os.popen('ash_rm "" + sys.argv[2] + " " + obs + "" "" + obj + ""').read() 
                                    else:
                                        print("There is a cloud of smoke but the " + obj + " is unchanged.")
                            else:
                                print("'To what?'")
                        else:
                            print("Change " + obj + " to what?")
                else:
                    if (os.system('ash_lk "" + kn + "" "" + obj + ""') ):
                        print("'You must drop it first.'")
                    else:
                        print("I see no " + obj + " here.")
            else:
                print("'Change what?'")
        if ( "" + sys.argv[1] + "" == 'clone'):
            if ( "" + obj + ""  ):
                if (os.system('ash_lk "" + obs + " " + hobs + "" "" + obj + ""') ):
                    if (! -r obj  ):
                        print("The " + obj + " does not wish to be cloned.")
                    else:
                        os.system('set -- x')
                        
                            elif ("" + sys.argv[1] + "" == 'as'):
                                if ( "" + sys.argv[2] + ""  ):
                                    if (os.path.isfile(sys.argv[2] ) ):
                                        print("You must destroy " + sys.argv[2] + " first.")
                                    else:
                                        if (os.system('cp obj sys.argv[2]')
                                        # >&- 2>&- ):
                                            print("Poof!  When the smoke clears, you see the new " + sys.argv[2] + ".")
                                            obs="" + obs + " " + sys.argv[2] + ""
                                        else:
                                            print("'You hear a dull thud but no clone appears.'")
                                else:
                                    print("'As what?'")
                            else:
                                print("Clone " + obj + " as what?")
                else:
                    if (os.system('ash_lk "" + kn + "" "" + obj + ""') ):
                        print("'You must drop it first.'")
                    else:
                        print("I see no " + obj + " here.")
            else:
                print("'Clone what?'")
        if ( "" + sys.argv[1] + "" == 'drop'):
            if ( "" + obj + ""  ):
                for it in [obj, x]:
                                    if (os.system('ash_lk "" + kn + "" "" + it + ""') ):
                        if (-w it  ):
                            print("You must destroy " + it + " first.")
                        else:
                            if (os.system('mv HOME/KNAP/it it')
                            # >&- 2>&- ):
                                print("" + it + ": dropped.")
                                kn= os.popen('ash_rm "" + kn + "" "" + it + ""').read() 
                                obs= os.popen('echo it obs').read() 
                            else:
                                print("The " + it + " is caught in your knapsack.")
                    else:
                        print("You're not carrying the " + it + "!")
            else:
                print("'Drop what?'")
        elif ("" + sys.argv[1] + "" == 'enter' or "" + sys.argv[1] + "" == 'go'):
            if ( "" + obj + ""  ):
                if (obj != up  ):
                    if (os.system('ash_lk "" + exs + " " + hexs + "" "" + obj + ""') ):
                        if (-x obj  ):
                            if (os.chdir($obj) ):
                                print("'You squeeze through the passage.'")
                            else:
                                print("You can't go that direction.")
                        else:
                            print("'An invisible force blocks your way.'")
                    else:
                        print("'I see no such passage.'")
                else:
                    if (os.chdir(..) ):
                        print("'You struggle upwards.'")
                    else:
                        print("You can't reach that high.")
            else:
                print("'Which passage?'")
        elif ("" + sys.argv[1] + "" == 'examine'):
            if ( "" + obj + ""  ):
                if (obj == all  ):
                    obj= os.popen('echo obs exs').read() 
                    x=
                for it in [obj, x]:
                                    if (os.system('ash_lk "" + obs + " " + hobs + " " + exs + " " + hexs + "" "" + it + ""') ):
                        print("Upon close inspection of the " + it + ", you see:")
                        os.system('ls -ld it2> /dev/null')
                        if ($? != 0  ):
                            print("-- when you look directly at the " + it + ", it vanishes.")
                    else:
                        if (os.system('ash_lk "" + kn + "" "" + it + ""') ):
                            print("'You must drop it first.'")
                        else:
                            print("I see no " + it + " here.")
            else:
                print("'Examine what?'")
        elif ("" + sys.argv[1] + "" == 'feed'):
            if ( "" + obj + ""  ):
                if (os.system('ash_lk "" + obs + " " + hobs + "" "" + obj + ""') ):
                    os.system('set -- x')
                    
                        elif ("" + sys.argv[1] + "" == 'to'):
                            if ( "" + sys.argv[2] + ""  ):
                                os.system('shift')
                                if (PATH=OPATH $*< $obj 2> /dev/null ):
                                    print("The " + sys.argv[1] + " monster devours your " + obj + ".")
                                    if (os.system('rm -f obj')
                                    # >&- 2>&- ):
                                        obs= os.popen('ash_rm "" + obs + "" "" + obj + ""').read() 
                                    else:
                                        print("'But he spits it back up.'")
                                else:
                                    print("The " + sys.argv[1] + " monster holds his nose in disdain.")
                            else:
                                print("'To what?'")
                        else:
                            print("Feed " + obj + " to what?")
                else:
                    if (os.system('ash_lk "" + kn + "" "" + obj + ""') ):
                        print("'You must drop it first.'")
                    else:
                        print("I see no " + obj + " here.")
            else:
                print("'Feed what?'")
        if ( "" + sys.argv[1] + "" == 'get' or "" + sys.argv[1] + "" == 'take'):
            if ( "" + obj + ""  ):
                if (obj == all  ):
                    obj="" + obs + ""
                    x=
                for it in [obj, x]:
                                    if (os.system('ash_lk "" + obs + " " + hobs + "" "" + it + ""') ):
                        if (os.system('ash_lk "" + kn + "" "" + it + ""') ):
                            print("'You already have one.'")
                        else:
                            if (os.system('mv it HOME/KNAP/it')
                            # >&- 2>&- ):
                                print("" + it + ": taken.")
                                kn="" + it + " " + kn + ""
                                obs= os.popen('ash_rm "" + obs + "" "" + it + ""').read() 
                            else:
                                print("The " + it + " is too heavy.")
                    else:
                        print("I see no " + it + " here.")
            else:
                print("'Get what?'")
        elif ("" + sys.argv[1] + "" == 'gripe' or "" + sys.argv[1] + "" == 'bug'):
            print("'Please describe the problem and your situation at the time it failed.\nEnd the bug report with a line containing just a Ctrl-D.'")
            os.system('cat') | os.system('mail MAINT -s 'ash bug'')
            print("'Thank you!'")
        elif ("" + sys.argv[1] + "" == 'help'):
            os.system('ash_help')
        elif ("" + sys.argv[1] + "" == 'inventory' or "" + sys.argv[1] + "" == 'i'):
            if ( "" + kn + ""  ):
                print("'Your knapsack contains:'")
                os.system('ash_pr kn')
            else:
                print("'You are poverty-stricken.'")
        elif ("" + sys.argv[1] + "" == 'kill' or "" + sys.argv[1] + "" == 'destroy'):
            if ( "" + obj + ""  ):
                if (obj == all  ):
                    x=
                    if (os.system('ask "Do you really want to attempt to " + verb + " them all?"') ):
                        obj= os.popen('echo obs').read() 
                    else:
                        print("'Chicken!'")
                        obj=
                for it in [obj, x]:
                                    if (os.system('ash_lk "" + obs + " " + hobs + "" "" + it + ""') ):
                        if (os.system('mv it HOME/LIM')
                        # <&- >&- 2>&- ):
                            if (verb == kill  ):
                                print("The " + it + " cannot defend himself; he dies.")
                            else:
                                print("You have destroyed the " + it + "; it vanishes.")
                            obs= os.popen('ash_rm "" + obs + "" "" + it + ""').read() 
                        else:
                            if (verb == kill  ):
                                print("Your feeble blows are no match for the " + it + ".")
                            else:
                                print("The " + it + " is indestructible.")
                    else:
                        if (os.system('ash_lk "" + kn + "" "" + it + ""') ):
                            print("You must drop the " + it + " first.")
                            found=false
                        else:
                            print("I see no " + it + " here.")
            else:
                print("'Kill what?'")
        elif ("" + sys.argv[1] + "" == 'look' or "" + sys.argv[1] + "" == 'l'):
            obs= os.popen('echo obs hobs').read() 
            hobs=
            if ( "" + obs + ""  ):
                print("'The room contains:'")
                os.system('ash_pr obs')
            else:
                print("'The room is empty.'")
            exs= os.popen('echo exs hexs').read() 
            hexs=
            if ( "" + exs + ""  ):
                print("'There are exits plainly labeled:'")
                os.system('ash_pr exs')
                print("'and a passage directly overhead.'")
            else:
                print("'The only exit is directly overhead.'")
        elif ("" + sys.argv[1] + "" == 'magic'):
            if ("" + obj + "" == mode  ):
                if (os.system('sh -c cha') ):
                    print("'You had your chance and you blew it.'")
                else:
                    if (os.system('ask 'Are you a wizard?'') ):
                        print("'Prove it!  Say the magic word: '")
                        obj = raw_input()
                        if ("" + obj + "" == armadillo  ):
                            print("'Yes, master!!'")
                            wiz=true
                        else:
                            print("Homie says: I don't think so")
                            cha=true
                    else:
                        print("I didn't think so.")
            else:
                print("'Nice try.'")
        elif ("" + sys.argv[1] + "" == 'open' or "" + sys.argv[1] + "" == 'read'):
            if ( "" + obj + ""  ):
                if (os.system('ash_lk "" + obs + " " + hobs + "" "" + obj + ""') ):
                    if (-r obj  ):
                        if (-s obj  ):
                            print("Opening the " + obj + " reveals:")
                            os.system('CAT< $obj')
                            if ($? != 0  ):
                                print("'-- oops, you lost the contents!'")
                        else:
                            print("There is nothing inside the " + obj + ".")
                    else:
                        print("You do not have the proper tools to open the " + obj + ".")
                else:
                    if (os.system('ash_lk "" + kn + "" "" + obj + ""') ):
                        print("'You must drop it first.'")
                        found=false
                    else:
                        print("I see no " + obj + " here.")
            else:
                print("'Open what?'")
        elif ("" + sys.argv[1] + "" == 'quit' or "" + sys.argv[1] + "" == 'exit'):
            if (os.system('ask 'Do you really want to quit now?'') ):
                if ( "" + kn + ""  ):
                    print("'The contents of your knapsack will still be there next time.'")
                os.system('rm -rf HOME/LIM')
                print("'See you later!'")
                exit(0)
        elif ("" + sys.argv[1] + "" == 'resurrect'):
            if ( "" + obj + ""  ):
                for it in [obj, x]:
                                    if (os.system('ash_lk "" + obs + " " + hobs + "" "" + it + ""') ):
                        print("The " + it + " is already alive and well.")
                    else:
                        if (os.system('mv HOME/LIM/it it')
                        # <&- >&- 2>&- ):
                            print("The " + it + " staggers to his feet.")
                            obs= os.popen('echo it obs').read() 
                        else:
                            print("There are sparks but no " + it + " appears.")
            else:
                print("'Resurrect what?'")
        elif ("" + sys.argv[1] + "" == 'steal'):
            if ( "" + obj + ""  ):
                if (os.system('ash_lk "" + obs + " " + hobs + "" "" + obj + ""') ):
                    print("'There is already one here.'")
                else:
                    os.system('set -- x')
                    
                        elif ("" + sys.argv[1] + "" == 'from'):
                            if ( "" + sys.argv[2] + ""  ):
                                os.system('shift')
                                if (PATH=OPATH $*> $obj 2> /dev/null ):
                                    print("The " + sys.argv[1] + " monster drops the " + obj + ".")
                                    obs= os.popen('echo obj obs').read() 
                                else:
                                    print("The " + sys.argv[1] + " monster runs away as you approach.")
                                    os.system('rm -f obj')
                                    # >&- 2>&-
                            else:
                                print("'From what?'")
                        else:
                            print("Steal " + obj + " from what?")
            else:
                print("'Steal what?'")
        if ( "" + sys.argv[1] + "" == 'throw'):
            if ( "" + obj + ""  ):
                if (os.system('ash_lk "" + obs + " " + hobs + "" "" + obj + ""') ):
                    os.system('set -- x')
                    
                        elif ("" + sys.argv[1] + "" == 'at'):
                            
                                elif ("" + sys.argv[2] + "" == 'daemon'):
                                    if (os.system('sh -c "lpr -r " + obj + ""') ):
                                        print("The daemon catches the " + obj + ", turns it into paper,\nand leaves it in the basket.")
                                        obs= os.popen('ash_rm "" + obs + "" "" + obj + ""').read() 
                                    else:
                                        print("The daemon is nowhere to be found.")
                                else:
                                    print("'At what?'")
                        else:
                            print("Throw " + obj + " at what?")
                else:
                    if (os.system('ash_lk "" + kn + "" "" + obj + ""') ):
                        print("'It is in your knapsack.'")
                        found=false
                    else:
                        print("I see no " + obj + " here.")
            else:
                print("'Throw what?'")
        if ( "" + sys.argv[2] + "" == 'u' or "" + sys.argv[2] + "" == 'up'):
            if (os.chdir(..) ):
                print("'You pull yourself up a level.'")
            else:
                print("You can't reach that high.")
        elif ("" + sys.argv[2] + "" == 'wake'):
            if ( "" + obj + ""  ):
                print("You awaken the " + obj + " monster:")
                PATH=OPATH obj x
                print("'The monster slithers back into the darkness.'")
            else:
                print("'Wake what?'")
        elif ("" + sys.argv[2] + "" == 'w' or "" + sys.argv[2] + "" == 'where'):
            print("You are in " + room + ".")
        elif ("" + sys.argv[2] + "" == 'xyzzy'):
            if (os.chdir(os.path.expanduser('~')) ):
                print("'A strange feeling comes over you.'")
            else:
                print("'Your spell fizzles out.'")
        else:
            if ( "" + verb + ""  ):
                if (os.system('sh -c wiz') ):
                    PATH=OPATH verb obj x
                else:
                    print("I don't know how to \"verb\".")
                    print("'Type "help" for assistance.'")
            else:
                print("'Say something!'")
