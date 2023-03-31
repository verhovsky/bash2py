import sys, os, os.path
from stat import *
os.system('/* getconf.h -- replacement definitions for ones the system doesn't provide. */
 on a posix system, but the system doesn't define the necessary
 Assume a 32-bit')
os.system('environment with signed 8-bit characters. */')
#ifndef CHAR_BIT
#  define CHAR_BIT	8
#endif
#ifndef CHAR_MAX
#  define CHAR_MAX	127
#endif
#ifndef CHAR_MIN
#  define CHAR_MIN	-128
#endif
#ifndef INT_BIT
#  define INT_BIT	(sizeof (int) * CHAR_BIT)
#endif
#ifndef INT_MAX
#  define INT_MAX	2147483647
#endif
#ifndef INT_MIN
#  define INT_MIN	(-2147483647-1)
#endif
#ifndef LONG_BIT
#  define LONG_BIT	(sizeof (long int) * CHAR_BIT)
#endif
#ifndef LONG_MAX
#  define LONG_MAX	2147483647L
#endif
#ifndef LONG_MIN
#  define LONG_MIN	(-2147483647L-1L)
#endif
#ifndef SCHAR_MAX
#  define SCHAR_MAX	CHAR_MAX
#endif
#ifndef SCHAR_MIN
#  define SCHAR_MIN	CHAR_MIN
#endif
#ifndef SHRT_MAX
#  define SHRT_MAX	32767
#endif
#ifndef SHRT_MIN
#  define SHRT_MIN	(-32768)
#endif
#ifndef UCHAR_MAX
#  define UCHAR_MAX	255
#endif
#ifndef UINT_MAX
#  define UINT_MAX	4294967295U
#endif
#ifndef ULONG_MAX
#  define ULONG_MAX	4294967295UL
#endif
#ifndef USHRT_MAX
#  define UCHAR_MAX	65535
#endif
