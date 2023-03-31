#! /usr/bin/env python
import sys,os,subprocess
from stat import *
# Bashmarks is a simple set of bash functions that allows you to bookmark
# folders in the command-line.
#
# To install, put bashmarks.sh somewhere such as ~/bin, then source it
# in your .bashrc file (or other bash startup file):
#   source ~/bin/bashmarks.sh
#
# To bookmark a folder, simply go to that folder, then bookmark it like so:
#   bookmark foo
#
# The bookmark will be named "foo"
#
# When you want to get back to that folder use:
#   go foo
#
# To see a list of bookmarks:
#   bookmarksshow
#
# Tab completion works, to go to the shoobie bookmark:
#   go sho[tab]
#
# Your bookmarks are stored in the ~/.bookmarks file
bookmarks_file=os.path.expanduser("~/.bookmarks")
# Create bookmarks_file it if it doesn't exist
if (! (os.path.isfile(bookmarks_file) and S_ISREG(os.stat(bookmarks_file).st_mode)) ):
    _rc = subprocess.call(["touch",str(bookmarks_file)])
def bookmark () :
    global bookmark_name
    global bookmark
    global bookmarks_file
    global replace

    bookmark_name=str(sys.argv[1])
    if (('bookmark_name' not in globals()) ):
        print(r'Invalid name, please provide a name for your bookmark. For example:')
        print(r'  bookmark foo')
    else:
        bookmark=os.popen("pwd").read()+"|"+str(bookmark_name)
        # Store the bookmark as folder|name
        if (('os.popen("grep \"|"+bookmark_name+"\" "+bookmarks_file).read()' not in globals()) ):
            print(str(bookmark))
            print("Bookmark '"+str(bookmark_name)+"' saved")
        else:
            print("Bookmark '"+str(bookmark_name)+"' already exists. Replace it? (y or n)")
            while (replace = raw_input()):
                if (replace == "y" ):
                    # Delete existing bookmark
                    _rc = subprocess.Popen("sed" + " " + "/.*|"+str(bookmark_name)+"/d" + " " + str(bookmarks_file),shell=True,stdout=file('~/.tmp','wb'))
                     and _rc = subprocess.call(["mv",os.path.expanduser("~/.tmp"),str(bookmarks_file)])
                    # Save new bookmark
                    print(str(bookmark))
                    print("Bookmark '"+str(bookmark_name)+"' saved")
                    break
                elif (replace == "n" ):
                    break
                else:
                    print("Please type 'y' or 'n'")

# Delete the named bookmark from the list
def bookmarkdelete () :
    global bookmark_name
    global bookmark
    global 
    global bookmarks_file

    bookmark_name=str(sys.argv[1])
    if (('bookmark_name' not in globals()) ):
        print(r'Invalid name, please provide the name of the bookmark to delete.')
    else:
        bookmark=os.popen("grep \"|"+str(bookmark_name)+str()+"\" \""+str(bookmarks_file)+"\"").read()
        if (('bookmark' not in globals()) ):
            print(r'Invalid name, please provide a valid bookmark name.')
        else:
            _rc = subprocess.call(["cat",str(bookmarks_file)]) | _rc = subprocess.Popen("grep" + " " + "-v" + " " + "|"+str(bookmark_name)+""+str() + " " + str(bookmarks_file),shell=True,stdout=file('bookmarks_temp','wb'))
             and _rc = subprocess.call(["mv","bookmarks_temp",str(bookmarks_file)])
            print("Bookmark '"+str(bookmark_name)+"' deleted")

# Show a list of the bookmarks
def bookmarksshow () :
    global bookmarks_file
    global FS

    _rc = subprocess.call(["cat",str(bookmarks_file)]) | _rc = subprocess.call(["awk",r'{ printf "%-40s%-40s%s\n","+str(sys.argv[1])+","+str(sys.argv[2])+","+str(sys.argv[3])+"}',FS=\|])

def go () :
    global bookmark_name
    global bookmark
    global 
    global bookmarks_file
    global dir

    bookmark_name=str(sys.argv[1])
    bookmark=os.popen("grep \"|"+str(bookmark_name)+str()+"\" \""+str(bookmarks_file)+"\"").read()
    if (('bookmark' not in globals()) ):
        print(r'Invalid name, please provide a valid bookmark name. For example:')
        print(r'  go foo')
        print()
        print(r'To bookmark a folder, go to the folder then do this (naming the bookmark '+"foo'):'")
        print(r'  bookmark foo')
    else:
        dir=os.popen("echo \""+str(bookmark)+"\" | cut -d| -f1").read()
        os.chdir(str(dir))

def _go_complete () :
    global bookmarks_file

    # Get a list of bookmark names, then grep for what was entered to narrow the list
    _rc = subprocess.call(["cat",str(bookmarks_file)]) | _rc = subprocess.call(["cut","-d\|","-f2"]) | _rc = subprocess.call(["grep",str(sys.argv[2])+".*"])

_rc = subprocess.call(["complete","-C","_go_complete",or,"default","go"])
