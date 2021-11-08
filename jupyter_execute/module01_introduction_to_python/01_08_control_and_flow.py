#!/usr/bin/env python
# coding: utf-8

# # Control and Flow

# ## Turing completeness

# Now that we understand how we can use objects to store and model our data, we only need to be able to control the flow of our
# program in order to have a program that can, in principle, do anything!
# 
# Specifically we need to be able to:
# 
# * Control whether a program statement should be executed or not, based on a variable. "Conditionality"
# * Jump back to an earlier point in the program, and run some statements again. "Branching"

# Once we have these, we can write computer programs to process information in arbitrary ways: we are *Turing Complete*!

# ## Conditionality

# Conditionality is achieved through Python's `if` statement:

# In[1]:


x = 5

if x < 0:
    print(x, " is negative")


# The absence of output here means the if clause prevented the print statement from running.

# In[2]:


x = -10

if x < 0:
    print(x, " is negative")


# The first time through, the print statement never happened.

# The **controlled** statements are indented. Once we remove the indent, the statements will once again happen regardless. 

# ### Else and Elif

# Python's if statement has optional elif (else-if) and else clauses:

# In[3]:


x = 5
if x < 0:
    print("x is negative")
else:
    print("x is positive")


# In[4]:


x = 5
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")


# Try editing the value of x here, and note that other sections are found.

# In[5]:


choice = "high"

if choice == "high":
    print(1)
elif choice == "medium":
    print(2)
else:
    print(3)


# ## Comparison

# `True` and `False` are used to represent **boolean** (true or false) values.

# In[6]:


1 > 2


# Comparison on strings is alphabetical.

# In[7]:


"UCL" > "KCL"


# But case sensitive:

# In[8]:


"UCL" > "kcl"


# There's no automatic conversion of the **string** True to true:

# In[9]:


True == "True"


# In python two there were subtle implied order comparisons between types, but it was  bad style to rely on these.
# In python three, you cannot compare these.

# In[10]:


"1" < 2


# In[11]:


"5" < 2


# In[12]:


"1" > 2


# Any statement that evaluates to `True` or `False` can be used to control an `if` Statement.

# ### Automatic Falsehood

# Various other things automatically count as true or false, which can make life easier when coding:

# In[13]:


mytext = "Hello"


# In[14]:


if mytext:
    print("Mytext is not empty")


# In[15]:


mytext2 = ""


# In[16]:


if mytext2:
    print("Mytext2 is not empty")


# We can use logical not and logical and to combine true and false:

# In[17]:


x = 3.2
if not (x > 0 and type(x) == int):
    print(x, "is not a positive integer")


# `not` also understands magic conversion from false-like things to True or False.

# In[18]:


not not "Who's there!"


# In[19]:


bool("")


# In[20]:


bool("James")


# In[21]:


bool([])


# In[22]:


bool(["a"])


# In[23]:


bool({})


# In[24]:


bool({"name": "James"})


# In[25]:


bool(0)


# In[26]:


bool(1)


# But subtly, although these quantities evaluate True or False in an if statement, they're not themselves actually True or False under ==:

# In[27]:


[] == False


# In[28]:


bool([]) == False


# ## Indentation

# In Python, indentation is semantically significant.
# You can choose how much indentation to use, so long as you
# are consistent, but four spaces is
# conventional. Please do not use tabs.
# 
# In the notebook, and most good editors, when you press `<tab>`, you get four spaces.

# No indentation when it is expected, results in an error:

# In[29]:


x = 2


# In[30]:


if x > 0:
print(x)


# but:

# In[31]:


if x > 0:
    print(x)


# ##  Pass

# 
# A statement expecting identation must have some indented code.
# This can be annoying when commenting things out. (With `#`)
# 
# 
# 

# In[32]:


if x > 0:
    # print x
    
print("Hello")


# 
# 
# 
# So the `pass` statement is used to do nothing.
# 
# 
# 

# In[33]:


if x > 0:
    # print x
    pass

print("Hello")

