#!/usr/bin/env python
# coding: utf-8

# # Managing software issues

# ## Issues
# 
# Code has *bugs*. It also has *features*, things it should do.
# 
# A good project has an organised way of managing these. Generally you should use an issue tracker.

# ## Some Issue Trackers
# 
# There are lots of good issue trackers.
# 
# The most commonly used open source ones are [Trac](http://trac.edgewall.org/) and [Redmine](http://www.redmine.org/).
# 
# Cloud based issue trackers include [Lighthouse](http://lighthouseapp.com/) and [GitHub](https://github.com/blog/831-issues-2-0-the-next-generation).
# 
# Commercial solutions include [Jira](https://www.atlassian.com/software/jira).
# 
# In this course, we'll be using the GitHub issue tracker.

# ## Anatomy of an issue
# 
# * Reporter
# * Description
# * Owner
# * Type [Bug, Feature]
# * Component
# * Status
# * Severity

# ## Reporting a Bug
# 
# The description should make the bug reproducible:
# 
# * Version
# * Steps
# 
# If possible, submit a minimal reproducing code fragment.

# ## Owning an issue
# 
# * Whoever the issue is assigned to works next.
# * If an issue needs someone else's work, assign it to them.

# ## Status 
# 
# * Submitted
# * Accepted
# * Underway
# * Blocked

# ## Resolutions
# 
# * Resolved
# * Will Not Fix
# * Not reproducible
# * Not a bug (working as intended)

# ## Bug triage
# 
# Some organisations use a severity matrix based on:
# 
# * Severity [Wrong answer, crash, unusable, workaround, cosmetic...]
# * Frequency [All users, most users, some users...]

# ## The backlog
# 
# The list of all the bugs that need to be fixed or
# features that have been requested is called the "backlog".

# ## Development cycles
# 
# Development goes in *cycles*.
# 
# Cycles range in length from a week to three months.
# 
# In a given cycle:
# 
# * Decide which features should be implemented
# * Decide which bugs should be fixed
# * Move these issues from the Backlog into the current cycle. (Aka Sprint)

# ## GitHub issues
# 
# GitHub doesn't have separate fields for status, component, severity etc.
# Instead, it just has labels, which you can create and delete.
# 
# See for example [Jupyter](https://github.com/jupyter/notebook/issues?labels=bug&page=1&state=open)
