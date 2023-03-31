import sys, os, os.path
from stat import *
# 1-Feb-86 09:37:35-MST,30567;000000000001
# Return-Path: <unix-sources-request@BRL.ARPA>
# Received: from BRL-TGR.ARPA by SIMTEL20.ARPA with TCP; Sat 1 Feb 86 09:36:16-MST
# Received: from usenet by TGR.BRL.ARPA id a002623; 1 Feb 86 9:33 EST
# From: chris <chris@globetek.uucp>
# Newsgroups: net.sources
# Subject: Improved Bcsh (Bourne Shell Cshell-Emulator)
# Message-ID: <219@globetek.UUCP>
# Date: 30 Jan 86 17:34:26 GMT
# To:       unix-sources@BRL-TGR.ARPA
#
# This is a new, improved version of my Bourne shell cshell-emulator.
# The code has been cleaned up quite a bit, and a couple of new features
# added (now supports 'noclobber' and 'iclobber' variables).  A bug with
# 'eval' that caused "illegal I/O" error messages on vanilla V7 shells has
# also been fixed.
# I have posted the program in its entirety because a context diff of the
# old and new versions was longer than the new version...
# --Chris
#	Bcsh -- A Simple Cshell-Like Command Pre-Processor For The Bourne Shell
#
#	"Copyright (c) Chris Robertson, December 1985"
#
#	This software may be used for any purpose provided the original
#	copyright notice and this notice are affixed thereto.  No warranties of
#	any kind whatsoever are provided with this software, and it is hereby
#	understood that the author is not liable for any damagages arising
#	from the use of this software.
#
#	Features Which the Cshell Does Not Have:
#	----------------------------------------
#
#	+  command history persists across bcsh sessions
# 	+  global last-command editing via 'g^string1^string2^' syntax
#	+  edit any command via $EDITOR or $VISUAL editors
#	+  history file name, .bcshrc file name, alias file name, and number
#	   of commands saved on termination can be set by environment variables
#	+  prompt may evaluate commands, such as `pwd`, `date`, etc.
#	+  the whole text of interactive 'for' and 'while' loops and 'if'
#	   statements goes into the history list and may be re-run or edited
#	+  multiple copies of commands and requests to see command history
#	   are not added to the history list
#	+  the history mechanism actually stores all commands entered in a
#	   current session, not just $history of them.  This means that you
#	   can increase $history on the fly and at once have a larger history.
#
#
#	Synonyms:
#	---------
#
#	logout, exit, bye	write out history file and exit
#	h, history		show current history list
#	
#	
#	Aliases:
#	--------
#
#	alias NAME CMND		create an alias called NAME to run CMND
#	unalias NAME		remove the alias NAME
#
#	There are no 'current-session only' aliases -- all alias and unalias
#	commands are permanent, and stored in the $aliasfile.
#
#	If an alias contains positional variables -- $1, $2, $*, etc. -- any
#	arguments following the alias name are considered to be values for
#	those variables, and the alias is turned into a command of the form
#	'set - arguments;alias'.  Otherwise, a simple substitution is performed
#	for the alias and the rest of the command preserved.  The cshell
#	convention of using '\!:n' in an alias to get bits of the current
#	command is mercifully abandoned.
#
#	Quotes are not necessary around the commands comprising an alias;
#	in fact, any enclosing quotes are stripped when the alias is added
#	to the file.
#
#	A couple of typical aliases might be:
#
#		goto	cd $1;pwd
#		l	ls -F
#
#	Note that aliasing something to "commands;logout" will not work -- if
#	you want something to happen routinely on logout put it in the file
#	specified by $logoutfile, default = $HOME/.blogout.
#
#
#	Command Substitutions:
#	----------------------
#
#	!!			substitute last command from history list
#	!!:N			substitute Nth element of last command from
#				history list -- 0 = command name, 1 = 1st arg
# 	!!:$			substitute last element of last command from
#				history list
# 	!!:*			substitute all arguments to last command
#				from history list
#	!NUMBER			substitute command NUMBER from the history list
#	!NUMBER:N		as above, but substitute Nth element, where
#				0 = command name, 1 = 1st arg, etc.
# 	!NUMBER:$		as above, but substitute last element
# 	!NUMBER:*		as above, but substitute all arguments
#	!-NUMBER		substitute the command NUMBER lines from the
#				end of the history list; 1 = last command
#	!-NUMBER:N		as above, but substitute Nth element, where
#				0 = command name, 1 = 1st arg, etc.
# 	!-NUMBER:$		as above, but substitute last element
# 	!-NUMBER:*		as above, but substitute all arguments
#	!?STRING		substitute most-recent command from history list
#				containing STRING -- STRING must be enclosed in
#				braces if followed by any other characters
#	!?STRING:N		as above, but substitute Nth element, where
#				0 = command name, 1 = 1st arg, etc.
# 	!?STRING:$		as above, but substitute last element	
# 	!?STRING:*		as above, but substitute all arguments
#
#
#	Command Editing:
#	----------------
#
#	CMND~e			edit CMND using $EDITOR, where CMND may be found
#				using a history substitution
#	CMND~v			edit CMND using $VISUAL, where CMND may be found
#				using a history substitution
# "	^string1^string2^	substitute string2 for string1 in last command"
#				command and run it
# "	g^string1^string2^	globally substitute string2 for string1 in  "
#				last command and run it
# 	!NUMBER:s/string1/string2/
#				substitute string2 for string1 in
#				command NUMBER and run it
# 	!NUMBER:gs/string1/string2/
#				globally substitute string2 for string1 in
#				command NUMBER and run it
# 	!?STRING:s/string1/string2/
#				substitute string2 for string1 in last command
#				containing STRING and run it
# 	!?STRING:gs/string1/string2/
#				globally substitute string2 for string1 in last
#				command containing STRING and run it
#	
#	Any command which ends in the string ":p" is treated as a normal
#	command until all substitutions have been completed.  The trailing
#	":p" is then stripped, and the command is simply echoed and added to
#	the history list instead of being executed.
#
#	None of the other colon extensions of the cshell are supported.
#
#
#	Shell Environment Variables:
#	----------------------------
#
#	EDITOR		editor used by ~e command, default = "ed"
#	VISUAL		editor used by ~v command, default = "vi"
#	MAIL		your system mailbox
#	PAGER		paging program used by history command, default = "more"
#	PS1		primary prompt
#	PS2		secondary prompt
#	history		number of commands in history list, default = 22
#	histfile	file history list is saved in, default = $HOME/.bhistory
#	savehist	number of commands remembered from last bcsh session
#	aliasfile	file of aliased commands, default = $HOME/.baliases
#	logoutfile	file of commands to be executed before termination
#	inc_cmdno	yes/no -- keep track of command numbers or not
#	noclobber	if set, existing files are not overwritten by '>'
#	iclobber	if both noclobber and iclobber are set, the user is
#			prompted for confirmation before existing files are
#			overwritten by '>'
#
#	Note:	if you are setting either noclobber or iclobber mid-session,
#		set them to 'yes'
#
#
#	Regular Shell Variables:
#	------------------------
#
#	Shell variables may be set via Bourne or cshell syntax, e.g., both
#	"set foo=bar" and "foo=bar" set a variable called "foo" with the value
#	"bar".  However, all variables are automatically set as environment
#	variables, so there is no need to export them.  Conversely, there
#	are NO local variables.  Sorry, folks.
#
#	A cshell-style "setenv" command is turned into a regular "set" command.
#
#
#	The Prompt:
#	----------
#
#	You may, if you wish, have a command executed in your prompt.  If
#	the variable PS1 contains a dollar sign or a backquote, it is
#	evaluated and the result used as the prompt, provided the evaluation
#	did not produce a "not found" error message.  The two special cases
#	of PS1 consisting solely of "$" or "$ " are handled correctly.  For
#	example, to have the prompt contain the current directory followed
#	by a space, enter:
#
#		PS1=\'echo "`pwd` "\'
#
#	You need the backslashed single quotes to prevent the command being
#	evaluated by the variable-setting mechanism and the shell before it
#	is assigned to PS1.
#
#	To include the command number in your prompt, enter the command:
#
#		PS1=\'echo "$cmdno "\'
#
#
#	Shell Control-Flow Syntax:
#	--------------------------
#
#	'While', 'for', 'case', and 'if' commands entered in Bourne shell
#	syntax are executed as normal.
#
#	A valiant attempt is made to convert 'foreach' loops into 'for' loops,
#	cshell-syntax 'while' loops into Bourne shell syntax, and 'switch'
#	statements into 'case' statements.  I cannot guarantee to always get it
#	right.  If you forget the 'do' in a 'while' or 'for' loop, or finish
#	them with 'end' instead of 'done', this will be corrected.
#
#	Note that cshell-to-Bourne control flow conversions do not take place
#	if control is nested -- e.g., a 'foreach' inside a 'while' will fail.
#
#	The simple-case cshell "if (condition) command" is turned into Bourne
#	syntax.  Other 'if' statements are left alone apart from making the
#	'then' a separate statement, because constructing a valid interactive
#	cshell 'if' statement is essentially an exercise in frustration anyway.
#	The cshell and Bourne shell have sufficiently different ideas about
#	conditions that if is probably best to resign yourself to learning
#	the Bourne shell conventions.
#
#	Note that since most of the testing built-ins of the cshell are
#	not available in the Bourne shell, a complex condition in a 'while'
#	loop or an 'if' statement will probably fail.
#	
#
#	Bugs, Caveats, etc.:
#	--------------------
#
#	This is not a super-speedy program.  Be patient, especially on startup.
#
#	To the best of my knowledge this program should work on ANY Bourne
#	shell -- note that if your shell does not understand 'echo -n' you
#	will have to re-set the values of '$n' and '$c'.
#
#	This program may run out of stack space on a 16-bit machine where
#	/bin/sh is not split-space.
#
#	Mail checking is done every 10 commands if $MAIL is set in your
#	environment.  For anything fancier, you will have to hack the code.
#
#	Because commands are stuffed in a file before sh is invoked on them,
#	error messages from failed commands are ugly.
#
#	Failed history substitutions either give nothing at all, or a
#	"not found" style of error message.
#
#	A command history is kept whether you want it or not.  This may be
#	perceived as a bug or a feature, depending on which side of bed you
#	got out on.
#
#	If you want a real backslash in a command, you will have to type two
# 	of them  because the shell swallows the first backslash in the initial
# 	command pickup.  This means that to include a non-history '!' in a
#	command you need '\\!' -- a real wart, especially for net mail,
#	but unavoidable.
#
#	Commands containing an '@' will break all sorts of things.
#
#	Very complex history substitutions may fail.
#
#	File names containing numbers may break numeric history sustitutions.
#
#	Commands containing bizzare sequences of characters may conflict
#	with internal kludges.
#
#	Aliasing something to "commands;logout" will not work -- if you
#	want something to happen routinely on logout, put it in the file
#	specified by $logoutfile, default = $HOME/.blogout.
#
#	Please send all bug reports to ihnp4!utzoo!globetek!chris.
#	Flames will be posted to net.general with 'Reply-to' set to your
# '	path...  :-)							'
#
#
#
#		************* VERY IMPORTANT NOTICE *************
#
# If your shell supports # comments, then REPLACE all the colon 'comments'
# with # comments.  If it does not, then REMOVE all the 'comment' lines from the
# working copy of the file, as it will run MUCH faster -- the shell evaluates
# lines starting with a colon but does not actually execute them, so you will
# save the read-and-evaluate time by removing them.

    if ( " os.popen('echo -n foo').read() " == '-n*'):
        n=
        c="\c"
    elif (" os.popen('echo -n foo').read() " == 'foo'):
        n=-n
        c=
    else:
        print("Your 'echo' command is broken.")
        exit(1)
