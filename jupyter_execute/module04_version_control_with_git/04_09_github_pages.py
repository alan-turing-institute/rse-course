#!/usr/bin/env python
# coding: utf-8

# # 4.9 Publishing from GitHub

# *Estimated time to complete this notebook: 5 minutes*

# # GitHub pages
# 
# ## Yaml Frontmatter
# 
# GitHub will publish repositories containing markdown as web pages, automatically. 
# 
# You'll need to add this content:
# 
# > ```
# >    ---
# >    ---
# > ```
# 
# A pair of lines with three dashes, to the top of each markdown file. This is how GitHub knows which markdown files to make into web pages.
# [Here's why](https://jekyllrb.com/docs/front-matter/) for the curious. 

# In[1]:


get_ipython().run_cell_magic('writefile', 'test.md', '---\ntitle: Github Pages Example\n---\nMountains and Lakes in the UK\n===================\n\nEngerland is not very mountainous.\nBut has some tall hills, and maybe a mountain or two depending on your definition.\n')


# In[2]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add github pages YAML frontmatter"\n')


# ## The gh-pages branch
# 
# GitHub creates github pages when you use a special named branch.
# By default this is `gh-pages` although you can change it to something else if you prefer.
# This is best used to create documentation for a program you write, but you can use it for anything.

# In[3]:


os.chdir(working_dir)


# In[18]:


get_ipython().run_cell_magic('bash', '', '\ngit checkout -b gh-pages\ngit push -uf origin gh-pages\n')


# The first time you do this, GitHub takes a few minutes to generate your pages. 
# 
# The website will appear at `http://username.github.io/repositoryname`, for example:
# 
# http://alan-turing-institute.github.io/github-example/

# ## Layout for GitHub pages
# 
# You can use GitHub pages to make HTML layouts, here's an [example of how to do it](http://github.com/UCL/ucl-github-pages-example), and [how it looks](http://ucl.github.com/ucl-github-pages-example). We won't go into the detail of this now, but after the class, you might want to try this.

# In[19]:


get_ipython().run_cell_magic('bash', '', '# Cleanup by removing the gh-pages branch \ngit checkout main\ngit push\ngit branch -d gh-pages\ngit push --delete origin gh-pages \ngit branch --remote\n')

