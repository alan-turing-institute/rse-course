### "dense"

import species
def AddToReaction(name, reaction):
    reaction.append(species.Species(name))

### "sparse"

from species import Species

def add_to_reaction(a_name,
                    a_reaction):
  l_species = Species(a_name)
  a_reaction.append( l_species )

### "layout1" 

reaction= {
    "reactants": ["H","H","O"],
    "products": ["H2O"]
}

### "layout2"

reaction2=(
{
  "reactants":
  [
    "H",
    "H",
    "O"
  ],
  "products":
  [
    "H2O"
  ]
}
)

### "naming1"

class ClassName(object):
    def methodName(variable_name):
        instance_variable=variable_name

### "naming2"

class class_name(object):
    def method_name(a_variable):
        m_instance_variable=a_variable

### "setup"

# Define some variables to make following fragments work
sInput="2.0"
input ="2.0"
iOffset=1
offset =1
anothervariable=1
flag1=True
variable=1
flag2=False
def do_something(): pass

### "naming3"

fNumber= float(sInput) + iOffset
number = float(input)  + offset

### "syntax1"

anothervariable+=1
if ((variable==anothervariable) and flag1 or flag2): do_something()

### "syntax2"

anothervariable = anothervariable + 1
variable_equality = (variable == anothervariable);
if ((variable_equality and flag1) or flag2):
   do_something()

