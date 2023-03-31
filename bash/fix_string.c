#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>
#include "burp.h"
#include "fix_string.h"

static burpT g_buffer      = {0, 0, 0};
static burpT g_new         = {0, 0, 0};
static burpT g_save_buffer = {0, 0, 0};
static burpT g_save_new    = {0, 0, 0};

int g_uses_sys        = 0;
int g_uses_os         = 0;
int g_uses_subprocess = 0;

fix_typeE	g_type;


#ifndef TEST
extern int g_translate_html;
extern	void seen_global(const char *nameP, int local);
#endif

static char *recursively_fix_string(const char *stringP, int separator);

#define WHITESPACE_MARKER 1

static void
exchange(burpT *oldP, burpT *newP)
{
	burpT	temp;

	temp   = *oldP;
	*oldP  = *newP;
	*newP  = temp;
}

static int
xspace(int c)
{
	return (isspace(c) || c == WHITESPACE_MARKER);
}

static char *
endSpecial(char *startP)
{

	char	*P, *P1;
	int		openbrace, closebrace, nesting;
	int		c;

	switch (*startP) {
	case '`':
		for (P = startP+1; *P != '`'; ++P) {
			if (*P == '\\') {
				++P;
		}	}
		return P+1;
	case '(':
		if (startP[1] == '(') {
			goto brace;
		}
		break;
	case '$':
		P = startP + 1;
brace:
		switch (*P) {
		case '(':
			openbrace  = '(';
			closebrace = ')';
			break;
		case '{':
			openbrace  = '{';
			closebrace = '}';
			break;
		case '[':
			openbrace  = '[';
			closebrace = ']';
			break;
		case '*':
		case '@':
		case '#':
		case '?':
		case '-':
		case '_':
		case '$':
		case '!':
		case '0':
		case '1':
		case '2':
		case '3':
		case '4':
		case '5':
		case '6':
		case '7':
		case '8':
		case '9':
			return P+1;
		default:
			for (;isalnum(*P) || *P == '_'; ++P);
			return P;
		}
		nesting = 0;
		for (; *P; ++P) {
			if (*P == openbrace) {
				++nesting;
				continue;
			}
			if (*P == closebrace) {
				if (!--nesting) {
					++P;
					return P;
				}
				continue;
			}
			if (*P == '\\') {
				++P;
			}
		}
	}
	return 0;
}


/* Turn anything not quoted into being double quoted */

