#include "command.h"

void print_translation(COMMAND* command);
void initialize_translator();
void close_translator();

//regex_utility headers
char* regex_fix_backticks(char *);