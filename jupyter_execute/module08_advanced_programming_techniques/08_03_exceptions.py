#!/usr/bin/env python
# coding: utf-8

# # 8.3 Exceptions

# *Estimated time for this notebook: 15 minutes*

# 
# When we learned about testing, we saw that Python complains when things go wrong by raising an "Exception" naming a type of error:
# 
# 
# 

# In[1]:


1 / 0


# Exceptions are objects, forming a [class hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy). We just raised an instance
# of the `ZeroDivisionError` class, making the program crash. If we want more
# information about where this class fits in the hierarchy, we can use [Python's
# `inspect` module](https://docs.python.org/3/library/inspect.html) to get a chain of classes, from `ZeroDivisionError` up to `object`:

# In[2]:


import inspect

inspect.getmro(ZeroDivisionError)


# 
# 
# So we can see that a zero division error is a particular kind of Arithmetic Error.
# 
# 
# 

# In[3]:


x = 1

for y in x:
    print(y)


# In[4]:


inspect.getmro(TypeError)


# ## Create your own Exception

# When we were looking at testing, we saw that it is important for code to crash with a meaningful exception type when something is wrong.
# We raise an Exception with `raise`. Often, we can look for an appropriate exception from the standard set to raise. 
# 
# However, we may want to define our own exceptions. Doing this is as simple as inheriting from Exception (or one of its subclasses):

# In[5]:


class MyCustomErrorType(ArithmeticError):
    pass


raise (MyCustomErrorType("Problem"))


# 
# 
# You can add custom data to your exception:
# 
# 
# 

# In[6]:


class MyCustomErrorType(Exception):
    def __init__(self, category=None):
        self.category = category

    def __str__(self):
        return f"Error, category {self.category}"


raise (MyCustomErrorType(404))


# 
# 
# The real power of exceptions comes, however, not in letting them crash the program, but in letting your program handle them. We say that an exception has been "thrown" and then "caught".
# 
# 
# 

# In[7]:


import yaml

try:
    config = yaml.safe_load(open("datasource.yaml"))
    user = config["userid"]
    password = config["password"]

except FileNotFoundError:
    print("No password file found, using anonymous user.")
    user = "anonymous"
    password = None


print(user)


# 
# 
# Note that we specify only the error we expect to happen and want to handle. Sometimes you see code that catches everything:
# 
# 
# 

# In[8]:


try:
    config = yaml.safe_lod(open("datasource.yaml"))
    user = config["userid"]
    password = config["password"]
except:
    user = "anonymous"
    password = None

print(user)


# This can be dangerous and can make it hard to find errors! There was a mistyped function name there ('`safe_lod`'), but we did not notice the error, as the generic except caught it. 
# Therefore, we should be specific and catch only the type of error we want.

# ## Managing multiple exceptions

# Let's create two credential files to read

# In[9]:


with open("datasource2.yaml", "w") as outfile:
    outfile.write("userid: eidle\n")
    outfile.write("password: secret\n")

with open("datasource3.yaml", "w") as outfile:
    outfile.write("user: eidle\n")
    outfile.write("password: secret\n")


# And create a function that reads credentials files and returns the username and password to use.

# In[10]:


def read_credentials(source):
    try:
        datasource = open(source)
        config = yaml.safe_load(datasource)
        user = config["userid"]
        password = config["password"]
        datasource.close()
    except FileNotFoundError:
        print("Password file missing")
        user = "anonymous"
        password = None
    except KeyError:
        print("Expected keys not found in file")
        user = "anonymous"
        password = None
    return user, password


# In[11]:


print(read_credentials("datasource2.yaml"))


# In[12]:


print(read_credentials("datasource.yaml"))


# In[13]:


print(read_credentials("datasource3.yaml"))


# This last code has a flaw: the file was successfully opened, the missing key was noticed, but not explicitly closed. It's normally OK, as Python will close the file as soon as it notices there are no longer any references to datasource in memory, after the function exits. But this is not good practice, you should keep a file handle for as short a time as possible.

# In[14]:


def read_credentials(source):
    try:
        datasource = open(source)
        config = yaml.safe_load(datasource)

        try:
            print("File loaded, trying to extract credentials")
            user = config["userid"]
            password = config["password"]
        except KeyError:
            print("Expected keys not found in file")
            user = "anonymous"
            password = None
        finally:
            # Runs irrespective of whether keys found
            print("Closing file")
            datasource.close()

    except FileNotFoundError:
        print("Password file missing")
        user = "anonymous"
        password = None

    return user, password


# The `finally` clause is executed whether or not an exception occurs.
# 
# The last optional clause of a `try` statement, an `else` clause is called only if an exception is NOT raised. It can be a better place than the `try` clause to put code other than that which you expect to raise the error, and which you do not want to be executed if the error is raised. It is executed in the same circumstances as code put in the end of the `try` block, the only difference is that errors raised during the `else` clause are not caught.

# In[15]:


