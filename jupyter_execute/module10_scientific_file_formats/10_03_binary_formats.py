#!/usr/bin/env python
# coding: utf-8

# # 10.3 Binary formats

# *Estimated time for this notebook: 15 minutes*

# ## Binary file formats

# Now we're getting toward a numerically-based data structure, using integers for object keys, we should think about binary serialisation.
# 
# Binary file formats are much smaller than human-readable text based formats, so important when handling really big datasets.
# 
# One can compress a textual file format, of course, and with good compression algorithms this will be similar in size to the binary file.
# However, this has performance implications.
# 
# A hand-designed binary format is fast and small, at the loss of human readability.

# Let's remind ourselves of the model we have been using previously.

# In[1]:


class Element:
    def __init__(self, symbol, id):
        self.symbol = symbol
        self.id = id


class Molecule:
    def __init__(self, id):
        self.elements = {}
        self.id = id

    def add_element(self, element, number):
        self.elements[element] = number

    def to_struct(self):
        return {element.symbol: number for element, number in self.elements.items()}


class Reaction:
    def __init__(self):
        self.reactants = {}
        self.products = {}

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


# In[2]:


s = System()

c = s.add_element("C")
o = s.add_element("O")
h = s.add_element("H")

co2 = s.add_molecule()
co2.add_element(c, 1)
co2.add_element(o, 2)

h2o = s.add_molecule()
h2o.add_element(h, 2)
h2o.add_element(o, 1)

o2 = s.add_molecule()
o2.add_element(o, 2)

h2 = s.add_molecule()
h2.add_element(h, 2)

glucose = s.add_molecule()
glucose.add_element(c, 6)
glucose.add_element(h, 12)
glucose.add_element(o, 6)

combustion_glucose = s.add_reaction()
combustion_glucose.add_reactant(glucose, 1)
combustion_glucose.add_reactant(o2, 6)
combustion_glucose.add_product(co2, 6)
combustion_glucose.add_product(h2o, 6)


# In[3]:


combustion_hydrogen = s.add_reaction()
combustion_hydrogen.add_reactant(h2, 2)
combustion_hydrogen.add_reactant(o2, 1)
combustion_hydrogen.add_product(h2o, 2)


# The problem with binary file formats, is that, lacking complex data structures, one needs to supply the *length* of an item before that item:

# In[4]:


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


# In[5]:


characterarray = []
FakeBinarySavingSystem().save(s, characterarray)


# In[6]:


characterarray


# Deserialisation is left **as an exercise for the reader** :).

# ## Endian-robust binary file formats

# Having prepared our data as a sequence of data which can be recorded in a single byte,
# we might think a binary file format on disk is as simple as saving
# each number in one byte:

# In[7]:


# First, turn symbol characters to equivalent integers (ascii)
intarray = [x.encode("ascii")[0] if isinstance(x, str) else x for x in characterarray]
intarray


# In[8]:


bytearray(intarray)


# In[9]:


with open("system.mol", "wb") as binfile:
    binfile.write(bytearray(intarray))


# However, this misses out on an unfortunate problem if we end up with large enough numbers to need more than one byte per integer, or we want to represent floats: different computer designs will put the most-significant bytes of a multi-byte integer or float either at the beginning ('big endian' systems) or at the end ('little endian' systems).

# To get around this, we need to use a portable standard for making binary files.
# 
# One possible choice is **XDR** (standing for eXternal Data Representation). XDR is a standard data serialization format that accounts for endian differences between systems.

# In[10]:


import xdrlib


class XDRSavingSystem(System):
    def __init__(self, system):
        super().__init__()
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


# In[11]:


xdrsys = XDRSavingSystem(s)


# In[12]:


xdrbuffer = xdrsys.save()
xdrbuffer.get_buffer()


# ## A higher level approach to binary file formats: HDF5

# This was quite painful. We've shown you it because it is very likely
# you will encounter this kind of unpleasant binary file format in your work.

# However, one recommended approach to building binary file formats is to use HDF5 (Hierarchical Data Format), a much higher level binary file format.

# HDF5's approach requires you to represent your system in terms of high-dimensional matrices, like NumPy arrays.
# It then saves these, and handles all the tedious number-of-field management for you.

# In[13]:


import h5py
import numpy as np


class HDF5SavingSystem(System):
    def __init__(self, system):
        super().__init__()
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


# In[14]:


saver = HDF5SavingSystem(s)


# In[15]:


saver.element_symbols()


# In[16]:


saver.molecule_matrix()


# In[17]:


saver.reaction_matrix()


# In[18]:


saver.write("foo.hdf5")


# Note that this binary representation is *not* human readable at all.

# In[19]:


with open("foo.hdf5", "rb") as f_in:
    bytes = f_in.read()
bytes[0:100]


# In[20]:


hdf_load = h5py.File("foo.hdf5")


# In[21]:


np.array(hdf_load["reactions"])


# Using a `sparse matrix` storage would be even better here, but we don't have time for that!