history=${history-22}
savehist=${savehist-22}
histfile=${histfile-HOME/.bhistory}
logoutfile=${logoutfile-HOME/.blogout}
EDITOR=${EDITOR-ed}
VISUAL=${VISUAL-vi}
PAGER=${PAGER-more}
aliasfile=${aliasfile-HOME/.baliases}
# the alias file may contain 1 blank line, so a test -s will not work

    if ( " os.popen('cat " + aliasfile + " 2> /dev/null').read() " == '""'):
        doalias=no
    else:
        doalias=yes
if (os.system('test -s "" + $ + "{sourcefile-" + HOME + "/.bcshrc}"') ):
    os.system('. ${sourcefile-HOME/.bcshrc}')
if (os.system('test -s "" + histfile + ""') ):
    cmdno=" os.popen('set - \').read() wc -l " + histfile + "\ os.popen(';echo " + sys.argv[1] + "').read() "
    cmdno=" os.popen('expr \"cmdno\" + 1').read() "
    lastcmd=" os.popen('sed -n '" + p + "' " + histfile + "').read() "
    copy=false
    ohist=histfile
    while (os.system('test ! -w "" + histfile + ""')):
        print("Cannot write to history file '" + histfile + "'.")
        print("n "Please enter a new history filename: " + c + """)
        histfile = raw_input()
        copy=true
    if (os.system('copy') ):
        os.system('cp ohist histfile')
