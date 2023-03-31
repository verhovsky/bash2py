/* translate.c -- Converting bash commands to corresponding Python statements. */

/* Copyright (C) 1989-2010 Free Software Foundation, Inc.

   This file is part of GNU Bash, the Bourne Again SHell.

   Bash is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   Bash is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with Bash.  If not, see <http://www.gnu.org/licenses/>.
 */

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
#include "bashintl.h"

#include "shell.h"
#include "flags.h"
#include <y.tab.h>	/* use <...> so we pick it up from the build directory */

#include "shmbutil.h"
#include "burp.h"

#include "builtins/common.h"

#if !HAVE_DECL_PRINTF
extern int printf __P((const char *, ...));	/* Yuck.  Double yuck. */
#endif

extern int indirection_level;

static int indentation;
static int indentation_amount = 4;

#if defined (PREFER_STDARG)
typedef void PFUNC __P((const char *, ...));

#else
#define PFUNC VFunction
static void fprintf(outputF, );
static void xprintf ();
#endif

static void reset_locals __P((void));
static void newline __P((char *));
static void indent __P((int));

static void make_command_string_internal __P((COMMAND *));
static void print_case_clauses __P((PATTERN_LIST *));
static void print_redirection_list __P((REDIRECT *, SIMPLE_COM *));
static void print_redirection __P((REDIRECT *));
static void print_heredoc_header __P((REDIRECT *));
static void print_heredoc_body __P((REDIRECT *));
static void print_heredocs __P((REDIRECT *));
static void print_deferred_heredocs __P((const char *));

static void print_for_command __P((FOR_COM *));
#if defined (ARITH_FOR_COMMAND)
static void print_arith_for_command __P((ARITH_FOR_COM *));
#endif
#if defined (SELECT_COMMAND)
static void print_select_command __P((SELECT_COM *));
#endif
static void print_group_command __P((GROUP_COM *));
static void print_case_command __P((CASE_COM *));
static void print_while_command __P((WHILE_COM *));
static void print_until_command __P((WHILE_COM *));
static void print_until_or_while __P((WHILE_COM *, char *));
static void print_if_command __P((IF_COM *));
#if defined (COND_COMMAND)
static void print_cond_node __P((COND_COM *));
#endif
static void print_function_def __P((FUNCTION_DEF *));

#define PRINTED_COMMAND_INITIAL_SIZE 64
#define PRINTED_COMMAND_GROW_SIZE 128

char *the_printed_command = (char *)NULL;
int the_printed_command_size = 0;
int command_string_index = 0;
int	token_cnt = 0;

int xtrace_fd = -1;
FILE *xtrace_fp = 0;

#define CHECK_XTRACE_FP	xtrace_fp = (xtrace_fp ? xtrace_fp : stderr)

#define PRINT_DEFERRED_HEREDOCS(x) \
		do { \
			if (deferred_heredocs) \
			print_deferred_heredocs (x); \
		} while (0)

/* Non-zero means the stuff being printed is inside of a function def. */
static int inside_function_def;
static int skip_this_indent;
static int was_heredoc;
static int printing_connection;
static REDIRECT *deferred_heredocs;

/* The depth of the group commands that we are currently printing.  This
   includes the group command that is a function body. */
static int group_command_nesting;

/* A buffer to indicate the indirection level (PS4) when set -x is enabled. */
static char indirection_string[100];


//MIW var declarations begin

static FILE* outputF;

static int external_cmd_mode = 0;
static char* case_var;
static int first_if = 1;
//MIW var declarations end

static burpT	g_output  = {0, 0, 0};
static burpT	g_comment = {0, 0, 0};

typedef struct function_nameS {
	struct function_nameS *m_nextP;
	char	*m_nameP;
} function_nameT;

function_nameT *g_function_namesP = 0;

static int
is_internal_function(char *nameP)
{
	function_nameT	*function_nameP;

	for (function_nameP = g_function_namesP; function_nameP; function_nameP = function_nameP->m_nextP) {
		if (!strcmp(nameP, function_nameP->m_nameP)) {
			return(1);
	}	}
	return (0);
}

int capture_globals = 0;
function_nameT *g_globalsP = 0;

void
seen_global(const char *nameP)
{
	function_nameT **tailPP, *globalP;
	char *P;

	if (capture_globals) {
		for (tailPP = &g_globalsP; globalP = *tailPP; tailPP = &(globalP->m_nextP)) {
			if (!strcmp(globalP->m_nameP, nameP)) {
				return;
		}	}
		globalP = (function_nameT *) malloc(sizeof(function_nameT) + strlen(nameP) + 1);
		P = (char *) (globalP+1);
		strcpy(P, nameP);
		globalP->m_nameP = P;
		globalP->m_nextP = 0;
		*tailPP          = globalP;
	}
}

//#define UNCHANGED burps(&g_output, "^^")
#define UNCHANGED

void initialize_translator(const char *shell_scriptP)
{
	if (!shell_scriptP) {
	  outputF = fopen("output.py", "w");
	  if (!outputF) {
		fprintf(stderr, "Can't open output.py\n");
		exit(1);
	  }
    } else {
	  char *P;
	  int  lth        = strlen(shell_scriptP);

	  if (lth > 3 && !strcmp(shell_scriptP+lth-3,".py")) {
		fprintf(stderr,"The bash input %s looks like it is already in python\n", shell_scriptP);
		exit(1);
	  }
	  char *filenameP = P = (char *) alloca(lth+4);
	  memcpy(filenameP, shell_scriptP, lth);
	  P = filenameP + lth;
	  memcpy(P, ".py", 3);
	  P += 3;
	  *P = 0;
	  
	  outputF = fopen(filenameP, "w");
	  if (!outputF) {
		fprintf(stderr, "Can't open %s\n", filenameP);
		exit(1);
	  }
	}
	fprintf(outputF,"#! /usr/bin/env python\n");
}

extern int g_uses_sys;
extern int g_uses_os;

void close_translator()
{
	int	separator = ' ';
	if (g_uses_sys || g_uses_os) {
		fprintf(outputF, "import");
		if (g_uses_sys) {
			fprintf(outputF, " sys");
			separator = ',';
		}
		if (g_uses_os) {
			fprintf(outputF, "%cos", separator);
		}
		fprintf(outputF, "\n");
	}
	fprintf(outputF, "from stat import *\n");

	if (g_output.m_lth) {
		fputs(g_output.m_P, outputF);
	}
	fclose(outputF);
}

extern int line_number;
static int comment_line_number = -1;

