#!/usr/bin/env python
# coding: utf-8

# # 10.0 Serialising and normalising data

# *Estimated time for this notebook: 15 minutes*

# Consider a simple python computational model of chemical reaction networks.
# In particular let's consider the combustion of glucose to carbon dioxide and water.

# In[1]:


class Element:
    def __init__(self, symbol, number):
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return str(self.symbol)


class Molecule:
    def __init__(self, mass):
        self.elements = {}  # Map from element to number of that element in the molecule
        self.mass = mass

    def add_element(self, element, number):
        self.elements[element] = number

    @staticmethod
    def as_subscript(number):
        if number == 1:
            return ""
        if number < 10:
            return "_" + str(number)
        return "_{" + str(number) + "}"

    def __str__(self):
        return "".join(
            [
                str(element) + Molecule.as_subscript(number)
                for element, number in self.elements.items()
            ]
        )


class Reaction:
    def __init__(self):
        self.reactants = {}  # Map from reactants to stoichiometries
        self.products = {}  # Map from products to stoichiometries

    def add_reactant(self, reactant, stoichiometry):
        self.reactants[reactant] = stoichiometry

    def add_product(self, product, stoichiometry):
        self.products[product] = stoichiometry

    @staticmethod
    def print_if_not_one(number):
        if number == 1:
            return ""
        return str(number)

    @staticmethod
    def side_as_string(side):
        return " + ".join(
            [
                Reaction.print_if_not_one(side[molecule]) + str(molecule)
                for molecule in side
            ]
        )

    def __str__(self):
        return (
            Reaction.side_as_string(self.reactants)
            + " \\rightarrow "
            + Reaction.side_as_string(self.products)
        )


class System:
    def __init__(self):
        self.reactions = []

    def add_reaction(self, reaction):
        self.reactions.append(reaction)

    def __str__(self):
        return "\n".join(self.reactions)


# In[2]:


c = Element("C", 12)
o = Element("O", 8)
h = Element("H", 1)

co2 = Molecule(44.01)
co2.add_element(c, 1)
co2.add_element(o, 2)

h2o = Molecule(18.01)
h2o.add_element(h, 2)
h2o.add_element(o, 1)

o2 = Molecule(32.00)
o2.add_element(o, 2)

glucose = Molecule(180.16)
glucose.add_element(c, 6)
glucose.add_element(h, 12)
glucose.add_element(o, 6)

combustion = Reaction()
combustion.add_reactant(glucose, 1)
combustion.add_reactant(o2, 6)
combustion.add_product(co2, 6)
combustion.add_product(h2o, 6)

print(combustion)


# In[3]:


from IPython.display import Math, display

display(Math(str(combustion)))


# We could reasonably consider using the LaTeX representation of this as a fileformat for reactions. (Though we need to represent the molecular mass in some way we've not thought of.)
# 
# We've already shown how to **serialise** the data to this representation.
# How hard would it be to **deserialise** it?
# 
# Actually, pretty darn hard.
# 
# In the wild, such datafiles will have all kinds of complications, and making a hand-coded string parser for such
# text will be highly problematic. In this lecture, we're going to look at the kind of problems that can arise, and
# some standard ways to solve them, which will lead us to the idea of **normalisation** in databases.
# 
# **Note** It is possible to create a structure which does look like such a fluent mathematical representation, which is known as a **Domain Specific Language**. Some information on this is covered in the optional [Domain Specific Languages notebook](10_x0_optional_domain_specific_languages.ipynb).

# ## Non-normal data representations: First normal form.

# Consider the mistakes that someone might make when typing in a reaction in the above format: they could easily, if there are multiple reactions in a system, type glucose in correctly as `C_6H_{12}O_6` the first time, but the second type accidentally type `C_6H_{12}o_6.`
# 
# The system wouldn't know these are the same molecule, so, for example, if building a mass action model of reaction kinetics, the differential equations would come out wrong. 

# The natural-seeming solution to this is, in your data format, to name each molecule and atom, and consider a representation in terms of CSV files:

# In[4]:


get_ipython().run_cell_magic('writefile', 'molecules.csv', '# name, elements, numbers\n\nwater, H O, 2 1\noxygen, O, 2\ncarbon_dioxide, C O, 1 2\nglucose, C H O, 6 12 6\n')


# In[5]:


get_ipython().run_cell_magic('writefile', 'reactions.csv', '\n# name, reactants, products, reactant_stoichiometries, product_stoichiometries\n\ncombustion_of_glucose, glucose oxygen, carbon_dioxide water, 1 6, 6 6\n')


# Writing a parser for these files would be very similar to the earthquake problem that you've already encountered.
# 
# However, the existence of multiple values in one column indicates that this file format is NOT **first normal form** (1NF).
# 
# **Note:** _A table is in first normal form if: every column is unique; no rows are duplicated; each column/row intersection contains only one value._

# It is not uncommon to encounter file-formats that violate 1NF in the wild. The main problem with them is that you will eventually have to deal with the separation character that you picked (`;` in this case) turning up in someone's content and you'll need to work out how to escape it.
# 
# The art of designing serialisations which work as row-and-column value tables for more complex data structures is the core of database design.

# ## Normalising the reaction model - a bad first attempt.

# How could we go about normalising this model. One choice is to list each molecule-element **relation** as a separate table row:

# In[6]:


get_ipython().run_cell_magic('writefile', 'molecules.csv', '# name, element, number\n\nwater, H, 2\nwater, O, 1\noxygen, O, 2\ncarbon_dioxide, C, 1\ncarbon_dioxide, O, 2\n')


# This is fine as far as it goes, but, it falls down as soon as we want to associate another property with a molecule and atom.
# 
# We could repeat the data each time:

# In[7]:


get_ipython().run_cell_magic('writefile', 'molecules.csv', '# name, element, number, molecular_mass, atomic_number\n\nwater, H, 2, 18.01, 1\nwater, O, 1, 18.01, 8\noxygen, O, 2, 32.00, 8\n')


# The existence of the same piece of information in multiple locations (eg. the `18.01` molecular mass of water) indicates that this file format is NOT **second normal form** (2NF).
# 
# 
# Furthermore, this would allow our data file to be potentially be self-inconsistent, violating the design principle that each piece of information should be stated only once. A data structure of this type is said to be NOT **second normal form**.
# 
# **Note:** _A table is in second normal form if: it is in first normal form; none of its attributes depend on any other attribute except the primary key._

# ## Normalising the model - relations and keys

# So, how do we do this correctly?

# We need to specify data about each molecule, reaction and atom once, and then specify the **relations** between them.

# In[8]:


get_ipython().run_cell_magic('writefile', 'molecules.csv', '# name, molecular_mass\n\nwater, 18.01\noxygen, 32.00\n')


# In[9]:


get_ipython().run_cell_magic('writefile', 'atoms.csv', '\n# symbol, atomic number\nH, 1\nO, 8\nC, 6\n')


# In[10]:


get_ipython().run_cell_magic('writefile', 'atoms_in_molecules.csv', '\n# rel_number, molecule, symbol, number\n0, water, H, 2\n1, water, O, 1\n2, oxygen, O, 2\n')


# This last table is called a **join table** - and is needed whenever we want to specify a "many-to-many" relationship.
# Here, each atom can be in more than one molecule, and each molecule has more than one atom.

# Note each table needs to have a set of columns which taken together form a unique identifier for that row; called a "key".
# If more than one is possible, we choose one and call it a **primary key**.
# In practice, we normally choose a single column for this: hence the 'rel_number' column, though the tuple {molecule, symbol} here is another **candidate key**.
