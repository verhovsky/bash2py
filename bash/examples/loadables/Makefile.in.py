import sys, os, os.path
from stat import *
#
# Simple makefile for the sample loadable builtins
#
# Copyright (C) 1996-2009 Free Software Foundation, Inc.     
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Include some boilerplate Gnu makefile definitions.
os.system('prefix == @prefix@')
os.system('exec_prefix == @exec_prefix@')
os.system('bindir == @bindir@')
os.system('libdir == @libdir@')
os.system('infodir == @infodir@')
os.system('includedir == @includedir@')
os.system('datarootdir == @datarootdir@')
os.system('topdir == @top_srcdir@')
os.system('BUILD_DIR == @BUILD_DIR@')
os.system('srcdir == @srcdir@')
os.system('VPATH == .:@srcdir@')
os.system('@SET_MAKE@')
os.system('CC == @CC@')
os.system('RM == rm -f')
os.system('SHELL == @MAKE_SHELL@')
os.system('host_os == @host_os@')
os.system('host_cpu == @host_cpu@')
os.system('host_vendor == @host_vendor@')
os.system('CFLAGS == @CFLAGS@')
os.system('LOCAL_CFLAGS == @LOCAL_CFLAGS@')
os.system('DEFS == @DEFS@')
os.system('LOCAL_DEFS == @LOCAL_DEFS@')
os.system('CPPFLAGS == @CPPFLAGS@')
os.system('BASHINCDIR == ${topdir}/include')
os.system('LIBBUILD == ${BUILD_DIR}/lib')
os.system('INTL_LIBSRC == ${topdir}/lib/intl')
os.system('INTL_BUILDDIR == ${LIBBUILD}/intl')
os.system('INTL_INC == @INTL_INC@')
os.system('LIBINTL_H == @LIBINTL_H@')
os.system('CCFLAGS ==  os.popen('DEFS').read()   os.popen('LOCAL_DEFS').read()   os.popen('LOCAL_CFLAGS').read()   os.popen('CFLAGS').read() ')
#
# These values are generated for configure by ${topdir}/support/shobj-conf.
# If your system is not supported by that script, but includes facilities for
# dynamic loading of shared objects, please update the script and send the
# changes to bash-maintainers@gnu.org.
#
os.system('SHOBJ_CC == @SHOBJ_CC@')
os.system('SHOBJ_CFLAGS == @SHOBJ_CFLAGS@')
os.system('SHOBJ_LD == @SHOBJ_LD@')
os.system('SHOBJ_LDFLAGS == @SHOBJ_LDFLAGS@ @LDFLAGS@')
os.system('SHOBJ_XLDFLAGS == @SHOBJ_XLDFLAGS@')
os.system('SHOBJ_LIBS == @SHOBJ_LIBS@')
os.system('SHOBJ_STATUS == @SHOBJ_STATUS@')
os.system('INC == -I. -I.. -I os.popen('topdir').read()  -I os.popen('topdir').read() /lib -I os.popen('topdir').read() /builtins -I os.popen('BASHINCDIR').read()  -I os.popen('BUILD_DIR').read()  -I os.popen('LIBBUILD').read()  -I os.popen('BUILD_DIR').read() /builtins  os.popen('INTL_INC').read() ')
os.system('.c.o:')