void seen_comment_char(int c)
{
	char *P;

	if (c < 0) {
		/* Start */
			
		g_comment.m_lth = 0;
		if (comment_line_number == -2 && token_cnt == 1) {
			burpc(&g_comment, '\n');
		}
		c = '#';
		comment_line_number = line_number;
	}
	if (c == '\n') {
		/* End */
		if (token_cnt == 1) {
			P = g_comment.m_P;
			if (*P != '#' || P[1] != '!') {
				burps(&g_output, P);
				burpc(&g_output, c);
				g_comment.m_lth  = 0;
				g_comment.m_P[0] = 0;
		}	}
		return;
	}
	if (c) {
		burpc(&g_comment, c);
	}
}

void print_translation(COMMAND * command)
{
	print_command(command);
}

/* Print COMMAND (a command tree) on standard output. */
void
print_command (command)
COMMAND *command;
{
	char *P;

	if (0 <= comment_line_number)  {
		if (comment_line_number + 1 < command->line) {
			burpc(&g_output,'\n');
			comment_line_number = -2;
	}	}

	command_string_index = 0;
	char * command_string = make_command_string (command);
	if (g_comment.m_lth) {
		burpc(&g_output, ' ');
		burps(&g_output, g_comment.m_P);
		g_comment.m_lth = 0;
	}
	burpc(&g_output, '\n');
}

/* Make a string which is the printed representation of the command
   tree in COMMAND.  We return this string.  However, the string is
   not consed, so you have to do that yourself if you want it to
   remain around. */
char *
make_command_string (command)
COMMAND *command;
{
	command_string_index = was_heredoc = 0;
	deferred_heredocs = 0;
	make_command_string_internal (command);
	return (the_printed_command);
}

/* The internal function.  This is the real workhorse. */
static void
make_command_string_internal (command)
COMMAND *command;
{
	char s[3];

	if (command) {
		if (skip_this_indent)
			skip_this_indent--;
		else
			indent (indentation);

		if (command->flags & CMD_TIME_PIPELINE) {
			UNCHANGED;
			burps(&g_output, "time ");
			if (command->flags & CMD_TIME_POSIX) {
				burps(&g_output, "-p ");
			}
		}

		if (command->flags & CMD_INVERT_RETURN) {
			UNCHANGED;
			burps(&g_output, "! ");
		}

		switch (command->type)
		{
		case cm_for:
			print_for_command (command->value.For);
			break;

#if defined (ARITH_FOR_COMMAND)
		case cm_arith_for:
			print_arith_for_command (command->value.ArithFor);
			break;
#endif

#if defined (SELECT_COMMAND)
		case cm_select:
			print_select_command (command->value.Select);
			break;
#endif

		case cm_case:
			print_case_command (command->value.Case);
			break;

		case cm_while:
			print_while_command (command->value.While);
			break;

		case cm_until:
			print_until_command (command->value.While);
			break;

		case cm_if:
			print_if_command (command->value.If);
			break;

#if defined (DPAREN_ARITHMETIC)
		case cm_arith:
			print_arith_command (command->value.Arith->exp);
			break;
#endif

#if defined (COND_COMMAND)
		case cm_cond:
			print_cond_command (command->value.Cond);
			break;
#endif

		case cm_simple:
			print_simple_command (command->value.Simple);
			break;

		case cm_connection:

			skip_this_indent++;
			printing_connection++;
			make_command_string_internal (command->value.Connection->first);

            UNCHANGED;
			switch (command->value.Connection->connector)
			{
			case '&':
			case '|':
			{
				char c = command->value.Connection->connector;

				s[0] = ' ';
				s[1] = c;
				s[2] = '\0';

				print_deferred_heredocs (s);

				if (c != '&' || command->value.Connection->second) {
					burpc(&g_output, ' ');
					skip_this_indent++;
				}
			}
			break;

			case AND_AND:
				print_deferred_heredocs (" && ");
				if (command->value.Connection->second)
					skip_this_indent++;
				break;

			case OR_OR:
				print_deferred_heredocs (" || ");
				if (command->value.Connection->second)
					skip_this_indent++;
				break;

			case ';':
				if (deferred_heredocs == 0) {
					if (was_heredoc == 0) {
						burpc(&g_output, '\n');
						indent (indentation);
						skip_this_indent++;
					} else {
						was_heredoc = 0;
					}
				} else {
					print_deferred_heredocs (inside_function_def ? "" : ";");
				}

				if (!inside_function_def) {
					if (command->value.Connection->second) {
						skip_this_indent++;
					}
				}
				break;

			default:
				fprintf(stderr, _("print_command: bad connector `%d'"),
						command->value.Connection->connector);
				assert(0);
				exit(1);
			}

			make_command_string_internal (command->value.Connection->second);
			PRINT_DEFERRED_HEREDOCS ("");
			printing_connection--;
			break;

			case cm_function_def:
				print_function_def (command->value.Function_def);
				break;

			case cm_group:
				print_group_command (command->value.Group);
				break;

			case cm_subshell:
				UNCHANGED;
				burps(&g_output, "( ");
				skip_this_indent++;
				make_command_string_internal (command->value.Subshell->command);
				burps(&g_output, " )");
				break;

			case cm_coproc:
				UNCHANGED;
				burps(&g_output, "coproc ");
				burps(&g_output, command->value.Coproc->name);
				burpc(&g_output, ' ');
				skip_this_indent++;
				make_command_string_internal (command->value.Coproc->command);
				break;

			default:
				UNCHANGED;
				command_error ("print_command", CMDERR_BADTYPE, command->type, 0);
				break;
		}
		if (command->redirects) {
			burpc(&g_output, ' ');
			print_redirection_list (command->redirects, NULL);
		}
	}
}

static char* translate_word(char* word_to_print)
{
	extern	char *fix_string(char *stringP);

	char* translated;
	if (!strcmp(word_to_print, "-gt") || !strcmp(word_to_print, "-ge")){
		word_to_print = ">";
	} else if (!strcmp(word_to_print, "-lt")||!strcmp(word_to_print, "-le")){
		word_to_print = "<";
	} else if (!strcmp(word_to_print, "-eq")){
		word_to_print = "==";
	} else if (!strcmp(word_to_print, "=")){
		word_to_print = "==";
	} else if (!strcmp(word_to_print, "-ne")){
		word_to_print = "!=";
	} else if (!strcmp(word_to_print, "[") || !strcmp(word_to_print, "]")) {
		word_to_print = "";
	} else if(!strcmp(word_to_print, "echo")) {
		word_to_print = "print";
	} else if (!strcmp(word_to_print, "\"$#\"")) {
		word_to_print = "len(sys.argv)";
		g_uses_sys = 1;
	} else if (!strcmp(word_to_print, "true")){
		word_to_print = "True";
	} else if (!strcmp(word_to_print, "[")){
		word_to_print = "";
	} else if (!strcmp(word_to_print, "]")){
		word_to_print = "";
	} else if (!strcmp(word_to_print, "-z")){
		word_to_print = " not ";
	} else if (!strcmp(word_to_print, "!")){
		word_to_print = " not ";
	}
	if (word_to_print[0] != '\0') {
		word_to_print = fix_string(word_to_print);
	}

	translated = word_to_print;
	return translated;
}

