#!/usr/bin/env python
# coding: utf-8

# # 10.1 Deserialisation

# *Estimated time for this notebook: 10 minutes*

# YAML (a recursive acronym for "YAML Ain't Markup Language") is a human-readable data-serialization language.
# 
# We're going to slightly modify our previous model and look at how to serialise it to YAML.

# In[1]:


class Element:
    def __init__(self, symbol):
        self.symbol = symbol


class Molecule:
    def __init__(self):
        self.elements = {}  # Map from element to number of that element in the molecule

    def add_element(self, element, number):
        self.elements[element] = number

    def to_struct(self):
        return {element.symbol: number for element, number in self.elements.items()}


class Reaction:
    def __init__(self):
        self.reactants = {}  # Map from reactants to stoichiometries
        self.products = {}  # Map from products to stoichiometries

    def add_reactant(self, reactant, stoichiometry):
        self.reactants[reactant] = stoichiometry

    def add_product(self, product, stoichiometry):
        self.products[product] = stoichiometry

    def to_struct(self):
        return {
            "reactants": [x.to_struct() for x in self.reactants],
            "products": [x.to_struct() for x in self.products],
            "stoichiometries": list(self.reactants.values())
            + list(self.products.values()),
        }


class System:
    def __init__(self):
        self.reactions = []

    def add_reaction(self, reaction):
        self.reactions.append(reaction)

    def to_struct(self):
        return [x.to_struct() for x in self.reactions]


# In[2]:


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
combustion_glucose.add_reactant(glucose, 1)
combustion_glucose.add_reactant(o2, 6)
combustion_glucose.add_product(co2, 6)
combustion_glucose.add_product(h2o, 6)

combustion_hydrogen = Reaction()
combustion_hydrogen.add_reactant(h2, 2)
combustion_hydrogen.add_reactant(o2, 1)
combustion_hydrogen.add_product(h2o, 2)

s = System()
s.add_reaction(combustion_glucose)
s.add_reaction(combustion_hydrogen)

s.to_struct()


# In[3]:


import yaml

print(yaml.dump(s.to_struct()))


# # Deserialising non-normal data structures

# We can see that this data structure, although seemingly 
# sensible, is horribly **non-normal**.
# 
# * The stoichiometries information requires us to align each one to the corresponding molecule in order.
# * Each element is described multiple times: we will have to ensure that each mention of `C` comes back to the same constructed element object.

# In[4]:


class YamlDeSerialisingSystem:
    def __init__(self):
        self.elements = {}
        self.molecules = {}

    def add_element(self, candidate):
        if candidate not in self.elements:
            self.elements[candidate] = Element(candidate)
        return self.elements[candidate]

    def add_molecule(self, candidate):
        if tuple(candidate.items()) not in self.molecules:
            m = Molecule()
            for symbol, number in candidate.items():
                m.add_element(self.add_element(symbol), number)
            self.molecules[tuple(candidate.items())] = m
        return self.molecules[tuple(candidate.items())]

    def parse_system(self, system_dict):
        system = System()
        for reaction in system_dict:
            r = Reaction()
            stoichiometries = reaction["stoichiometries"]
            for molecule in reaction["reactants"]:
                r.add_reactant(self.add_molecule(molecule), stoichiometries.pop(0))
            for molecule in reaction["products"]:
                r.add_product(self.add_molecule(molecule), stoichiometries.pop(0))
            system.add_reaction(r)
        return system


# In[5]:


de_serialiser = YamlDeSerialisingSystem()
round_trip = de_serialiser.parse_system(s.to_struct())


# In[6]:


round_trip.to_struct()


# In[7]:


de_serialiser.elements


# In[8]:


de_serialiser.molecules


# In[9]:


list(round_trip.reactions[0].reactants.keys())[1].to_struct()


# In[10]:


list(round_trip.reactions[1].reactants.keys())[1].to_struct()


# In order to de-serialise this data, we had to construct a unique key to distinguish repeated mentions of the same identical item.
# 
# Effectively, we ended up choosing primary keys for our datatypes:

# In[11]:


list(de_serialiser.molecules.keys())


# Remembering that a combination of columns uniquely defining an item is a valid  key - there is a key correspondence between a candidate key in the database sense and a "hashable" data structure that can be used to a key in a `dict`. 
# 
# Note that to make this example even reasonably doable, we had to exclude additional data from the objects (mass, rate etc)

# # Normalising a YAML structure

# To make this structure easier to de-serialise, we can make a normalised file-format, by defining primary keys (hashable types) for each entity on write:

# In[12]:


class YamlSavingSystem:
    def __init__(self):
        self.elements = set()
        self.molecules = set()

    def element_key(self, element):
        return element.symbol

    def molecule_key(self, molecule):
        key = ""
        for element, number in molecule.elements.items():
            key += element.symbol
            key += str(number)
        return key

    def save(self, system):
        for reaction in system.reactions:
            for molecule in reaction.reactants:
                self.molecules.add(molecule)
                for element in molecule.elements:
                    self.elements.add(element)
            for molecule in reaction.products:
                self.molecules.add(molecule)
                for element in molecule.elements:
                    self.elements.add(element)

        result = {
            "elements": [self.element_key(element) for element in self.elements],
            "molecules": {
                self.molecule_key(molecule): {
                    self.element_key(element): number
                    for element, number in molecule.elements.items()
                }
                for molecule in self.molecules
            },
            "reactions": [
                {
                    "reactants": {
                        self.molecule_key(reactant): stoich
                        for reactant, stoich in reaction.reactants.items()
                    },
                    "products": {
                        self.molecule_key(product): stoich
                        for product, stoich in reaction.products.items()
                    },
                }
                for reaction in system.reactions
            ],
        }
        return result


# In[13]:


saver = YamlSavingSystem()
print(yaml.dump(saver.save(s)))


# We can see that to make an easily parsed file format, without having to
# guess-recognise repeated entities based on their names
# (which is highly subject to data entry error), we effectively recover
# the same tables as found for the database model.
# 
# An alternative is to use a simple integer for such a primary key:

# In[14]:


class YamlIntegerKeySavingSystem:
    def __init__(self):
        self.elements = {}
        self.molecules = {}

    def add_element(self, element):
        if element not in self.elements:
            self.elements[element] = len(self.elements)
        return self.elements[element]

    def add_molecule(self, molecule):
        if molecule not in self.molecules:
            self.molecules[molecule] = len(self.molecules)
        return self.molecules[molecule]

    def element_key(self, element):
        return self.elements[element]

    def molecule_key(self, molecule):
        return self.molecules[molecule]

    def save(self, system):
        for reaction in system.reactions:
            for molecule in reaction.reactants:
                self.add_molecule(molecule)
                for element in molecule.elements:
                    self.add_element(element)
            for molecule in reaction.products:
                self.add_molecule(molecule)
                for element in molecule.elements:
                    self.add_element(element)

        result = {
            "elements": [element.symbol for element in self.elements],
            "molecules": {
                self.molecule_key(molecule): {
                    self.element_key(element): number
                    for element, number in molecule.elements.items()
                }
                for molecule in self.molecules
            },
            "reactions": [
                {
                    "reactants": {
                        self.molecule_key(reactant): stoich
                        for reactant, stoich in reaction.reactants.items()
                    },
                    "products": {
                        self.molecule_key(product): stoich
                        for product, stoich in reaction.products.items()
                    },
                }
                for reaction in system.reactions
            ],
        }
        return result


# In[15]:


saver = YamlIntegerKeySavingSystem()
print(yaml.dump(saver.save(s)))

