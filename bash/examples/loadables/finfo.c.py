import sys, os, os.path
from stat import *
os.system('/*')
os.system('* finfo - print file info')
os.system('*')
os.system('* Chet Ramey')
os.system('* chet@po.cwru.edu')
os.system('*/')
#ifdef HAVE_CONFIG_H
#  include <config.h>
#endif
#include <sys/types.h>
#include "posixstat.h"
#include <stdio.h>
#include <pwd.h>
#include <grp.h>
#include <errno.h>
#include "posixtime.h"
#include "bashansi.h"
#include "shell.h"
#include "builtins.h"
#include "common.h"
#ifndef errno
os.system('extern int errno')
#endif