void
print_word_list (list, separator)
WORD_LIST *list;
char *separator;
{
	WORD_LIST *w;

	char* word_to_print;
	for (w = list; w; w = w->next){
		word_to_print = w->word->word;
		word_to_print = translate_word(word_to_print);
		burps(&g_output, word_to_print);
		if (w->next) {
			burps(&g_output, separator);
		}
	}
}

void
print_printf_cmd (list, separator)
WORD_LIST *list;
char *separator;
{
	WORD_LIST *w = list;
	char* format_string = w->word->word;
	burps(&g_output, "print( ");
	burps(&g_output, format_string);
	burps(&g_output, " % (");
	w = w->next;
	char* word_to_print;


	for (; w; w = w->next){
		word_to_print = w->word->word;
		word_to_print = translate_word(word_to_print);
		burps(&g_output, word_to_print);
		if (w->next) {
			burps(&g_output, ", ");
		}
	}
	burps(&g_output, ") )\n");
}

/* export [-fn] [-p] var[=value] */

void
print_export_cmd (list, separator)
WORD_LIST *list;
char *separator;
{
	WORD_LIST	*nodeP;
	char		*wordP, *P;

	for (nodeP = list; nodeP; nodeP = nodeP->next) {
		wordP = nodeP->word->word;
		if (*wordP != '-') {
			g_uses_os = 1;
			burps(&g_output, "os.environ['");
			P = strchr(wordP, '=');
			if (!P) {
				burps(&g_output, wordP);
				burps(&g_output, "'] = ");
				burps(&g_output, wordP);
			} else {
				burpn(&g_output, wordP, P - wordP);
				burps(&g_output, "'] = ");
				burps(&g_output, P+1);
			}
			break;
	}	}
	return;
}

void
_print_word_list (list, separator)
WORD_LIST *list;
char *separator;
{
	UNCHANGED;
	printf("ERROR");
}

/* Return a string denoting what our indirection level is. */

char *
indirection_level_string ()
{
	register int i, j;
	char *ps4;
	char ps4_firstc[MB_LEN_MAX+1];
	int ps4_firstc_len, ps4_len;

	indirection_string[0] = '\0';
	ps4 = get_string_value ("PS4");

	if (ps4 == 0 || *ps4 == '\0')
		return (indirection_string);

	change_flag ('x', FLAG_OFF);
	ps4 = decode_prompt_string (ps4);
	change_flag ('x', FLAG_ON);

	if (ps4 == 0 || *ps4 == '\0')
		return (indirection_string);

#if defined (HANDLE_MULTIBYTE)
	ps4_len = strnlen (ps4, MB_CUR_MAX);
	ps4_firstc_len = MBLEN (ps4, ps4_len);
	if (ps4_firstc_len == 1 || ps4_firstc_len == 0 || MB_INVALIDCH (ps4_firstc_len))
	{
		ps4_firstc[0] = ps4[0];
		ps4_firstc[ps4_firstc_len = 1] = '\0';
	}
	else
		memcpy (ps4_firstc, ps4, ps4_firstc_len);
#else
	ps4_firstc[0] = ps4[0];
	ps4_firstc[ps4_firstc_len = 1] = '\0';
#endif

	for (i = j = 0; ps4_firstc[0] && j < indirection_level && i < 99; i += ps4_firstc_len, j++)
	{
		if (ps4_firstc_len == 1)
			indirection_string[i] = ps4_firstc[0];
		else
			memcpy (indirection_string+i, ps4_firstc, ps4_firstc_len);
	}

	for (j = ps4_firstc_len; *ps4 && ps4[j] && i < 99; i++, j++)
		indirection_string[i] = ps4[j];

	indirection_string[i] = '\0';
	free (ps4);
	return (indirection_string);
}

void
xtrace_print_assignment (name, value, assign_list, xflags)
char *name, *value;
int assign_list, xflags;
{
	char *nval;

	CHECK_XTRACE_FP;

	if (xflags)
		fprintf (xtrace_fp, "%s", indirection_level_string ());

	/* VALUE should not be NULL when this is called. */
	if (*value == '\0' || assign_list)
		nval = value;
	else if (sh_contains_shell_metas (value))
		nval = sh_single_quote (value);
	else if (ansic_shouldquote (value))
		nval = ansic_quote (value, 0, (int *)0);
	else
		nval = value;

	if (assign_list)
		fprintf (xtrace_fp, "%s=(%s)\n", name, nval);
	else
		fprintf (xtrace_fp, "%s=%s\n", name, nval);

	if (nval != value)
		FREE (nval);

	fflush (xtrace_fp);
}

/* A function to print the words of a simple command when set -x is on. */
void
xtrace_print_word_list (list, xtflags)
WORD_LIST *list;
int xtflags;
{
	WORD_LIST *w;
	char *t, *x;

	CHECK_XTRACE_FP;

	if (xtflags)
		fprintf (xtrace_fp, "%s", indirection_level_string ());

	for (w = list; w; w = w->next)
	{
		t = w->word->word;
		if (t == 0 || *t == '\0')
			fprintf (xtrace_fp, "''%s", w->next ? " " : "");
		else if (sh_contains_shell_metas (t))
		{
			x = sh_single_quote (t);
			fprintf (xtrace_fp, "%s%s", x, w->next ? " " : "");
			free (x);
		}
		else if (ansic_shouldquote (t))
		{
			x = ansic_quote (t, 0, (int *)0);
			fprintf (xtrace_fp, "%s%s", x, w->next ? " " : "");
			free (x);
		}
		else
			fprintf (xtrace_fp, "%s%s", t, w->next ? " " : "");
	}
	fprintf (xtrace_fp, "\n");
	fflush (xtrace_fp);
}

void
print_for_command_head (for_command)
FOR_COM *for_command;
{
	burps(&g_output, "for ");
	burps(&g_output, for_command->name->word);
	burps(&g_output, " in [");
	print_word_list (for_command->map_list, ", ");
	burps(&g_output, "]:");
}

