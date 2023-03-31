import sys, os, os.path
from stat import *
#
# @(#) ren 2.1.1 2002-03-17
# 1990-06-01 John H. DuBois III (john@armory.com)
# 1991-02-25 Improved help info
# 1992-06-07 Remove quotes from around shell pattern as required by new ksh
# 1994-05-10 Exit if no globbing chars given.
# 1995-01-23 Allow filename set to be given on command line.
# 1997-09-24 1.4 Let [] be used for globbing.  Added x option.
# 1997-11-26 1.4.1 Notice if the sequences of globbing chars aren't the same.
# 1999-05-13 Changed name to ren to avoid conflict with /etc/rename
# 2000-01-01 1.4.2 Let input patterns that contain whitespace be used.
# 2001-02-14 1.5 Better test for whether old & new globbing seqs are identical.
# 2001-02-20 1.6 Added pP options.
# 2001-02-27 1.7 Added qf options.  Improved interpretation of rename patterns.
# 2001-05-10 1.8 Allow multiple pP options.  Added Qr options.
# 2001-07-25 2.0 Added mz options.
# 2001-11-25 2.1 Allow segment ranges to be given with -m.  Work under ksh93.
# 2002-03-17 2.1.1 Fixed bug in test for legal expressions.
# todo: It would be nice to be able to escape metacharacters with '\'
# todo: Should enhance patterns to make ] in a pair of brackets work ([]])
# todo: Allow use of all ksh globbing patterns.
# todo: Allow use of extended regexps, with () to enumerate pieces and \num to
# todo: select them.
#
# Modifications for bash made by Chet Ramey <chet@po.cwru.edu>
name=${0##*/}
Usage="Usage:

tell=false
verbose=false
warn=true
warnNoFiles=true
debug=false
recurse=false
inclPat=
exclPat=
os.system('declare -i inclCt=0 exclCt=0')
check=true
os.system('declare -i j op_end_seg')
# Begin bash additions
os.system('shopt -s extglob')
#
# ksh print emulation
#
#	print [-Rnprsu[n]] [-f format] [arg ...]
#
#	-	end of options
#	-R	BSD-style -- only accept -n, no escapes
#	-n	do not add trailing newline
#	-p	no-op (no coprocesses)
#	-r	no escapes
#	-s	print to the history file
#	-u n	redirect output to fd n
#	-f format	printf "$format" "$@"
#
def print () 
{ 
    os.system('local eflag=-e')
    
    os.system('local nflag= fflag= c')
    
    os.system('local fd=1')
    
    OPTIND=1
    
    while (os.system('getopts "fRnprsu:" c')):
        
            if ( c == 'R'):
                eflag=
            elif (c == 'r'):
                eflag=
            elif (c == 'n'):
                nflag=-n
            elif (c == 's'):
                sflag=y
            elif (c == 'f'):
                fflag=y
            elif (c == 'u'):
                fd=OPTARG
            elif (c == 'p'):

    
    os.system('shift ( OPTIND - 1 )')
    
    if (-n "" + fflag + ""  ):
        os.system('builtin printf "" + $ + "@"&>$fd')
        
        os.system('return')
    
    
        if ( "" + sflag + "" == 'y'):
            os.system('builtin history -s "" + $ + "*"')
        else:
            os.system('builtin print eflag nflag "" + $ + "@"&>$fd')
}
# End bash additions
while (os.system('getopts :htvxp:P:fqQrm:z: opt')):
    
        if ( opt == 'h'):
            os.system('print -r -- "" + name + ": rename files by changing parts of filenames that match a pattern.
')
            exit(0)
        elif (opt == 'f'):
            check=false
        elif (opt == 'q'):
            warn=false
        elif (opt == 'Q'):
            warnNoFiles=false
        elif (opt == 'r'):
            warnNoFiles=false
            recurse=true
        elif (opt == 't'):
            tell=true
        elif (opt == 'v'):
            verbose=true
        elif (opt == 'x'):
            verbose=true
            debug=true
        elif (opt == 'p'):
            inclPats[inclCt]=OPTARG
            ((inclCt+=1))
        elif (opt == 'P'):
            exclPats[exclCt]=OPTARG
            ((exclCt+=1))
        elif (opt == 'm'):
            # Store operation for each segment number in ops[num]
            # Store ending segment number in op_end_seg[num]
            range=${OPTARG%%=*}
            op=${OPTARG#*=}
            start=${range%%:*}
            end=${range#*:}
            if ("$start" != +([0-9]) or "$start" -eq 0 ):
                os.system('print -ru2 -- "" + name + ": Bad starting segment number given with -m: " + start + ""')
                exit(1)
            if ("$end" != +([0-9]) or "$end" -eq 0 ):
                os.system('print -ru2 -- "" + name + ": Bad ending segment number given with -m: " + end + ""')
                exit(1)
            if (start -gt end ):
                os.system('print -ru2 -- "" + name + ": Ending segment (" + end + ") is less than starting segment (" + start + ")"')
                exit(1)
            if ("$op" != @(|*[!_a-zA-Z0-9])i@(|[!_a-zA-Z0-9]*) ):
                os.system('print -ru2 -- "" + name + ": Operation given with -m does not reference 'i': " + op + ""')
                exit(1)
            # Test whether operation is legal.  let returns 1 both for error
            # indication and when last expression evaluates to 0, so evaluate 1
            # after test expression.
            i=1
            "" + op + "" 12> /dev/null || { os.system('print -ru2 -- "" + name + ": Bad operation given with -m: " + op + ""')
            exit(1) }
            ops[start]=op
            op_end_seg[start]=end
        elif (opt == 'z'):
            if ("$OPTARG" != +([0-9]) or "$OPTARG" -eq 0 ):
                os.system('print -ru2 -- "" + name + ": Bad length given with -z: " + OPTARG + ""')
                exit(1)
            os.system('typeset -ZOPTARG j') || exit(1)
        elif (opt == '+?'):
            # no way to tell getopts to not treat +x as an option
            os.system('print -r -u2 "" + name + ": Do not prefix options with '+'."')
            exit(1)
        elif (opt == ':'):
            os.system('print -r -u2 "" + name + ": Option -" + OPTARG + " requires a value.
')
            exit(1)
        elif (opt == '\?'):
            os.system('print -r -u2 "" + name + ": -" + OPTARG + ": no such option.
')
            exit(1)
# remove args that were options
OPTIND=OPTIND-1
os.system('shift OPTIND')
oldpat=sys.argv[1]
newpat=sys.argv[2]
# If -m is given, a non-existant or null newpat should be set to oldpat
if (${#ops[*]} > 0  ):
    
        if ( $# == '0'):

        elif ($# == '1'):
            os.system('set -- "" + oldpat + "" "" + oldpat + ""')
            newpat=oldpat
            os.system('debug') && os.system('print -ru2 -- "Set new pattern to: " + newpat + ""')
        else:
            if (-z "" + newpat + ""  ):
                os.system('shift 2')
                os.system('set -- "" + oldpat + "" "" + oldpat + "" "" + $ + "@"')
                newpat=oldpat
                os.system('debug') && os.system('print -ru2 -- "Set new pattern to: " + newpat + ""')
# Make sure input patterns that contain whitespace can be expanded properly
IFS=
origPat=oldpat
# Generate list of filenames to act on.

    if ( $# == '[01]'):
        os.system('print -u2 "" + Usage + "\nUse -h for help."')
        exit(1)
    elif ($# == '2'):
        if (os.system('recurse') ):
            os.system('print -r -u2 "" + name + ": No directory names given with -r.  Use -h for help."')
            exit(1)
        os.system('set -- oldpat')
        # Get list of all filenames that match 1st globbing pattern.
        if (! -a $1 ):
            os.system('warnNoFiles') && os.system('print -r -- "" + name + ": No filenames match this pattern: " + oldpat + ""')
            exit()
    else:
        os.system('shift 2')
os.system('integer patSegNum=1 numPatSegs')
# For old ksh
# while [[ "$oldpat" = *'[\*\?]'* ]]; do
# Example oldpat: foo*.a
# Example newpat: bar*.b
# Build list of non-pattern segments and globbing segments found in arguments.
# Note the patterns given are used to get the list of filenames to act on,
# to delimit constant segments, and to determine which parts of filenames are
# to be replaced.
# Examples given for first iteration (in the example, the only iteration)
# The || newpat  is to ensure that new pattern does not have more globbing
# segments than old pattern
while ("$oldpat" = *@([\*\?]|\[+([!\]])\])* or "$newpat" = *@([\*\?]|\[+([!\]])\])*):
    ## Get leftmost globbing pattern in oldpat
    # Make r be oldpat with smallest left piece that includes a globbing
    # pattern removed from it
    r=${oldpat#*@([\*\?]|\[+([!\]])\])}
    # r=.a
    # Make pat be oldpat with the above removed from it, leaving smallest
    # left piece that includes a globbing pattern
    pat=${oldpat%%"" + r + ""}
    # pat=foo*
    # Make l be pat with the globbing pattern removed from the right,
    # leaving a constant string
    l=${pat%@([\*\?]|\[+([!\]])\])}
    # l=foo
    # Remove the constant part of pat from the left, leaving the globbing
    # pattern
    pat=${pat#"" + l + ""}
    # pat=*
    # Do the same thing for newpat, solely to provide a reliable test that
    # both oldpat & newpat contain exactly the same sequence of globbing
    # patterns.
    r=${newpat#*@([\*\?]|\[+([!\]])\])}
    # r=.b
    npat=${newpat%%"" + r + ""}
    # pat=bar*
    l=${npat%@([\*\?]|\[+([!\]])\])}
    # l=bar
    npat=${npat#"" + l + ""}
    # npat=*
    if ("$pat" != "$npat" ):
        os.system('print -ru2 -- "" + name + ": Old-pattern and new-pattern do not have the same sequence of globbing chars.
')
        exit(1)
    ## Find parts before & after pattern
    # oldpre[] stores the old constant part before the pattern,
    # so that it can be removed and replaced with the new constant part.
    oldpre[patSegNum]=${oldpat%%"" + pat + ""*}
    # oldpre[1]=foo
    # oldsuf stores the part that follows the globbing pattern,
    # so that it too can be removed.
    # After oldpre[] & oldsuf[] have been removed from a filename, what remains
    # is the part matched by the globbing pattern, which is to be retained.
    oldsuf[patSegNum]=${oldpat#*"" + pat + ""}
    # oldsuf[1]=.a
    # newpre[] stores the new constant part before the pattern,
    # so that it can be used to replace the old constant part.
    newpre[patSegNum]=${newpat%%"" + pat + ""*}
    # newpre[1]=bar
    # Get rid of processed part of patterns
    oldpat=${oldpat#${oldpre[patSegNum]}"" + pat + ""}
    # oldpat=.a
    newpat=${newpat#${newpre[patSegNum]}"" + pat + ""}
    # newpat=.b
    # Store either * or ? in pats[], depending on whether this segment matches 1
    # or any number of characters.
    "$pat" = \[* && pat=?
    pats[patSegNum]=pat
    ((patSegNum+=1))
if (patSegNum == 1  ):
    os.system('print -u2 "No globbing chars in pattern."')
    exit(1)
oldpre[patSegNum]=${oldpat%%"" + pat + ""*}
# oldpre[2]=.a
oldsuf[patSegNum]=${oldpat#*"" + pat + ""}
# oldsuf[2]=.a
newpre[patSegNum]=${newpat%%"" + pat + ""*}
# newpre[2]=.b
numPatSegs=patSegNum
if (os.system('debug') ):
    patSegNum=1
    while (patSegNum -le numPatSegs):
        os.system('print -ru2 -- "Old prefix: <" + $ + "{oldpre[patSegNum]}>   Old suffix: <" + $ + "{oldsuf[patSegNum]}>   New prefix: <" + $ + "{newpre[patSegNum]}>   Pattern: <" + $ + "{pats[patSegNum]}>"')
        ((patSegNum+=1))
# Example filename: foox.a
# Example oldpat: foo*.a
# Example newpat: bar*.b
os.system('integer numFiles=0')
# Usage: renameFile filename [dirname]
# [dirname] is a directory name to prefix filenames with when they are printed
# for informational purposes.
# Uses globals:
#     inclCt exclCt inclPats[] exclPats[] ops[]
#     numPatSegs oldpre[] oldsuf[] newpre[] pats[]
#     check warn tell verbose name
# Modifies globals: numFiles
def renameFile () 
{ 
    os.system('typeset file=sys.argv[1] subdir=sys.argv[2]')
    
    os.system('integer patSegNum patnum')
    
    os.system('typeset origname porigname newfile matchtext pnewfile matchsegs')
    
    os.system('integer startseg endseg')
    
    origname=file
    
    # origname=foox.a
    
    porigname=subdirfile
    
    # Unfortunately, ksh88 does not do a good job of allowing for patterns
    
    # stored in variables.  Without the conditional expression being eval'ed,
    
    # only sh patterns are recognized.  If the expression is eval'ed, full
    
    # ksh expressions can be used, but then expressions that contain whitespace
    
    # break unless the user passed a pattern with the whitespace properly
    
    # quoted, which is not intuititive.  This is fixed in ksh93; full patterns
    
    # work without being eval'ed.
    
    if (inclCt > 0  ):
        patnum=0
        
        while (patnum < inclCt ):
            "$file" = ${inclPats[patnum]} && break
            
            ((patnum+=1))
        
        if (patnum == inclCt  ):
            os.system('debug') && os.system('print -ru2 -- "Skipping not-included filename '" + porigname + "'"')
            
            os.system('return 1')
    
    patnum=0
    
    while (patnum < exclCt ):
        if ("$file" = ${exclPats[patnum]} ):
            os.system('debug') && os.system('print -ru2 -- "Skipping excluded filename '" + porigname + "'"')
            
            os.system('return 1')
        
        ((patnum+=1))
    
    # Extract matching segments from filename
    
    ((numFiles+=1))
    
    patSegNum=1
    
    while (patSegNum -le numPatSegs):
        # Remove a fixed prefix		iteration:	1		2
        
        file=${file#${oldpre[patSegNum]}}
        
        # file=x.a	file=
        
        # Save the part of this suffix that is to be retained.  To do this, we
        
        # need to know what part of the suffix matched the current globbing
        
        # segment.  If the globbing segment is a *, this is done by removing
        
        # the minimum part of the suffix that matches oldsuf (since * matches
        
        # the longest segment possible).  If the globbing segment is ? or []
        
        # (the latter has already been coverted to ?), it is done by taking the
        
        # next character.
        
        if ("" + $ + "{pats[patSegNum]}" == \?  ):
            matchtext=${file#?}
            
            matchtext=${file%matchtext}
        else:
            matchtext=${file%${oldsuf[patSegNum]}}
            
            # matchtext=x	matchtext=
        
        os.system('debug') && os.system('print -ru2 -- "Matching segment " + patSegNum + ": " + matchtext + ""')
        
        file=${file#matchtext}
        
        # file=.a	file=.a
        
        matchsegs[patSegNum]=matchtext
        
        ((patSegNum+=1))
    
    # Paste fixed and matching segments together to form new filename.
    
    patSegNum=0
    
    newfile=
    
    while (patSegNum -le numPatSegs):
        matchtext=${matchsegs[patSegNum]}
        
        startseg=patSegNum
        
        if (-n "" + $ + "{ops[startseg]}"  ):
            endseg=${op_end_seg[startseg]}
            
            while (patSegNum < endseg ):
                ((patSegNum+=1))
                
                matchtext=matchtext${matchsegs[patSegNum]}
            
            if ("$matchtext" != +([-0-9]) ):
                os.system('print -ru2 -- "Segment(s) " + startseg + " - " + endseg + " (" + matchtext + ") of file '" + porigname + "' do not form an integer; skipping this file."')
                
                os.system('return 2')
            
            i=matchtext
            
            "j=" + $ + "{ops[startseg]}" || { 
                os.system('print -ru2 -- "Operation failed on segment(s) " + startseg + " - " + endseg + " (" + matchtext + ") of file '" + file + "'; skipping this file."')
                
                os.system('return 2')
            }
            
            os.system('debug') && os.system('print -ru2 -- "Converted " + matchtext + " to " + j + ""')
            
            matchtext=j
        
        newfile=newfile${newpre[startseg]}matchtext
        
        # newfile=barx	newfile=barx.b
        
        ((patSegNum+=1))
    
    pnewfile=subdirnewfile
    
    if (os.system('check') && os.path.isfile("" + newfile + "" ) ):
        os.system('warn') && os.system('print -ru2 -- "" + name + ": Not renaming \"porigname\"; destination filename \"pnewfile\" already exists."')
        
        os.system('return 2')
    
    if (os.system('tell') ):
        os.system('print -n -r -- "Would move: " + porigname + " -> " + pnewfile + ""')
        
        os.system('warn') && os.path.isfile("" + newfile + "" ) && os.system('print -n -r " (destination filename already exists; would replace it)"')
        
        os.system('print ""')
    else:
        if (os.system('verbose') ):
            os.system('print -n -r -- "Moving: " + porigname + " -> " + pnewfile + ""')
            
            os.system('warn') && os.path.isfile("" + newfile + "" ) && os.system('print -n -r -- " (replacing old destination filename \"pnewfile\")"')
            
            os.system('print ""')
        else:
            if (os.system('warn') && os.path.isfile("" + newfile + "" ) ):
                os.system('print -r -- "" + name + ": Note: Replacing old file \"pnewfile\""')
        
        os.system('mv -f -- "" + origname + "" "" + newfile + ""')
}
if (os.system('recurse') ):
    oPWD=PWD
    os.system('find "" + $ + "@" -depth -type d ! -name '*
 -print') | while (dir = raw_input()):
        os.chdir(--)
        if (os.chdir(--) ):
            for file in [origPat]:
                            os.system('renameFile "" + file + "" "" + dir + "/"')
        else:
            os.system('print -ru2 -- "" + name + ": Could not access directory '" + dir + "' - skipped."')
else:
    for file in ["" + $ + "@"]:
            os.system('renameFile "" + file + ""')
if (numFiles == 0  ):
    os.system('warnNoFiles') && os.system('print -ru2 -- "" + name + ": All filenames were excluded by patterns given with -p or -P."')
