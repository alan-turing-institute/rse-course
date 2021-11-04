#!/usr/bin/env python
# coding: utf-8

# # Advanced Python Programming

# ... or, how to avoid repeating yourself.

# ## Avoid Boiler-Plate

# Code can often be annoyingly full of "boiler-plate" code: characters you don't really want to have to type.
# 
# Not only is this tedious, it's also time-consuming and dangerous: unnecessary code is an unnecessary potential place for mistakes.
# 
# There are two important phrases in software design that we've spoken of before in this context:
# 
# > Once And Only Once
# >
# > Don't Repeat Yourself (DRY)
# 
# All concepts, ideas, or instructions should be in the program in just one place.
# Every line in the program should say something useful and important.
# 
# We refer to code that respects this principle as DRY code.
# 
# In this chapter, we'll look at some techniques that can enable us to refactor away repetitive code.
# 
# Since in many of these places, the techniques will involve working with
# functions as if they were variables, we'll learn some **functional**
# programming. We'll also learn more about the innards of how Python implements
# classes.
# 
# We'll also think about how to write programs that *generate* the more verbose, repetitive program we could otherwise write.
# We call this **metaprogramming**.
# 