void
xtrace_print_for_command_head (for_command)
FOR_COM *for_command;
{
	CHECK_XTRACE_FP;
	fprintf (xtrace_fp, "%s", indirection_level_string ());
	fprintf (xtrace_fp, "for %s in ", for_command->name->word);
	xtrace_print_word_list (for_command->map_list, 0);
}

static void
print_for_command (for_command)
FOR_COM *for_command;
{
	print_for_command_head (for_command);
	newline ("");

	indentation += indentation_amount;
	make_command_string_internal (for_command->action);
	PRINT_DEFERRED_HEREDOCS ("");
	indentation -= indentation_amount;
}

#if defined (ARITH_FOR_COMMAND)
static void
print_arith_for_command (arith_for_command)
ARITH_FOR_COM *arith_for_command;
{
	burps(&g_output, "for ((");
	print_word_list (arith_for_command->init, " ");
	burps(&g_output, "; ");
	print_word_list (arith_for_command->test, " ");
	burps(&g_output, "; ");
	print_word_list (arith_for_command->step, " ");
	burps(&g_output, "))");
	newline ("do\n");
	indentation += indentation_amount;
	make_command_string_internal (arith_for_command->action);
	indentation -= indentation_amount;
	newline ("done");
}
#endif /* ARITH_FOR_COMMAND */

#if defined (SELECT_COMMAND)
void
print_select_command_head (select_command)
SELECT_COM *select_command;
{
	burps(&g_output, "select ");
	burps(&g_output, select_command->name->word);
	burps(&g_output, " in ");
	print_word_list (select_command->map_list, " ");
}

void
xtrace_print_select_command_head (select_command)
SELECT_COM *select_command;
{
	CHECK_XTRACE_FP;
	fprintf (xtrace_fp, "%s", indirection_level_string ());
	fprintf (xtrace_fp, "select %s in ", select_command->name->word);
	xtrace_print_word_list (select_command->map_list, 0);
}

static void
print_select_command (select_command)
SELECT_COM *select_command;
{
	print_select_command_head (select_command);

	burpc(&g_output, ';');
	newline ("do\n");
	indentation += indentation_amount;
	make_command_string_internal (select_command->action);
	PRINT_DEFERRED_HEREDOCS ("");
	indentation -= indentation_amount;
	newline ("done");
}
#endif /* SELECT_COMMAND */

static void
print_group_command (group_command)
GROUP_COM *group_command;
{
	group_command_nesting++;
	burps(&g_output, "{ ");

	if (inside_function_def == 0) {
		skip_this_indent++;
	} else {
		/* This is a group command { ... } inside of a function
	 definition, and should be printed as a multiline group
	 command, using the current indentation. */
		burpc(&g_output, '\n');
		indentation += indentation_amount;
	}

	make_command_string_internal (group_command->command);

	if (inside_function_def) {
		burpc(&g_output, '\n');
		indentation -= indentation_amount;
		indent (indentation);
	} else {
		burpc(&g_output, ' ');
	}

	burpc(&g_output, '}');

	group_command_nesting--;
}

void
print_case_command_head (case_command)
CASE_COM *case_command;
{
	case_var = case_command->word->word;
	case_var = translate_word(case_var);
}

void
xtrace_print_case_command_head (case_command)
CASE_COM *case_command;
{
	CHECK_XTRACE_FP;
	fprintf (xtrace_fp, "%s", indirection_level_string ());
	fprintf (xtrace_fp, "case %s in\n", case_command->word->word);
}

static void
print_case_command (case_command)
CASE_COM *case_command;
{
	print_case_command_head (case_command);
	if (case_command->clauses)
		print_case_clauses (case_command->clauses);
	first_if = 1;
}

static void print_case_ors(WORD_LIST* patterns){
	WORD_LIST *w;
	for (w = patterns; w; w = w->next){
		if (!strcmp(w->word->word, "*")){
			continue;
		}
		burps(&g_output, " or ");
		burps(&g_output, case_var);
		burps(&g_output, " == '");
		burps(&g_output, w->word->word);
		burpc(&g_output, '\'');
	}
}

static void
print_case_clauses (clauses)
PATTERN_LIST *clauses;
{
	while (clauses)
	{
		newline ("");
		if (!strcmp(clauses->patterns->word->word, "*")){
			burps(&g_output, "else:");
		} else {
			if (first_if) {
				burps(&g_output, "if ( ");
				burps(&g_output, case_var);
				burps(&g_output, " == ");
				first_if  = 0;
			} else{
				burps(&g_output, "elif ( ");
				burps(&g_output, case_var);
				burps(&g_output, " == ");
			}
			burpc(&g_output, '\'');
			burps(&g_output, clauses->patterns->word->word);
			burpc(&g_output, '\'');
			print_case_ors(clauses->patterns->next);
			burps(&g_output, "):");

		}
		burpc(&g_output, '\n');

		indentation += indentation_amount;
		make_command_string_internal (clauses->action);
		indentation -= indentation_amount;
		PRINT_DEFERRED_HEREDOCS ("");

		clauses = clauses->next;
	}
	indentation -= indentation_amount;
}

static void
print_while_command (while_command)
WHILE_COM *while_command;
{
	print_until_or_while (while_command, "while");
}

static void
print_until_command (while_command)
WHILE_COM *while_command;
{
	print_until_or_while (while_command, "until");
}

static void
print_until_or_while (while_command, which)
WHILE_COM *while_command;
char *which;
{
	burps(&g_output, which);
	burpc(&g_output, ' ');
	skip_this_indent++;
	burpc(&g_output, '(');
	make_command_string_internal (while_command->test);
	burps(&g_output, "):\n");
	PRINT_DEFERRED_HEREDOCS ("");
	indentation += indentation_amount;
	make_command_string_internal (while_command->action);
	PRINT_DEFERRED_HEREDOCS ("");
	indentation -= indentation_amount;
}

static void
print_if_command (if_command)
IF_COM *if_command;
{
	burps(&g_output, "if (");
	skip_this_indent++;
	make_command_string_internal (if_command->test);
	burps(&g_output, " ):\n");
	indentation += indentation_amount;
	make_command_string_internal (if_command->true_case);
	PRINT_DEFERRED_HEREDOCS ("");
	indentation -= indentation_amount;

	if (if_command->false_case)
	{
		newline ("else:\n");
		indentation += indentation_amount;
		make_command_string_internal (if_command->false_case);
		PRINT_DEFERRED_HEREDOCS ("");
		indentation -= indentation_amount;
	}
}

