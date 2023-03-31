import sys, os, os.path
from stat import *
os.system('/* This module should be dynamically loaded with enable -f')
os.system('* which would create a new builtin named mypid. You'll need
')
os.system('* is a shell builtin variable.')
os.system('*/')
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include "builtins.h"
#include "shell.h"
#define INIT_DYNAMIC_VAR(var, val, gfunc, afunc) \
