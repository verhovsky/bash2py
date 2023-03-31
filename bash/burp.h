
typedef struct {
	char	*m_P;
	int 	m_lth;
	int		m_max;
} burpT;

void burp(burpT *burpP, const char *fmtP, ...);
void burpc(burpT *burpP, const char c);
void burpn(burpT *burpP, const char *stringP, int lth);
void burps(burpT *burpP, const char *stringP);

extern int	g_burp_indent;
extern int	g_burp_disable_indent;