else:
    os.system('cat /dev/null> $histfile')
    cmdno=1
    lastcmd=
# keep track of command number as the default
inc_cmdno=${inc_cmdo-yes}
# default prompts -- PS1 and PS2 may be SET but EMPTY, so '${PS1-% }' syntax
# is not used here

    if ( "" + PS1 + "" == '""'):
        PS1="% "

    if ( "" + PS2 + "" == '""'):
        PS2="> "
os.environ[''] = FILE_TO_TRANSLATE

    if ( "" + MAIL + "" == '""'):

    else:
        if (os.path.isfile(MAIL ) ):
            mailsize= os.popen('set - \').read() wc -c MAIL\ os.popen(';echo sys.argv[1]').read() 
        else:
            mailsize=0
os.system('trap ':' 2')
os.system('trap exit 3')
os.system('trap "tail -n " + savehist + " " + histfile + ">/tmp/hist" + $ + "" + $ + ";uniq /tmp/hist" + $ + "" + $ + " > " + histfile + ";rm -f /tmp/*" + $ + "" + $ + ";exit 0" 15')
getcmd=yes
mailcheck=
exclaim=
echoit=
mailprompt=
while (os.system(':')):
    run=yes
    
        if ( "" + mailprompt + "" == '""'):

        else:
            print("" + mailprompt + "")
    
        if ( "" + getcmd + "" == 'yes'):
            os.system(': guess if the prompt should be evaluated or not')
            
                elif ("" + PS1 + "" == '\$' or "" + PS1 + "" == '\$\ '):
                    print("n "" + PS1 + "" + c + """)
                elif ("" + PS1 + "" == '*\`*' or "" + PS1 + "" == '*\$*'):
                    tmp=" os.popen('(eval " + PS1 + ") 2>&1').read() "
                    
                        elif ("" + tmp + "" == '*not\ found'):
                            print("n "" + PS1 + "" + c + """)
                        else:
                            print("n "" + tmp + "" + c + """)
                else:
                    print("n "" + PS1 + "" + c + """)
            cmd = raw_input() || cmd="exit"
        else:

    
        if ( "" + MAIL + "" == '""'):

        else:
            os.system(': check for mail every 10 commands')
            
                elif ("" + mailcheck + "" == '1111111111'):
                    mailcheck=
                    if (os.path.isfile(MAIL ) ):
                        newsize=" os.popen('set - \').read() wc -c " + MAIL + "\ os.popen(';echo " + sys.argv[1] + "').read() "
                    else:
                        newsize=0
                    if (os.system('test "" + newsize + "" > "" + mailsize + ""') ):
                        mailprompt="You have new mail"
                    else:
                        mailprompt=
                    mailsize=newsize
                else:
                    mailcheck=1mailcheck
    hist=no
    
        if ( "" + cmd + "" == '""'):
            continue
        elif ("" + cmd + "" == 'sh'):
            os.system('sh')
            run=no
        elif ("" + cmd + "" == '!!'):
            cmd=lastcmd
            echoit=yes
            getcmd=no
            continue
        elif ("" + cmd + "" == '*:p'):
            cmd=" os.popen('expr \"cmd\" : '\(.*\):p'').read()  +~+p"
            getcmd=no
            continue
        elif ("" + cmd + "" == 'foreach[\ \	]*'):
            while (os.system('test "" + line + "" != "end"')):
                print("n "" + PS2 + "" + c + """)
                line = raw_input()
                cmd="" + $ + "{cmd};" + line + ""
            print("" + cmd + "")> /tmp/bcsh$$
            os.system('ed - /tmp/bcsh$$') <<++++
		s/end/done/
		s/foreach[ 	]\(.*\)(/for \1 in /
		s/)//
		s/;/;do /
		w
++++

        elif ("" + cmd + "" == 'for[\ \	]*' or "" + cmd + "" == 'while[\ \	]*'):
            # try to catch the most common cshell-to-Bourne-shell# mistakes
            print("n "" + PS2 + "" + c + """)
            line = raw_input()
            
                elif ("" + line + "" == '*do'):
                    line="do :"
                elif ("" + line + "" == '*do*'):

                else:
                    line="do " + line + ""
            cmd="" + $ + "{cmd};" + line + ""
            while (os.system('test "" + line + "" != "done"') && os.system('test "" + line + "" != "end"')):
                print("n "" + PS2 + "" + c + """)
                line = raw_input()
                
                    if ( "" + line + "" == 'end'):
                        line=done
                cmd="" + $ + "{cmd};" + line + ""
            print("" + cmd + "")> /tmp/bcsh$$
        if ( "" + line + "" == 'if[\ \	]*'):
            while (os.system('test "" + line + "" != "fi"') && os.system('test "" + line + "" != "endif"')):
                print("n "" + PS2 + "" + c + """)
                line = raw_input()
                
                    elif ("" + line + "" == '*[a-z]*then'):
                        line=" os.popen('expr \"line\" : '\(.*\)then'').read() ;then"
                    elif ("" + line + "" == 'endif'):
                        line=fi
                cmd="" + $ + "{cmd};" + line + ""
            print("" + cmd + "")> /tmp/bcsh$$
            
                if ( " os.popen('grep then /tmp/bcsh" + $ + "" + $ + "').read() " == '""'):
                    # fix 'if foo bar' cases
                    os.system('ed - /tmp/bcsh$$') <<++++
			s/)/);then/
			s/.*/;fi/
			w
