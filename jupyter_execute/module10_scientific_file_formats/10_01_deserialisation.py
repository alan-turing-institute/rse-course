#!/usr/bin/env python
# coding: utf-8

# # Deserialisation

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
        return {x.symbol: self.elements[x] for x in self.elements}


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

    def parse_system(self, system):
        s = System()
        for reaction in system:
            r = Reaction()
            stoichiometries = reaction["stoichiometries"]
            for molecule in reaction["reactants"]:
                r.add_reactant(self.add_molecule(molecule), stoichiometries.pop(0))
            for molecule in reaction["products"]:
                r.add_product(self.add_molecule(molecule), stoichiometries.pop(0))
            s.add_reaction(r)
        return s


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


# ## Reference counting

# The above approach of using a dictionary to determine the integer keys
# for objects is a bit clunky.
# 
# Another good approach is to use counted objects either via a static member or by using a factory pattern:

# In[16]:


class Element:
    def __init__(self, symbol, id):
        self.symbol = symbol
        self.id = id


class Molecule:
    def __init__(self, id):
        self.elements = {}  # Map from element to number of that element in the molecule
        self.id = id

    def add_element(self, element, number):
        self.elements[element] = number

    def to_struct(self):
        return {x.symbol: self.elements[x] for x in self.elements}


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


class System:  # This will be our factory
    def __init__(self):
        self.reactions = []
        self.elements = []
        self.molecules = []

    def add_element(self, symbol):
        new_element = Element(symbol, len(self.elements))
        self.elements.append(new_element)
        return new_element

    def add_molecule(self):
        new_molecule = Molecule(len(self.molecules))
        self.molecules.append(new_molecule)
        return new_molecule

    def add_reaction(self):
        new_reaction = Reaction()
        self.reactions.append(new_reaction)
        return new_reaction

    def save(self):

        result = {
            "elements": [element.symbol for element in self.elements],
            "molecules": {
                molecule.id: {
                    element.id: number for element, number in molecule.elements.items()
                }
                for molecule in self.molecules
            },
            "reactions": [
                {
                    "reactants": {
                        reactant.id: stoich
                        for reactant, stoich in reaction.reactants.items()
                    },
                    "products": {
                        product.id: stoich
                        for product, stoich in reaction.products.items()
                    },
                }
                for reaction in self.reactions
            ],
        }

        return result


# In[17]:


s2 = System()

c = s2.add_element("C")
o = s2.add_element("O")
h = s2.add_element("H")

co2 = s2.add_molecule()
co2.add_element(c, 1)
co2.add_element(o, 2)

h2o = s2.add_molecule()
h2o.add_element(h, 2)
h2o.add_element(o, 1)

o2 = s2.add_molecule()
o2.add_element(o, 2)

h2 = s2.add_molecule()
h2.add_element(h, 2)

glucose = s2.add_molecule()
glucose.add_element(c, 6)
glucose.add_element(h, 12)
glucose.add_element(o, 6)

combustion_glucose = s2.add_reaction()
combustion_glucose.add_reactant(glucose, 1)
combustion_glucose.add_reactant(o2, 6)
combustion_glucose.add_product(co2, 6)
combustion_glucose.add_product(h2o, 6)


# In[18]:


combustion_hydrogen = s2.add_reaction()
combustion_hydrogen.add_reactant(h2, 2)
combustion_hydrogen.add_reactant(o2, 1)
combustion_hydrogen.add_product(h2o, 2)


# In[19]:


s2.save()


# In[20]:


print(yaml.dump(s2.save()))


# ## Binary file formats

# Now we're getting toward a numerically-based data structure, using integers for object keys, we should think about binary serialisation.
# 
# Binary file formats are much smaller than human-readable text based formats, so important when handling really big datasets.
# 
# One can compress a textual file format, of course, and with good compression algorithms this will be similar in size to the binary file. (C.f. discussions of Shannon information density!) However, this has performance implications.
# 
# A hand-designed binary format is fast and small, at the loss of human readability.

# The problem with binary file formats, is that, lacking complex data structures, one needs to supply the *length* of an item before that item:

# In[21]:


class FakeBinarySavingSystem:
    # Pretend binary-style writing to a list to make it easier to read at first.
    def save(self, system, buffer):
        buffer.append(len(system.elements))
        for element in system.elements:
            buffer.append(element.symbol)

        buffer.append(len(system.molecules))
        for molecule in system.molecules:
            buffer.append(len(molecule.elements))
            for element, number in molecule.elements.items():
                buffer.append(element.id)
                buffer.append(number)

        buffer.append(len(system.reactions))
        for reaction in system.reactions:
            buffer.append(len(reaction.reactants))
            for reactant, stoich in reaction.reactants.items():
                buffer.append(reactant.id)
                buffer.append(stoich)
            buffer.append(len(reaction.products))
            for product, stoich in reaction.products.items():
                buffer.append(product.id)
                buffer.append(stoich)


# In[22]:


import io

