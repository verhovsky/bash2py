#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>
#include "burp.h"
#include "fix_string.h"

static burpT g_buffer      = {0, 0, 0};
static burpT g_new         = {0, 0, 0};

int g_uses_sys        = 0;
int g_uses_os         = 0;
int g_uses_subprocess = 0;
int	g_uses_signal     = 0;

fix_typeE	g_type;
int			g_in_array;
extern int  g_translate_html;

#ifndef TEST
extern	void seen_global(const char *nameP, int local);
#endif

static char *recursively_fix_string(const char *stringP, int separator);

#define START_QUOTE_MARKER 1
#define END_QUOTE_MARKER 2

static void
exchange(burpT *oldP, burpT *newP)
{
	burpT	temp;

	temp   = *oldP;
	*oldP  = *newP;
	*newP  = temp;
}

static char *
endSpecial(char *startP, char **part2PP)
{

	char	*P, *P1;
	int		openbrace, closebrace, nesting, in_quote;
	int		c;

	switch (*startP) {
	case '`':
		P        = startP + 1;
		if (part2PP) {
			*part2PP = P;
		}
		for (P = startP+1; (c = *P) != '`'; ++P) {
			if (!c) {
				return 0;
			}
			if (c == '\\') {
				++P;
		}	}
		return P+1;
	case '(':
		if (part2PP) {
			*part2PP = P;
		}
		if (startP[1] == '(') {
			goto brace;
		}
		break;
	case '$':
		P = startP + 1;
		if (part2PP) {
			*part2PP = P;
		}
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
			++P;
			if (part2PP) {
				*part2PP = P;
			}
			goto check_array;
		default:
			for (;isalnum(*P) || *P == '_'; ++P);
			if (part2PP) {
				*part2PP = P;
			}
check_array:
			if (*P != '[') {
				return P;
			}
			openbrace  = '[';
			closebrace = ']';
		}
		nesting  = 0;
		in_quote = 0;
		for (; c = *P; ++P) {
			if (!in_quote) {
				if (c == openbrace) {
					++nesting;
					continue;
				}
				if (c == closebrace) {
					if (!--nesting) {
						++P;
						goto check_array;
					}
					continue;
			}	}
			switch (c) {
			case '\\':
				++P;
				break;
			case '"':
				if (in_quote) {
					in_quote = 0;
				} else {
					in_quote = 1;
				}
				break;
			case START_QUOTE_MARKER:
				in_quote = 1;
				break;
			case END_QUOTE_MARKER:
				in_quote = 0;
				break;
			}
		}
	}
	return 0;
}


/* Replace single quotes by double quotes escaping contents correctly
 * this simplifies things since no longer need to worry about single quote
 */

static void
replaceSingleQuotes(void)
{
	int 	in_quotes;
	unsigned char c, c1;
	char	*P;

	in_quotes   = 0;
	g_new.m_lth = 0;
	for (P = g_buffer.m_P; c = *((unsigned char *) P); ++P) {
		switch (c) {
		case '"':
			if (!in_quotes) {
				in_quotes = c;
			} else if (in_quotes == c) {
				in_quotes = 0;
			} else {
				burpc(&g_new, '\\');
			}
			break;
		case '\'':
			if (!in_quotes) {
				in_quotes = c;
				c         = '"';
			} else if (in_quotes == c) {
				in_quotes = 0;
				c         = '"';
			}
			break;
		case '\\':
		case '$':
		case '`':
			if (in_quotes == '\'') {
				burpc(&g_new, '\\');
			}
			break;
		default:
			if (in_quotes != '\'') {
				break;
			}
			if (!isprint(c)) {
				switch (c) {
				case '\a':
					burps(&g_new, "\\a");
					break;
				case '\b':
					burps(&g_new, "\\b");
					break;
				case '\f':
					burps(&g_new, "\\f");
					break;
				case '\n':
					burps(&g_new, "\\n");
					break;
				case '\r':
					burps(&g_new, "\\r");
					break;
				case '\t':
					burps(&g_new, "\\t");
					break;
				default:
					burps(&g_new, "\\x");
					c1 = c >> 4;
					if (c1 < 10) {
						c1 += '0';
					} else {
						c1 += 'a'-10;
					}
					burpc(&g_new, c1);
					c1 = c & 0xF;
					if (c1 < 10) {
						c1 += '0';
					} else {
						c1 += 'a'-10;
					}
					burpc(&g_new, c1);
				}
				continue;
		}	}
		burpc(&g_new, c);
	}
	exchange(&g_buffer, &g_new);
}

