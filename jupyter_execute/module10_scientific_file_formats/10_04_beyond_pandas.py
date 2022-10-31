#!/usr/bin/env python
# coding: utf-8

# # 10.04 Larger datasets - beyond pandas and csv

# *Estimated time for this notebook: 20 minutes.*

# Much of the data that we deal with can be represented in tabular form, and can be handled in data structures such as the *pandas DataFrame*.
# We have already (briefly) seen how we can read and write csv files from pandas, and there are also methods for reading the results of SQL queries into _pandas DataFrames_.
# 
# However, if we have very large datasets (millions of rows), or cases where we need fast and intensive processing on these tables, _pandas_ may not be the best choice.

# ## Row-wise vs column-wise
# 
# Let's read a csv file containing international men's football results into a _pandas DataFrame_:

# In[1]:


import pandas as pd

df = pd.read_csv("match_results.csv")
df.head()


# The obvious way to think of this table is _"row-wise"_ i.e. each row is a single match, with various attributes (the columns).
# If we want to look at a certain match, we can pick it out using its index, and then look at it in detail:

# In[2]:


match = df.iloc[3]
print(f"{match.home_team} {match.home_score}:{match.away_score} {match.away_team}")


# Similarly, when more matches get played, we can simply append more rows to the end of the table.
# 
# However, for storing the data and for performing some types of operation on it, this is far from the most efficient approach.
# Note that the different columns here have different _types_ - we have dates, strings, integers, bools.
# If we look at the data in a *columnar* way, we can make use of this, and use some compression tricks.
# 
# Since some data types such as integers have fixed and known sizes, we can easily imagine that it's more efficient to pack these together, so the "home_score" column would be \[0,4,2,2,3,...\], without having to worry about other columns containing e.g. strings, of varying size.
# 
# However, we can do even better.
# 

# ### Run length compression
# 
# If we look at the last column, which is a boolean telling us whether the match was at a "neutral" venue (e.g. at a World Cup or European Championship).
# Most matches will be at non-neutral venues, but every two or four years there will be a cluster of "neutral" matches.

# In[3]:


# find the longest run of matches with the same value of 'neutral'
previous_val = df.neutral.values[0]
run = 0
longest_run = 0
for val in df.neutral.values[1:]:
    if val == previous_val:
        run += 1
        if run > longest_run:
            longest_run = run
    else:
        run = 0
print("longest run is:", longest_run)


# We could save a _lot_ of space, with no loss of information, if rather than saving every value, we instead save something that means "False 198 times, followed by True 64 times, followed by ...".

# ### Dictionary compression
# 
# Often the most space-consuming type in a dataset is a string.
# Each character will take one or two bytes (based on either UTF-8 or UTF-16 encoding), and we could either store each one as a variable-length string (so short strings will take less space than long strings), or we can decide on a maximum length for our string field, and pad the shorter strings.
# The former option takes less space, but is much less efficient when it comes to looking up values.
# 
# However, in many data tables, the same values are repeated many times.

# In[4]:


# how many rows in the table?
print(f"Table has {len(df)} rows")
# how many unique values in 'home_team' column?
print(f"Number of unique home_team values: {len(df.home_team.unique())}")
# how many times does 'Brazil' appear?
print(f"Brazil has been the home team {df.home_team.value_counts().Brazil} times")


# Again, we could save a lot of space if we make a lookup table, so we e.g. assign each team name to an integer, and rather than taking 20 bytes to store the longest team name, we would just use 2 bytes for every team.

