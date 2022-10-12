#!/usr/bin/env python
# coding: utf-8

# # 3.0 Field and Record Data

# *Estimated time to complete this notebook: 20 minutes*

# ## 3.01 Separated Value Files

# Let's carry on with our sunspots example from 2.5.3: We had downloaded some semicolon separated data and decided it was better to use a library than to write our own parser.

# In[1]:


import requests

spots = requests.get("http://www.sidc.be/silso/INFO/snmtotcsv.php")
spots.text.split("\n")[0]


# We want to work programmatically with *Separated Value* files.

# These are files which have:
# 
# * Each *record* on a line
# * Each record has multiple *fields*
# * Fields are separated by some *separator*

# Typical separators are the `space`, `tab`, `comma`, and `semicolon` separated values files, e.g.:
# 
# * Space separated value (e.g. `field1 "field two" field3` )
# * Comma separated value (e.g. `field1, another field, "wow, another field"`)

# Comma-separated-value is abbreviated CSV, and tab separated value TSV.

# CSV is also used to refer to all the different sub-kinds of separated value files, i.e. some people use CSV to refer to tab, space and semicolon separated files.

# CSV is not a particularly superb data format, because it forces your data model to be a list of lists. Richer file formats describe "serialisations" for dictionaries and for deeper-than-two nested list structures as well.

# Nevertheless, because you can always export *spreadsheets* as CSV files, (each cell is a field, each row is a record)
# CSV files are very popular. 

# ## 3.02 CSV variants

# Some CSV formats define a comment character, so that rows beginning with, e.g., a #, are not treated as data, but give
# a human comment.

# Some CSV formats define a three-deep list structure, where a double-newline separates records into blocks.

# Some CSV formats assume that the first line defines the names of the fields, e.g.:
# 
# ```
# name, age
# James, 39
# Will, 2
# ```

# ## 3.03 Python CSV readers

# The Python standard library has a `csv` module. However, it's less powerful than the CSV capabilities in `numpy` or [pandas](https://pandas.pydata.org/) which is built on top of numpy.

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('http://www.sidc.be/silso/INFO/snmtotcsv.php', sep=";", header=None)
df.head()


# Pandas `read_csv` is a powerful CSV reader tool. A path to the data is given, this can be something on a local machine, or in this case the path is a url. 
# 
# 
# I used the `sep` optional argument to specify the delimeter. The optional argument `header` specifies if the data contains headers, and if so; the row numbers to use as column names.
# 
# 
# The data is loaded into a DataFrame. The `head` method shows us the first 5 entries in the dataframe. The `tail` method shows us the last 5 entries.

# In[4]:


df.tail()


# In[5]:


df[3][0]


# We can now plot the "Sunspot cycle":

# In[6]:


df.plot(x=2, y=3)


# The plot command accepted an series of 'X' values and an series of 'Y' values, identified by their column number in this case, as the dataframe does not have (useful) column headers yet.

# ## 3.04 Naming Columns

# I happen to know that the columns here are defined as follows:

# From http://www.sidc.be/silso/infosnmtot:
# 
# > CSV
# 
# > Filename: SN_m_tot_V2.0.csv
# > Format: Comma Separated values (adapted for import in spreadsheets)
# The separator is the semicolon ';'.
# 
# > Contents:
# * Column 1-2: Gregorian calendar date
# - Year
# - Month
# * Column 3: Date in fraction of year.
# * Column 4: Monthly mean total sunspot number.
# * Column 5: Monthly mean standard deviation of the input sunspot numbers.
# * Column 6: Number of observations used to compute the monthly mean total sunspot number.
# * Column 7: Definitive/provisional marker. '1' indicates that the value is definitive. '0' indicates that the value is still provisional.

# I can actually specify this to the formatter:

# In[7]:


df_w_names = pd.read_csv('http://www.sidc.be/silso/INFO/snmtotcsv.php',
                         sep=";",
                         header=None,
                         names=["year", "month", "date", "mean", "deviation", "observations", "definitive"])
df_w_names.head()


# In[8]:


df_w_names.plot(x='date', y='mean')


# Note: The plot method used for the DataFrame is just a wrapper around  matplotlib's plt.plot():

# ## 3.05 Typed Fields

# It's also often useful to check, and if necessary specify, the datatype of each field.

# In[9]:


df_w_names.dtypes # Check the data types of all columns in the DataFrame


# In this case the data types seem sensible, however if we wanted to convert the year into a floating point number instead, we could via:

# In[10]:


df_w_names['year']=df_w_names['year'].astype('float64')
df_w_names.dtypes


# In[11]:


df_w_names.head()


# ## 3.06 Filtering data

# Sometimes it is necessary to filter data, for example to only see the sunspots for the year 2018 you would use:

# In[12]:


df_twenty_eighteen = df_w_names[(df_w_names['year'] == 2018)]
df_twenty_eighteen.head(20)


# Even though we used 
# ```bash
# df_twenty_eighteen.head(20)
# ```
# to show us the first 20 results from the dataframe, only 12 are shown as there are only 12 months in a year
# 
# If we wanted all data from 1997 to 1999 we could via:

# In[13]:


df_nineties = df_w_names[(df_w_names['year'] >= 1997) & (df_w_names['year'] < 2000)]


# In[14]:


df_nineties.head()


# In[15]:


df_nineties.tail()

