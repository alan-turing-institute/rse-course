#!/usr/bin/env python
# coding: utf-8

# # 10.3 Markup Languages

# *Estimated time for this notebook: 15 minutes*

# XML and its relatives (including HTML) are based on the idea of *marking up* content with labels on its purpose:
#     
#     <name>James</name> is a <job>Programmer</job>

# One of the easiest ways to make a markup-language based fileformat is the use of a *templating language*.

# In[1]:


from IPython.display import Math, display
from parsereactions import parser

with open("system.tex", "r") as f_latex:
    system = parser.parse(f_latex.read())
display(Math(str(system)))


# In[2]:


get_ipython().run_cell_magic('writefile', 'chemistry_template.mko', '<?xml version="1.0" encoding="UTF-8"?>\n<system>\n%for reaction in reactions:\n    <reaction>\n        <reactants>\n        %for molecule in reaction.reactants.molecules:\n            <molecule stoichiometry="${reaction.reactants.molecules[molecule]}">\n            %for element in molecule.elements:\n                <atom symbol="${element.symbol}" number="${molecule.elements[element]}"/>\n            %endfor\n            </molecule>\n        %endfor\n        </reactants>\n        <products>\n        %for molecule in reaction.products.molecules:\n            <molecule stoichiometry="${reaction.products.molecules[molecule]}">\n            %for element in molecule.elements:\n                <atom symbol="${element.symbol}" number="${molecule.elements[element]}"/>\n            %endfor\n            </molecule>\n        %endfor\n        </products>\n    </reaction>\n%endfor\n</system>\n')


# In[3]:


from mako.template import Template

mytemplate = Template(filename="chemistry_template.mko")
with open("system.xml", "w") as xmlfile:
    xmlfile.write((mytemplate.render(**vars(system))))


# In[4]:


get_ipython().system('cat system.xml')


# Markup languages are verbose (jokingly called the "angle bracket tax") but very clear.

# ## Data as text

# The above serialisation specifies all data as XML "Attributes". An alternative is to put the data in the text:

# In[5]:


get_ipython().run_cell_magic('writefile', 'chemistry_template2.mko', '<?xml version="1.0" encoding="UTF-8"?>\n<system>\n%for reaction in reactions:\n    <reaction>\n        <reactants>\n        %for molecule in reaction.reactants.molecules:\n            <molecule stoichiometry="${reaction.reactants.molecules[molecule]}">\n            %for element in molecule.elements:\n                <atom symbol="${element.symbol}">${molecule.elements[element]}</atom>\n            %endfor\n            </molecule>\n        %endfor\n        </reactants>\n        <products>\n        %for molecule in reaction.products.molecules:\n            <molecule stoichiometry="${reaction.products.molecules[molecule]}">\n            %for element in molecule.elements:\n                <atom symbol="${element.symbol}">${molecule.elements[element]}</atom>\n            %endfor\n            </molecule>\n        %endfor\n        </products>\n    </reaction>\n%endfor\n</system>\n')


# In[6]:


mytemplate = Template(filename="chemistry_template2.mko")
with open("system2.xml", "w") as xmlfile:
    xmlfile.write((mytemplate.render(**vars(system))))


# In[7]:


get_ipython().system('cat system2.xml')


# ## Parsing XML

# XML is normally parsed by building a tree-structure of all the `tags` in the file, called a `DOM` or Document Object Model.

# In[8]:


from lxml import etree

with open("system.xml", "r") as xmlfile:
    tree = etree.parse(xmlfile)
print(etree.tostring(tree, pretty_print=True, encoding=str))


# We can navigate the tree, with each **element** being an iterable yielding its children: 

# In[9]:


tree.getroot()[0][0][1].attrib["stoichiometry"]


# ## Searching XML

# `xpath` is a sophisticated tool for searching XML DOMs:
# 
# There's a good explanation of how it works here: https://www.w3schools.com/xml/xml_xpath.asp but the basics are reproduced below.

