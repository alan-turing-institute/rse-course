#!/usr/bin/env python
# coding: utf-8

# # Semantic file formats

# ## The dream of a semantic web

# So how can we fulfill the dream of a file-format which is **self-documenting**:
# universally unambiguous and interpretable?

# (Of course, it might not be true, but we don't have capacity to discuss how to model reliability
# and contested testimony.)

# By using URIs to define a controlled vocabulary, we can be unambiguous.
# 
# But the number of different concepts to be labelled is huge: so we need a **distributed** solution:
# a global structure of people defining ontologies, (with methods for resolving duplications and inconsistencies.)

# Humanity has a technology that can do this: the world wide web. We've seen how many different
# actors are defining ontologies.

# We also need a shared semantic structure for our file formats. XML allows everyone to define their
# own schema. Our universal file format requires a restriction to a basic language, which allows us
# to say the things we need:

# ## The Triple

# We can then use these defined terms to specify facts, using a URI for the subject, verb, and object of our sentence.

# In[1]:


get_ipython().run_cell_magic('writefile', 'reaction.ttl ', '\n<http://dbpedia.org/ontology/water>\n    <http://purl.obolibrary.org/obo/PATO_0001681>\n        "18.01528"^^<http://purl.obolibrary.org/obo/UO_0000088>\n            .')


# * [Water](http://dbpedia.org/ontology/water)
# * [Molar mass](http://purl.obolibrary.org/obo/PATO_0001681)
# * [Grams per mole](http://purl.obolibrary.org/obo/UO_0000088)

# This is an unambiguous statement, consisting of a subject, a verb, and an object, each of which is either a URI or a literal value. Here, the object is a *literal* with a type.

# ## RDF file formats

# We have used the RDF (Resource Description Framework) **semantic** format, in its "Turtle" syntactic form:
# 
# ```
# subject verb object .
# subject2 verb2 object2 .
# ```

# We can parse it:

# In[2]:


from rdflib import Graph

graph = Graph()
graph.parse("reaction.ttl", format="ttl")

print(len(graph))

for statement in graph:
    print(statement)


# The equivalent in **RDF-XML** is:

# In[3]:


print(graph.serialize(format="xml"))


# We can also use namespace prefixes in Turtle:

# In[4]:


print(graph.serialize(format="ttl"))


# ## Normal forms and Triples

# How do we encode the sentence "water has two hydrogen atoms" in RDF?

# See [Defining N-ary Relations on the Semantic Web](https://www.w3.org/TR/swbp-n-aryRelations/) for the definitive story.

# I'm not going to search carefully here for existing ontologies for the relationships we need:
# later we will understand how to define these as being the same as or subclasses of concepts
# in other ontologies. That's part of the value of a distributed approach: we can define
# what we need, and because the Semantic Web tools make rigorous the concepts of `rdfs:sameAs` and `rdfs:subclassOf` this will be OK.

# However, there's a problem. We can do:

# In[5]:


get_ipython().run_cell_magic('writefile', 'reaction.ttl ', '\n@prefix disr: <http://www.turing.ac.uk/rsd-engineering/ontologies/reactions/> .\n@prefix dbo: <http://dbpedia.org/ontology/> .\n@prefix obo: <http://purl.obolibrary.org/obo/> .\n\ndbo:water obo:PATO_0001681 "18.01528"^^obo:UO_0000088 ;\n          disr:containsElement obo:CHEBI_33260 .')


# * [ElementalHydrogen](http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:33260)

# We've introduced the semicolon in Turtle to say two statements about the same entity. The equivalent RDF-XML is:

# In[6]:


graph = Graph()
graph.parse("reaction.ttl", format="ttl")
print(len(graph))
print(graph.serialize(format="xml"))


# However, we can't express `hasTwo` in this way without making an infinite number of properties!
# 
# RDF doesn't have a concept of adverbs. Why not?

# It turns out there's a fundamental relationship between the RDF triple and a RELATION in
# the relational database model.
# 
# * The **subject** corresponds to the relational primary key.
# * The **verb** (RDF "property") corresponds to the relational column name.
# * The **object** corresponds to the value in the corresponding column.

# We already found out that to model the relationship of atoms to molecules we needed a join table, and the
# number of atoms was metadata on the join.
# 
# So, we need an entity type (RDF **class**) which describes an `ElementInMolecule`.

# Fortunately, we don't have to create a universal URI for every single relationship, thanks to RDF's concept of an anonymous entity: something which is uniquely defined by its relationships.
# 
# Imagine if we had to make a URN for oxygen-in-water, hydrogen-in-water etc!

# In[7]:


