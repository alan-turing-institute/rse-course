#!/usr/bin/env python
# coding: utf-8

# # Fork and Pull
# 
# ## Different ways of collaborating 
# 
# We have just seen how we can work with others on GitHub: we add them as collaborators on our repositories and give them permissions to push changes. 
# 
# Let's talk now about some other type of collaboration. 
# 
# Imagine you are a user of an Open Source project like Numpy and find a bug in one of their methods. 
# 
# You can inspect and clone Numpy's code in GitHub https://github.com/numpy/numpy, play around a bit and find how to fix the bug. 
# 
# Numpy has done so much for you asking nothing in return, that you really want to contribute back by fixing the bug for them. 
# 
# You make all of the changes but you can't push it back to Numpy's repository because you don't have permissions.
# 
# The right way to do this is __forking Numpy's repository__. 

# ## Forking a repository on GitHub
# 
# By forking a repository, all you do is make a copy of it in your GitHub account, where you will have write permissions as well.
# 
# If you fork Numpy's repository, you will find a new repository in your GitHub account that is an exact copy of Numpy. You can then clone it to your computer, work locally on fixing the bug and push the changes to your _fork_ of Numpy. 
# 
# Once you are happy with with the changes, GitHub also offers you a way to notify Numpy's developers of this changes so that they can include them in the official Numpy repository via starting a __Pull Request__.

# ## Pull Request
# 
# You can create a Pull Request and select those changes that you think can be useful for fixing Numpy's bug. 
# 
# Numpy's developers will review your code and make comments and suggestions on your fix. Then, you can commit more improvements in the pull request for them to review and so on. 
# 
# Once Numpy's developers are happy with your changes, they'll accept your Pull Request and merge the changes into their original repository, for everyone to use.

# ## Practical example - Team up!
# 
# We will be working in the same repository with one of you being the leader and the other being the collaborator. 
# 
# Collaborators need to go to the leader's GitHub profile and find the repository we created for that lesson. Mine is in https://github.com/jamespjh/github-example

# ### 1. Fork repository
# 
# You will see on the top right of the page a `Fork` button with an accompanying number indicating how many GitHub users have forked that repository. 
# 
# Collaborators need to navigate to the leader's repository and click the `Fork` button. 
# 
# Collaborators: note how GitHub has redirected you to your own GitHub page and you are now looking at an exact copy of the team leader's repository.

# ### 2. Clone your forked repo
# 
# Collaborators: go to your terminal and clone the newly created fork.
# 
# ```
# git clone git@github.com:jamespjh/github-example.git
# ```

# ### 3. Create a feature branch
# 
# It's a good practice to create a new branch that'll contain the changes we want. We'll learn more about branches later on. For now, just think of this as a separate area where our changes will be kept not to interfere with other people's work.
# 
# ```
# git checkout -b southwest
# ```

# ### 4. Make, commit and push changes to new branch
# 
# For example, let's create a new file called `SouthWest.md` and edit it to add this text:
# 
# ```
# * Exmoor
# * Dartmoor
# * Bodmin Moor
# ```
# 
# Save it, and push this changes to your fork's new branch:
# 
# ```
# git add SouthWest.md
# git commit -m "The South West is also hilly."
# git push origin southwest
# ```

# ### 5. Create Pull Request
# 
# Go back to the collaborator's GitHub site and reload the fork. GitHub has noticed there is a new branch and is presenting us with a green button to `Compare & pull request`. Fantastic! Click that button.
# 
# Fill in the form with additional information about your change, as you consider necesary to make the team leader understand what this is all about.
# 
# Take some time to inspect the commits and the changes you are submitting for review. When you are ready, click on the `Create Pull Request` button. 
# 
# Now, the leader needs to go to their GitHub site. They have been notified there is a pull request in their repo awaiting revision. 

# ### 6. Feedback from team leader
# 
# Leaders can see the list of pull requests in the vertical menu of the repo, on the right hand side of the screen. Select the pull request the collaborator has done, and inspect the changes. 
# 
# There are three tabs: in one you can start a conversation with the collaborator about their changes, and in the others you can have a look at the commits and changes made. 
# 
# Go to the tab labeled as "Files Changed". When you hover over the changes, a small `+` button appears. Select one line you want to make a comment on. For example, the line that contains "Exmoor". 
# 
# GitHub allows you to add a comment about that specific part of the change. Your collaborator has forgotten to add a title at the beginning of the file right before "Exmoor", so tell them so in the form presented after clicking the `+` button.

# ### 7. Fixes by collaborator
# 
# Collaborators will be notified of this comment by email and also in their profiles page. Click the link accompanying  this notification to read the comment from the team leader. 
# 
# Go back to your local repository, make the changes suggested and push them to the new branch.
# 
# Add this at the beginning of your file:
# 
# ```
# Hills in the South West:
# =======================
# 
# ```
# 
# Then push the change to your fork:
# 
# ```
# git add .
# git commit -m "Titles added as requested."
# git push origin southwest
# ```
# 
# This change will automatically be added to the pull request you started.

# ### 8. Leader accepts pull request 
# 
# The team leader will be notified of the new changes that can be reviewed in the same fashion as earlier. 
# 
# Let's assume the team leader is now happy with the changes.
# 
# Leaders can see in the "Conversation" tab of the pull request a green button labelled ```Merge pull request```. Click it and confirm the decision. 
# 
# The collaborator's pull request has been accepted and appears now in the original repository owned by the team leader. 
# 
# Fork and Pull Request done!

# ## Some Considerations
# 
# * Fork and Pull Request are things happening only on the repository's server side (GitHub in our case). Consequently, you can't do things like `git fork` or `git pull-request` from the local copy of a repository.
# * You don't always need to fork repositories with the intention of contributing. You can fork a library you use, install it manually on your computer, and add more functionality or customise the existing one, so that it is more useful for you and your team. 
# * Numpy's example is only illustrative. Normally, Open Source projects have in their documentation (sometimes in the form of a wiki) a set of instructions you need to follow if you want to contribute to their software.
# * Pull Requests can also be done for merging branches in a non-forked repository. It's typically used in teams to merge code from a branch into the master branch and ask team colleagues for code reviews before merging.
# * It's a good practice before starting a fork and a pull request to have a look at existing forks and pull requests. On GitHub, you can find the list of pull requests on the horizontal menu on the top of the page. Try to also find the network graph displaying all existing forks of a repo, like this example in the NumpyDoc repo: https://github.com/numpy/numpydoc/network
