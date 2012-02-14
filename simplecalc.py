from ply import lex, yacc

exp = raw_input("calculate ")
###########################
###lexer
tokens=('NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'FACTORIAL')
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_FACTORIAL = r'\!'
#ignore
t_ignore = ' '
#number returns value
def t_NUMBER(t):
    r'[0-9]|[0-9][1-9]+'
    #r'[0-9]+'
    t.value=int(t.value)
    return t
#t_error
def t_error(t):
    t.lexer.skip(1)
#finalize lexer
lex.lex()
###########################

###########################
###parser

#precedence
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'FACTORIAL'),
    )

def p_expression(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression FACTORIAL
    expression : NUMBER
    """
    #print p.lexer
    if len(p)==2:
        p[0] = p[1]
    elif len(p)==4:
        if p[2] == "+":
            p[0] = p[1] + p[3]
        elif p[2] == "-":
            p[0] = p[1] - p[3]
        elif p[2] == "*":
            p[0] = p[1] * p[3]
        elif p[2] == "/":
            p[0] = p[1] / p[3]
        print p[0]
    elif len(p) ==3:
        if p[2] == "!":
            p[0] = factorial(p[1])
            print p[0]

def factorial(n):
    result = 1
    for i in xrange(n):
        result = result*(i+1)
    return result


def p_error(p):
    print("Syntax error at '%s'" % p.value)
yacc.yacc()
yacc.parse(exp)