++++

        if ( " os.popen('grep then /tmp/bcsh" + $ + "" + $ + "').read() " == 'case[\ \	]*'):
            while (os.system('test "" + line + "" != "esac"')):
                print("n "" + PS2 + "" + c + """)line = raw_input()
                cmd="" + $ + "{cmd}@" + line + ""
            cmd=" os.popen('echo \"cmd\" | tr '@' ' '').read() "
            print("" + cmd + "")> /tmp/bcsh$$
        elif (" os.popen('grep then /tmp/bcsh" + $ + "" + $ + "').read() " == 'switch[\ \	]*'):
            while (os.system('test "" + line + "" != "endsw"')):
                print("n "" + PS2 + "" + c + """)
                line = raw_input()
                cmd="" + $ + "{cmd}@" + line + ""
            print("" + cmd + "")> /tmp/bcsh$$
            os.system('ed - /tmp/bcsh$$') <<'++++'
		1,$s/@/\
/g
		g/switch.*(/s//case "/
		s/)/" in/
		1,$s/case[	 ]\(.*\):$/;;\
	\1)/
		2d
		1,$s/endsw/;;\
esac/
		g/breaksw/s///
		1,$s/default.*/;;\
	*)/
		w
++++
cmd=" os.popen('cat /tmp/bcsh" + $ + "" + $ + "').read() "
        elif (" os.popen('grep then /tmp/bcsh" + $ + "" + $ + "').read() " == '*!*'):
            hist=yes
    
        if ( "" + hist + "" == 'yes'):
            # deal with genuine exclamation marks, go back and parse again
            
                elif ("" + cmd + "" == '*\>![\ \	]*' or "" + cmd + "" == '*\\!*'):
                    cmd=" os.popen('echo \"cmd\" | sed -e 's@\\!@REALEXCLAMATIONMARK@g'').read() "
                    exclaim=yes
                    getcmd=no
                    continue
            # break command into elements, parse each one
            tmp=
            for i in [cmd]:
                            # find element with !, peel off stuff up to !
                
                    if ( "" + i + "" == '!'):
                        # most likely a typo for !!, so fix it
                        front=
                        i=!!
                    elif ("" + i + "" == '!!*'):
                        front=
                        i=" os.popen('expr \"i\" : '.*\(!!.*\)'').read() "
                    elif ("" + i + "" == '*!!*'):
                        front=" os.popen('expr \"i\" : '\(.*\)!!.*'').read() "
                        i=" os.popen('expr \"i\" : '.*\(!!.*\)'').read() "
                    elif ("" + i + "" == '!*'):
                        front=
                        i=" os.popen('expr \"i\" : '.*!\(.*\)'').read() "
                    else:
                        tmp="" + tmp + "" + i + " "
                        continue
                
                    if ( "" + i + "" == '!!*'):
                        # want last command
                        rest=" os.popen('expr \"i\" : '!!\(.*\)'').read() "
                        i=lastcmd
                    elif ("" + i + "" == '-*'):
                        # we want to search back through the history list
                        
                            elif ("" + i + "" == '-'):
                                rest=" os.popen('expr \"i\" : '-\(.*\)'').read() "
                                i=lastcmd
                            elif ("" + i + "" == '-[0-9]*'):
                                wanted=" os.popen('expr \"i\" : '-\([0-9][0-9]*\).*'').read() "
                                rest=" os.popen('expr \"i\" : '-[0-9][0-9]*\(.*\)'').read() "
                                i=" os.popen('tail -n " + wanted + " " + histfile + " | sed -e "1q"').read() "
                    if ( "" + i + "" == '[0-9]*'):
                        # find which number command is wanted
                        wanted=" os.popen('expr \"i\" : '\([0-9][0-9]*\).*'').read() "
                        rest=" os.popen('expr \"i\" : '[0-9][0-9]*\(.*\)'').read() "
                        i=" os.popen('grep -n . " + histfile + " | grep \"^wanted\"').read() "
                        i=" os.popen('expr \"i\" : \"${wanted}.\(.*\)\"').read() "
                    elif ("" + i + "" == '\?*'):
                        # find which 'command-contains' match is wanted
                        
                            elif ("" + i + "" == '\?{*}*'):
                                wanted=" os.popen('expr \"i\" : '?{\(.*\)}.*'').read() "
                                rest=" os.popen('expr \"i\" : '?.*}\(.*\)'').read() "
                            elif ("" + i + "" == '\?*:*'):
                                wanted=" os.popen('expr \"i\" : '?\(.*\):.*'').read() "
                                rest=" os.popen('expr \"i\" : '?.*\(:.*\)'').read() "
                            elif ("" + i + "" == '\?*'):
                                wanted=" os.popen('expr \"i\" : '?\(.*\)'').read() "
                                rest=
                        i=" os.popen('grep \"wanted\" " + histfile + " | sed -n '" + p + "'').read() "
                    else:
                        # find which 'start-of-command' match is wanted
                        
                            if ( "" + i + "" == '{*}*'):
                                wanted=" os.popen('expr \"i\" : '{\(.*\)}.*'').read() "
                                rest=" os.popen('expr \"i\" : '.*}\(.*\)'').read() "
                            elif ("" + i + "" == '*:*'):
                                wanted=" os.popen('expr \"i\" : '\(.*\):.*'').read() "
                                rest=" os.popen('expr \"i\" : '.*\(:.*\)'').read() "
                            else:
                                wanted="" + i + ""
                                rest=
                        i=" os.popen('grep \"^wanted\" " + histfile + " | sed -n '" + p + "'').read() "
                # see if we actually found anything to substitute
                
                    if ( "" + i + "" == '""'):
                        badsub="Event not found"
                        break
                    else:
                        badsub=no
                
                    if ( "" + rest + "" == '""'):
                        tmp="" + front + "" + tmp + "" + i + " "
                        continue
                    elif ("" + rest + "" == ':[0-9]*'):
                        # find which element of $i is wanted
                        number=" os.popen('expr \"rest\" : ':\([0-9][0-9]*\).*'').read() "
                        rest=" os.popen('expr \"rest\" : ':[0-9][0-9]*\(.*\)'').read() "
                        # count through $i till we get to the
                        # right element
                        counter=0
                        for element in [i]:
                                                    
                                elif ("" + counter + "" == '$number'):
                                    break
                                else:
                                    counter=" os.popen('expr \"counter\" + 1').read() "
                                    # counter=$[ $counter + 1 ]
                        
                            if ( "" + counter + "" == '$number'):
                                badsub=no
                            else:
                                badsub="Bad command element"
                                break
                        tmp="" + tmp + "" + front + "" + element + "" + rest + " "
                        continue
                    if ( "" + counter + "" == ':\$*'):
                        # spin through $i till we hit the last element
                        rest=" os.popen('expr \"rest\" : ':\" + $ + "\(.*\)'').read() "
                        for element in [i]:
                                                    os.system(':')
                        tmp="" + tmp + "" + front + "" + element + "" + rest + " "
                        continue
                    elif ("" + counter + "" == ':\**'):
                        # we want all elements except the command itself
                        rest=" os.popen('expr \"rest\" : ':\*\(.*\)'').read() "
                        save=i
                        os.system('set - i')
                        os.system('shift')
                        
                            elif ("" + $ + "*" == '""'):
                                badsub="No arguments to command '" + save + "'"
                                break
                            else:
                                badsub=no
                        tmp="" + tmp + "" + front + "" + $ + "*" + rest + " "
                        continue
                    if ( "" + $ + "*" == ':s*' or "" + $ + "*" == ':gs*'):
                        # we are doing a substitution
                        # put / on end if needed
                        
                            elif ("" + rest + "" == ':s/*/*/*' or "" + rest + "" == ':gs/*/*/*'):

                            elif ("" + rest + "" == ':s/*/*' or "" + rest + "" == ':gs/*/*'):
                                rest="" + $ + "{rest}/"
                        # find what substitution is wanted
                        first=" os.popen('expr \"rest\" : ':*s\/\(.*\)\/.*\/.*'').read() "
                        second=" os.popen('expr \"i\" : ':*s/.*/\(.*\)/.*'').read() "
                        # see if it is a global substitution
                        
                            if ( "" + rest + "" == ':gs*'):
                                global=g
                            elif ("" + rest + "" == ':s*'):
                                global=
                        rest=" os.popen('expr \"rest\" : '.*/.*/.*/\(.*\)'').read() "
                        i=" os.popen('echo \"i\" | sed -e \"s@first@second@global\"').read() "
                        # see if subsitution worked
                        
                            if ( "" + i + "" == '""'):
                                badsub="Substiution failed"
                                break
                            else:
                                badsub=no
                        tmp="" + tmp + "" + front + "" + i + "" + rest + " "
                        continue
                    else:
                        tmp="" + tmp + "" + front + "" + i + "" + rest + " "
            
                if ( "" + badsub + "" == 'no'):

                else:
                    print("" + badsub + "")
                    badsub=no
                    continue
            cmd="" + tmp + ""
            echoit=yes
            getcmd=no
            continue
        else:
            run=yes
    
        if ( "" + cmd + "" == '*\^*\^*\^*'):
            # see if the substitution is global
            
                elif ("" + cmd + "" == 'g*'):
                    global=g
                else:
                    global=
            # put a '^' on the end if necessary
            
                if ( "" + cmd + "" == '*\^'):

                else:
                    cmd="" + $ + "{cmd}^"
            # find what substitution is wanted
            first=" os.popen('expr \"cmd\" : '*\^\(.*\)\^.*\^.*'').read() "
            second=" os.popen('expr \"cmd\" : '*\^.*\^\(.*\)\^.*'').read() "
            rest=" os.popen('expr \"cmd\" : '*\^.*\^.*\^\(.*\)'').read() "
            cmd=" os.popen('echo \"lastcmd\" | sed -e \"s@first@second@global\"').read() " + rest + ""
            # see if the substitution worked
            
                if ( "" + cmd + "" == '""'):
                    print("Substitution failed")
                    continue
            echoit=yes
            getcmd=no
            continue
        if ( "" + cmd + "" == '*~e'):
            print("" + cmd + "") | os.system('sed -e "s@~e@@"> /tmp/bcsh$$')
            os.system('EDITOR /tmp/bcsh$$')
            cmd=" os.popen('cat /tmp/bcsh" + $ + "" + $ + "').read() "
            getcmd=no
            continue
        elif ("" + cmd + "" == '*~v'):
            print("" + cmd + "") | os.system('sed -e "s@~v@@"> /tmp/bcsh$$')
            print("" + lastcmd + "")> /tmp/bcsh$$
            os.system('VISUAL /tmp/bcsh$$')
            cmd=" os.popen('cat /tmp/bcsh" + $ + "" + $ + "').read() "
            getcmd=no
            continue
        elif ("" + cmd + "" == 'exec[\ \	]*'):
            os.system('tail -n savehist histfile> /tmp/hist$$')
            os.system('uniq /tmp/hist$$> $histfile')
            os.system('rm -f /tmp/*$$')
            print("cmd")> /tmp/cmd$$
            os.system('. /tmp/cmd$$')
        elif ("" + cmd + "" == 'login[\ \	]*' or "" + cmd + "" == 'newgrp[\ \	]*'):
            os.system('tail -n savehist histfile> /tmp/hist$$')
            os.system('uniq /tmp/hist$$> $histfile')
            os.system('rm -f /tmp/*$$')
            print("cmd")> /tmp/cmd$$
            os.system('. /tmp/cmd$$')
        elif ("" + cmd + "" == 'logout' or "" + cmd + "" == 'exit' or "" + cmd + "" == 'bye'):
            if (os.system('test -s "" + logoutfile + ""') ):
                # sh $logoutfile
                os.system('SHELL logoutfile')
            os.system('tail -n savehist histfile> /tmp/hist$$')
            os.system('uniq /tmp/hist$$> $histfile')
            os.system('rm -f /tmp/*$$')
            exit(0)
        elif ("" + cmd + "" == 'h' or "" + cmd + "" == 'history'):
            os.system('grep -n . histfile') | os.system('tail -n history') | os.system('sed -e 's@:@	@'') | os.system('PAGER')
            continue
        elif ("" + cmd + "" == 'h[\ \	]\|*' or "" + cmd + "" == 'h[\ \	]\>*' or "" + cmd + "" == 'h\|*' or "" + cmd + "" == 'h\>*'):
            cmd=" os.popen('echo \"cmd\" | sed -e \"s@h@grep -n . histfile | tail -n history | sed -e 's@:@	@'@\"').read() "
            getcmd=no
            continue
        elif ("" + cmd + "" == 'history[\ \	]*\|*' or "" + cmd + "" == 'history[\ \	]*\>*'):
            cmd=" os.popen('echo \"cmd\" | sed -e \"s@history@grep -n . histfile | tail -n history | sed -e 's@:@ @'@\"').read() "
            getcmd=no
            continue
        elif ("" + cmd + "" == 'source[\ \	]*'):
            os.system('set - cmd')
            os.system('shift')
            print(". $*")> /tmp/cmd$$
            os.system('. /tmp/cmd$$')
            run=no
        elif ("" + cmd + "" == 'wait'):
            os.system('wait')
            run=no
        elif ("" + cmd + "" == '.[\ \	]*'):
            print("cmd")> /tmp/cmd$$
            os.system('. /tmp/cmd$$')
            run=no
        elif ("" + cmd + "" == 'cd' or "" + cmd + "" == 'cd[\ \	]*'):
            # check if it will work first, or else this shell will terminate
            # if the cd dies.  If you have a built-in test, you might want
            # to replace the try-it-and-see below with a couple of tests,
            # but it is probably just as fast like this.
            print("cmd")> /tmp/cmd$$
            if (( os.system('SHELL /tmp/cmd$$') ) ):
                os.system('. /tmp/cmd$$')
            run=no
        elif ("" + cmd + "" == 'awk[\ \	]*' or "" + cmd + "" == 'dd[\ \	]*' or "" + cmd + "" == 'cc[\ \	]*' or "" + cmd + "" == 'make[\ \	]*'):
            # these are the only commands I can think of whose syntax
            # includes an equals sign.  Add others as you find them.
            print("" + cmd + "")> /tmp/bcsh$$
        elif ("" + cmd + "" == 'setenv*' or "" + cmd + "" == '*=*'):
            # handle setting shell variables, turning cshell syntax to Bourne
            # syntax -- note all variables must be exported or they will not
            # be usable in other commands
            print("" + cmd + "")> /tmp/cmd$$
            os.system('ed - /tmp/cmd$$') <<++++
		g/^setenv[ 	]/s/[ 	]/@/
		g/^setenv@/s/[ 	]/=/
		g/^setenv@/s///
		g/^set/s///
		.t.
		\$s/=.*//
		s/^/export /
		w
