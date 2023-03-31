import sys, os, os.path
from stat import *
# remap_keybindings.bash
# Author: Noah Friedman <friedman@prep.ai.mit.edu>
# Created: 1992-01-11
# Last modified: 1993-02-03
# Public domain
# Conversion to bash v2 syntax done by Chet Ramey
# Commentary:
# Code:
#:docstring remap_keybindings:
# Usage: remap_keybindings old_function new_function
#
# Clear all readline keybindings associated with OLD_FUNCTION (a Readline
# function) rebinding them to NEW_FUNCTION (`self-insert' by default)
#
# This requires bash version 1.10 or newer, since previous versions did not
# implement the `bind' builtin.
#:end docstring:
###;;;autoload