get_ipython().run_cell_magic('writefile', 'reaction.ttl ', '\n@prefix disr: <http://www.turing.ac.uk/rsd-engineering/ontologies/reactions/> .\n@prefix dbo: <http://dbpedia.org/ontology/> .\n@prefix obo: <http://purl.obolibrary.org/obo/> .\n@prefix xs: <http://www.w3.org/2001/XMLSchema> .\n\ndbo:water obo:PATO_0001681 "18.01528"^^obo:UO_0000088 ;\n          disr:containsElement obo:CHEBI_33260 ;\n          disr:hasElementQuantity [ \n              disr:countedElement obo:CHEBI_33260 ; \n              disr:countOfElement "2"^^xs:integer\n          ] .')


# Here we have used `[ ]` to indicate an anonymous entity, with no subject. We then define
# two predicates on that subject, using properties corresponding to our column names in the join table.

# Another turtle syntax for an anonymous "blank node" is this:

# In[8]:


get_ipython().run_cell_magic('writefile', 'reaction.ttl ', '\n@prefix disr: <http://www.turing.ac.uk/rsd-engineering/ontologies/reactions/> .\n@prefix dbo: <http://dbpedia.org/ontology/> .\n@prefix obo: <http://purl.obolibrary.org/obo/> .\n@prefix xs: <http://www.w3.org/2001/XMLSchema> .\n\ndbo:water obo:PATO_0001681 "18.01528"^^obo:UO_0000088 ;\n          disr:containsElement obo:CHEBI_33260 ;\n          disr:hasElementQuantity _:a .\n                \n_:a disr:countedElement obo:CHEBI_33260 ; \n    disr:countOfElement "2"^^xs:integer .')


# ## Serialising to RDF 

# Here's code to write our model to Turtle:

# In[9]:


get_ipython().run_cell_magic('writefile', 'chemistry_turtle_template.mko', '\n@prefix disr: <http://www.turing.ac.uk/rsd-engineering/ontologies/reactions/> .\n@prefix obo: <http://purl.obolibrary.org/obo/> .\n@prefix xs: <http://www.w3.org/2001/XMLSchema> .\n        \n[ \n%for reaction in reactions:\n    disr:hasReaction [\n        %for molecule in reaction.reactants.molecules:\n            disr:hasReactant [\n                %for element in molecule.elements:\n                    disr:hasElementQuantity [\n                        disr:countedElement [\n                            a obo:CHEBI_33259;\n                            disr:symbol "${element.symbol}"^^xs:string\n                        ] ;\n                        disr:countOfElement "${molecule.elements[element]}"^^xs:integer\n                    ];\n                %endfor\n                a obo:CHEBI_23367\n            ] ;\n        %endfor\n        %for molecule in reaction.products.molecules:\n            disr:hasProduct [\n                %for element in molecule.elements:\n                    disr:hasElementQuantity [\n                        disr:countedElement [\n                            a obo:CHEBI_33259;\n                            disr:symbol "${element.symbol}"^^xs:string\n                        ] ;\n                        disr:countOfElement "${molecule.elements[element]}"^^xs:integer\n                    ] ;\n                %endfor\n                a obo:CHEBI_23367\n            ] ;\n        %endfor\n        a disr:reaction\n    ] ;\n%endfor\na disr:system\n].')


# "a" in Turtle is an always available abbreviation for https://www.w3.org/1999/02/22-rdf-syntax-ns#type
#     

# We've also used:
# 
# * [Molecular entity](http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A23367)
# * [Elemental molecular entity](http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI%3A33259)

# I've skipped serialising the stoichiometries: to do that correctly I also need to create a
# relationship class for molecule-in-reaction.

# And we've not attempted to relate our elements to their formal definitions, since our model
# isn't recording this at the moment. We could add this statement later.

# In[10]:


import mako
from parsereactions import parser
from IPython.display import display, Math

with open("system.tex") as texfile:
    system = parser.parse(texfile.read())
display(Math(str(system)))


# In[11]:


from mako.template import Template

mytemplate = Template(filename="chemistry_turtle_template.mko")
with open("system.ttl", "w") as ttlfile:
    ttlfile.write((mytemplate.render(**vars(system))))


# In[12]:


get_ipython().system('cat system.ttl')


# In[13]:


graph = Graph()
graph.parse("system.ttl", format="ttl")
print(graph.serialize(format="xml"))


# We can see why the group of triples is called a *graph*: each node is an entity and each arc a property relating entities.

# Note that this format is very very verbose. It is **not** designed to be a nice human-readable format.
# 
# Instead, the purpose is to maximise the capability of machines to reason with found data.

# ## Formalising our ontology: RDFS

# Our http://www.turing.ac.uk/rsd-engineering/ontologies/reactions/ namespace now contains the following properties:

# * disr:hasReaction
# * disr:hasReactant
# * disr:hasProduct
# * disr:containsElement
# * disr:countedElement
# * disr:hasElementQuantity     
# * disr:countOfElement
# * disr:symbol

# And two classes:

# * disr:system
# * disr:reaction