arraybuffer = []
FakeBinarySavingSystem().save(s2, arraybuffer)


# In[23]:


arraybuffer


# Deserialisation is left **as an exercise for the reader** :).

# ## Endian-robust binary file formats

# Having prepared our data as a sequence of data which can be recorded in a single byte,
# we might think a binary file format on disk is as simple as saving
# each number in one byte:

# In[24]:


# First, turn symbol characters to equivalent integers (ascii)
intarray = [x.encode("ascii")[0] if type(x) == str else x for x in arraybuffer]
intarray


# In[25]:


bytearray(intarray)


# In[26]:


with open("system.mol", "bw") as binfile:
    binfile.write(bytearray(intarray))


# However, this misses out on an unfortunate problem if we end up with large enough numbers to need more than one byte per integer, or we want to represent floats: different computer designs but the most-significant bytes of a multi-byte integer or float at the beginning or
# end ('big endian' or 'little endian' data).

# To get around this, we need to use a portable standard for making binary files.
# 
# One possible choice is **XDR** (standing for eXternal Data Representation). XDR is a standard data serialization format that accounts for endian differences between systems.

# In[27]:


import xdrlib


class XDRSavingSystem(System):
    def __init__(self, system):
        # Shallow Copy constructor
        self.elements = system.elements
        self.reactions = system.reactions
        self.molecules = system.molecules
        self.buffer = xdrlib.Packer()

    def _pack_pair(self, item):
        self.buffer.pack_int(item[0].id)
        self.buffer.pack_int(item[1])

    def _pack_molecule(self, mol):
        self.buffer.pack_array(mol.elements.items(), self._pack_pair)

    def _pack_reaction(self, reaction):
        self.buffer.pack_array(reaction.reactants.items(), self._pack_pair)
        self.buffer.pack_array(reaction.products.items(), self._pack_pair)

    def save(self):
        el_symbols = list(map(lambda x: x.symbol.encode("utf-8"), self.elements))
        # Note that pack_array AUTOMATICALLY packs the length of the array first!
        self.buffer.pack_array(el_symbols, self.buffer.pack_string)
        self.buffer.pack_array(self.molecules, self._pack_molecule)
        self.buffer.pack_array(self.reactions, self._pack_reaction)
        return self.buffer


# In[28]:


xdrsys = XDRSavingSystem(s2)


# In[29]:


xdrbuffer = xdrsys.save()
xdrbuffer.get_buffer()


# ## A higher level approach to binary file formats: HDF5

# This was quite painful. We've shown you it because it is very likely
# you will encounter this kind of unpleasant binary file format in your work.

# However, the recommended approach to building binary file formats is to use HDF5 (Hierarchical Data Format), a much higher level binary file format.

# HDF5's approach requires you to represent your system in terms of high-dimensional matrices, like NumPy arrays.
# It then saves these, and handles all the tedious number-of-field management for you.

# In[30]:


import h5py
import numpy as np


class HDF5SavingSystem(System):
    def __init__(self, system):
        # Shallow Copy constructor
        self.elements = system.elements
        self.reactions = system.reactions
        self.molecules = system.molecules

    def element_symbols(self):
        return list(map(lambda x: x.symbol.encode("ascii"), self.elements))

    def molecule_matrix(self):
        molecule_matrix = np.zeros((len(self.elements), len(self.molecules)), dtype=int)

        for molecule in self.molecules:
            for element, n in molecule.elements.items():
                molecule_matrix[element.id, molecule.id] = n

        return molecule_matrix

    def reaction_matrix(self):
        reaction_matrix = np.zeros(
            (len(self.molecules), len(self.reactions)), dtype=int
        )

        for i, reaction in enumerate(self.reactions):
            for reactant, n in reaction.reactants.items():
                reaction_matrix[reactant.id, i] = -1 * n

            for product, n in reaction.products.items():
                reaction_matrix[product.id, i] = n

        return reaction_matrix

    def write(self, filename):
        hdf = h5py.File(filename, "w")
        string_type = h5py.special_dtype(vlen=bytes)
        hdf.create_dataset(
            "symbols", (len(self.elements), 1), string_type, self.element_symbols()
        )
        hdf.create_dataset("molecules", data=self.molecule_matrix())
        hdf.create_dataset("reactions", data=self.reaction_matrix())
        hdf.close()


# In[31]:


saver = HDF5SavingSystem(s2)


# In[32]:


saver.element_symbols()


# In[33]:


saver.molecule_matrix()


# In[34]:


saver.reaction_matrix()


# In[35]:


saver.write("foo.hdf5")


# Note that this binary representation is *not* human readable at all.

# In[36]:


get_ipython().run_cell_magic('bash', '', '# Read the first 100 characters from the file\nhead -c 100 foo.hdf5')


# In[37]:


import h5py

hdf_load = h5py.File("foo.hdf5")


# In[38]:


np.array(hdf_load["reactions"])


# Using a `sparse matrix` storage would be even better here, but we don't have time for that!
