import ply.lex as lex

tokens = ['CHAR']

def t_CHAR(t):
    r'[^\s]'
    return t

t_ignore = ' \t\n'
lexer = lex.lex()

lexer.input("This is a test")
for tok in lexer:
    print(tok.value, end="")