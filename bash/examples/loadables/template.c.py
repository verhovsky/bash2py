import sys, os, os.path
from stat import *
os.system('/* template - example template for loadable builtin */')
os.system('/* See Makefile for compilation details. */')
#include <config.h>
#if defined (HAVE_UNISTD_H)
#  include <unistd.h>
#endif
#include "bashansi.h"
#include <stdio.h>
#include <errno.h>
#include "builtins.h"
#include "shell.h"
#include "bashgetopt.h"
#if !defined (errno)
os.system('extern int errno')
#endif