#if defined (DPAREN_ARITHMETIC)
void
print_arith_command (arith_cmd_list)
WORD_LIST *arith_cmd_list;
{
	burps(&g_output, "((");
	print_word_list (arith_cmd_list, " ");
	burps(&g_output, "))");
}
#endif

#if defined (COND_COMMAND)
static void
print_cond_node (cond)
COND_COM *cond;
{	  
	if (cond->flags & CMD_INVERT_RETURN) {
		burps(&g_output, "! ");
	}

	switch (cond->type) {
	case COND_EXPR:
		burps(&g_output, "( ");
		print_cond_node (cond->left);
		burps(&g_output, " )");
		break;
	case COND_AND:
		print_cond_node (cond->left);
		burps(&g_output, " and ");
		print_cond_node (cond->right);
		break;
	case COND_OR:
		print_cond_node (cond->left);
		burps(&g_output, " or ");
		print_cond_node (cond->right);
		break;
	case COND_UNARY:
		burps(&g_output, cond->op->word);
		burpc(&g_output, ' ');
		print_cond_node (cond->left);
		break;
	case COND_BINARY:
		print_cond_node (cond->left);
		burpc(&g_output, ' ');
		burps(&g_output, cond->op->word);
		burpc(&g_output, ' ');
		print_cond_node (cond->right);
		break;
	case COND_TERM: {
		char* word = cond->op->word;
		if (!strcmp(word, "$#")) {
			word = "len(sys.argv)";
			g_uses_sys = 1;
		}
		burps(&g_output, word );		/* need to add quoting here */
	}}
}

void
print_cond_command (cond)
COND_COM *cond;
{
	print_cond_node (cond);
}

#ifdef DEBUG
void
debug_print_cond_command (cond)
COND_COM *cond;
{
	fprintf (stderr, "DEBUG: ");
	command_string_index = 0;
	print_cond_command (cond);
	fprintf (stderr, "%s\n", the_printed_command);
}
#endif


int check_if_supported(SIMPLE_COM* cmd){
	WORD_LIST *w;
	for (w = cmd->words; w; w = w->next){
		char* the_word = w->word->word;
	}
	return 1;
}

int has_equal_sign(SIMPLE_COM *simple_command){
	char* word = simple_command->words->word->word;
	int i;
	for (i = 0; word[i]!= '\0'; i++){
		if (word[i]== '=')
			return 1;
	}
	return 0;
}


// means that have to call this with os.system
int is_external_command(SIMPLE_COM *simple_command){
	WORD_LIST* word_list = simple_command->words;

	const int num_internal_commands = 16;

	const char *internal_commands[num_internal_commands];

	internal_commands[0] = "exit";
	internal_commands[1] = "[";
	internal_commands[2] = "echo";
	internal_commands[3] = "cd";
	internal_commands[4] = "pwd";
	internal_commands[5] = "read";
	internal_commands[6] = "true";
	internal_commands[7] = "false";
	internal_commands[8] = "break";
	internal_commands[9] = "continue";
	internal_commands[10] = "";
	internal_commands[11] = "[";
	internal_commands[12] = "let";
	internal_commands[13] = "printf";
	internal_commands[14] = "export";
	internal_commands[15] = "eval";

	int i;
	for (i = 0; i < num_internal_commands; i++){
		if (!strcmp(word_list->word->word, internal_commands[i]))
			return 0;
	}
	if (has_equal_sign(simple_command))
		return 0;
	return 1;
}



void print_simple_command_helper(SIMPLE_COM *simple_command){
	if (!check_if_supported(simple_command)){
		burp(&g_output, "### UNSUPPORTED COMMAND ON LINE %d", simple_command->line);
		assert(0);
		return;
	}

	if (is_external_command(simple_command)){
		external_cmd_mode = 1;
		g_uses_os = 1;
        if (is_internal_function(simple_command->words->word->word)) {
			burps(&g_output, simple_command->words->word->word);
			burpc(&g_output, '(');
		} else {
			burps(&g_output, "os.system(");
			print_word_list (simple_command->words, " + \" \" + ");
		}
	} else {
		WORD_LIST* word_list = simple_command->words;
		if (word_list->next && word_list->next->next && word_list->next->next->next && !strcmp(word_list->word->word, "[")){
			word_list = word_list->next;
			if (!strcmp(word_list->word->word, "!")){
				burps(&g_output, " not ");
				word_list = word_list->next;
			}
			if (!strcmp(word_list->word->word, "-f") || !strcmp(word_list->word->word, "-e")){
				g_uses_os = 1;
				burps(&g_output, "os.path.isfile(");
				print_word_list(word_list->next, " ");
				burpc(&g_output, ')');
			} else if (!strcmp(word_list->word->word, "-b")){
				g_uses_os = 1;
				burps(&g_output, "S_ISBLK(os.stat(");
				print_word_list(word_list->next, " ");
				burps(&g_output, ").st_mode)");
			} else if (!strcmp(word_list->word->word, "-c")){
				g_uses_os = 1;
				burps(&g_output, "S_ISCHR(os.stat(");
				print_word_list(word_list->next, " ");
				burps(&g_output, ").st_mode)");
			} else if (!strcmp(word_list->word->word, "-d")){
				g_uses_os = 1;
				burps(&g_output, "S_ISDIR(os.stat(");
				print_word_list(word_list->next, " ");
				burps(&g_output, ").st_mode)");
			}
			/*
			else if (!strcmp(word_list->word->word, "-f")){
				g_uses_os = 1;
				burps(&g_output, "S_ISREG(os.stat(");
				print_word_list(word_list->next, " ");
				burps(&g_output, ").st_mode)");
			}
			*/
			else if (!strcmp(word_list->word->word, "-h")){
				g_uses_os = 1;
				burps(&g_output, "S_ISLNK(os.stat(");
				print_word_list(word_list->next, " ");
				burps(&g_output, ").st_mode)");
			} else if (!strcmp(word_list->word->word, "-k")){
				g_uses_os = 1;
				burps(&g_output, "S_ISCHR(os.stat(");
				print_word_list(word_list->next, " ");
				burps(&g_output, ").st_mode)");
			} else if (!strcmp(word_list->word->word, "-z")){
				print_word_list(word_list->next, " ");
                burps(&g_output, "not in globals()");
			}
			else {
				print_word_list(word_list, " ");
			}
		} else if (!strcmp(word_list->word->word, "exit")){
			if (word_list->next) {
				burps(&g_output, "exit(");
				burps(&g_output, word_list->next->word->word);
				burpc(&g_output, ')');
			} else {
				burps(&g_output, "exit()");
			}
		} else if (!strcmp(word_list->word->word, "[")) {
			print_word_list(word_list, " ");
		} else if (!strcmp(word_list->word->word, "echo")){
			WORD_LIST* print_next = word_list->next;
			if (print_next != NULL){
				if (!strcmp(print_next->word->word, "-n") || !strcmp(print_next->word->word, "-e")){
					print_next = print_next->next;
				}
			}
			if (print_next != NULL){
				burps(&g_output, "print(");
				if (print_next->word->word[0] == '"'){
					print_word_list(print_next, " ");
				} else {
					print_word_list(print_next, " ");
				}
				burpc(&g_output, ')');
			}
		} else if (!strcmp(word_list->word->word, "cd")){
			g_uses_os = 1;
			if (word_list->next) {
				burps(&g_output, "os.chdir(");
				burps(&g_output, word_list->next->word->word);
				burpc(&g_output, ')');
			} else {
				burps(&g_output, "os.chdir(os.path.expanduser('~'))");			
			}
		} else if (!strcmp(word_list->word->word, "pwd")){
			g_uses_os = 1;
			burps(&g_output, "os.getcwd()");
		} else if (!strcmp(word_list->word->word, "eval")){
			burps(&g_output, "exec(");
			print_word_list(word_list->next, " ");
			burpc(&g_output, ')');
		} else if (!strcmp(word_list->word->word, "read")){
			if (word_list->next) {
				burps(&g_output, word_list->next->word->word);
				burps(&g_output, " = raw_input()");
			} else {
				burps(&g_output, "raw_input()");
			}
		} else if (!strcmp(word_list->word->word, "true")){
			burps(&g_output, "True");
		} else if (!strcmp(word_list->word->word, "false")){
			burps(&g_output, "False");
		} else if (!strcmp(word_list->word->word, "break")){
			burps(&g_output, "break");
		} else if (!strcmp(word_list->word->word, "continue")){
			burps(&g_output, "continue");
		} else if (has_equal_sign(simple_command)) {
			print_word_list(word_list, " ");
		} else if (!strcmp(word_list->word->word, "let")){
			print_word_list(word_list->next, " ");
		} else if (!strcmp(word_list->word->word, "printf")){
			print_printf_cmd(word_list->next, " ");
		} else if (!strcmp(word_list->word->word, "export")){
			print_export_cmd(word_list->next, " ");
		} else {
			print_word_list(word_list, " ");
		}
	}
}
void
print_simple_command (simple_command)
SIMPLE_COM *simple_command;
{
	external_cmd_mode = 0;
	print_simple_command_helper(simple_command);
	if (simple_command->redirects)
	{
		print_redirection_list (simple_command->redirects, simple_command);
	}
	if (external_cmd_mode) {
		burps(&g_output, ")");
	}

}