static void
addDoubleQuotes(void)
{
	typedef enum {
		start_state       = 0,
        end_quote_state   = 1,
		whitespace_state  = 2,
		integer_state     = 3,
		float_state       = 4,
		special_state     = 5,
		punctuation_state = 6,
		unquoted_state    = 7
	} stateT;

	char	*P, *startP, *P1;
	int		c, in_quote, lth;
	stateT	state;

	// If it is a range leave it alone
	if (g_buffer.m_P[0] == '{') {
		return;
	}

restart:
	in_quote = 0;
	state    = start_state;
	startP   = 0;

	for (P = g_buffer.m_P; (c = *P) == '_' || isalpha(c) || (P != g_buffer.m_P && isdigit(c)); ++P);
	P1 = P;
	if (c == '[') {
		for (++P; isdigit(*P); ++P);
		if (*P == ']') {
			c = *++P;
	}	}
	if (c == '=') {
#ifndef TEST
		c   = *P1;
		*P1 = 0;
		seen_global(g_buffer.m_P, 0);
		*P1 = c;
#endif
		++P;
	} else {
		P = g_buffer.m_P;
	}

	for (; ; ++P) {
		switch (c = *P) {
		case '\'':
			if (in_quote) {
				if (in_quote == '\'') {
					in_quote = 0;
				}
				break;
			}
			in_quote = '\'';
			break;
		case '"':
			if (in_quote) {
				if (in_quote == '"') {
					in_quote = 0;
				}
				break;
			}
			in_quote = '"';
			break;
		case '$':
		case '`':
			if (!in_quote) {
				state = unquoted_state;
				if (!startP) {
					startP = P;
			}	}
			// This takes priority
			P = endSpecial(P) - 1;
			break;
		case '\\':
			if (in_quote != '\'') {
				++P;
			}
			break;
		case '.':
			if (in_quote) {
				break;
			}
			switch (state) {
			case integer_state:
				state = float_state;
				break;
			case float_state:
				state = unquoted_state;
				break;
			}
			state = unquoted_state;
			if (!startP) {
				startP = P;
			}
			break;
		default:
			if (in_quote) {
				break;
			}
			if (xspace(c) || !c || c == '|' || c == '&' || c == ';' || c == '(' || c == ')' || c == '<' || c == '>') {
				if (state == unquoted_state) {
					// add trailing quote
					g_new.m_lth = 0;
					burpn(&g_new, g_buffer.m_P, startP - g_buffer.m_P);
					burpc(&g_new, '"');
					for (P1 = startP; P1 < P; ++P1) {
						if (*P1 == '"') {
							burpc(&g_new, '\\');
						}
						burpc(&g_new, *P1);
					}
					burpc(&g_new, '"');
					burps(&g_new, P);
					exchange(&g_buffer, &g_new);
					goto restart;
				}
				if (!c) {
					return;
				} 
				state = whitespace_state;
				continue;
			}
			switch (state) {
			case unquoted_state:
				continue;
			case start_state:
        	case end_quote_state:
			case whitespace_state:
				startP = P;
			}
			
			if (isdigit(c)) {
				if (state < integer_state) {
					state = integer_state;
				}
				continue;
			}
			if (c == '.') {
				if (state < float_state) {
					state = float_state;
				} else {
					state = unquoted_state;
				}
				continue;
			}
			if (c == '$' || c == '`' || (c == '(' && P[1] == '(')) {
				if (P == startP) {
					state = special_state;
				} else {
					state = unquoted_state;
				}
				P = endSpecial(P) - 1;
				continue;
			}
			if (!isalnum(c) && c != '_' && c != '.') {
				if (state < punctuation_state) {
					state = punctuation_state;
				}
				continue;
			}
			state = unquoted_state;
	}	}
}

static void
emit_variable(char *startP, char *endP, int braced)
{
	char	*P, *P1;
	int		c, c1;

	c 	  = *endP;
	*endP = 0;

	if (braced) {
		P1 = strchr(startP, ':');
		if (P1) {
			if (P1[1] == '-') {
				*P1 = 0;
				burps(&g_new,"'");
				burps(&g_new, P1+2);
				burps(&g_new, "' if dir().count('");
				burps(&g_new, startP);
				burps(&g_new, "') == 0 or ");
				burps(&g_new, startP);
				burps(&g_new, " == '' else ");
				emit_variable(startP, P1, 0);
				*endP = c;
				return;
			}
			*endP = c;
			endP  = P1;
			c     = *endP;
			*endP = 0;
	}	}

	switch (*startP) {
	case '*':
		g_uses_sys = 1;
		burps(&g_new, "\" \".join(sys.argv[1:])");
		break;
	case '@':
		g_uses_sys = 1;
		burps(&g_new, "'\"'+\"\\\" \\\"\".join(sys.argv[1:])+'\"'");
		break;
	case '#':
		// Expands to the number of positional parameters
		g_uses_sys = 1;
		burps(&g_new, "len(sys.argv)");
		break;
	case '$':
		// Expands to the process id of the shell
		g_uses_os = 1;
		burps(&g_new, "os.getpid()");
		break;
	case '!':
		burps(&g_new, "DOLLAR_EXCLAMATION");
		break;
	case '_':
		burps(&g_new, "DOLLAR_UNDERBAR");
		break;
		break;
	case '-':
		burps(&g_new, "DOLLAR_HYPHEN");
		break;
		// Expands to the current option flags
		break;
	case '0':
		burps(&g_new, "__file__");
		break;
	case '1':
	case '2':
	case '3':
	case '4':
	case '5':
	case '6':
	case '7':
	case '8':
	case '9':
		g_uses_sys = 1;
		for (P = startP+1; isdigit(*P) && P < endP; ++P);
		burps(&g_new, "sys.argv[");
		burpn(&g_new, startP, P - startP);
		burps(&g_new, "]");
		break;
	case '?':
		burps(&g_new, "_rc");
		break;
	default:
		burps(&g_new, startP);
#ifndef TEST
		for (P = startP; (c1 = *P) && (isalnum(c1) || c1 == '_'); ++P);
		*P = 0;
		seen_global(startP, 0);
		*P = c1;
#endif
	}
	*endP = c;
}

