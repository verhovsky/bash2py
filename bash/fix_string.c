#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>
#include "burp.h"

static burpT g_buffer      = {0, 0, 0};
static burpT g_new         = {0, 0, 0};
static burpT g_save_buffer = {0, 0, 0};
static burpT g_save_new    = {0, 0, 0};

int g_uses_sys = 0;
int g_uses_os  = 0;

#ifdef TEST
int g_verbose = 0;
#endif

static void
exchange(burpT *oldP, burpT *newP)
{
	burpT	temp;

	temp   = *oldP;
	*oldP  = *newP;
	*newP  = temp;
}

/* Bash:

Enclosing characters in single quotes preserves the literal value of each
character within the quotes. A single quote may not occur between single
quotes, even when preceded by a backslash. 

*/

static void
fixSingleQuotes(void)
{
	char	*P;
	int		in_quote;

restart:
	in_quote = 0;
	for (P = g_buffer.m_P; *P; ++P) {
		switch (*P) {
		case '"':
			if (in_quote) {
				if (in_quote == '"') {
					in_quote = 0;
				}
				break;
			}
			in_quote = '"';
			break;
		case '\\':
			if (in_quote != '\'') {
				++P;
			}
			break;
		case '`':
			if (in_quote != '\'') {
				for (++P; *P != '`'; ++P) {
					if (*P == '\\') {
						++P;
			}	}	}
			break;
		case '\'':
			if (in_quote) {
				if (in_quote == '\'') {
					in_quote = 0;
				}
				break;
			} 
				
			if (P == g_buffer.m_P || P[-1] != 'r') {
				g_new.m_lth = 0;
				burpn(&g_new, g_buffer.m_P, P - g_buffer.m_P);
				burpc(&g_new, 'r');
				burps(&g_new, P);
				exchange(&g_buffer, &g_new);
				goto restart;
			}
			in_quote = '\'';
			break;
		}
	}
}

static char *
endSpecial(char *startP)
{
#ifndef TEST
	extern	void seen_global(const char *nameP);
#endif

	char	*P;
	int		openbrace, closebrace, nesting;
	char	*nameP;
	int		name_lth, c;

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
		nameP = 0;
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
		case '$':
		case '!':
		case '0':
		case '_':
			return P+1;
		default:
			openbrace  = 0;
		}
		if (openbrace) {
			nesting = 0;
			for (; *P; ++P) {
				if (*P == openbrace) {
					++nesting;
                    nameP = P+1;
					continue;
				}
				if (*P == closebrace) {
					if (nameP) {
						name_lth = P - nameP;
					}
					if (!--nesting) {
						++P;
						goto seen;
					}
					continue;
				}
				if (*P == '\\') {
					++P;
				}
		}	}
		if (isdigit(*P)) {
			return P+1;
		}
		nameP = P;
		for (; isalnum(*P) || *P == '_'; ++P);
		name_lth = P - nameP;