static void
print_heredocs (heredocs)
REDIRECT *heredocs;
{
	REDIRECT *hdtail;

	burpc(&g_output, ' ');
	for (hdtail = heredocs; hdtail; hdtail = hdtail->next)
	{
		print_redirection (hdtail);
		burpc(&g_output, '\n');
	}
	was_heredoc = 1;
}

/* Print heredocs that are attached to the command before the connector
   represented by CSTRING.  The parsing semantics require us to print the
   here-doc delimiters, then the connector (CSTRING), then the here-doc
   bodies.  We don't print the connector if it's a `;', but we use it to
   note not to print an extra space after the last heredoc body and
   newline. */
static void
print_deferred_heredocs (cstring)
const char *cstring;
{
	REDIRECT *hdtail;

	for (hdtail = deferred_heredocs; hdtail; hdtail = hdtail->next) {
		burpc(&g_output, ' ');
		print_heredoc_header (hdtail);
	}
	if (cstring[0] && (cstring[0] != ';' || cstring[1])) {
		burps(&g_output, cstring);
	}
	if (deferred_heredocs) {
		burpc(&g_output, '\n');
	}
	for (hdtail = deferred_heredocs; hdtail; hdtail = hdtail->next) {
		print_heredoc_body (hdtail);
		burpc(&g_output, '\n');
	}
	if (deferred_heredocs) {
		if (cstring && cstring[0] && (cstring[0] != ';' || cstring[1])) {
			burpc(&g_output, ' ');	/* make sure there's at least one space */
		}
		dispose_redirects (deferred_heredocs);
		was_heredoc = 1;
	}
	deferred_heredocs = (REDIRECT *)NULL;
}

static void
print_redirection_list (  REDIRECT *redirects, SIMPLE_COM *simple_command)
{
	REDIRECT *heredocs, *hdtail, *newredir;

	heredocs = (REDIRECT *)NULL;
	hdtail = heredocs;

	was_heredoc = 0;
	while (redirects)
	{
		/* Defer printing the here documents until we've printed the
	 rest of the redirections. */
		if (redirects->instruction == r_reading_until || redirects->instruction == r_deblank_reading_until)
		{
			newredir = copy_redirect (redirects);
			newredir->next = (REDIRECT *)NULL;
			if (heredocs)
			{
				hdtail->next = newredir;
				hdtail = newredir;
			}
			else
				hdtail = heredocs = newredir;
		}
		else if (redirects->instruction == r_duplicating_output_word && redirects->redirector.dest == 1)
		{
			/* Temporarily translate it as the execution code does. */
			redirects->instruction = r_err_and_out;
			print_redirection (redirects);
			redirects->instruction = r_duplicating_output_word;
		}
		else
			print_redirection (redirects);

		redirects = redirects->next;
		if (redirects) {
			burpc(&g_output, ' ');
		}
	}

	/* Now that we've printed all the other redirections (on one line),
     print the here documents. */
	if (heredocs && printing_connection) {
		deferred_heredocs = heredocs;
	} else if (heredocs) {
		print_heredocs (heredocs);
		dispose_redirects (heredocs);
	}
}

static void
print_heredoc_header (redirect)
REDIRECT *redirect;
{
	int kill_leading;
	char *x;

	kill_leading = redirect->instruction == r_deblank_reading_until;

	/* Here doc header */
	if (redirect->rflags & REDIR_VARASSIGN) {
		burpc(&g_output, '{');
		burps(&g_output, redirect->redirector.filename->word);
		burpc(&g_output, '}');
	} else if (redirect->redirector.dest != 0) {
		burp(&g_output, "%d", redirect->redirector.dest);
	}

	/* If the here document delimiter is quoted, single-quote it. */
	if (redirect->redirectee.filename->flags & W_QUOTED) {
		x = sh_single_quote (redirect->here_doc_eof);
		burps(&g_output, "<<");
		if (kill_leading) {
			burpc(&g_output, '-');
		}
		burps(&g_output, x);
		free (x);
	} else {
		burps(&g_output, "<<");
		if (kill_leading) {
			burpc(&g_output, '-');
		}
		burps(&g_output, redirect->here_doc_eof);
	}
}