/* Convert double quotes so that all non-escaped bracketting double quotes
 * are given clear internal codes  to simplify subsequent logic */

static void
markQuotes(void)
{
	int 	in_quotes, c, lth;
	char	*P, *P1, *P3;

	in_quotes   = 0;
	g_new.m_lth = 0;
	for (P = g_buffer.m_P; c = *P; ++P) {
		switch (c) {
		case '"':
			if (!in_quotes) {
				in_quotes = c;
				c = START_QUOTE_MARKER;
			} else if (in_quotes) {
				in_quotes = 0;
				c = END_QUOTE_MARKER;
			} 
			break;
		case '\\':
			burpc(&g_new, '\\');
			c = *++P;
			break;
		case '$':
		case '`':
			P1 = endSpecial(P, &P3);
			if (!P1) {
				break;
			}
			burpn(&g_new, P, P3-P);
			if ((lth = (P1 - P3)) > 0) {
				burpT	save_buffer, save_new;

				save_buffer = g_buffer;
				save_new    = g_new;

				burp_init(&g_buffer);
				burp_init(&g_new);
				burpn(&g_buffer, P3, lth);
				markQuotes();
				P3 = g_buffer.m_P;
				// free(g_new.m_P);
				g_new    = save_new;
				burps(&g_new, P3);
				assert(P3 == g_buffer.m_P);
				// free(g_buffer.m_P);
				g_buffer = save_buffer;
			} 
			P = P1 - 1;
			continue;
		}
		burpc(&g_new, c);
	}
	exchange(&g_buffer, &g_new);
}

static int
punctuationChar(int c)
{
	switch (c) {
	case '.':
	case '_':
	case '-':
	case '+':
	case '~':
	case '/':
		return 0;
	default:
		if (isalnum(c)) {
			return 0;
		}
		return 1;
	}
	return 1;
}

/* Turn anything not quoted that needs to be quoted into being double quoted */