# | XPath Expression | Result |
# | :- | :- |
# | `/bookstore/book[1]` | Selects the first `book` that is the child of a `bookstore` |
# | `/bookstore/book[last()]` | Selects the last `book` that is the child of a `bookstore` |
# | `/bookstore/book[last()-1]` | Selects the last but one `book` that is the child of a `bookstore` |
# | `/bookstore/book[position()<3]`| Selects the first two `book`s that are children of a `bookstore` |
# | `//title[@lang]` | Selects all `title`s that have an attribute named "lang" |
# | `//title[@lang='en']` | Selects all `title`s that have a "lang" attribute with a value of "en" |
# | `/bookstore/book[price>35.00]` | Selects all `book`s that are children of a `bookstore` and have a `price` with a value greater than 35.00 |
# | `/bookstore/book[price>35.00]/title` | Selects all the `title`s of a `book` of a `bookstore` that have a `price` with a value greater than 35.00 |

# In[10]:


# For all molecules
# ... with a child atom whose number attribute is '1'
# ... return the symbol attribute of that child
tree.xpath("//molecule/atom[@number='1']/@symbol")


# It is useful to understand grammars like these using the "FOR-LET-WHERE-ORDER-RETURN" (pronounced Flower) model.

# The above says: "For element in molecules where number is one, return symbol", roughly equivalent to `[element.symbol for element in molecule for molecule in document if element.number==1]` in Python.

# In[11]:


with open("system2.xml") as xmlfile:
    tree2 = etree.parse(xmlfile)
# For all molecules with a child atom whose text is 1
# ... return the symbol attribute of any child (however deeply nested)
print(tree2.xpath("//molecule[atom=1]//@symbol"))


# Note how we select on text content rather than attributes by using the element tag directly. The above says "for every molecule where at least one element is present with just a single atom, return all the symbols of all the elements in that molecule."

# ## Transforming XML : XSLT

# Two technologies (XSLT and XQUERY) provide capability to produce text output from an XML tree.

# We'll look at XSLT as support is more widespread, including in the python library we're using. XQuery is probably easier to use and understand, but with less support.
# 
# However, XSLT is a beautiful functional declarative language, once you read past the angle-brackets.

# Here's an XSLT to transform our reaction system into a LaTeX representation:

# In[12]:


get_ipython().run_cell_magic('writefile', 'xmltotex.xsl', '\n<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">\n    <xsl:output method="xml" indent="yes" omit-xml-declaration="yes" />\n        \n    <!-- Decompose reaction into "reactants \\rightarrow products" -->\n    <xsl:template match="//reaction">\n        <xsl:apply-templates select="reactants"/>\n        <xsl:text> \\rightarrow </xsl:text>\n        <xsl:apply-templates select="products"/>\n        <xsl:text>\\\\&#xa;</xsl:text>\n    </xsl:template>\n        \n    <!-- For a molecule anywhere except the first position write " + " and the number of molecules-->\n    <xsl:template match="//molecule[position()!=1]">\n        <xsl:text> + </xsl:text>\n        <xsl:apply-templates select="@stoichiometry"/>\n        <xsl:apply-templates/>\n    </xsl:template>\n\n    <!-- For a molecule in first position write the number of molecules -->\n    <xsl:template match="//molecule[position()=1]">\n        <xsl:apply-templates select="@stoichiometry"/>\n        <xsl:apply-templates/>\n    </xsl:template>\n\n    <!-- If the stoichiometry is one then ignore it -->\n    <xsl:template match="@stoichiometry[.=\'1\']"/>\n    \n    <!-- Otherwise, use the default template for attributes, which is just to copy value -->\n    \n    <!-- Decompose element into "symbol number" -->\n    <xsl:template match="//atom">\n        <xsl:value-of select="@symbol"/>\n        <xsl:apply-templates select="@number"/>\n    </xsl:template>\n        \n    <!-- If the number of elements/molecules is one then ignore it -->        \n    <xsl:template match="@number[.=1]"/>\n    \n    <!-- ... otherwise replace it with "_ value" -->        \n    <xsl:template match="@number[.!=1][10>.]">\n        <xsl:text>_</xsl:text>\n        <xsl:value-of select="."/>\n    </xsl:template>\n        \n    <!-- If a number is greater than 10 then wrap it in "{}" -->        \n    <xsl:template match="@number[.!=1][.>9]">\n        <xsl:text>_{</xsl:text>\n        <xsl:value-of select="."/>\n        <xsl:text>}</xsl:text>          \n    </xsl:template>\n        \n    <!-- Do not copy input whitespace to output -->\n    <xsl:template match="text()" />\n</xsl:stylesheet>\n')


