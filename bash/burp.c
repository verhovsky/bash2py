
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

int  g_burp_indent         = 0;
int  g_burp_disable_indent = 0;

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
burpc1(burpT *burpP, const char c)
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

static void
indentation(burpT *burpP)
{
	int i;

	if (burpP->m_lth && burpP->m_P[burpP->m_lth-1] == '\n') {
		if (!g_burp_disable_indent) {
			assert(0 <= g_burp_indent);
			for (i = g_burp_indent * 4; i > 0; --i) {
				burpc1(burpP, ' ');
}	}	}	}

void
burpc(burpT *burpP, const char c)
{
	indentation(burpP);
	burpc1(burpP, c);
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

	indentation(burpP);
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
burpn(burpT *burpP, const char *stringP, int lth)
{
	char	*P;

	assert(0 <= lth);
	if (0 < lth) {
		indentation(burpP);
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