# We would now like to find a way to formally specify some of the relationships between these.
#    
# The **type** (`http://www.w3.org/1999/02/22-rdf-syntax-ns#type` or `a`) of the subject of hasReaction
# must be `disr:system`.
# 
# 

# [RDFS](https://www.w3.org/TR/rdf-schema/) will allow us to specify which URNs define classes and which properties,
# and the domain and range (valid subjects and objects) of our properties.

# For example:

# In[14]:


get_ipython().run_cell_magic('writefile', 'turing_ontology.ttl', '\n@prefix disr: <http://www.turing.ac.uk/rsd-engineering/ontologies/reactions/> .\n@prefix obo: <http://purl.obolibrary.org/obo/> .\n@prefix xs: <http://www.w3.org/2001/XMLSchema> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n\ndisr:system a rdfs:Class .\ndisr:reaction a rdfs:Class .\ndisr:hasReaction a rdf:Property .\ndisr:hasReaction rdfs:domain disr:system .\ndisr:hasReaction rdfs:range disr:reaction .          ')


# This will allow us to make our file format briefer: given this schema, if
# 
# `_:a hasReaction _:b`
# 
# then we can **infer** that
# 
# `_:a a disr:system .
# _:b a disr:reaction .`
# 
# without explicitly stating it.
# 
# Obviously there's a lot more to do to define our other classes, including defining a class for our anonymous element-in-molecule nodes.

# This can get very interesting:

# In[15]:


get_ipython().run_cell_magic('writefile', 'turing_ontology.ttl', '\n@prefix disr: <http://www.turing.ac.uk/rsd-engineering/ontologies/reactions/> .\n@prefix obo: <http://purl.obolibrary.org/obo/> .\n@prefix xs: <http://www.w3.org/2001/XMLSchema> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n\ndisr:system a rdfs:Class .\ndisr:reaction a rdfs:Class .\ndisr:hasReaction a rdf:Property .\ndisr:hasReaction rdfs:domain disr:system .\ndisr:hasReaction rdfs:range disr:reaction .     \n\ndisr:hasParticipant a rdf:Property .\ndisr:hasReactant rdfs:subPropertyOf disr:hasParticipant .\ndisr:hasProduct rdfs:subPropertyOf disr:hasParticipant')


# [OWL](https://www.w3.org/TR/owl-ref/) extends RDFS even further. 

# Inferring additional rules from existing rules and schema is very powerful: an interesting branch of AI. (Unfortunately the [python tool](https://github.com/RDFLib/OWL-RL) for doing this automatically is currently not updated to python 3 so I'm not going to demo it. Instead, we'll see in a moment how to apply inferences to our graph to introduce new properties.)

# ## SPARQL

# So, once I've got a bunch of triples, how do I learn anything at all from them? The language
# is so verbose it seems useless!

# SPARQL is a very powerful language for asking questions of knowledge bases defined in RDF triples:

# In[16]:


results = graph.query(
    """
    SELECT DISTINCT ?asymbol ?bsymbol
    WHERE {
        ?molecule disr:hasElementQuantity ?a .
        ?a disr:countedElement ?elementa .
        ?elementa disr:symbol ?asymbol .
        ?molecule disr:hasElementQuantity ?b .
        ?b disr:countedElement ?elementb .
        ?elementb disr:symbol ?bsymbol
    }
    """
)

for row in results:
    print("Elements %s and %s are found in the same molecule" % row)


# We can see how this works: you make a number of statements in triple-form, but with some
# quantities as dummy-variables. SPARQL finds all possible subgraphs of the triple graph which
# are compatible with the statements in your query.
# 
# 

# We can also use SPARQL to specify **inference rules**:

# In[17]:


graph.update(
    """
    INSERT { ?elementa disr:inMoleculeWith ?elementb }
    WHERE {
        ?molecule disr:hasElementQuantity ?a .
        ?a disr:countedElement ?elementa .
        ?elementa disr:symbol ?asymbol .
        ?molecule disr:hasElementQuantity ?b .
        ?b disr:countedElement ?elementb .
        ?elementb disr:symbol ?bsymbol
    }
    """
)


# In[18]:


graph.query(
    """
    SELECT DISTINCT ?asymbol ?bsymbol
    WHERE {
          ?elementa disr:inMoleculeWith ?elementb .
          ?elementa disr:symbol ?asymbol .
          ?elementb disr:symbol ?bsymbol
    }
    """
)

for row in results:
    print("Elements %s and %s are found in the same molecule" % row)


# Exercise for reader: express "If x is the subject of a hasReaction relationship, then x must be a system"
# in SPARQL.

# Exercise for reader: search for a SPARQL endpoint knowledge base in your domain.
# 
# Connect to it using [Python RDFLib's SPARQL endpoint wrapper](https://github.com/RDFLib/sparqlwrapper) and ask it a question.
