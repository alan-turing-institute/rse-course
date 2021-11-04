#!/usr/bin/env python
# coding: utf-8

# # Domain specific languages

# ## Lex and Yacc

# Let's go back to our nice looks-like LaTeX file format:

# In[1]:


get_ipython().run_cell_magic('writefile', 'system.py', '\n\nclass Element:\n    def __init__(self, symbol):\n        self.symbol = symbol\n\n    def __str__(self):\n        return str(self.symbol)\n\n\nclass Molecule:\n    def __init__(self):\n        self.elements = {}  # Map from element to number of that element in the molecule\n\n    def add_element(self, element, number):\n        if not isinstance(element, Element):\n            element = Element(element)\n        self.elements[element] = number\n\n    @staticmethod\n    def as_subscript(number):\n        if number == 1:\n            return ""\n        if number < 10:\n            return "_" + str(number)\n        return "_{" + str(number) + "}"\n\n    def __str__(self):\n        return "".join(\n            [\n                str(element) + Molecule.as_subscript(self.elements[element])\n                for element in self.elements\n            ]\n        )\n\n\nclass Side:\n    def __init__(self):\n        self.molecules = {}\n\n    def add(self, reactant, stoichiometry):\n        self.molecules[reactant] = stoichiometry\n\n    @staticmethod\n    def print_if_not_one(number):\n        if number == 1:\n            return ""\n        else:\n            return str(number)\n\n    def __str__(self):\n        return " + ".join(\n            [\n                Side.print_if_not_one(self.molecules[molecule]) + str(molecule)\n                for molecule in self.molecules\n            ]\n        )\n\n\nclass Reaction:\n    def __init__(self):\n        self.reactants = Side()\n        self.products = Side()\n\n    def __str__(self):\n        return str(self.reactants) + " \\\\rightarrow " + str(self.products)\n\n\nclass System:\n    def __init__(self):\n        self.reactions = []\n\n    def add_reaction(self, reaction):\n        self.reactions.append(reaction)\n\n    def __str__(self):\n        return "\\\\\\\\ \\n".join(map(str, self.reactions))')


# In[2]:


from system import *

s2 = System()

c = Element("C")
o = Element("O")
h = Element("H")

co2 = Molecule()
co2.add_element(c, 1)
co2.add_element(o, 2)

h2o = Molecule()
h2o.add_element(h, 2)
h2o.add_element(o, 1)

o2 = Molecule()
o2.add_element(o, 2)

h2 = Molecule()
h2.add_element(h, 2)

glucose = Molecule()
glucose.add_element(c, 6)
glucose.add_element(h, 12)
glucose.add_element(o, 6)

combustion_glucose = Reaction()
combustion_glucose.reactants.add(glucose, 1)
combustion_glucose.reactants.add(o2, 6)
combustion_glucose.products.add(co2, 6)
combustion_glucose.products.add(h2o, 6)
s2.add_reaction(combustion_glucose)


combustion_hydrogen = Reaction()
combustion_hydrogen.reactants.add(h2, 2)
combustion_hydrogen.reactants.add(o2, 1)
combustion_hydrogen.products.add(h2o, 2)
s2.add_reaction(combustion_hydrogen)

print(s2)


# In[3]:


from IPython.display import display, Math

display(Math(str(s2)))


# How might we write a parser for this? Clearly we'll encounter the problems we previously solved in ensuring each molecule is the
# and atom only gets one object instance, but we solved this by using an appropriate primary key. (The above implementation is designed to make this easy, learning from the previous lecture.)
# 
# But we'll also run into a bunch of problems which are basically string parsing : noting, for example, that `_2` and `_{12}` make a number of atoms in a molecule, or that `+` joins molecules.
# 
# This will be very hard to do with straightforward python string processing.

# Instead, we will use a tool called `ply` (Python Lex-Yacc) which contains `Lex` (for generating lexical analysers) and `Yacc` (Yet Another Compiler-Compiler). Together these allow us to define the **grammar** of our file format.

# In[4]:


import ply


# The theory of "context free grammars" is rich and deep, and we will just scratch the surface here.

# ## Tokenising with Lex

# First, we need to turn our file into a "token stream", using regular expressions to match the kinds of symbol in our source:

# In[5]:


get_ipython().run_cell_magic('writefile', 'lexreactions.py', '\nfrom ply import lex\n\ntokens = (\n    "ELEMENT",\n    "NUMBER",\n    "SUBSCRIPT",\n    "LBRACE",\n    "RBRACE",\n    "PLUS",\n    "ARROW",\n    "NEWLINE",\n    "TEXNEWLINE",\n)\n\n# Tokens\nt_PLUS = r"\\+"\nt_SUBSCRIPT = r"_"\nt_LBRACE = r"\\{"\nt_RBRACE = r"\\}"\nt_TEXNEWLINE = r"\\\\\\\\"\nt_ARROW = r"\\\\rightarrow"\nt_ELEMENT = r"[A-Z][a-z]?"\nt_NEWLINE = r"\\n+"\n\n\ndef t_NUMBER(t):\n    r"\\d+"\n    t.value = int(t.value)\n    return t\n\n\nt_ignore = " "\n\n\ndef t_error(t):\n    print(f"Did not recognise character \'{t.value[0]:s}\' as part of a valid token")\n    t.lexer.skip(1)\n\n\n# Build the lexer\nlexer = lex.lex()')


