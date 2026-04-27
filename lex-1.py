import ply.lex as lex

tokens = ['ADD', 'ID', 'NUMBER']

t_ADD = r'ADD'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()
lexer.input("ADD item1 2")

for tok in lexer:
    print(tok)