# In[13]:


with open("xmltotex.xsl") as xslfile:
    transform_xsl = xslfile.read()
transform = etree.XSLT(etree.XML(transform_xsl))


# In[14]:


print(str(transform(tree)))


# In[15]:


display(Math(str(transform(tree))))


# ## Validating XML : Schema

# XML Schema is a way to define how an XML file is allowed to be: which attributes and tags should exist where.
#     
# You should always define one of these when using an XML file format.

# In[16]:


get_ipython().run_cell_magic('writefile', 'reactions.xsd', '\n<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">\n\n<xs:element name="atom">\n    <xs:complexType>\n        <xs:attribute name="symbol" type="xs:string"/>\n        <xs:attribute name="number" type="xs:integer"/>\n    </xs:complexType>\n</xs:element>\n    \n<xs:element name="molecule">\n    <xs:complexType>\n        <xs:sequence>\n            <xs:element ref="atom" maxOccurs="unbounded"/>\n        </xs:sequence>\n        <xs:attribute name="stoichiometry" type="xs:integer"/>\n    </xs:complexType>\n</xs:element>\n    \n<xs:element name="reaction">\n    <xs:complexType>\n        <xs:sequence>\n            <xs:element name="reactants">\n                <xs:complexType>\n                    <xs:sequence>\n                        <xs:element ref="molecule" maxOccurs="unbounded"/>\n                    </xs:sequence>\n                </xs:complexType>\n            </xs:element>\n            <xs:element name="products">\n                <xs:complexType>\n                    <xs:sequence>\n                        <xs:element ref="molecule" maxOccurs="unbounded"/>\n                    </xs:sequence>\n                </xs:complexType>\n            </xs:element>\n        </xs:sequence>\n    </xs:complexType>\n</xs:element>\n\n<xs:element name="system">\n    <xs:complexType>\n        <xs:sequence>\n            <xs:element ref="reaction" maxOccurs="unbounded"/>\n        </xs:sequence>\n    </xs:complexType>\n</xs:element>\n    \n</xs:schema>\n')


# In[17]:


with open("reactions.xsd") as xsdfile:
    schema_xsd = xsdfile.read()
schema = etree.XMLSchema(etree.XML(schema_xsd))


# In[18]:


parser = etree.XMLParser(schema=schema)


# In[19]:


with open("system.xml") as xmlfile:
    tree = etree.parse(xmlfile, parser)
# For all atoms return their symbol attribute
tree.xpath("//atom/@symbol")


# Compare parsing something that is not valid under the schema:

# In[20]:


get_ipython().run_cell_magic('writefile', 'invalid_system.xml', '\n<system>\n    <reaction>\n        <reactants>\n            <molecule stoichiometry="two">\n                <atom symbol="H" number="2"/>\n            </molecule>\n            <molecule stoichiometry="1">\n                <atom symbol="O" number="2"/>\n            </molecule>\n        </reactants>\n        <products>\n            <molecule stoichiometry="2">\n                <atom symbol="H" number="2"/>\n                <atom symbol="O" number="1"/>\n            </molecule>\n        </products>\n    </reaction>\n</system>\n')


# In[21]:


try:
    with open("invalid_system.xml") as xmlfile:
        tree = etree.parse(xmlfile, parser)
    tree.xpath("//element//@symbol")
except etree.XMLSyntaxError as e:
    print(e)


# This shows us that the validation has failed and why.