++++
os.system('. /tmp/cmd$$')
            os.system('rm -f /tmp/cmd$$')
            run=no
        elif ("" + cmd + "" == 'unset[\ \	]*' or "" + cmd + "" == 'umask[\ \	]*' or "" + cmd + "" == 'export[\ \	]*' or "" + cmd + "" == 'set[\ \	]*'):
            # handle commands which twiddle current environment
            os.system('cmd')
            run=no
        elif ("" + cmd + "" == 'alias' or "" + cmd + "" == 'alias[\ \	]'):
            if (os.path.isfile(aliasfile ) ):
                os.system('PAGER aliasfile')
            lastcmd=cmd
            run=no
            continue
        elif ("" + cmd + "" == 'alias[\ \	]*'):
            
                elif ("" + cmd + "" == 'alias[\ \	]\|*' or "" + cmd + "" == 'alias[\ \	]\>*'):
                    cmd=" os.popen('echo \"cmd\" | sed -e \"s@alias@cat aliasfile@\"').read() "
                    getcmd=no
                    continue
                elif ("" + cmd + "" == 'alias[\ \	]*[\ \	]*'):

                else:
                    print("Syntax: alias name command")
                    cmd=
                    continue
            os.system('set - cmd')
            os.system('shift')
            cmd="" + $ + "*"
            # make sure there is always 1 blank line in file so
            # unaliasing will always work -- ed normally refuses
            # to write an empty file
            print("")>> $aliasfile
            os.system('cat >> $aliasfile') <<++++
