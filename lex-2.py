import ply.lex as lex
import ply.yacc as yacc

tokens = ('NUMBER', 'PLUS', 'MINUS', 'MULT', 'DIV')

t_PLUS  = r'\+'
t_MINUS = r'-'
t_MULT  = r'\*'
t_DIV   = r'/'
t_NUMBER = r'\d+'
t_ignore = ' \t'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

def p_expr(p):
    '''
    expr : expr PLUS term
         | expr MINUS term
         | term
    '''
    if len(p) == 4:
        p[0] = p[1] + p[3] if p[2] == '+' else p[1] - p[3]
    else:
        p[0] = p[1]

def p_term(p):
    '''
    term : term MULT factor
         | term DIV factor
         | factor
    '''
    if len(p) == 4:
        p[0] = p[1] * p[3] if p[2] == '*' else p[1] / p[3]
    else:
        p[0] = p[1]

def p_factor(p):
    'factor : NUMBER'
    p[0] = int(p[1])

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()
print(parser.parse("2+3*5-4"))