static void
emitSpecial(char *P, char *endP)
{
	char *P1, *P2;

	if (*P == '$' && P[1] == '(' && P[2] == '(') {
		// Discard the $(..) wrapper
		endP[-1] = 0;
		burps(&g_new, P+2);
		return;
	} 
	if (*P == '`' || (*P == '$' && P[1] == '(')) {
		endP[-1] = 0;
		if (*P == '`') {
			++P;
			for (P1 = P2 = P; *P1; ++P1) {
				if (*P1 == '\\') {
					++P1;
				}
				*P2++ = *P1;
			}
			*P2 = 0;
		} else {
			P  += 2;
		}
		P1 = recursively_fix_string(P,'"');
		g_uses_os = 1;
		burps(&g_new, "os.popen(");
		burps_html(&g_new, P1);
		free(P1);
		burps(&g_new, ").read()");
		return;
	} 
	// A variable that might not look like a string
	if (g_type == FIX_STRING) {
		burps(&g_new, "str(");
	}
	if (*P == '(') {
		// remove ((..)) wrapper
		P       += 2;
		endP[-2] = 0;
		burps(&g_new, P);
		return;
	} 
	if (*P == '[') {
		// remove [...] wrapper
		++P;
		endP[-1] = 0;
		burps(&g_new, P);
		return;
	}
	if (P[1] != '{') {
		emit_variable(P+1, endP, 0);
	} else {
		emit_variable(P+2, endP-1, 1);
	}
	if (g_type == FIX_STRING) {
		burpc(&g_new, ')');
	}
	return;
}

/* Produce a command that can be executed */

static void
addOuterQuotes(void)
{
	char	*P, *endP;
	int 	in_quotes;
	int		c;

	g_new.m_lth = 0;
	in_quotes   = 0;
	for (P = g_buffer.m_P; c = *P; ++P) {
		switch(c) {
		case '`':
		case '(':
		case '$':
			endP = endSpecial(P);
			if (!endP) {
				break;
			}
			if (in_quotes) {
				if (in_quotes == '"') {
					burpc(&g_new, '"');
				}
				burpc(&g_new, '+');
			}
			emitSpecial(P, endP);
			P = endP - 1;
			in_quotes = '$';
			continue;
		}
		if (in_quotes == '$') {
			burpc(&g_new, '+');
			in_quotes = 0;
		}
		if (in_quotes == 0) {
			burpc(&g_new, '"');
			in_quotes = '"';
		}
		if (c == '"' || c == '\\') {
			burpc(&g_new, '\\');
		}
		burpc(&g_new, c);
	}
	if (in_quotes == '"') {
		burpc(&g_new, '"');
	}
	exchange(&g_buffer, &g_new);
	return;
}

/* Break up expansions in strings into separate strings */

static void
splitDoubleQuotes(int in_backquotes)
{
	char	*P, *P1, *P2, *endP, *startP;
	int		in_quote, lth, c;

	in_quote    = 0;
	g_new.m_lth = 0;

	for (P = g_buffer.m_P; c = *P; ++P) {
		burpc(&g_new, c);
		switch (c) {
		case '\'':
			if (in_quote) {
				if (in_quote == '\'') {
					burpc(&g_new, WHITESPACE_MARKER);
					in_quote = 0;
				}
				break;
			}
			g_new.m_lth--;
			burpc(&g_new,'r');
			burpc(&g_new,'\'');
			in_quote = c;
			break;
		case '\\':
			if (in_quote != '\'') {
				++P;
				burpc(&g_new, *P);
			}
			break;
		case '"':
			if (in_quote) {
				if (in_quote == '"') {
					burpc(&g_new, WHITESPACE_MARKER);
					in_quote = 0;
				}
				break;
			}
			startP   = P;
			in_quote = c;
			break;
		case '`':
		case '(':
		case '$':
			endP = endSpecial(P);
			if (!endP) {
				break;
			}
			g_new.m_lth--;	// Discard the character just emitted
			if (P == startP+1) {
				// Discard quote before special term
				g_new.m_lth--;
			} else {
				burpc(&g_new, '"');
				burpc(&g_new, WHITESPACE_MARKER);
			}
			emitSpecial(P, endP);
			burpc(&g_new, WHITESPACE_MARKER);
			P = endP - 1;
			if (*endP == '"') {
				++P;
				in_quote = 0;
			} else {
				burpc(&g_new, '"');
			}
		}
	}
	exchange(&g_buffer, &g_new);
}
	