# ### Delta compression
# 
# If we really want to compress our data as much as possible for writing to disk, and we don't care about making it human readable, we can use further tricks such as delta compression.
# For time series data, if something is relatively smoothly varying, we can save a lot of space by storing just the difference from one data point to the next, rather than each value.
# As an illustration of how this could work: rather than storing all the dates in the "date" table of our dataframe, we could just store the first date, and then for every subsequent row we just store the number of days since the previous row.
# 
# In the case where the column we're trying to compress contains integers or floats, we wouldn't save any space if we were to store the differences as integers or floats as well, but lots of clever schemes exist for packing small deltas within a few bytes.
# 
# For example, given the sequence:
# 
# `5, 3, 3, 4, 2, 1, 2, 0`
# 
# the deltas are:
# 
# `-2, 0, 1, -2, -1, 1, -2`
# 
# we can rescale this set of deltas by subtracting the minimum value (-2) from each element, such that the new minimum is 0, giving:
# 
# `0, 2, 3, 0, 1, 3, 0`
# 
# and finally we can encode this "block" along with a "header", as follows:
# ```
# header: 8 (block size), 5 (first value)
# block: -2 (minimum delta), 2 (bitwidth), 00101100011100b (0,2,3,0,1,3,0 packed on 2 bits)
# ```
# 
# For this trivial example, we are not actually saving that much space, but we could extend this to have many more blocks, and/or longer blocks, and/or have a block/miniblock structure (e.g. for when we need to change the bitwidth to deal with larger deltas), and the overall saving could be huge.
# 
# Of course, doing all these compression steps by hand is fiddly, and we would be very likely to make a mistake!  But luckily, libraries exist that do the hard work for us, and can seamlessly convert between pandas DataFrames and compressed columnar formats.

# ### Putting this into action: *parquet*
# 
# One data format that implements all these forms of compression (see [here](https://github.com/apache/parquet-format/blob/master/Encodings.md)) is "_parquet_": https://parquet.apache.org/
# Parquet files can be read in many languages, including Python, R, C++, and Java.
# 
# Let's write our dataframe as a _parquet_ file:

# In[5]:


df.to_parquet("match_results.parquet")


# How much space did we save compared to the csv?

# In[6]:


get_ipython().system('du -skh match_results.*')


# About a factor of 9!

# ## _Arrow_ and _feather_
# 
# You may have noticed that one of the packages that we installed in order to write the parquet file was `pyarrow`.
# Apache arrow is one of the under-the-hood technologies that parquet uses to process data.
# It is an "in-memory" columnar data format with some nice properties: random access is O(1) and each value cell is next to the previous and following one in memory, so it is efficient for iteration.

# We can convert our pandas dataframe directly into an arrow table:

# In[7]:


from timeit import timeit

import pyarrow as pa
import pyarrow.compute as pc


# In[8]:


table = pa.Table.from_pandas(df)
table


# Some things such as summing over columns are usually faster than in pandas:

# In[9]:


ptime = timeit("df.away_score.sum()", globals=globals(), number=10000)
atime = timeit('pc.sum(table.column("away_score"))', globals=globals(), number=10000)
print(f"Pandas took {ptime}, Arrow took {atime} to sum this column 10k times")


# So _arrow_ is about a factor 3-4 faster in this particular case.
# 
# Should we always use _arrow_ instead of _pandas_ then?   It depends.
# Arrow may be faster for some operations, so if you're speed-limited, it could be worth switching (or at least testing whether it's worth it).
# But on the other hand, _pandas_ has a healthy userbase, a well-known API, and established interfaces to other tools (e.g. _matplotlib_ for plotting).
# The good news is that it's very easy to convert between _pandas DataFrames_ and _arrow Tables_, and vice versa, so it shouldn't be a problem to try both and see what works best for your use-case.

# ### Writing to disk:  _feather_
# 
# We have already seen that we can write tabular data in a columnar format to disk as a _parquet_ file.
# Another option is _feather_.
# _Feather_ is a direct on-disk representation of the in-memory _arrow_ format - it doesn't have the same compression that _parquet_ applies by default.
# 
# Let's write our _arrow_ table to a _feather_ file:

# In[10]:


import pyarrow.feather as feather

feather.write_feather(table, "match_results.feather")


# Now we have the same table in csv, _parquet_, and _feather_ format.
# Compare the sizes again:

# In[11]:


get_ipython().system(' du -skh match_results.*')


# The _feather_ format didn't compress anywhere near as much as the _parquet_ file (but is still much smaller than csv).
# 
# So which is better, _feather_ or _parquet_?   Again, it depends what you are doing.
# If you will be storing or transferring large quantities of data, _parquet_ is probably preferable.
# However, there is a CPU cost to the compression/decompression, so if you are more worried about the speed of reading and writing files, you might want to use _feather_.
