#!/usr/bin/env python
# coding: utf-8

# # Argparse

# 
# This is the standard library for building programs with a command-line interface.
# 
# 
# 
# 
# 
# 

# In[1]:


get_ipython().run_cell_magic('writefile', 'greeter.py', '#!/usr/bin/env python\nfrom argparse import ArgumentParser\n\nif __name__ == "__main__":\n    parser = ArgumentParser(description="Generate appropriate greetings")\n    parser.add_argument("--title", "-t")\n    parser.add_argument("--polite", "-p", action="store_true")\n    parser.add_argument("personal")\n    parser.add_argument("family")\n    arguments = parser.parse_args()\n\n    greeting = "How do you do, " if arguments.polite else "Hey, "\n    if arguments.title:\n        greeting += arguments.title + " "\n    greeting += arguments.personal + " " + arguments.family + "."\n    print(greeting)')


# 
# 
# 
# 
# 

# In[2]:


get_ipython().run_cell_magic('bash', '', '#!/usr/bin/env bash\n#%%cmd (windows)\nchmod u+x greeter.py')


# In[3]:


get_ipython().run_cell_magic('bash', '', './greeter.py --help')


# In[4]:


get_ipython().run_cell_magic('bash', '', './greeter.py James Hetherington')


# In[5]:


get_ipython().run_cell_magic('bash', '', './greeter.py --polite James Hetherington')


# In[6]:


get_ipython().run_cell_magic('bash', '', './greeter.py James Hetherington --title Dr')