$cmd
++++
#		ed - $aliasfile << '++++'
            #		g/alias[ 	]/s///
            #		g/^['"]\(.*\)['"]$/s//\1/
            #		g/^/s//alias	/
            #		w
            #++++
            os.system('sort -u -o aliasfile aliasfile')
            doalias=yes
            cmd="alias " + cmd + ""
            run=no
        if ( "" + cmd + "" == 'unalias[\ \	]*'):
            os.system('set - cmd')
            
                elif (len(sys.argv) == '2'):
                    cmd=sys.argv[2]
                else:
                    print("Syntax: unalias alias_name")
                    continue
            os.system('ed - aliasfile') <<++++
		/^$cmd[ 	]/d
		w
++++

                if ( " os.popen('set - \').read() wc -l " + aliasfile + "\ os.popen(';echo " + sys.argv[1] + "').read() " == '1'):
                    # just removed last alias
                    doalias=no
            run=no
        else:
            
                if ( "" + doalias + "" == 'yes'):
                    os.system('set - cmd')
                    tmp=" os.popen('grep \"^sys.argv[1] \" " + aliasfile + "').read() "
                    
                        elif ("" + tmp + "" == '$1[\ \	]*'):
                            os.system('shift')
                            cmd=$*
                            os.system('set - tmp')
                            os.system('shift')
                            tmp=$*
                            
                                elif ("" + tmp + "" == '*\$*'):
                                    # uses positional variables
                                    cmd="set - " + cmd + " ; " + tmp + ""
                                    getcmd=no
                                    continue
                                else:
                                    cmd="" + tmp + " " + cmd + ""
                                    getcmd=no
                                    continue
                        else:
                            print("" + cmd + "")> /tmp/bcsh$$
                if ( "" + tmp + "" == 'no'):
                    print("" + cmd + "")> /tmp/bcsh$$
    
        if ( "" + cmd + "" == '*+~+p'):
            cmd=" os.popen('expr \"cmd\" : '\(.*\)+~+p'').read() "
            echoit=yes
            run=no
    
        if ( "" + cmd + "" == '""'):
            continue
        else:
            
                elif ("" + exclaim + "" == 'yes'):
                    cmd=" os.popen('echo \"cmd\" | sed -e 's@REALEXCLAMATIONMARK@!@g'').read() "
                    print("" + cmd + "")> /tmp/bcsh$$
            
                if ( "" + echoit + "" == 'yes'):
                    print("cmd")
            
                if ( "" + run + "" == 'yes'):
                    
                        elif ("" + $ + "{noclobber+yes}" == 'yes'):
                            
                                elif ("" + cmd + "" == '*\>![\ \	]*'):
                                    os.system('ed - /tmp/bcsh$$') <<++++
					g/>!/s//>/
					w