# In[6]:


from lexreactions import lexer


# In[7]:


tokens = []
lexer.input(str(s2))
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    tokens.append(tok)


# In[8]:


print(str(s2))


# In[9]:


tokens


# Note that the parser will reject invalid tokens:

# In[10]:


lexer.input("""2H_2 + O_2 \\leftarrow 2H_2O""")
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)


# ## Writing a grammar

# So, how do we express our algebra for chemical reactions as a grammar?

# We write a series of production rules, expressing how a system is made up of equations, an equation is made up of molecules etc:

# ```
# system : equation
# system : system TEXNEWLINE NEWLINE equation
# equation : side ARROW side
# side : molecules
# molecules : molecule
# molecules : NUMBER molecule
# side : side PLUS molecules
# molecule : countedelement
# countedelement : ELEMENT
# countedelement : ELEMENT atomcount
# molecule : molecule countedelement
# atomcount : SUBSCRIPT NUMBER
# atomcount : SUBSCRIPT LBRACE NUMBER RBRACE
# ```

# Note how we right that a system is made of more than one equation:
# 
# ```
# system : equation # A system could be one equation
# system : system NEWLINE equation # Or it could be a system then an equation
# ```
# 
# ... which implies, recursively, that a system could also be:
# 
# ```
# system: equation NEWLINE equation NEWLINE equation ...
# ```

# This is an **incredibly** powerful idea. The full grammar for Python 3 can be defined in only a few hundred lines of specification: https://docs.python.org/3/reference/grammar.html

# ## Parsing with Yacc

# A parser defined with Yacc builds up the final object, by breaking down the
# file according to the rules of the grammar, and then building up objects
# as the individual tokens coalesce into the full grammar.
# 
# Here, we will for clarity not attempt to solve the problem of having multiple molecule instances for the same molecule - the normalisation problem solved last lecture.

# In Yacc, each grammar rule is defined by a Python function where the docstring for the function contains the appropriate grammar specification.
# 
# Each function accepts an argument `p` that is a list of symbols in the grammar. It must implement the actions of that rule. For example:
# 
# ```python
# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     #   ^            ^        ^    ^
#     #  p[0]         p[1]     p[2] p[3]
#     p[0] = p[1] + p[3]
# ```

# In[11]:


get_ipython().run_cell_magic('writefile', 'parsereactions.py', '\n# Yacc example\nimport ply.yacc as yacc\n\n# Get the components of our system\nfrom system import Element, Molecule, Side, Reaction, System\n\n# Get the token map from the lexer.  This is required.\nfrom lexreactions import tokens\n\n\ndef p_expression_system(p):\n    "system : equation"\n    p[0] = System()\n    p[0].add_reaction(p[1])\n\n\ndef p_expression_combine_system(p):\n    "system : system TEXNEWLINE NEWLINE equation"\n    p[0] = p[1]\n    p[0].add_reaction(p[4])\n\n\ndef p_equation(p):\n    "equation : side ARROW side"\n    p[0] = Reaction()\n    p[0].reactants = p[1]\n    p[0].products = p[3]\n\n\ndef p_side(p):\n    "side : molecules"\n    p[0] = Side()\n    p[0].add(p[1][0], p[1][1])\n\n\ndef p_molecules(p):\n    "molecules : molecule"\n    p[0] = (p[1], 1)\n\n\ndef p_stoichiometry(p):\n    "molecules : NUMBER molecule"\n    p[0] = (p[2], p[1])\n\n\ndef p_plus(p):\n    "side : side PLUS molecules"\n    p[0] = p[1]\n    p[0].add(p[3][0], p[3][1])\n\n\ndef p_molecule(p):\n    "molecule : countedelement"\n    p[0] = Molecule()\n    p[0].add_element(p[1][0], p[1][1])\n\n\ndef p_countedelement(p):\n    "countedelement : ELEMENT"\n    p[0] = (p[1], 1)\n\n\ndef p_ncountedelement(p):\n    "countedelement : ELEMENT atomcount"\n    p[0] = (p[1], p[2])\n\n\ndef p_multi_element(p):\n    "molecule : molecule countedelement"\n    p[0] = p[1]\n    p[0].add_element(p[2][0], p[2][1])\n\n\ndef p_multi_atoms(p):\n    "atomcount : SUBSCRIPT NUMBER"\n    p[0] = int(p[2])\n\n\ndef p_many_atoms(p):\n    "atomcount : SUBSCRIPT LBRACE NUMBER RBRACE"\n    p[0] = int(p[3])\n\n\n# Error rule for syntax errors\ndef p_error(p):\n    print("Syntax error in input!")\n\n\n# Build the parser\nparser = yacc.yacc()')


