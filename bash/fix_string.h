typedef enum {
	FIX_NONE=0, FIX_SKIP=1, FIX_STRING=2, FIX_STRING1=3, FIX_STRING2=4, FIX_INT=5, FIX_ARRAY=6
} fix_typeE;

char *fix_string(const char *stringP, fix_typeE type);