/* replace {<word1>..<word2>} with range(<word1>, <word2>)
   replace {<word1>..<word2>..<word3>} with range(<word1>,<word2>,<word3>)

def fixRange(x):
    output = x
    rangePatternNoStep=r' \{(\w+)\.\.(\w+)\}'
    matchNoStep = re.search(rangePatternNoStep, output)
    rangePatternStep=r' \{(\w+)\.\.(\w+)\.\.(\w+)\}'
    matchStep = re.search(rangePatternStep, output)
    if matchNoStep != None:
        output = re.sub(rangePatternNoStep, r'range(\1, \2)', output)
    if matchStep != None:
        output = re.sub(rangePatternStep, r'range(\1, \2, \3)', output)
    return output

*/

static void
fixRange(void)
{
	char	*P, *startP, *secondP, *lastP, *endP;
	char	*P1;
	int		inquote;
	int		c, lth, nesting;

restart:
	startP  = 0;
  	inquote = 0;
  	for (P = g_buffer.m_P; c = *P; ++P) {
		switch (c) {
		case '"':
		case '\'':
			if (!inquote) {
				inquote      = c;
				break;
			} 
			if (inquote == c) {
				inquote      = 0;
                startP       = 0;
				nesting      = 0;
			}
			break;
		case '\\':
			if (inquote) {
				++P;
			}
			break;
		case '{':
			if (!startP) {
				startP = P;
				secondP = 0;
				lastP   = 0;
			} else {
				startP = 0;
			}
			break;
		case '.':
			if (startP && P[1] == '.') {
				if (secondP) {
					assert(0);
				} else if (lastP) {
					secondP = lastP;
				}
				lastP = P+2;
				++P;
			}
			break;
		case '}':
			if (!lastP) {
				break;
			}
			g_new.m_lth = 0;
			burpn(&g_new, g_buffer.m_P, startP - g_buffer.m_P);
			burpn(&g_new, "range(", 6);
			if (secondP) {
				endP = secondP;
			} else {
				endP = lastP;
			}
			lth = endP - startP - 3;
			burpn(&g_new, startP+1, lth);
			burpc(&g_new, ',');
			if (secondP) {
				burpn(&g_new, secondP, lastP - secondP - 2);
				burpc(&g_new, ',');
			}
			burpn(&g_new, lastP, P - lastP);
			burpc(&g_new, ')');
			burps(&g_new, P+1);
			exchange(&g_buffer, &g_new);
		}
	}
	return;
}

static void
fixPath(void)
{
	char	*P,	*startP, *P1;
	int		inquote, c, lth;

  	inquote = 0;
	startP  = 0;
  	for (P = g_buffer.m_P; c = *P; ++P) {
		switch (c) {
		case '"':
		case '\'':
			if (!inquote) {
				inquote      = c;
				startP       = P;
				break;
			} 
			if (inquote == c) {
				inquote      = 0;
				startP       = 0;
			}
			break;
		case '\\':
			if (inquote) {
				++P;
			}
			break;
		case '~':
			if (inquote != '"') {
				break;
			}
			g_new.m_lth = 0;
			if (P == startP+1) {
				burpn(&g_new, g_buffer.m_P, startP - g_buffer.m_P);
			} else {
				burpn(&g_new, g_buffer.m_P, P - g_buffer.m_P);
				burps(&g_new, "\" + ");
			}
			g_uses_os = 1;
			burps(&g_new, "os.path.expanduser(\"");
			burpc(&g_new,*P);
			for (P1 = P+1; isalnum(*P1) || *P1 == '_' || *P1 == '-' || *P1 == '.' || *P1 == '/'; ++P1) {
				burpc(&g_new, *P1);
			}
			burps(&g_new, "\")");
			if (*P1 != '"') {
				burps(&g_new, " + \"");
				lth = g_new.m_lth - 2;
				burps(&g_new, P1);
			} else {
				lth = g_new.m_lth - 1;
				burps(&g_new, P1+1);
			}
			exchange(&g_buffer, &g_new);
			P = g_buffer.m_P + lth;
			inquote = 0;
			startP  = 0;
			break;
	}	}
				
	return;
}