seen:
		if (nameP) {
			c = nameP[name_lth];
			nameP[name_lth] = 0;
#ifndef TEST
			seen_global(nameP);
#endif
			nameP[name_lth] = c;
		}
		return(P);
	}
	return 0;
}

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
	if (c == '=') {
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
			if (state == unquoted_state) {
				goto add_trailing_quote;
			}
			break;
		case '`':
			if (!in_quote) {
				state = unquoted_state;
				if (!startP) {
					startP = P;
			}	}
			// This takes priority
			for (++P; *P != '`'; ++P) {
				if (*P == '\\') {
					++P;
			}	}
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
			if (isspace(c) || !c || c == '|' || c == '&' || c == ';' || c == '(' || c == ')' || c == '<' || c == '>' || c== '"') {
				if (state == unquoted_state) {
add_trailing_quote: g_new.m_lth = 0;
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
				state = unquoted_state;
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
compactDoubleQuotes(void)
{
	char	*P;
	int		c, in_quote;

	// If it is a range leave it alone
	if (g_buffer.m_P[0] == '{') {
		return;
	}

	in_quote = 0;
	for (P = g_buffer.m_P; c = *P; ++P) {
		switch (c) {
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
					if (P[1] != '"') {
						in_quote = 0;
					} else {
						memcpy(P, P+2, g_buffer.m_lth - (P - g_buffer.m_P) - 2);
						g_buffer.m_lth -= 2;
						g_buffer.m_P[g_buffer.m_lth] = 0;
					}
				}
				break;
			}
			in_quote = '"';
			break;
		case '`':
			// This takes priority
			for (++P; *P != '`'; ++P) {
				if (*P == '\\') {
					++P;
			}	}
			break;
		case '\\':
			if (in_quote != '\'') {
				++P;
			}
			break;
	}	}
}

/* Break up expansions in strings into separate strings */

static void
splitDoubleQuotes(int in_backquotes)
{
	char	*P, *P1, *endP, *startP;
	int		in_quote, lth, c, c1;

restart:

	in_quote = 0;
	for (P = g_buffer.m_P; c = *P; ++P) {
		switch (c) {
		case '\'':
			if (in_quote) {
				if (in_quote == c) {
					in_quote = 0;
				}
				break;
			}
			for (++P; *P != '\''; ++P);
			break;
		case '\\':
			++P;
			break;
		case '"':
			startP   = P;
			
			for (++P; *P && *P != '"'; ++P) {
				if (*P == '\\') {
					++P;
				}
				endP = endSpecial(P);
				if (!endP) {
					continue;
				}
				g_new.m_lth = 0;
				if (P == startP+1) {
					burpn(&g_new, g_buffer.m_P, startP - g_buffer.m_P);
					if (*P != '`') {
						burps(&g_new, "str(");
						burpn(&g_new, P, endP - P);
						burpc(&g_new, ')');
					} else {
						exchange(&g_buffer, &g_save_buffer);
						exchange(&g_new,    &g_save_new);
						g_buffer.m_lth = 0;
						burpc(&g_buffer, '"');
						for (P1 = P+1; P1 < endP - 1; ++P1) {
							if (*P1 == '"') {
								burpc(&g_buffer,'\\');
							} else if (*P1 == '\\') {
								burpc(&g_buffer, *P1++);
							}
							burpc(&g_buffer,*P1);
						}
						burpc(&g_buffer, '"');
						splitDoubleQuotes(1);
						P1 = g_buffer.m_P;
						exchange(&g_buffer, &g_save_buffer);
						exchange(&g_new,    &g_save_new);
						g_uses_os = 1;
						burps(&g_new, "os.popen(");
						burps(&g_new, P1);
						burps(&g_new, ").read()");
					}

					if (*endP == '"') {
						c1 = endP[1];
						if (c1 && !isspace(c1)) {
							burpc(&g_new, '+');
						}
						burps(&g_new, endP+1);
						exchange(&g_buffer, &g_new);
						goto restart;
					}
					burps(&g_new, " + ");
					burpc(&g_new, '"');
					burps(&g_new, endP);
					exchange(&g_buffer, &g_new);
					goto restart;
				}
				burpn(&g_new, g_buffer.m_P, P - g_buffer.m_P);
				burpc(&g_new, '"');
				burps(&g_new, " + ");
				burpc(&g_new, '"');
				burps(&g_new, P);
				exchange(&g_buffer, &g_new);
				goto restart;
			}
		}
	}
}
	
/* Replace an evaluation of the form $((<eval>)) by (<eval>)

def fixArithmeticExpansion(x):
    return re.sub(r'\$\((\(.*\))\)', r"\1", x)
*/

static void
fixArithmeticExpansion(void)
{
	char	*P, *startP;
	int		inquote, c, nesting, lth;

restart:
	startP  = 0;
  	inquote = 0;
	nesting = 0;
  	for (P = g_buffer.m_P; c = *P; ++P) {
		if (!inquote) {
			switch (c) {
			case '"':
			case '\'':
				inquote = c;
				break;
			case '$':
				if (P[1] == '(' && P[2] == '(') {
					startP = P;
					P += 2;
				}
				break;
			case '(':
				if (startP) {
					++nesting;
				}
				break;
			case ')':
				if (startP) {
					if (nesting) {
						--nesting;
						break;
					}
					if (P[1] == ')') {
						lth = P - startP - 2;
						memcpy(startP, startP + 2, lth);
						startP += lth;
						lth = strlen(P+1);
						memcpy(startP,P+1,lth);
						startP += lth;
						*startP = 0;
						goto restart;
			}	}	}
		} else {
			if (c == '\\') {
				++P;
			} else if (c == inquote) {
				inquote = 0;
			}
		}
	}
	return;
}

/* replace `<command>` by os.popen('<command>').read()

def fixBackticksAndEval(x):
    return re.sub(r'`(.*?)`', r" os.popen('\1').read() ", x)
*/

static void
fixBackticks(void)
{
	char	*P, *startP;
	char	*P1;
	int		inquote, c, lth;

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
			}
			break;
		case '\\':
			if (inquote) {
				++P;
			}
			break;
		case '`':
			if (!startP) {
				startP = P;
				break;
			}
			g_uses_os = 1;
			g_new.m_lth = 0;
			burpn(&g_new, g_buffer.m_P, startP - g_buffer.m_P);
			burps(&g_new, " os.popen(\"");
			for (P1 = startP + 1; P1 < P; ++P1) {
				if (*P1 == '"') {
					burpc(&g_new, '\\');
				} else if (*P1 == '\\') {
					burpc(&g_new, *P1++);
				}
				burpc(&g_new, *P1);
			}
			burps(&g_new, "\").read() ");
			burps(&g_new, P+1);
			exchange(&g_buffer, &g_new);
			goto restart;
		}
	}
	return;
}

