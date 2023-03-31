typedef enum {
	FIX_NONE=0, FIX_SKIP=1, FIX_STRING=2, FIX_INT=3, FIX_ARRAY=4
} fix_typeE;

char *fix_string(const char *stringP, fix_typeE type);


