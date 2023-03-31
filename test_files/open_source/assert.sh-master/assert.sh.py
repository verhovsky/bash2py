#! /usr/bin/env python
import sys,os,subprocess,signal
from stat import *
# assert.sh 1.0 - bash unit testing framework
# Copyright (C) 2009, 2010, 2011, 2012 Robert Lehmann
#
# http://github.com/lehmannro/assert.sh
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
os.environ['DISCOVERONLY'] = '' if dir().count('DISCOVERONLY') == 0 else DISCOVERONLY
os.environ['DEBUG'] = '' if dir().count('DEBUG') == 0 else DEBUG
os.environ['STOP'] = '' if dir().count('STOP') == 0 else STOP
os.environ['INVARIANT'] = '' if dir().count('INVARIANT') == 0 else INVARIANT
os.environ['CONTINUE'] = '' if dir().count('CONTINUE') == 0 else CONTINUE
args=str(os.popen("getopt -n \""+str(__file__)+"\" -l     verbose,help,stop,discover,invariant,continue vhxdic "+str(" ".join(sys.argv[1:]))).read()) or exit(-1)
for arg in [args]:
    
    if ( str(arg) == '-h'):
        print(str(__file__) + " [-vxidc]","[--verbose] [--stop] [--invariant] [--discover] [--continue]")
        print(str(os.popen("sed \"s/./ /g\" <<< \""+str(__file__)+"\"").read()) + " [-h] [--help]")
        exit(0)
    elif ( str(arg) == '--help'):
        _rc = subprocess.call("cat",shell=True,stdin=subprocess.PIPE)
        _rc.communicate("Usage: " + str(__file__) + " [options]\nLanguage-agnostic unit tests for subprocesses.\n\nOptions:\n  -v, --verbose    generate output for every individual test case\n  -x, --stop       stop running tests after the first failure\n  -i, --invariant  do not measure timings to remain invariant between runs\n  -d, --discover   collect test suites only, do not run any tests\n  -c, --continue   do not modify exit code to test suite status\n  -h               show brief usage information and exit\n  --help           show this help message and exit\n")
        exit(0)
    elif ( str(arg) == '-v' or str(arg) == '--verbose'):
        DEBUG=1
    elif ( str(arg) == '-x' or str(arg) == '--stop'):
        STOP=1
    elif ( str(arg) == '-i' or str(arg) == '--invariant'):
        INVARIANT=1
    elif ( str(arg) == '-d' or str(arg) == '--discover'):
        DISCOVERONLY=1
    elif ( str(arg) == '-c' or str(arg) == '--continue'):
        CONTINUE=1
_indent = "\n\t"
# local format helper
def _assert_reset () :
    global tests_ran
    global tests_failed
    global tests_errors
    global tests_starttime

    tests_ran=0
    tests_failed=0
    tests_errors=()
    tests_starttime=str(os.popen("date +%s.%N").read())

# seconds_since_epoch.nanoseconds
def assert_end () :
    global tests_endtime
    global tests
    global tests_ran
    global DISCOVERONLY
    global DEBUG
    global INVARIANT
    global report_time
    global tests_starttime
    global tests_failed
    global tests_errors
    global error
    global tests_failed_previous
    global tests_suite_status

    # assert_end [suite ..]
    tests_endtime=str(os.popen("date +%s.%N").read())
    tests=str(tests_ran) + " " + str('' if len(sys.argv) < 2 else " ".join(sys.argv[1:]) ) + "tests"
    (str(DISCOVERONLY) != '') and print("collected " + str(tests) + ".") and _assert_reset() and return
    (str(DEBUG) != '') and print()
    ('str(INVARIANT)' not in globals()) and report_time=" in " + str(os.popen("bc         <<< \""+str(tests_endtime%.N)+" - "+str(tests_starttime%.N)+"\"         | sed -e \"s/\\\\.\\\\([0-9]\\\\{0,3\\\\}\\\\)[0-9]*/.\\\\1/\" -e \"s/^\\\\./0./\"").read()) + "s" or report_time=
    if (str(tests_failed) == 0 ):
        print("all " + str(tests) + " passed" + str(report_time) + ".")
    else:
        for error in [str(tests_errors[@])]:
            print(str(error))
        print(str(tests_failed) + " of " + str(tests) + " failed" + str(report_time) + ".")
    tests_failed_previous=tests_failed
    tests_failed > 0 and tests_suite_status=1
    _assert_reset()
    return(tests_failed_previous)

def assert () :
    global DISCOVERONLY
    global result
    global expected
    global DEBUG

    # assert <command> <expected stdout> [stdin]
    tests_ran++  or 
    (str(DISCOVERONLY) != '') and return or True
    # printf required for formatting
    expected = "x" + str('' if dir().count('2') == 0 else sys.argv[2])
    # x required to overwrite older results
    result=str(os.popen("eval 2>/dev/null "+str(sys.argv[1])+" <<< "+str('' if dir().count('3') == 0 else sys.argv[3])).read()) or True
    # Note: $expected is already decorated
    if ("x" + str(result) == str(expected) ):
        (str(DEBUG) != '') and print(.) or True
        return
    result=str(os.popen("sed -e :a -e \"\\"+str(DOLLAR_EXCLAMATION)+"N;s/\\\\n/\\\\\\\\n/;ta\" <<< \""+str(result)+"\"").read())
    ('str(result)' not in globals()) and result="nothing" or result="\"" + str(result) + "\""
    ('str(sys.argv[2])' not in globals()) and expected="nothing" or expected="\"" + str(sys.argv[2]) + "\""
    _rc = subprocess.call(["_assert_fail","expected " + str(expected) + str(DOLLAR_UNDERBAR) + "got " + str(result),str(sys.argv[1]),str(sys.argv[3])])

def assert_raises () :
    global DISCOVERONLY
    global status
    global expected
    global DEBUG

    # assert_raises <command> <expected code> [stdin]
    tests_ran++  or 
    (str(DISCOVERONLY) != '') and return or True
    status=0
    ( exec(sys.argv[1]) ) > /dev/null 2>&1 or status=_rc
    expected='0' if dir().count('2') == 0 or 2 == '' else sys.argv[2]
    if (str(status) == str(expected) ):
        (str(DEBUG) != '') and print(.) or True
        return
    _rc = subprocess.call(["_assert_fail","program terminated with code " + str(status) + " instead of " + str(expected),str(sys.argv[1]),str(sys.argv[3])])

def _assert_fail () :
    global DEBUG
    global report
    global tests_ran
    global STOP
    global tests_errors
    global tests_failed

    # _assert_fail <failure> <command> <stdin>
    (str(DEBUG) != '') and print("X")
    report="test #" + str(tests_ran) + " \"" + str(sys.argv[2]) + str('' if dir().count('3') == 0 or 3 == '' else  <<< sys.argv[3]) + "\" failed:" + str(DOLLAR_UNDERBAR) + str(sys.argv[1])
    if ((str(STOP) != '') ):
        (str(DEBUG) != '') and print()
        print(str(report))
        exit(1)
    tests_errors[tests_failed]=str(report)
    tests_failed++  or 

_assert_reset()
tests_suite_status=('0' if dir().count('tests_suite_status') == 0 or tests_suite_status == '' else tests_suite_status)
# remember if any of the tests failed so far
def _assert_cleanup () :
    global CONTINUE
    global tests_suite_status

    status=_rc
    
    # modify exit code if it's not already non-zero
    status == 0 and ('CONTINUE' not in globals()) and exit(tests_suite_status)

signal.signal(signal.SIGEXIT,_assert_cleanup)

