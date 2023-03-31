#! /usr/bin/env python
import subprocess
from stat import *
_rc = subprocess.call(["test/errlog"])
_rc = subprocess.call(["test/outlog"])
