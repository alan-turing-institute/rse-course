
# Yacc example
from system import *

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexreactions import tokens


def p_expression_system(p):
    "system : equation"
    p[0] = System()
    p[0].add_reaction(p[1])


def p_expression_combine_system(p):
    "system : system TEXNEWLINE NEWLINE equation"
    p[0] = p[1]
    p[0].add_reaction(p[4])


def p_equation(p):
    "equation : side ARROW side"
    p[0] = Reaction()
    p[0].reactants = p[1]
    p[0].products = p[3]


def p_side(p):
    "side : molecules"
    p[0] = Side()
    p[0].add(p[1][0], p[1][1])


def p_molecules(p):
    "molecules : molecule"
    p[0] = (p[1], 1)


def p_stoichiometry(p):
    "molecules : NUMBER molecule"
    p[0] = (p[2], p[1])


def p_plus(p):
    "side : side PLUS molecules"
    p[0] = p[1]
    p[0].add(p[3][0], p[3][1])


def p_molecule(p):
    "molecule : countedelement"
    p[0] = Molecule()
    p[0].add_element(p[1][0], p[1][1])


def p_countedelement(p):
    "countedelement : ELEMENT"
    p[0] = (p[1], 1)


def p_ncountedelement(p):
    "countedelement : ELEMENT atomcount"
    p[0] = (p[1], p[2])


def p_multi_element(p):
    "molecule : molecule countedelement"
    p[0] = p[1]
    p[0].add_element(p[2][0], p[2][1])


def p_multi_atoms(p):
    "atomcount : SUBSCRIPT NUMBER"
    p[0] = int(p[2])


def p_many_atoms(p):
    "atomcount : SUBSCRIPT LBRACE NUMBER RBRACE"
    p[0] = int(p[3])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