/* replace $(<command>) by os.popen('<command>').read()

def fixEval(x):
    return re.sub( r'\$\((.*?)\)', r" os.popen('\1').read() ", x)
*/

static void
fixEval(void)
{
	char	*P, *startP;
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
		case '$':
			if (P[1] == '(') {
				startP = P;
				++P;
			}
			break;
		case '(':
			if (startP) {
				++nesting;
			}
			break;
		case ')':
			if (!startP) {
				break;
			}
			if (nesting) {
				--nesting;
				break;
			}
			g_uses_os = 1;
			g_new.m_lth = 0;
			burpn(&g_new, g_buffer.m_P, startP - g_buffer.m_P);
			burps(&g_new, " os.popen('");
			burpn(&g_new, startP + 2, P - startP - 2);
			burps(&g_new, "').read() ");
			burps(&g_new, P+1);
			exchange(&g_buffer, &g_new);
			goto restart;
		}
	}
	return;
}

/* Replace $<number> by sys.argv[<number>]

def fixArguments(x):
    return re.sub(r'\$(\d+)', r"sys.argv[\1]", x)
*/

static void
fixArguments(void)
{
	char	*P, *startP;
	char	*P1;
	int		inquote;
	int		c, lth;

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
			}
			break;
		case '\\':
			if (inquote) {
				++P;
			}
			break;
		case '$':
			switch (P[1]) {
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
				for (startP = P++; isdigit(*P); ++P);
				g_new.m_lth = 0;
				burpn(&g_new, g_buffer.m_P, startP - g_buffer.m_P);
				burps(&g_new, " sys.argv[");
				burpn(&g_new, startP + 1, P - startP - 1);
				burps(&g_new, "] ");
				burps(&g_new, P);
				exchange(&g_buffer, &g_new);
				goto restart;
			case '?':
				startP = P++;
				g_new.m_lth = 0;
				burpn(&g_new, g_buffer.m_P, startP - g_buffer.m_P);
				burps(&g_new, " _rc ");
				burps(&g_new, P+1);
				exchange(&g_buffer, &g_new);
				goto restart;
				break;
			}
		}
	}
	return;
}

/* replace ${<variable>} with <variable> if not a number
                         else sys.argv[<number>]

def fixBracketVariables(x):
    return re.sub(r'\$\{([a-zA-Z_]\w*)\}', r"\1", x)
*/

static void
fixBracketVariables(void)
{
	char	*P, *startP;
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
		case '$':
			if (P[1] == '{') {
				startP = P;
				++P;
			}
			break;
		case '{':
			if (startP) {
				++nesting;
			}
			break;
		case '}':
			if (!startP) {
				break;
			}
			if (nesting) {
				--nesting;
				break;
			}
			for (P1 = startP+2; ; ++P1) {
				if (P1 == P) {
					g_uses_sys = 1;
					g_new.m_lth = 0;
					burpn(&g_new, g_buffer.m_P, startP - g_buffer.m_P);
					burps(&g_new, "sys.argv[");
					burpn(&g_new, startP+2, P - startP - 2);
					burpc(&g_new, ']');
					burps(&g_new, P + 1);
					exchange(&g_buffer, &g_new);
					goto restart;
				}
				if (!isdigit(*P1)) {
					break;
			}	}

			lth = P - startP - 2;
			memcpy(startP, startP+2, lth);
			startP += lth;
			lth = strlen(P+1);
			memcpy(startP, P+1, lth);
			startP += lth;
			*startP = 0;
			g_buffer.m_lth = startP - g_buffer.m_P;
			goto restart;
		}
	}
	return;
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

/* replace $[<value>] by <value>

def fixSquareBrackets(x):
    return re.sub(r'\$\[(.*?)\]', r'\1', x)

*/