def read_credentials(source):
    try:
        datasource = open(source)

    except FileNotFoundError:
        print("Password file missing")
        user = "anonymous"
        password = None

    else:
        # Runs only if opening the file was successful
        config = yaml.safe_load(datasource)
        try:
            print("File loaded, trying to extract credentials")
            user = config["userid"]
            password = config["password"]
        except KeyError:
            print("Expected keys not found in file")
            user = "anonymous"
            password = None
        finally:
            # Runs irrespective of whether keys found
            print("Closing file")
            datasource.close()

    return user, password


# Don't worry if `else` seems useless to you; most languages' implementations of try/except don't support such a clause. An alternative way of avoiding leaving the file open in the original implementation (and without using `else` or `finally`) is to use a context manager:

# In[16]:


def read_credentials(source):
    try:
        with open(source) as datasource:  # closes the file when done
            config = yaml.safe_load(datasource)
        user = config["userid"]
        password = config["password"]
    except FileNotFoundError:
        print("Password file missing")
        user = "anonymous"
        password = None
    except KeyError:
        print("Expected keys not found in file")
        user = "anonymous"
        password = None
    return user, password


# ## Catching Exceptions Elsewhere
# 
# Exceptions do not have to be caught close to the part of the program calling
# them. They can be caught anywhere "above" the calling point in
# the call stack: control can jump arbitrarily far in the program: up to the `except` clause of the "highest" containing try statement.
# 
# 
# 

# In[17]:


def f4(x):
    if x == 0:
        return
    if x == 1:
        raise ArithmeticError()
    if x == 2:
        raise SyntaxError()
    if x == 3:
        raise TypeError()


# In[18]:


def f3(x):
    try:
        print("F3Before")
        f4(x)
        print("F3After")
    except ArithmeticError:
        print("F3Except (💣)")


# In[19]:


def f2(x):
    try:
        print("F2Before")
        f3(x)
        print("F2After")
    except SyntaxError:
        print("F2Except (💣)")


# In[20]:


def f1(x):
    try:
        print("F1Before")
        f2(x)
        print("F1After")
    except TypeError:
        print("F1Except (💣)")


# In[21]:


f1(0)


# In[22]:


f1(1)


# In[23]:


f1(2)


# In[24]:


f1(3)


# ## Design with Exceptions

# 
# Now we know how exceptions work, we need to think about the design implications... How best to use them.
# 
# Traditional software design theory will tell you that they should only be used
# to describe and recover from **exceptional** conditions: things going wrong.
# Normal program flow shouldn't use them.
# 
# Python's designers take a different view: use of exceptions in normal flow is
# considered OK. For example, all iterators raise a `StopIteration` exception to
# indicate the iteration is complete.
# 
# A commonly recommended Python design pattern is to use exceptions to determine
# whether an object implements a protocol (concept/interface), rather than testing
# on type.
# 
# For example, we might want a function which can be supplied *either* a data
# series *or* a path to a location on disk where data can be found. We can
# examine the type of the supplied content:

# In[25]:


import yaml


def analysis(source):
    if type(source) == dict:
        name = source["modelname"]
    else:
        content = open(source)
        source = yaml.safe_load(content)
        name = source["modelname"]
    print(name)


# In[26]:


analysis({"modelname": "Super"})


# In[27]:


with open("example.yaml", "w") as outfile:
    outfile.write("modelname: brilliant\n")


# In[28]:


analysis("example.yaml")


# 
# 
# 
# However, we can also use the try-it-and-handle-exceptions approach to this. 
# 
# 
# 

# In[29]:


def analysis(source):
    try:
        name = source["modelname"]
    except TypeError:
        content = open(source)
        source = yaml.safe_load(content)
        name = source["modelname"]
    print(name)


analysis("example.yaml")


# This approach is more extensible, and **behaves properly if we give it some
# other data-source which responds like a dictionary or string.**

# In[30]:


def analysis(source):
    try:
        name = source["modelname"]
    except TypeError:
        # Source was not a dictionary-like object
        # Maybe it is a file path
        try:
            content = open(source)
            source = yaml.safe_load(content)
            name = source["modelname"]
        except IOError:
            # Maybe it was already raw YAML content
            source = yaml.safe_load(source)
            name = source["modelname"]
    print(name)


analysis("modelname: Amazing")


# ## Re-Raising Exceptions
# 
# Sometimes we want to catch an error, partially handle it, perhaps add some
# extra data to the exception, and then re-raise to be caught again further up
# the call stack. 
# 
# The keyword "`raise`" with no argument in an `except:` clause will cause the
# caught error to be re-thrown. Doing this is the only circumstance where it is
# safe to do `except:` without catching a specific type of error.

# In[31]:


try:
    # Something
    pass
except:
    # Do this code here if anything goes wrong
    raise


# If you want to be more explicit about where the error came from, you can use the `raise from` syntax, which will create a chain of exceptions:

# In[32]:


def lower_function():
    raise ValueError("Error in lower function!")


def higher_function():
    try:
        lower_function()
    except ValueError as e:
        raise RuntimeError("Error in higher function!") from e


higher_function()


# 
# 
# It can be useful to catch and re-throw an error as you go up the chain, doing any clean-up needed for each layer of a program.
# 
# The error will finally be caught and not re-thrown only at a higher program
# layer that knows how to recover. This is known as the "throw low catch high"
# principle.
# 
# 
# 