++++

                                elif ("" + cmd + "" == '*\>\>*'):

                                elif ("" + cmd + "" == '*\>*'):
                                    outfile=" os.popen('expr \"cmd\" : '.*>\(.*\)'').read() "
                                        elif ("" + outfile + "" == '\&*'):

                                        else:
                                            os.system('set - outfile')
                                            outfile="" + sys.argv[1] + ""
                                            if (os.system('test -s "" + outfile + ""') ):
                                                
                                                    elif ("" + $ + "{iclobber+yes}" == 'yes'):
                                                        print("n "Overwrite " + $ + "{outfile}? " + c + """)
                                                        answer = raw_input()
                                                        
                                                            elif ("" + answer + "" == 'y*'):

                                                            else:
                                                                print("':'")> /tmp/bcsh$$
                                                    else:
                                                        print("" + $ + "{outfile}: file exists")
                                                        print("':'")> /tmp/bcsh$$
                        else:
                            
                                if ( "" + cmd + "" == '*\>![\ \	]*'):
                                    os.system('ed - /tmp/bcsh$$') <<++++
					g/>!/s//>/g
					w
++++
( os.system('trap 'exit 1' 2 3')
                    os.system('BASH /tmp/bcsh$$') )
            
                if ( "" + cmd + "" == '$lastcmd'):

                else:
                    
                        elif ("" + exclaim + "" == 'yes'):
                            cmd=" os.popen('echo \"cmd\" | sed -e 's@!@\\\\!@g'').read() "
                    os.system('cat >> $histfile') <<++++
$cmd
++++
lastcmd=cmd
                    
                        if ( "" + inc_cmdno + "" == 'yes'):
                            cmdno=" os.popen('expr \"cmdno\" + 1').read() "
                            # cmdno=$[$cmdno + 1]
    # The next commented-out line sets the prompt to include the command
    # number -- you should only un-comment this if it is the ONLY thing
    # you ever want as your prompt, because it will override attempts
    # to set PS1 from the command level.  If you want the command number
    # in your prompt without sacrificing the ability to change the prompt
    # later, replace the default setting for PS1 before the beginning of
    # the main loop with the following:  PS1='echo -n "${cmdno}% "'
    # Doing it this way is, however, slower than the simple version below.
    PS1="" + $ + "{cmdno}% "
    getcmd=yes
    echoit=no
    exclaim=no
exit(0)
# Christine Robertson  {linus, ihnp4, decvax}!utzoo!globetek!chris
