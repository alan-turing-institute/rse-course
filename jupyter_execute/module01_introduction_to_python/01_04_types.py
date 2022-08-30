#!/usr/bin/env python
# coding: utf-8

# # 1.4 Types
# *Estimated time to complete this notebook: 20 minutes*

# We have seen that Python objects have a 'type':

# In[1]:


type(5)


# ## 1.4.1 Floats and integers

# Python has two core numeric types, `int` for integer, and `float` for real number.

# In[2]:


one = 1
ten = 10
one_float = 1.0
ten_float = 10.0


# Zero after a point is optional. But the **Dot** makes it a float.

# In[3]:


tenth = one_float / ten_float


# In[4]:


tenth


# In[5]:


type(one)


# In[6]:


type(one_float)


# The meaning of an operator varies depending on the type it is applied to!

# In[7]:


print(one // ten)


# In[8]:


one_float / ten_float


# In[9]:


print(type(one / ten))


# In[10]:


type(tenth)


# The divided by operator when applied to floats, and integers means divide by for real numbers.
# 
# The `//` operator means divide and then round down

# In[11]:


10 // 3


# In[12]:


10.0 / 3


# In[13]:


10 / 3.0


# There is a function for every type name, which is used to convert the input to an output of the desired type.

# In[14]:


x = float(5)
type(x)


# In[15]:


10 / float(3)


# I lied when I said that the `float` type was a real number. It's actually a computer representation of a real number
# called a "floating point number". Representing $\sqrt 2$ or $\frac{1}{3}$ perfectly would be impossible in a computer, so we use a finite amount of memory to do it.

# In[16]:


N = 10000.0
sum([1 / N] * int(N))


# *Supplementary material*:
# 
# * https://docs.python.org/2/tutorial/floatingpoint.html
# * http://floating-point-gui.de/formats/fp/
# * Advanced: http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html

# ## 1.4.2 Strings

# Python has a built in `string` type, supporting many
# useful methods.

# In[17]:


given = "James"
family = "Hetherington"
full = given + " " + family


# So `+` for strings means "join them together" - *concatenate*.

# In[18]:


print(full.upper())


# As for `float` and `int`, the name of a type can be used as a function to convert between types:

# In[19]:


ten, one


# In[20]:


print(ten + one)


# In[21]:


print(float(str(ten) + str(one)))


# We can remove extraneous material from the start and end of a string:

# In[22]:


"    Hello  ".strip()


# Note that you can write strings in Python using either single (`' ... '`) or double (`" ... "`) quote marks. The two ways are equivalent. However, if your string includes a single quote (e.g. an apostrophe), you should use double quotes to surround it:

# In[23]:


"James's Class"


# And vice versa: if your string has a double quote inside it, you should wrap the whole string in single quotes.

# In[24]:


'"Wow!", said Bob.'


# ## 1.4.3 Lists

# Python's basic **container** type is the `list`.

# We can define our own list with square brackets:

# In[25]:


[1, 3, 7]


# In[26]:


type([1, 3, 7])


# Lists *do not* have to contain just one type:

# In[27]:


various_things = [1, 2, "banana", 3.4, [1, 2]]


# We access an **element** of a list with an `int` in square brackets:

# In[28]:


various_things[2]


# In[29]:


index = 0
various_things[index]


# Note that list indices start from zero.

# We can use a string to join together a list of strings:

# In[30]:


name = ["James", "Philip", "John", "Hetherington"]
print("==".join(name))


# And we can split up a string into a list:

# In[31]:


"Ernst Stavro Blofeld".split(" ")


# In[32]:


"Ernst Stavro Blofeld".split("o")


# And combine these:

# In[33]:


"->".join("John Ronald Reuel Tolkien".split(" "))


# A matrix can be represented by **nesting** lists -- putting lists inside other lists.

# In[34]:


identity = [[1, 0], [0, 1]]


# In[35]:


identity[0][0]


# ... but later we will learn about a better way of representing matrices.

# ## 1.4.4 Ranges

# Another useful type is range, which gives you a sequence of consecutive numbers. In contrast to a list, ranges generate the numbers as you need them, rather than all at once.
# 
# If you try to print a range, you'll see something that looks a little strange: 

# In[36]:


range(5)


# We don't see the contents, because *they haven't been generatead yet*. Instead, Python gives us a description of the object - in this case, its type (range) and its lower and upper limits.

# We can quickly make a list with numbers counted up by converting this range:

# In[37]:


count_to_five = range(5)
print(list(count_to_five))


# Ranges in Python can be customised in other ways, such as by specifying the lower limit or the step (that is, the difference between successive elements). You can find more information about them in the [official Python documentation](https://docs.python.org/3/library/stdtypes.html#ranges).

# ## 1.4.5 Sequences

# Many other things can be treated like `lists`. Python calls things that can be treated like lists `sequences`.

# A string is one such *sequence type*.

# Sequences support various useful operations, including:
# - Accessing a single element at a particular index: `sequence[index]`
# - Accessing multiple elements (a *slice*): `sequence[start:end_plus_one]`
# - Getting the length of a sequence: `len(sequence)`
# - Checking whether the sequence contains an element: `element in sequence`
# 
# The following examples illustrate these operations with lists, strings and ranges.

# In[38]:


print(count_to_five[1])


# In[39]:


print("James"[2])


# In[40]:


count_to_five = range(5)


# In[41]:


count_to_five[1:3]


# In[42]:


"Hello World"[4:8]


# In[43]:


len(various_things)


# In[44]:


len("Python")


# In[45]:


name


# In[46]:


"John" in name


# In[47]:


3 in count_to_five


# ## 1.4.6 Unpacking

# Multiple values can be **unpacked** when assigning from sequences, like dealing out decks of cards.

# In[48]:


mylist = ["Hello", "World"]
a, b = mylist
print(b)


# In[49]:


range(4)


# In[50]:


zero, one, two, three = range(4)


# In[51]:


two


# If there is too much or too little data, an error results:

# In[52]:


zero, one, two, three = range(7)


# In[53]:


zero, one, two, three = range(2)


# Python provides some handy syntax to split a sequence into its first element ("head") and the remaining ones (its "tail"):

# In[54]:


head, *tail = range(4)
print("head is", head)
print("tail is", tail)


# Note the syntax with the \*. The same pattern can be used, for example, to extract the middle segment of a sequence whose length we might not know:

# In[55]:


one, *two, three = range(10)


# In[56]:


print("one is", one)
print("two is", two)
print("three is", three)

