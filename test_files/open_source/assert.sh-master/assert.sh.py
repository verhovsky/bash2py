#! /usr/bin/env python
import sys,os,subprocess
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
os.environ['DISCOVERONLY'] = str('' if dir().count('DISCOVERONLY') == 0 or DISCOVERONLY == '' else DISCOVERONLY)
os.environ['DEBUG'] = str('' if dir().count('DEBUG') == 0 or DEBUG == '' else DEBUG)
os.environ['STOP'] = str('' if dir().count('STOP') == 0 or STOP == '' else STOP)
os.environ['INVARIANT'] = str('' if dir().count('INVARIANT') == 0 or INVARIANT == '' else INVARIANT)
os.environ['CONTINUE'] = str('' if dir().count('CONTINUE') == 0 or CONTINUE == '' else CONTINUE)
args=os.popen("getopt -n \""+str(__file__)+"\" -l     verbose,help,stop,discover,invariant,continue vhxdic "+str(" ".join(sys.argv[1:]))).read() or exit(-1)
for arg in [args]:
    
    if ( str(arg) == '-h'):
        print(str(__file__)+" [-vxidc]","[--verbose] [--stop] [--invariant] [--discover] [--continue]")
        print(os.popen("sed 's/./ /g' <<< \""+str(__file__)+"\"").read()+" [-h] [--help]")
        exit(0)
    elif ( str(arg) == '--help'):
        _rc = subprocess.Popen("cat",shell=True,stdin=subprocess.PIPE)
        _rc.communicate("""Usage: $0 [options]
        Language-agnostic unit tests for subprocesses.
        
        Options:
          -v, --verbose    generate output for every individual test case
          -x, --stop       stop running tests after the first failure
          -i, --invariant  do not measure timings to remain invariant between runs
          -d, --discover   collect test suites only, do not run any tests
          -c, --continue   do not modify exit code to test suite status
          -h               show brief usage information and exit
          --help           show this help message and exit
        """)
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
    tests_starttime=os.popen("date +%s.%N").read()

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
    tests_endtime=os.popen("date +%s.%N").read()
    tests=str(tests_ran)+" "+str(" ".join(sys.argv[1:]))+"tests"
    (DISCOVERONLY != '') and print("collected "+str(tests)+".") and _assert_reset() and return
    (DEBUG != '') and print()
    ('INVARIANT' not in globals()) and report_time=" in "+os.popen("bc         <<< \""+str(tests_endtime%.N)+" - "+str(tests_starttime%.N)+"\"         | sed -e 's/\\.\\([0-9]\\{0,3\\}\\)[0-9]*/.\\1/' -e 's/^\\./0./'").read()+"s" or report_time=
    if (tests_failed == 0 ):
        print("all "+str(tests)+" passed"+str(report_time)+".")
    else:
        for error in [tests_errors[@]]:
            print(str(error))
        print(str(tests_failed)+" of "+str(tests)+" failed"+str(report_time)+".")
    tests_failed_previous=str(tests_failed)
    tests_failed > 0 and tests_suite_status=1
    _assert_reset()
    return(tests_failed_previous)

def assert () :
    global DISCOVERONLY
    global result
    global expected
    global DEBUG

    # assert <command> <expected stdout> [stdin]
    tests_ran++  or _rc = subprocess.call([:])
    (DISCOVERONLY != '') and return or True
    # printf required for formatting
    expected = "x"+str('' if dir().count('2') == 0 or 2 == '' else sys.argv[2])
    # x required to overwrite older results
    result=os.popen("eval 2>/dev/null "+str(sys.argv[1])+" <<< "+str('' if dir().count('3') == 0 or 3 == '' else sys.argv[3])).read() or True
    # Note: $expected is already decorated
    if ("x"+result == expected ):
        (DEBUG != '') and print(".") or True
        return
    result=os.popen("sed -e :a -e '"+str(DOLLAR_EXCLAMATION)+"N;s/\\n/\\\\n/;ta' <<< \""+str(result)+"\"").read()
    ('result' not in globals()) and result="nothing" or result="\""+str(result)+"\""
    ('sys.argv[2]' not in globals()) and expected="nothing" or expected="\""+str(sys.argv[2])+"\""
    _rc = subprocess.call(["_assert_fail","expected "+str(expected)+""+str(DOLLAR_UNDERBAR)+"got "+str(result),str(sys.argv[1]),str(sys.argv[3])])

def assert_raises () :
    global DISCOVERONLY
    global status
    global expected
    global DEBUG

    # assert_raises <command> <expected code> [stdin]
    tests_ran++  or _rc = subprocess.call([:])
    (DISCOVERONLY != '') and return or True
    status=0
    ( exec(str(sys.argv[1])) ) > /dev/null 2>&1 or status=str(_rc)
    expected=str('0' if dir().count('2') == 0 or 2 == '' else sys.argv[2])
    if (status == expected ):
        (DEBUG != '') and print(".") or True
        return
    _rc = subprocess.call(["_assert_fail","program terminated with code "+str(status)+" instead of "+str(expected),str(sys.argv[1]),str(sys.argv[3])])

def _assert_fail () :
    global DEBUG
    global report
    global tests_ran
    global STOP
    global tests_failed

    # _assert_fail <failure> <command> <stdin>
    (DEBUG != '') and print("X")
    report="test #"+str(tests_ran)+" \""+str(sys.argv[2])+""+str(sys.argv[3])+"\" failed:"+str(DOLLAR_UNDERBAR)+""+str(sys.argv[1])
    if ((STOP != '') ):
        (DEBUG != '') and print()
        print(str(report))
        exit(1)
    "tests_errors["+str(tests_failed)+"]=\""+str(report)+"\""
    tests_failed++  or _rc = subprocess.call([:])

_assert_reset()
_rc = subprocess.call([:,str(tests_suite_status)])
# remember if any of the tests failed so far
def _assert_cleanup () :
    global CONTINUE
    global tests_suite_status

    status=str(_rc)
    # modify exit code if it's not already non-zero
    status == 0 and ('CONTINUE' not in globals()) and exit(tests_suite_status)

_rc = subprocess.call(["trap","_assert_cleanup","EXIT"])