static void
fixSquareBrackets(void)
{
	char	*startP, *P;
	int		inquote, c, nesting, lth;

restart:
  	inquote = 0;
	startP  = 0;
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
			}
			break;
		case '\\':
			if (inquote) {
				++P;
			}
			break;
		case '$':
			if (P[1] == '[') {
				startP = P;
				nesting = 0;
			}
			break;
		case '[':
			++nesting;
			break;
		case ']':
			if (!startP) {
				break;
			}
			if (nesting) {
				--nesting;
			}
			lth = P - startP - 3;
			memcpy(startP, startP+2,lth);
			startP += lth;
			lth     = strlen(P+1);
			memcpy(startP, P+1, lth);
			startP += lth;
			*startP = 0;
			g_buffer.m_lth = startP - g_buffer.m_P;
			goto restart;
		}
	}
	return;
}

/* 
def fixVariables(x):
    return re.sub( r'\$([a-zA-Z_]\w*)', r"\1", x)
*/

static void
fixVariables(void)
{
	char	*P;
	int		inquote, c, lth;

restart:
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
			}
			break;
		case '\\':
			if (inquote) {
				++P;
			}
			break;
		case '$':
			lth = strlen(P+1);
			memcpy(P, P+1, lth);
			P += lth;
			*P = 0;
			--g_buffer.m_lth;
			goto restart;
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

char *
fix_string(const char *stringP)
{
  	int 		lth;
	const char 	*P;
	char		*P1;


	/* Strip */
  	for (P = stringP; isspace(*P); ++P);
	g_buffer.m_lth = 0;
	burps(&g_buffer, P);
	for (lth = g_buffer.m_lth; lth && isspace(g_buffer.m_P[lth-1]); --lth);
  	g_buffer.m_P[lth] = 0;
	g_buffer.m_lth    = lth;
    if (lth < 1) {
		goto done;
	}

	fixSingleQuotes();
#ifdef TEST
	if (g_verbose) {
		printf("  fixSingleQuotes> %s\n", g_buffer.m_P);
	}
#endif
	addDoubleQuotes();
#ifdef TEST
	if (g_verbose) {
		printf("  addDoubleQuotes> %s\n", g_buffer.m_P);
	}
#endif
	splitDoubleQuotes(0);
#ifdef TEST
	if (g_verbose) {
		printf("splitDoubleQuotes> %s\n", g_buffer.m_P);
	}
#endif
	fixArithmeticExpansion();
#ifdef TEST
	if (g_verbose) {
		printf("    fixArithmetic> %s\n", g_buffer.m_P);
	}
#endif
	fixBackticks();
#ifdef TEST
	if (g_verbose) {
		printf("     fixBackTicks> %s\n", g_buffer.m_P);
	}
#endif
	fixEval();
#ifdef TEST
	if (g_verbose) {
		printf("          fixEval> %s\n", g_buffer.m_P);
	}
#endif
	fixArguments();
#ifdef TEST
	if (g_verbose) {
		printf("     fixArguments> %s\n", g_buffer.m_P);
	}
#endif
	fixBracketVariables();
#ifdef TEST
	if (g_verbose) {
		printf("   fixBracketVars> %s\n", g_buffer.m_P);
	}
#endif
	fixRange();
#ifdef TEST
	if (g_verbose) {
		printf("         fixRange> %s\n", g_buffer.m_P);
	}
#endif
	fixSquareBrackets();
#ifdef TEST
	if (g_verbose) {
		printf("fixSquareBrackets> %s\n", g_buffer.m_P);
	}
#endif
	fixVariables();
#ifdef TEST
	if (g_verbose) {
		printf("     fixVariables> %s\n", g_buffer.m_P);
	}
#endif
	fixPath();
#ifdef TEST
	if (g_verbose) {
		printf("          fixPath> %s\n", g_buffer.m_P);
	}
#endif
	compactDoubleQuotes();
#ifdef TEST
	if (g_verbose) {
		printf("comptDoubleQuotes> %s\n", g_buffer.m_P);
	}
#endif
done:
	P1             = g_buffer.m_P;
	g_buffer.m_P   = 0;
	g_buffer.m_lth = 0;
	g_buffer.m_max = 0;
	return P1;
}

#ifdef TEST
int
main(int argc, char **argv)
{
	char	*bufferP   = 0;
	size_t	buffer_lth = 0;
	char	*P;
	int	lth;

	if (argc == 2) {
		if (!strcmp(argv[1], "-v")) {
			g_verbose = 1;
	}	}
	while(0 <= getline(&bufferP, &buffer_lth, stdin)) {
		lth = strlen(bufferP);
		if (lth && bufferP[lth-1] == '\n') {
			bufferP[lth-1] = 0;
		}
		printf("> %s$\n", bufferP);
		P = fix_string(bufferP);
		printf("< %s$\n", P);
		free(P);
	}
	return(0);
}
#endif
