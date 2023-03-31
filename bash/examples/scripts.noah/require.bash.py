import sys, os, os.path
from stat import *
# require.bash
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created: 1992-07-08
# Last modified: 1993-09-29
# Public domain
# Commentary:
# These functions provide an interface based on the lisp implementation for
# loading libraries when they are needed and eliminating redundant loading.
# The basic idea is that each "package" (or set of routines, even if it is
# only one function) registers itself with a symbol that marks a "feature"
# as being "provided".  If later you "require" a given feature, you save
# yourself the trouble of explicitly loading it again.
# 
# At the bottom of each package, put a "provide foobar", so when another
# package has a "require foobar", it gets loaded and registered as a
# "feature" that won't need to get loaded again.  (See warning below for
# reasons why provide should be put at the end.)
#
# The list of provided features are kept in the `FEATURES' variable, which
# is not exported.  Care should be taken not to munge this in the shell.
# The search path comes from a colon-separated `FPATH' variable.  It has no
# default value and must be set by the user.
#
# Require uses `fpath_search', which works by scanning all of FPATH for a
# file named the same as the required symbol but with a `.bash' appended to
# the name.  If that is found, it is loaded.  If it is not, FPATH is
# searched again for a file name the same as the feature (i.e. without any
# extension).  Fpath_search may be useful for doing library filename
# lookups in other functions (such as a `load' or `autoload' function).
#
# Warning: Because require ultimately uses the builtin `source' command to
# read in files, it has no way of undoing the commands contained in the
# file if there is an error or if no provide statement appeared (this
# differs from the lisp implementation of require, which normally undoes
# most of the forms that were loaded if the require fails).  Therefore, to
# minize the number of problems caused by requiring a faulty package (such
# as syntax errors in the source file) it is better to put the provide at
# the end of the file, rather than at the beginning.
# Code:
# Exporting this variable would cause considerable lossage, since none of
# the functions are exported (or at least, they're not guaranteed to be)
os.environ[''] = FILE_TO_TRANSLATE
#:docstring :
# Null function.  Provided only so that one can put page breaks in source
# files without any ill effects.
#:end docstring:
#
# (\\014 == C-l)
os.system('eval "function " + $ + "(echo -e \\014) () { : }"')
#:docstring featurep:
# Usage: featurep argument
#
# Returns 0 (true) if argument is a provided feature.  Returns 1 (false)
# otherwise. 
#:end docstring:
###;;;autoload
def featurep () 
{ 
    os.system('local feature="" + sys.argv[1] + ""')
    
    
        if ( " " + $ + "{FEATURES} " == '*" ${feature} "*'):
            os.system('return 0')
    
    os.system('return 1')
}
#:docstring provide:
# Usage: provide symbol ...
#
# Register a list of symbols as provided features
#:end docstring:
###;;;autoload
def provide () 
{ 
    os.system('local feature')
    
    for feature in ["" + $ + "@"]:
            if (! os.system('featurep "" + $ + "{feature}"') ):
            FEATURES="" + $ + "{FEATURES} " + $ + "{feature}"
    
    os.system('return 0')
}
#:docstring require:
# Usage: require feature {file}
#
# Load FEATURE if it is not already provided.  Note that require does not
# call `provide' to register features.  The loaded file must do that
# itself.  If the package does not explicitly do a `provide' after being
# loaded, require will complain about the feature not being provided on
# stderr.
#
# Optional argument FILE means to try to load FEATURE from FILE.  If no
# file argument is given, require searches through FPATH (see fpath_search)
# for the appropriate file.
#
# If the variable REQUIRE_FAILURE_FATAL is set, require will cause the
# current shell invocation to exit, rather than merely return.  This may be
# useful for a shell script that vitally depends on a package. 
#
#:end docstring:
###;;;autoload
def require () 
{ 
    os.system('local feature="" + sys.argv[1] + ""')
    
    os.system('local path="" + sys.argv[2] + ""')
    
    os.system('local file')
    
    if (! os.system('featurep "" + $ + "{feature}"') ):
        file= os.popen('fpath_search "" + $ + "{feature}" "" + $ + "{path}"').read()  && os.system('source "" + $ + "{file}"')
        
        if (! os.system('featurep "" + $ + "{feature}"') ):
            print("require: " + $ + "{feature}: feature was not provided.")1>&2
            
            if ("" + $ + "{REQUIRE_FAILURE_FATAL+set}" == "set"  ):
                exit(1)
            
            os.system('return 1')
    
    os.system('return 0')
}
#:docstring fpath_search:
# Usage: fpath_search filename {path ...}
#
# Search $FPATH for `filename' or, if `path' (a list) is specified, search
# those directories instead of $FPATH.  First the path is searched for an
# occurrence of `filename.bash, then a second search is made for just
# `filename'.
#:end docstring:
###;;;autoload