# In[12]:


from parsereactions import parser

roundtrip_system = parser.parse(str(s2))


# In[13]:


get_ipython().run_cell_magic('bash', '', '# Read the first 100 lines from the file\nhead -n 100 parser.out')


# In[14]:


display(Math(str(roundtrip_system)))


# In[15]:


with open("system.tex", "w") as texfile:
    texfile.write(str(roundtrip_system))


# In[16]:


get_ipython().system('cat system.tex')


# ## Internal DSLs

# In doing the above, we have defined what is called an "external DSL":
#     our code is in Python, but the file format is a language with a grammar
#     of its own.
#     
# However, we can use the language itself to define something almost
# as fluent, without having to write our own grammar,
# by using operator overloading and metaprogramming tricks:

# In[17]:


get_ipython().run_cell_magic('writefile', 'reactionsdsl.py', '\n\nclass Element:\n    def __init__(self, symbol):\n        self.symbol = symbol\n\n    def __str__(self):\n        return str(self.symbol)\n\n    def __mul__(self, other):\n        """Let Molecule handle the multiplication"""\n        return (self / 1) * other\n\n    def __truediv__(self, number):\n        """`Element / number => Molecule`"""\n        res = Molecule()\n        res.add_element(self, number)\n        return res\n\n\nclass Molecule:\n    def __init__(self):\n        self.elements = {}  # Map from element to number of that element in the molecule\n\n    def add_element(self, element, number):\n        if not isinstance(element, Element):\n            element = Element(element)\n        self.elements[element] = number\n\n    @staticmethod\n    def as_subscript(number):\n        if number == 1:\n            return ""\n        if number < 10:\n            return "_" + str(number)\n        return "_{" + str(number) + "}"\n\n    def __str__(self):\n        return "".join(\n            [\n                str(element) + Molecule.as_subscript(self.elements[element])\n                for element in self.elements\n            ]\n        )\n\n    def __mul__(self, other):\n        """`Molecule * Element => Molecule`\n        `Molecule * Molecule => Molecule`\n        """\n        if type(other) == Molecule:\n            self.elements.update(other.elements)\n        else:\n            self.add_element(other, 1)\n        return self\n\n    def __rmul__(self, stoich):\n        """`Number * Molecule => Side`"""\n        res = Side()\n        res.add(self, stoich)\n        return res\n\n    def __add__(self, other):\n        """`Molecule + X => Side`"""\n        if type(other) == Side:\n            other.molecules[self] = 1\n            return other\n        res = Side()\n        res.add(self, 1)\n        res.add(other, 1)\n        return res\n\n\nclass Side:\n    def __init__(self):\n        self.molecules = {}\n\n    def add(self, reactant, stoichiometry):\n        self.molecules[reactant] = stoichiometry\n\n    @staticmethod\n    def print_if_not_one(number):\n        if number == 1:\n            return ""\n        else:\n            return str(number)\n\n    def __str__(self):\n        return " + ".join(\n            [\n                Side.print_if_not_one(self.molecules[molecule]) + str(molecule)\n                for molecule in self.molecules\n            ]\n        )\n\n    def __add__(self, other):\n        """Side + X => Side"""\n        self.molecules.update(other.molecules)\n        return self\n\n    def __eq__(self, other):\n        res = Reaction()\n        res.reactants = self\n        res.products = other\n        current_system.add_reaction(res)  # Closure!\n        return f"Added: \'{res}\'"\n\n\nclass Reaction:\n    def __init__(self):\n        self.reactants = Side()\n        self.products = Side()\n\n    def __str__(self):\n        return str(self.reactants) + " \\\\rightarrow " + str(self.products)\n\n\nclass System:\n    def __init__(self):\n        self.reactions = []\n\n    def add_reaction(self, reaction):\n        self.reactions.append(reaction)\n\n    def __str__(self):\n        return "\\\\\\\\ \\n".join(map(str, self.reactions))\n\n\ncurrent_system = System()')


# In[18]:


from reactionsdsl import Element, current_system


# In[19]:


# Here we add new symbols to the global scope
# This is *not* good practice, we do it here to demonstrate that it is possible to do
for symbol in ("C", "O", "H"):
    globals()[symbol] = Element(symbol)


# In[20]:


O / 2 + 2 * (H / 2) == 2 * (H / 2 * O)


# In[21]:


(C / 6) * (H / 12) * (O / 6) + 6 * (O / 2) == 6 * (H / 2 * O) + 6 * (C * (O / 2))


# In[22]:


display(Math(str(current_system)))


# Python is not perfect for this, because it lacks the idea of parenthesis-free function dispatch and other things that make internal DSLs pretty.
