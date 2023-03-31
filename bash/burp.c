
#include "config.h"

#include <stdio.h>
#include <assert.h>

#if defined (HAVE_UNISTD_H)
#  ifdef _MINIX
#    include <sys/types.h>
#  endif
#  include <unistd.h>
#endif

#if defined (PREFER_STDARG)
#  include <stdarg.h>
#else
#  include <varargs.h>
#endif

#include "bashansi.h"

#include "burp.h"

static void
increase_burp(burpT *burpP)
{
	int	max;

	if (!burpP->m_P) {
		burpP->m_lth = 0;
		burpP->m_max = 0;
		max          = 4196;
		burpP->m_P   = (char *) malloc(max);
		if (!burpP->m_P) {
			fprintf(stderr, "Burp can't malloc(%d)\n", max);
			assert(0);
			exit(1);
		}
		burpP->m_max = max;
		return;
	}
	max = burpP->m_max << 1;
	if (max & 0x40000000) {
		// Very serious problems trying to print whatever it might be..
		fprintf(stderr,"Burp can't print\n");
		assert(0);
		exit(1);
	}
	burpP->m_P = realloc(burpP->m_P, max);
	if (!burpP->m_P) {
		fprintf(stderr, "Burp can't realloc(%d)\n", max);
		assert(0);
		exit(1);
	}
	burpP->m_max = max;
}

void 
burp(burpT *burpP, const char *fmtP, ...)	/* proc */
{
	va_list	    arg;
	size_t		size, left;
	int			ret;
	
	va_start(arg, fmtP);
		
	if (!fmtP) {
		fprintf(stderr, "Burp has no format string\n");
		assert(0);
		exit(1);
	}

	for (;;) {
		left = burpP->m_max - burpP->m_lth;
		// Caution: microsoft bug causes ret == -1 if printing any 0xFFFF character
		if (left > 79 && (ret =  vsnprintf(burpP->m_P+burpP->m_lth, left, fmtP, arg)) < left && 0 <= ret) {
			break;

		}
		increase_burp(burpP);
	}
	burpP->m_lth += ret;
	va_end(arg);
 	return;
}

void
burpc(burpT *burpP, const char c)
{
	char	*P;

	if ((burpP->m_max - burpP->m_lth) < 2) {
		increase_burp(burpP);
	}
	P = burpP->m_P + burpP->m_lth;
	*P++ = c;
	burpP->m_lth++;
	*P   = 0;
	return;
}

void
burpn(burpT *burpP, const char *stringP, int lth)
{
	char	*P;

	assert(0 <= lth);
	if (0 < lth) {
		while ((burpP->m_max - burpP->m_lth) < lth + 1) {
			increase_burp(burpP);
		}
		P = burpP->m_P + burpP->m_lth;
		memcpy(P, stringP, lth);
		burpP->m_lth += lth;
		P            += lth;
		*P            = 0;
	}
	return;
}

void
burps(burpT *burpP, const char *stringP)
{
	burpn(burpP, stringP, strlen(stringP));
}