static void
addDoubleQuotes(void)
{
	typedef enum {
		start_state       = 0,
		punctuation_state = 1,
		integer_state     = 2,
		float_state       = 3,
		unquoted_state    = 4,
		quoted_state      = 5
	} stateT;

	char	*P, *startP, *start_textP, *P1, *P3;
	int		c, lth, in_array;
	stateT	state;

	// If it is a range leave it alone
	if (g_buffer.m_P[0] == '{') {
		return;
	}

	state       = start_state;
	start_textP = 0;
	g_new.m_lth = 0;

	for (P = startP = g_buffer.m_P; (c = *P) == '_' || isalpha(c) || (P != g_buffer.m_P && isdigit(c)); ++P);
	P1 = P;
	if (P != g_buffer.m_P) {
check_array:
		if (c == '[') {
			in_array = 1;
			for (++P; c = *P; ++P) {
				switch (c) {
				case ']':
					if (--in_array) {
						continue;
					}
					c = *++P;
					goto check_array;
				case '[':
					++in_array;
				default:
					continue;
				}
				break;
	}	}	}

	switch (c) {
    case '+':
	case '-':
		if (P[1] != '=') {
			P = g_buffer.m_P;
			break;
		}
	case '=':
#ifndef TEST
		c   = *P1;
		*P1 = 0;
		seen_global(g_buffer.m_P, 0);
		*P1 = c;
#endif
		P = P1;
		break;
	default:
		P = g_buffer.m_P;
	}

	for (; ; ++P) {
		switch (c = *P) {
		case START_QUOTE_MARKER:
			state       = quoted_state;
			start_textP = 0;
			break;
		case END_QUOTE_MARKER:
			state       = start_state;
			start_textP = 0;
			break;
		case '$':
		case '`':
			P1 = endSpecial(P, &P3);
			if (!P1) {
				break;
			}
			if (c == '`' || (P[1] == '(' && P[2] != '(')) {
				P3 = P1;
			}
			if (state < unquoted_state) {
				if (!start_textP) {
					start_textP = P;
				}
				if (integer_state <= state || !punctuationChar(*P1)) {
					state = unquoted_state;
				}
			}
			if (state == unquoted_state) {
				if (startP <= start_textP) {
					burpn(&g_new, startP, start_textP - startP);
					burpc(&g_new, START_QUOTE_MARKER);
					startP = start_textP;
			}	}
			burpn(&g_new, startP, P3 - startP);
			lth = P1 - P3;
			if (lth > 0) {
				burpT	save_buffer, save_new;

				save_buffer = g_buffer;
				save_new    = g_new;

				burp_init(&g_buffer);
				burp_init(&g_new);
				burpn(&g_buffer, P3, lth);
				addDoubleQuotes();
				P3 = g_buffer.m_P;
				// free(g_new.m_P);
				g_new    = save_new;

				burps(&g_new, P3);
				assert(P3 == g_buffer.m_P);
				// free(g_buffer.m_P);
				g_buffer = save_buffer;
			} 
			startP      = P1;
			P           = P1 - 1;
			break;
		case '-':
			if (state == quoted_state) {
				break;
			}
			if (!start_textP) {
				start_textP = P;
			}
			if (state <= punctuation_state) {
				state = integer_state;
			} else {
				state = unquoted_state;
			}
			break;
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
			if (state == quoted_state) {
				break;
			}
			if (!start_textP) {
				start_textP = P;
			}
			if (state < integer_state) {
				state = integer_state;
			}
			break;
		case '.':
			if (state == quoted_state) {
				break;
			}
			if (!start_textP) {
				start_textP = P;
			}
			if (state < float_state) {
				state = float_state;
			} else {
				state = unquoted_state;
			}
			break;
		default:
			if (state == quoted_state) {
				break;
			}
			if (!punctuationChar(c)) {
				if (!start_textP) {
					start_textP = P;
				}
				state = unquoted_state;
				break;
			}

			if (state == unquoted_state) {
				if (startP <= start_textP) {
					burpn(&g_new, startP, start_textP - startP);
					burpc(&g_new, START_QUOTE_MARKER);
					startP = start_textP;
				}
				burpn(&g_new, startP, P - startP);
				burpc(&g_new, END_QUOTE_MARKER);
				startP      = P;
				start_textP = 0;
				state       = start_state;
			}
			if (!c) {
				burps(&g_new, startP);
				exchange(&g_buffer, &g_new);
				return;
			} 
			state = punctuation_state;
	}	}
}

static void emitSpecial(char *startP, char *endP);

