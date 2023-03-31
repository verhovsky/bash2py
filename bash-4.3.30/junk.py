#! /usr/bin/env python
#The statement below also gets interpreted incorrectly. 
#believe the desired output would be:
#if (OPTION.val != "1")
if (str(OPTION.val) != "1" ):
    print("Option is disabled")
