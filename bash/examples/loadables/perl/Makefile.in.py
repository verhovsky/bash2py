import sys, os, os.path
from stat import *
#
# Makefile for builtin perl interpreter
#
#
#   Copyright (C) 1998 Free Software Foundation, Inc.     
#
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
os.system('PERL5 == perl5')
os.system('CFLAGS == @CFLAGS@')
#
# These values are generated for configure by ${topdir}/support/shobj-conf.
# If your system is not supported by that script, but includes facilities for
# dynamic loading of shared objects, please update the script and send the
# changes to bash-maintainers@gnu.org.
#
os.system('SHOBJ_CC == @SHOBJ_CC@')
os.system('SHOBJ_CFLAGS == @SHOBJ_CFLAGS@')
os.system('SHOBJ_LD == @SHOBJ_LD@')
os.system('SHOBJ_LDFLAGS == @SHOBJ_LDFLAGS@')
os.system('SHOBJ_XLDFLAGS == @SHOBJ_XLDFLAGS@')
os.system('SHOBJ_LIBS == @SHOBJ_LIBS@')
os.system('SHOBJ_STATUS == @SHOBJ_STATUS@')
# Values used for compiling the perl files
os.system('PERL_LDOPTS ==  os.popen('${PERL5} -MExtUtils::Embed -e ldopts').read() ')
os.system('PERL_CFLAGS == ${CCFLAGS}  os.popen('${PERL5} -MExtUtils::Embed -e ccopts').read() ')
os.system('SRC == bperl.c iperl.c perlxsi.c')
os.system('OBJ == bperl.o iperl.o perlxsi.o')
os.system('BUILTIN == bperl5')
os.system('INC == -I. -I.. -I os.popen('topdir').read()  -I os.popen('topdir').read() /lib -I os.popen('topdir').read() /builtins -I os.popen('topdir').read() /include -I os.popen('BUILD_DIR').read()  -I os.popen('BUILD_DIR').read() /lib -I os.popen('BUILD_DIR').read() /builtins')
os.system('${BUILTIN}: ${OBJ}')
os.system('${RM} $@')
os.system('${SHOBJ_LD} ${SHOBJ_LDFLAGS} ${SHOBJ_XLDFLAGS} -o $@ ${OBJ} ${PERL_LDOPTS} ${SHOBJ_LIBS}')
os.system('bperl.o: bperl.c')
os.system('${RM} $@')
os.system(' os.popen('SHOBJ_CC').read()   os.popen('SHOBJ_CFLAGS').read()   os.popen('CFLAGS').read()   os.popen('INC').read()  -c -o $@ ${srcdir}/bperl.c')
os.system('iperl.o: iperl.c')
os.system('${RM} $@')
os.system(' os.popen('SHOBJ_CC').read()  ${SHOBJ_CFLAGS}  os.popen('PERL_CFLAGS').read()  -c -o $@ ${srcdir}/iperl.c')
os.system('perlxsi.c:')
os.system('${PERL5} -MExtUtils::Embed -e xsinit -- -o $@')
os.system('perlxsi.o: perlxsi.c')
os.system('${RM} $@')
os.system('${SHOBJ_CC} ${SHOBJ_CFLAGS}  os.popen('PERL_CFLAGS').read()  -c -o $@ perlxsi.c')
os.system('clean mostlyclean:')
os.system('${RM} ${OBJ}')
os.system('${RM} ${BUILTIN}')
os.system('distclean maintainer-clean: clean')
os.system('${RM} perlxsi.c')