static void
print_heredoc_body (redirect)
REDIRECT *redirect;
{
	/* Here doc body */
	burps(&g_output, redirect->redirectee.filename->word);
	burps(&g_output, redirect->here_doc_eof);
}

static void
print_redirection (redirect)
REDIRECT *redirect;
{
	int redirector, redir_fd;
	WORD_DESC *redirectee, *redir_word;

	redirectee = redirect->redirectee.filename;
	redir_fd = redirect->redirectee.dest;

	redir_word = redirect->redirector.filename;
	redirector = redirect->redirector.dest;

	switch (redirect->instruction)
	{
	case r_input_direction:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burpc(&g_output, '}');
		} else if (redirector != 0) {
			burp(&g_output, "%d", redirector);
		}
		burps(&g_output, "< ");
		burps(&g_output, redirectee->word);
		break;

	case r_output_direction:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burpc(&g_output, '}');
		} else if (redirector != 1) {
			burp(&g_output, "%d", redirector);
		}
		burps(&g_output, "> ");
		burps(&g_output, redirectee->word);
		break;

	case r_inputa_direction:	/* Redirection created by the shell. */
		burpc(&g_output, '&');
		break;

	case r_output_force:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burpc(&g_output, '}');
		} else if (redirector != 1) {
			burp(&g_output, "%d", redirector);
		}
		burps(&g_output, ">|");
		burps(&g_output, redirectee->word);
		break;

	case r_appending_to:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burpc(&g_output, '}');
		} else if (redirector != 1) {
			burp(&g_output, "%d", redirector);
		}
		burps(&g_output, ">> ");
		burps(&g_output, redirectee->word);
		break;

	case r_input_output:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burpc(&g_output, '}');
		} else if (redirector != 1) {
			burp(&g_output, "%d", redirector);
		}
		burps(&g_output, "<> ");
		burps(&g_output, redirectee->word);
		break;

	case r_deblank_reading_until:
	case r_reading_until:
		print_heredoc_header (redirect);
		burpc(&g_output, '\n');
		print_heredoc_body (redirect);
		break;

	case r_reading_string:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burpc(&g_output, '}');
		} else if (redirector != 0) {
			burp(&g_output, "%d", redirector);
		}
		burps(&g_output, "<<< ");
		burps(&g_output, redirect->redirectee.filename->word);
		break;

	case r_duplicating_input:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burp(&g_output, "{%s}<&%d", redir_word->word, redir_fd);
		} else {
			burp(&g_output, "%d<&%d", redirector, redir_fd);
		}
		break;

	case r_duplicating_output:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burp(&g_output, "{%s}>&%d", redir_word->word, redir_fd);
		} else {
			burp(&g_output, "%d>&%d", redirector, redir_fd);
		}
		break;

	case r_duplicating_input_word:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burps(&g_output, "}<&");
			burps(&g_output, redirectee->word);
		} else {
			burp(&g_output, "%d<&%s", redirector, redirectee->word);
		}
		break;

	case r_duplicating_output_word:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burps(&g_output, "}>&");
			burps(&g_output, redirectee->word);
		} else {
			burp(&g_output, "%d>&%s", redirector, redirectee->word);
		}
		break;

	case r_move_input:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burp(&g_output, "{%s}<&%d-", redir_word->word, redir_fd);
		} else {
			burp(&g_output, "%d<&%d-", redirector, redir_fd);
		}
		break;

	case r_move_output:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burp(&g_output, "{%s}>&%d-", redir_word->word, redir_fd);
		} else {
			burp(&g_output, "%d>&%d-", redirector, redir_fd);
		}
		break;

	case r_move_input_word:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burps(&g_output, "}<&");
			burps(&g_output, redirectee->word);
			burpc(&g_output, '-');
		} else {
			burp(&g_output, "%d<&%s-", redirector, redirectee->word);
		}
		break;

	case r_move_output_word:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burps(&g_output, "}>&");
			burps(&g_output, redirectee->word);
			burpc(&g_output, '-');
		} else {
			burp(&g_output, "%d>&%s-", redirector, redirectee->word);
		}
		break;

	case r_close_this:
		if (redirect->rflags & REDIR_VARASSIGN) {
			burpc(&g_output, '{');
			burps(&g_output, redir_word->word);
			burps(&g_output, "}>&-");
		} else {
			burp(&g_output, "%d>&-", redirector);
		}
		break;

	case r_err_and_out:
		burps(&g_output, "&>");
		burps(&g_output, redirectee->word);
		break;

	case r_append_err_and_out:
		burps(&g_output, "&>>");
		burps(&g_output, redirectee->word);
		break;
	}
}

static void
reset_locals ()
{
	inside_function_def = 0;
	indentation = 0;
	printing_connection = 0;
	deferred_heredocs = 0;
}

static void
print_function_def (func)
FUNCTION_DEF *func;
{
	static burpT	save = {0,0,0};
	
	burpT	temp;
	COMMAND *cmdcopy;
	REDIRECT *func_redirects;
	char	 *nameP = func->name->word;
	function_nameT	 *function_nameP;
	function_nameT	 *globalP, *nextP;
	char	 *P;

	function_nameP = (function_nameT *) malloc(sizeof(function_nameT) + strlen(nameP) + 1);
	P = (char *) (function_nameP+1);
	strcpy(P, nameP);
	function_nameP->m_nameP = P;
	function_nameP->m_nextP = g_function_namesP;
	g_function_namesP       = function_nameP;
	
	func_redirects = NULL;
	burps(&g_output, "def ");
	burps(&g_output, nameP);
	burps(&g_output, " () :\n");

	temp     = save;
	save     = g_output;
	g_output = temp;
	g_output.m_lth = 0;

	capture_globals = 1;
	add_unwind_protect (reset_locals, 0);

	indent (indentation);

	inside_function_def++;
	indentation += indentation_amount;

	cmdcopy = copy_command (func->command);
	if (cmdcopy->type == cm_group)
	{
		func_redirects = cmdcopy->redirects;
		cmdcopy->redirects = (REDIRECT *)NULL;
	}
	make_command_string_internal (cmdcopy->type == cm_group
			? cmdcopy->value.Group->command
					: cmdcopy);

	remove_unwind_protect ();

	if (g_globalsP) {
		for (globalP = g_globalsP; globalP; globalP = nextP) {
			burps(&save, "    global ");
			burps(&save, globalP->m_nameP);
			burpc(&save, '\n');
			nextP = globalP->m_nextP;
			free(globalP);
	    }
		g_globalsP = 0;
		burpc(&save, '\n');
	}

	burpc(&g_output, '\n');
	burps(&save, g_output.m_P);
	temp     = save;
	save     = g_output;
	g_output = temp;

	capture_globals = 0;
	indentation -= indentation_amount;
	inside_function_def--;

	if (func_redirects)
	{ /* { */
		print_redirection_list (func_redirects, NULL);
		cmdcopy->redirects = func_redirects;
	}

	dispose_command (cmdcopy);
}

