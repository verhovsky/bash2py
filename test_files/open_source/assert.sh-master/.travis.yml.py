#! /usr/bin/env python
import subprocess
from stat import *
_rc = subprocess.call(["language":,"bash"])
_rc = subprocess.call(["script":,"bash","tests.sh"])
_rc = subprocess.call(["before_install":])
_rc = subprocess.call([-,"sudo","apt-get","install","bc"])