static char *
fix_string1(const char *stringP, int separator)
{
  	int 	lth;
	const char	*P0;
	char 	*P, *P1, *P2, *P3;
	int		c;

	/* Strip */
  	for (P0 = stringP; xspace(*P0); ++P0);
	g_buffer.m_lth = 0;
	burps(&g_buffer, P0);
	for (lth = g_buffer.m_lth; lth && xspace(g_buffer.m_P[lth-1]); --lth);
  	g_buffer.m_P[lth] = 0;
	g_buffer.m_lth    = lth;
    if (0 < lth) {
		if (separator == '"') {
			addOuterQuotes();
		} else {
			addDoubleQuotes();
			splitDoubleQuotes(0);
		}
		fixRange();
		fixPath();
	}
	P = g_buffer.m_P;
	burp_init(&g_buffer);
	if (separator == '"') {
		return P;
	}

	for (P1 = P; c = *P1; ++P1) {
		if (c == WHITESPACE_MARKER) {
			for (P3 = P1+1; isspace(*P3); ++P3);
			if (!*P3) {
				break;
			}
			if (separator == '+' && P1[1] == ' ') {
				if (P < P1) {
					if (P1[-1] == '"' && *P3 == '"') {
						g_buffer.m_lth--;
						// Joint two adjacent strings with a blank
						c  = ' ';
						P1 = P3;
						goto advance;
					}
					if (P1[-1] == '\'' && *P3 == 'r' && P3[1] == '\'') {
						g_buffer.m_lth--;
						// Joint two adjacent strings with a blank
						c = ' ';
						P1 = P3+1;
						goto advance;
					}
				} 
				c = g_buffer.m_P[g_buffer.m_lth-1];
				if (c == '\'') {
					--g_buffer.m_lth;
					burps(&g_buffer, " '+");
					P1 = P3-1;
					continue;
				}
				if (c == '"') {
					--g_buffer.m_lth;
					burps(&g_buffer, " \"+");
					P1 = P3-1;
					continue;
				} 
				if (*P3 == '"') {
					burps(&g_buffer, "+\" ");
					P1 = P3;
					continue;
				}
				if (*P3 == 'r' && P3[1] == '\'') {
					burps(&g_buffer, "+r' ");
					P1 = P3 + 1;
					continue;
				}
				burps(&g_buffer, "+\" \"+");
				P1 = P3-1;
				continue;
			} 
			P1 = P3-1;
			c = separator;
		}
advance:
		burpc(&g_buffer, c);
	}
	free(P);
	P = g_buffer.m_P;
	burp_init(&g_buffer);
	return P;
}

static char *
recursively_fix_string(const char *stringP, int separator)
{
	burpT	buffer      = g_buffer;
	burpT	new1        = g_new;
	burpT	save_buffer = g_save_buffer;
	burpT	save_new    = g_save_new;
	char	*P;

	burp_init(&g_buffer);
	burp_init(&g_new);
	burp_init(&g_save_buffer);
	burp_init(&g_save_new);

	P = fix_string1(stringP, separator);

	/* Memory leakage here but don't know where P came from */
	g_buffer      = buffer;
	g_new         = new1;
	g_save_buffer = save_buffer;
	g_save_new    = save_new;
	return(P);
}

char *fix_string(const char *stringP, fix_typeE type)
{
	char *P;

#ifndef TEST
	int save         = g_translate_html;
	g_translate_html = 0;
#endif
	g_type           = type;
	P = fix_string1(stringP,'+');
#ifndef TEST
	g_translate_html = save;
#endif
	return P;
}

#ifdef TEST
int
main(int argc, char **argv)
{
	char	*bufferP   = 0;
	size_t	buffer_lth = 0;
	char	*P;
	int	lth;

	while(0 <= getline(&bufferP, &buffer_lth, stdin)) {
		lth = strlen(bufferP);
		if (lth && bufferP[lth-1] == '\n') {
			bufferP[lth-1] = 0;
		}
		printf("> %s$\n", bufferP);
		P = fix_string(bufferP, FIX_STRING);
		printf("< %s$\n", P);
		free(P);
	}
	return(0);
}
#endif
