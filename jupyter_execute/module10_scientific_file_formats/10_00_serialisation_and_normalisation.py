#!/usr/bin/env python
# coding: utf-8

# # What can go wrong?

# Consider a simple python computational model of chemical reaction networks:

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
                str(element) + Molecule.as_subscript(self.elements[element])
                for element in self.elements
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
        else:
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


from IPython.display import display, Math

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
# Next lecture, we'll look at how we might create a file format which does indeed look like such a fluent mathematical
# representation, which we'll call a **Domain Specific Language**.

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
# However, this would allow our data file to be potentially be self-inconsistent, violating the design principle that each piece of information should be stated only once. A data structure of this type is said to be NOT **second normal form**.
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
# (Each atom can be in more than one molecule, and each molecule has more than one atom.)

# Note each table needs to have a set of columns which taken together form a unique identifier for that row; called a "key". If more than one is possible, we choose one and call it a **primary key**. (And in practice, we normally choose a single column for this: hence the 'rel_number' column, though the tuple {molecule, symbol} here is another **candidate key**.)

# Now, proper database tools use much more sophisticated representations than just csv files -
# including **indices** to enable hash-table like efficient lookups, and support for managing multiple users at the same time.
# 
# However, the **principles** of database normalisation and the relational model will be helpful
# right across our thinking about data representation, whether these are dataframes in Pandas, tensors in tensorflow, or anything else...

# ## Making a database - SQLite

# Let's look at how we would use a simple database in Python to represent atoms and molecules. If you've never seen SQL before, you might want to attend an introductory course, such as one of the 'Software Carpentry' sessions. Here we're going to assume some existing knowledge but we will use a Python-style way to interact with databases instead of relying on raw SQL.

# In[11]:


import os

try:
    os.remove("molecules.db")
    print("Removing database to start again from scratch")
except FileNotFoundError:
    print("No DB since this notebook was last run")


# In[12]:


import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///molecules.db", echo=True)


# SQLite is a simple very-lightweight database tool - without support for concurrent users - but it's great for little hacks like this. For full-on database work you'll probably want to use a more fully-featured database like https://www.postgresql.org.

# The metadata for the database describing the tables present, and their columns, is defined in Python using SQLAlchemy, the leading python database tool, thus:

# In[13]:


from sqlalchemy import Table, Column, Integer, Float, String, MetaData, ForeignKey

metadata = MetaData()
molecules = Table(
    "molecules",
    metadata,
    Column("name", String, primary_key=True),
    Column("mass", Float),
)

atoms = Table(
    "atoms",
    metadata,
    Column("symbol", String, primary_key=True),
    Column("number", Integer),
)


# In[14]:


atoms_in_molecules = Table(
    "atoms_molecules",
    metadata,
    Column("atom", ForeignKey("atoms.symbol")),
    Column("molecule", ForeignKey("molecules.name")),
    Column("number", Integer),
)


# In[15]:


metadata.create_all(engine)
print(metadata)


# Note the SQL syntax for creating tables is generated by the python tool, and sent to the database server.

# ```
# CREATE TABLE molecules (
# 	name VARCHAR NOT NULL, 
# 	mass FLOAT, 
# 	PRIMARY KEY (name)
# )
# ```

# We'll turn off our automatic printing of all the raw sql to avoid this notebook being unreadable.

# In[16]:


engine.echo = False


# We can also write data to our database using this python tooling:

# In[17]:


ins = molecules.insert().values(name="water", mass="18.01")


# In[18]:


conn = engine.connect()
conn.execute(ins)


# And query it:

# In[19]:


from sqlalchemy.sql import select

s = select([molecules])
result = conn.execute(s)
print(result.fetchone()["mass"])


# If we have enough understanding of SQL syntax, we can use appropriate **join** statements to find, for example, the mass of all molecules which contain oxygen:

# In[20]:


conn.execute(molecules.insert().values(name="oxygen", mass="32.00"))
conn.execute(atoms.insert().values(symbol="O", number=8))
conn.execute(atoms.insert().values(symbol="H", number=1))
conn.execute(atoms_in_molecules.insert().values(molecule="water", atom="O", number=1))
conn.execute(atoms_in_molecules.insert().values(molecule="oxygen", atom="O", number=1))
conn.execute(atoms_in_molecules.insert().values(molecule="water", atom="H", number=2))


# In[21]:


result = conn.execute(
    """
    SELECT mass
    FROM   molecules
          JOIN atoms_molecules
            ON molecules.NAME = atoms_molecules.molecule
          JOIN atoms
            ON atoms.symbol = atoms_molecules.atom
    WHERE  atoms.symbol = 'H'
    """
)
print(result.fetchall())


# But we can do much better...

# ## Data and Objects - the Object-Relational-Mapping

# We notice that when we find a correct relational model for our data, many of the rows are suggestive of exactly the data
# we would expect to supply to an object constructor - data about an object. References to keys of other tables in rows suggest composition
# relations while many-to-many join tables often represent aggregation relationships, and data about the relationship.

# As a result of this, powerful tools exist to **automatically** create object structures from database schema, including saving and loading.

# In[22]:


import os

try:
    os.remove("molecules.db")
    print("Removing database to start again from scratch")
except FileNotFoundError:
    print("No DB since this notebook was last run")


# In[23]:


import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///molecules.db")


# In[24]:


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Element(Base):
    __tablename__ = "atoms"
    symbol = Column(String, primary_key=True)
    number = Column(Integer)
    molecules = relationship("AtomsPerMolecule", backref="atom")


# In[25]:


class Molecule(Base):
    __tablename__ = "molecules"
    name = Column(String, primary_key=True)
    mass = Column(Float)
    atoms = relationship("AtomsPerMolecule", backref="molecule")


# In[26]:


class AtomsPerMolecule(Base):
    __tablename__ = "atoms_per_molecule"
    id = Column(Integer, primary_key=True)
    atom_id = Column(None, ForeignKey("atoms.symbol"))
    molecule_id = Column(None, ForeignKey("molecules.name"))
    number = Column(Integer)


# If we now create our tables, the system will automatically create a DB:

# In[27]:


Base.metadata.create_all(engine)


# In[28]:


engine.echo = False


# And we can create objects with a simple interface that looks just like ordinary classes:

# In[29]:


oxygen = Element(symbol="O", number=8)
hydrogen = Element(symbol="H", number=1)
elements = [oxygen, hydrogen]


# In[30]:


water = Molecule(name="water", mass=18.01)
oxygen_m = Molecule(name="oxygen", mass=16.00)
hydrogen_m = Molecule(name="hydrogen", mass=2.02)
molecules = [water, oxygen_m, hydrogen_m]


# In[31]:


# Note that we are using the `backref` name to construct the `atom_id` and `molecule_id`.
# These lookup instances of Element and Molecule that are already in our database
amounts = [
    AtomsPerMolecule(atom=oxygen, molecule=water, number=1),
    AtomsPerMolecule(atom=hydrogen, molecule=water, number=2),
    AtomsPerMolecule(atom=oxygen, molecule=oxygen_m, number=2),
    AtomsPerMolecule(atom=hydrogen, molecule=hydrogen_m, number=2),
]


# In[32]:


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


# In[33]:


session.bulk_save_objects(elements + molecules + amounts)


# In[34]:


oxygen.molecules[0].molecule.name


# In[35]:


session.query(Molecule).all()[0].name


# In[36]:


session.commit()


# This is a very powerful technique - we get our class-type interface in python, with database persistence and searchability for free!

# ## Moving on from databases

# Databases are often a good choice for storing data, but can only be interacted with programmatically. Often, we want to make a file format to represent our dataset which can be easily replicated or shared. The next part of this module focuses on the design of such file-formats, both binary and **human-readable**.

# One choice, now we know about it, is to serialise all the database tables as CSV:

# In[37]:


import pandas


# In[38]:


str(session.query(Molecule).statement)


# In[39]:


dataframe = pandas.read_sql(session.query(Molecule).statement, session.bind)


# In[40]:


dataframe


# In[41]:


print(dataframe.to_csv())


# Deserialising is also easy:

# In[42]:


get_ipython().run_cell_magic('writefile', 'atoms.csv', '\nsymbol,number\nC,6\nN,7\n')


# In[43]:


from pathlib import Path

atoms = pandas.read_csv(open("atoms.csv"))
atoms


# In[44]:


atoms.to_sql("atoms", session.bind, if_exists="append", index=False)


# In[45]:


session.query(Element).all()[3].number


# However, we know from last term that another common choice is to represent
# such complicated data structures in YAML. The implications of what we've just learned for serialising to and from such
# structured data is the topic of the next lecture.
