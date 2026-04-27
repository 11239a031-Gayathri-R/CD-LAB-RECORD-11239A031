import ply.lex as lex

tokens = ['VOWEL', 'CONSONANT']

def t_VOWEL(t):
    r'[aeiouAEIOU]'
    return t

def t_CONSONANT(t):
    r'[a-zA-Z]'
    return t

t_ignore = ' \t\n'
lexer = lex.lex()

lexer.input("Bakery")
for tok in lexer:
    print(tok)