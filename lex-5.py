import ply.lex as lex
import ply.yacc as yacc

tokens = ('NUMBER',)

t_NUMBER = r'\d+'
t_ignore = ' \t\n'

def p_expr(p):
    'expr : NUMBER'
    n = int(p[1])
    print("Even" if n % 2 == 0 else "Odd")

def p_error(p):
    print("Syntax error")

lexer = lex.lex()
parser = yacc.yacc()
parser.parse("123")