static void
emit_variable(char *startP, char *endP, int braced)
{
	char	*P, *P1;
	int		c, c1, save_type;

	c 	  = *endP;
	*endP = 0;

	if (braced) {
		P1 = strchr(startP, ':');
		if (P1) {
			switch (P1[1]) {
			case '-':
				*P1 = 0;
				burpc(&g_new, '\'');
				burps(&g_new, P1+2);
				burps(&g_new, "' if ");
				switch (*startP) {
				case '*':
				case '@':
					burps(&g_new, "len(sys.argv) < 2");
					break;
				default:
					burps(&g_new, "dir().count('");
					burps(&g_new, startP);
					burps(&g_new, "') == 0");
					if (P1[2]) {
						burps(&g_new, " or ");
						burps(&g_new, startP);
						burps(&g_new, " == ''");
					}
					break;
				}
				burps(&g_new, " else ");
				emit_variable(startP, P1, 0);
				*endP = c;
				return;
			case '+':
				*P1 = 0;
				burps(&g_new, "'' if ");
				switch (*startP) {
				case '*':
				case '@':
					burps(&g_new, "len(sys.argv) < 2");
					break;
				default:
					burps(&g_new, "dir().count('");
					burps(&g_new, startP);
					burps(&g_new, "') == 0");
					burps(&g_new, " or ");
					burps(&g_new, startP);
					burps(&g_new, " == ''");
				}
				burps(&g_new, " else ");
				P1 = recursively_fix_string(P1+2, '+');
				burps(&g_new, P1);
				*endP = c;
				return;
			case '=':
				*P1 = 0;
				emit_variable(startP, P1, 0);
				burps(&g_new,"=('");
				burps(&g_new, P1+2);
				burps(&g_new, "' if dir().count('");
				burps(&g_new, startP);
				burps(&g_new, "') == 0 or ");
				burps(&g_new, startP);
				burps(&g_new, " == '' else ");
				emit_variable(startP, P1, 0);
				burpc(&g_new, ')');
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
		for (P = startP; (c1 = *P) && (isalnum(c1) || c1 == '_'); ++P);
		*P = 0;
#ifndef TEST
		if (P != startP) {
			seen_global(startP, 0);
		}
#endif
		burps(&g_new, startP);
		*P = c1;
		for (;  c1 = *P; ) {
			switch (c1) {
			case '`':
			case '$':
				P1 = endSpecial(P, 0);
				if (!P1) {
					break;
				}
				emitSpecial(P, P1);
				P = P1;
				continue;
			}
			burpc(&g_new, c1);
			++P;
		}
	}
	*endP = c;
}

static void
emitSpecial(char *P, char *endP)
{
	char *P1, *P2;

	if (*P == '$' && P[1] == '(' && P[2] == '(') {
		fix_typeE save_type;
		// Discard the $(..) wrapper
		endP[-1] = 0;
		save_type = g_type;
		g_type    = FIX_INT;
		P1 = recursively_fix_string(P+2,'"');
		g_type    = save_type;
		burps(&g_new, P1);
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
		burps(&g_new, ").read()");
		free(P1);
		return;
	} 
	// A variable that might not look like a string
#if 0
	if (g_type == FIX_STRING && !g_in_array) {
		burps(&g_new, "str(");
	}
#endif
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
#if 0
	if (g_type == FIX_STRING && !g_in_array) {
		burpc(&g_new, ')');
	}
#endif
	return;
}

/* Produce a command that can be executed as a string */

static void
addOuterQuotes(void)
{
	char	*P, *endP;
	int 	in_quotes, add_plus;
	int		c;

	g_new.m_lth = 0;
	in_quotes   = 0;
	add_plus    = 0;
	for (P = g_buffer.m_P; c = *P; ++P) {
		if (add_plus) {
			// Only add in the + is something after the special
			burpc(&g_new, '+');
			add_plus = 0;
		}
		switch(c) {
		case '`':
		case '(':
		case '$':
			endP = endSpecial(P, 0);
			if (!endP) {
				break;
			}
			if (in_quotes && g_type != FIX_INT) {
				burpc(&g_new, END_QUOTE_MARKER);
				burps(&g_new, "+str(");
			}
			emitSpecial(P, endP);
			if (in_quotes && g_type != FIX_INT) {
				burpc(&g_new, ')');
			}
			P = endP - 1;
			in_quotes = 0;
			if (g_type != FIX_INT) {
				add_plus  = 1;
			}
			continue;
		}
		if (!in_quotes && g_type != FIX_INT) {
			burpc(&g_new, START_QUOTE_MARKER);
			in_quotes = 1;
		}
		switch (c) {
		case START_QUOTE_MARKER:
		case END_QUOTE_MARKER:
		case '"':
		case '\\':
			burpc(&g_new, '\\');
			break;
		}
		burpc(&g_new, c);
	}
	if (in_quotes) {
		burpc(&g_new, END_QUOTE_MARKER);
	}
	exchange(&g_buffer, &g_new);
	return;
}

/* Break up expansions in strings into separate strings */

static void
splitDoubleQuotes(void)
{
	char	*P, *P1, *P2, *endP;
	int		in_quote, lth, make_string, c;

	in_quote    = 0;
	g_in_array  = 0;
	g_new.m_lth = 0;

	for (P = g_buffer.m_P; c = *P; ++P) {
		burpc(&g_new, c);
		switch (c) {
		case '\\':
			// Move over this character
			++P;
			burpc(&g_new, *P);
			break;
		case '[':
			if (!in_quote) {
				++g_in_array;
			}
			break;
		case ']':
			if (!in_quote) {
				--g_in_array;
			}
			break;
		case START_QUOTE_MARKER:
			in_quote = '"';
			break;
		case END_QUOTE_MARKER:
			in_quote = 0;
			break;
		case '`':
		case '(':
		case '$':
			endP = endSpecial(P, 0);
			if (!endP) {
				break;
			}
			g_new.m_lth--;	// Discard the character just emitted
			make_string = 0;
			if (in_quote) {
				if (P[-1] == START_QUOTE_MARKER) {
					// Discard quote before special term
					g_new.m_lth--;
				} else {
					burpc(&g_new, END_QUOTE_MARKER);
					burps(&g_new, " + ");
					make_string = 1;
			}	}
			switch (*endP) {
			case END_QUOTE_MARKER:
				if (!endP[1]) {
					make_string = 1;
				}
				break;
			default:
				if (*endP && in_quote) {
					make_string = 1;
			}	}
			if (make_string) {
				burps(&g_new, "str(");
			}
			emitSpecial(P, endP);
			if (make_string) {
				burpc(&g_new, ')');
			}
			if (*endP == END_QUOTE_MARKER) {
				++endP;
				in_quote = 0;
			}
			if (!*endP) {
				goto done;
			}
			P = endP - 1;
			if (in_quote) {
				burps(&g_new, " + ");
				*P-- = START_QUOTE_MARKER;
			}
		}
	}
done:
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
	char	*P, *start_rangeP, *startP, *secondP, *lastP, *endP;
	char	*P1;
	int		in_quote;
	int		c, lth, nesting;

	start_rangeP = 0;
  	in_quote     = 0;
	g_new.m_lth  = 0;
  	for (P = startP = g_buffer.m_P; c = *P; ++P) {
		switch (c) {
		case START_QUOTE_MARKER:
			in_quote = '"';
			break;
		case END_QUOTE_MARKER:
			in_quote     = 0;
            start_rangeP = 0;
			nesting      = 0;
			break;
		case '\\':
			if (in_quote) {
				++P;
			}
			break;
		case '{':
			if (!start_rangeP) {
				start_rangeP = P;
				secondP      = 0;
				lastP        = 0;
			} else {
				start_rangeP = 0;
			}
			break;
		case '.':
			if (start_rangeP && P[1] == '.') {
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
			burpn(&g_new, startP, start_rangeP - startP);
			burpn(&g_new, "range(", 6);
			if (secondP) {
				endP = secondP;
			} else {
				endP = lastP;
			}
			lth = endP - start_rangeP - 3;
			burpn(&g_new, start_rangeP+1, lth);
			burpc(&g_new, ',');
			if (secondP) {
				burpn(&g_new, secondP, lastP - secondP - 2);
				burpc(&g_new, ',');
			}
			burpn(&g_new, lastP, P - lastP);
			burpc(&g_new, ')');
			start_rangeP = 0;
			startP       = P + 1;
		}
	}
	burps(&g_new, startP);
	exchange(&g_buffer, &g_new);
	return;
}

static void
fixPath(void)
{
	char	*P,	*startP, *P1;
	int		in_quote, c, lth;

  	in_quote    = 0;
	g_new.m_lth = 0;
  	for (P = startP = g_buffer.m_P; c = *P; ++P) {
		switch (c) {
		case START_QUOTE_MARKER:
			in_quote     = 1;
			break;
		case END_QUOTE_MARKER:
			in_quote     = 0;
			break;
		case '~':
			if (!in_quote) {
				break;
			}
			if (P[-1] == START_QUOTE_MARKER) {
				// Discard opening quote
				burpn(&g_new, startP, P - startP - 1);
			} else {
				burpn(&g_new, startP, P - startP);
				burpc(&g_new, END_QUOTE_MARKER);
				burps(&g_new, " + ");
			}
			g_uses_os = 1;
			burps(&g_new, "os.path.expanduser(\"~");
			for (P1 = P+1; isalnum(*P1) || *P1 == '_' || *P1 == '-' || *P1 == '.' || *P1 == '/'; ++P1) {
				burpc(&g_new, *P1);
			}
			burps(&g_new, "\")");
			if (*P1 == END_QUOTE_MARKER) {
				++P1;
				in_quote = 0;
			}
			startP = P1;
			if (!*P1) {
				goto done;
			}
			if (in_quote) {
				burps(&g_new, " + ");
				startP = --P1;
				*P1 = START_QUOTE_MARKER;
			}
			P = startP;
	}	}
done:
	burps(&g_new, startP);
	exchange(&g_buffer, &g_new);
	return;
}

static void
unmarkQuotes(void)
{
	char	*P;

	for (P = g_buffer.m_P; ; ++P) {
		switch (*P) {
		case 0:
			return;
		case START_QUOTE_MARKER:
		case END_QUOTE_MARKER:
			*P = '"';
}	}	}

/* Transforms g_buffer
 * Separator can be:
	 + indicating concatonate parts (normal behaviour)
     " indicating we are embedding the contents of this string inside popen
 */
static char *
fix_string1(int separator)
{
  	int 	lth;
	const char	*P0;
	char 	*P, *P1, *P2, *P3;
	int		c;

    if (0 < g_buffer.m_lth) {
		replaceSingleQuotes();
		if (g_type != FIX_INT) {
			markQuotes();
		}
		if (separator == '"') {
            addOuterQuotes();
        } else {
            addDoubleQuotes();
            splitDoubleQuotes();
        }
		fixRange();
		fixPath();
	}
	if (separator == '"') {
		unmarkQuotes();
		return g_buffer.m_P;
	}

	for (P = g_buffer.m_P; P1 = strchr(P, END_QUOTE_MARKER); P = P1+1) {
		for (P3 = P1+1; isspace(*P3); ++P3);
		if (!*P3) {
			break;
		}
		if (*P3 == START_QUOTE_MARKER) {
			// Join two adjacent strings with a blank
			memcpy(P1, P3, g_buffer.m_lth - (P3 - g_buffer.m_P));
			*P1 = ' ';
			g_buffer.m_lth -= (P3 - P1);
			g_buffer.m_P[g_buffer.m_lth] = 0;
		}
	}
	unmarkQuotes();
	return g_buffer.m_P;
}

static char *
recursively_fix_string(const char *stringP, int separator)
{
	burpT	save_buffer = g_buffer;
	burpT	save_new    = g_new;
	char	*P;

	if (!*stringP) {
		return stringP;
	}

	burp_init(&g_buffer);
	burp_init(&g_new);

	burps(&g_buffer, stringP);
	P = fix_string1(separator);
	assert(P = g_buffer.m_P);
	free(g_new.m_P);
	g_new    = save_new;
	g_buffer = save_buffer;
	return(P);
}

char *fix_string(const char *stringP, fix_typeE type)
{
	const char *P0;
	char 		*P;
	int			lth;

#ifndef TEST
	int save         = g_translate_html;
	g_translate_html = 0;
#endif
	g_type           = type;

  	for (P0 = stringP; isspace(*P0); ++P0);
	g_buffer.m_lth = 0;
	burps(&g_buffer, P0);
	for (lth = g_buffer.m_lth; lth && isspace(g_buffer.m_P[lth-1]); --lth);
  	g_buffer.m_P[lth] = 0;
	g_buffer.m_lth    = lth;

	P = fix_string1('+');
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
	}
	return(0);
}
#endif
