
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

extern int g_translate_html;

void
burp_init(burpT *burpP)
{
	memset(burpP, 0, sizeof(burpT));
}

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
		if (!burpP->m_disable_indent) {
			assert(0 <= burpP->m_indent);
			for (i = burpP->m_indent * 4; i > 0; --i) {
				burpc1(burpP, ' ');
}	}	}	}

void
burpc(burpT *burpP, const char c)
{
	if (g_translate_html) {
		burpP->m_ungetc = burpP->m_lth;
		switch (c) {
		case '<':
			g_translate_html = 0;
			burps(burpP, "&lt;");
			g_translate_html = 1;
			return;
		case '>':
			g_translate_html = 0;
			burps(burpP, "&gt;");
			g_translate_html = 1;
			return;
		case '&':
			g_translate_html = 0;
			burps(burpP, "&amp;");
			g_translate_html = 1;
			return;
	}	}
	indentation(burpP);
	burpc1(burpP, c);
	assert(burpP->m_lth < burpP->m_max);
}

void
burp_ungetc(burpT *burpP)
{
	assert(burpP->m_ungetc < burpP->m_lth);
	burpP->m_lth = burpP->m_ungetc;
}

void 
burp(burpT *burpP, const char *fmtP, ...)	/* proc */
{
	static burpT	burp_temp = {0,0,0};

	va_list	    arg;
	size_t		size, left;
	int			ret, c;
	char		*P;
	
	va_start(arg, fmtP);
		
	if (!fmtP) {
		fprintf(stderr, "Burp has no format string\n");
		assert(0);
		exit(1);
	}

	indentation(burpP);
	burp_temp.m_lth = 0;
	for (;;) {
		left = burp_temp.m_max - burp_temp.m_lth;
		// Caution: microsoft bug causes ret == -1 if printing any 0xFFFF character
		if (left > 79 && (ret =  vsnprintf(burp_temp.m_P+burp_temp.m_lth, left, fmtP, arg)) < left && 0 <= ret) {
			break;

		}
		increase_burp(&burp_temp);
	}
	burp_temp.m_lth += ret;
	va_end(arg);

	for (P = burp_temp.m_P; c = *P; ++P) {
		burpc(burpP, c);
	}
 	return;
}

void
burpn(burpT *burpP, const char *stringP, int lth)
{
	int	i;

	assert(0 <= lth);
	if (0 < lth) {
		indentation(burpP);
		for (i = 0; i < lth; ++i) {
			burpc(burpP, stringP[i]);
	}	}
	return;
}

void
burps(burpT *burpP, const char *stringP)
{
	burpn(burpP, stringP, strlen(stringP));
}

void
burps_html(burpT *burpP, const char *stringP)
{
	int save = g_translate_html;

	g_translate_html = 0;
	burps(burpP, stringP);
	g_translate_html = save;
}
