
from ply import lex

tokens = (
    "ELEMENT",
    "NUMBER",
    "SUBSCRIPT",
    "LBRACE",
    "RBRACE",
    "PLUS",
    "ARROW",
    "NEWLINE",
    "TEXNEWLINE",
)

# Tokens

t_PLUS = r"\+"
t_SUBSCRIPT = r"_"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_TEXNEWLINE = r"\\\\"
t_ARROW = r"\\rightarrow"
t_ELEMENT = r"[A-Z][a-z]*?"


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


t_ignore = " "


def t_NEWLINE(t):
    r"\n+"
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