/* Return the string representation of the named function.
   NAME is the name of the function.
   COMMAND is the function body.  It should be a GROUP_COM.
   flags&FUNC_MULTILINE is non-zero to pretty-print, or zero for all on one line.
   flags&FUNC_EXTERNAL means convert from internal to external form
 */

static void
newline (string)
char *string;
{
	burpc(&g_output, '\n');
	indent (indentation);
	if (string && *string) {
		burps(&g_output, string);
	}
}

static char *indentation_string;
static int indentation_size;

static void
indent (amount)
int amount;
{
	register int i;

	RESIZE_MALLOCED_BUFFER (indentation_string, 0, amount, indentation_size, 16);

	for (i = 0; amount > 0; amount--)
		indentation_string[i++] = ' ';
	indentation_string[i] = '\0';
	burps(&g_output, indentation_string);
}

//pointless stuff

char *
named_function_string (name, command, flags)
char *name;
COMMAND *command;
int flags;
{
	char *result;
	int old_indent, old_amount;
	COMMAND *cmdcopy;
	REDIRECT *func_redirects;

	old_indent = indentation;
	old_amount = indentation_amount;
	command_string_index = was_heredoc = 0;
	deferred_heredocs = 0;

	if (name && *name) {
		burps(&g_output, name);
		burpc(&g_output, ' ');
	}

	burps(&g_output, "() ");

	if ((flags & FUNC_MULTILINE) == 0)
	{
		indentation = 1;
		indentation_amount = 0;
	} else {
		burpc(&g_output, '\n');
		indentation += indentation_amount;
	}

	inside_function_def++;

	burps(&g_output, (flags & FUNC_MULTILINE) ? "{ \n" : "{ ");

	cmdcopy = copy_command (command);
	/* Take any redirections specified in the function definition (which should
     apply to the function as a whole) and save them for printing later. */
	func_redirects = (REDIRECT *)NULL;
	if (cmdcopy->type == cm_group)
	{
		func_redirects = cmdcopy->redirects;
		cmdcopy->redirects = (REDIRECT *)NULL;
	}
	make_command_string_internal (cmdcopy->type == cm_group
			? cmdcopy->value.Group->command
					: cmdcopy);

	indentation = old_indent;
	indentation_amount = old_amount;
	inside_function_def--;

	if (func_redirects)
	{ /* { */
		newline ("} ");
		print_redirection_list (func_redirects, NULL);
		cmdcopy->redirects = func_redirects;
	}
	else
		newline ("}");

	result = the_printed_command;

	if ((flags & FUNC_MULTILINE) == 0)
	{
#if 0
		register int i;
		for (i = 0; result[i]; i++)
			if (result[i] == '\n')
			{
				strcpy (result + i, result + i + 1);
				--i;
			}
#else
		if (result[2] == '\n')	/* XXX -- experimental */
			strcpy (result + 2, result + 3);
#endif
	}

	dispose_command (cmdcopy);

	if (flags & FUNC_EXTERNAL)
		result = remove_quoted_escapes (result);

	return (result);
}


void
xtrace_set (fd, fp)
int fd;
FILE *fp;
{
	if (fd >= 0 && sh_validfd (fd) == 0)
	{
		internal_error (_("xtrace_set: %d: invalid file descriptor"), fd);
		return;
	}
	if (fp == 0)
	{
		internal_error (_("xtrace_set: NULL file pointer"));
		return;
	}
	if (fd >= 0 && fileno (fp) != fd)
		internal_warning (_("xtrace fd (%d) != fileno xtrace fp (%d)"), fd, fileno (fp));

	xtrace_fd = fd;
	xtrace_fp = fp;
}

void
xtrace_init ()
{
	xtrace_set (-1, stderr);
}

void
xtrace_reset ()
{
	if (xtrace_fd >= 0 && xtrace_fp)
	{
		fflush (xtrace_fp);
		fclose (xtrace_fp);
	}
	else if (xtrace_fd >= 0)
		close (xtrace_fd);

	xtrace_fd = -1;
	xtrace_fp = stderr;
}

void
xtrace_fdchk (fd)
int fd;
{
	if (fd == xtrace_fd)
		xtrace_reset ();
}


void
xtrace_print_cond_term (type, invert, op, arg1, arg2)
int type, invert;
WORD_DESC *op;
char *arg1, *arg2;
{
	CHECK_XTRACE_FP;
	command_string_index = 0;
	fprintf (xtrace_fp, "%s", indirection_level_string ());
	fprintf (xtrace_fp, "[[ ");
	if (invert)
		fprintf (xtrace_fp, "! ");

	if (type == COND_UNARY)
	{
		fprintf (xtrace_fp, "%s ", op->word);
		fprintf (xtrace_fp, "%s", (arg1 && *arg1) ? arg1 : "''");
	}
	else if (type == COND_BINARY)
	{
		fprintf (xtrace_fp, "%s", (arg1 && *arg1) ? arg1 : "''");
		fprintf (xtrace_fp, " %s ", op->word);
		fprintf (xtrace_fp, "%s", (arg2 && *arg2) ? arg2 : "''");
	}

	fprintf (xtrace_fp, " ]]\n");

	fflush (xtrace_fp);
}	  
#endif /* COND_COMMAND */

#if defined (DPAREN_ARITHMETIC) || defined (ARITH_FOR_COMMAND)
/* A function to print the words of an arithmetic command when set -x is on. */
void
xtrace_print_arith_cmd (list)
WORD_LIST *list;
{
	WORD_LIST *w;

	CHECK_XTRACE_FP;
	fprintf (xtrace_fp, "%s", indirection_level_string ());
	fprintf (xtrace_fp, "(( ");
	for (w = list; w; w = w->next)
		fprintf (xtrace_fp, "%s%s", w->word->word, w->next ? " " : "");
	fprintf (xtrace_fp, " ))\n");

	fflush (xtrace_fp);
}
#endif
