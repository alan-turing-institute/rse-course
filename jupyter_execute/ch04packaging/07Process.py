#!/usr/bin/env python
# coding: utf-8

# # Software Project Management

# ## Software Engineering Stages

# 
# * Requirements
# * Functional Design
# * Architectural Design
# * Implementation
# * Integration
# 

# ## Requirements Engineering

# 
# Requirements capture obviously means describing the things the software needs to be able to do.
# 
# A common approach is to write down lots of "user stories", describing how the software helps the user achieve something:
# 
# > As a clinician, when I finish an analysis, I want a report to be created on the test results, so that I can
# > send it to the patient.
# 
# As a *role*, when *condition or circumstance applies* I want *a goal or desire* so that *benefits occur*.
# 
# These are easy to map into the Gherkin behaviour driven design test language.
# 

# ## Functional and architectural design

# 
# Engineers try to separate the functional design, how the software appears to and is used by the user, from the
# architectural design, how the software achieves that functionality.
# 
# Changes to functional design require users to adapt, and are thus often more costly than changes to architectural design.
# 

# ## Waterfall

# 
# The _Waterfall_ design philosophy argues that the elements of design should occur in order: first requirements capture, then functional design,
# then architectural design. This approach is based on the idea that if a mistake is made in the design, then programming effort is wasted,
# so significant effort is spent in trying to ensure that requirements are well understood and that the design is correct before programming starts.
# 

# ## Why Waterfall?

# 
# Without a design approach, programmers resort to designing as we go, typing in code, trying what works, and making it up as we go along.
# When trying to collaborate to make software with others this can result in lots of wasted time, software that only the author understands,
# components built by colleagues that don't work together, or code that the programmer thinks is nice but that doesn't meet the user's requirements.
# 

# ## Problems with Waterfall

# 
# Waterfall results in a contractual approach to development, building an us-and-them relationship between users, business types, designers, and programmers.
# 
# > I built what the design said, so I did my job.
# 
# Waterfall results in a paperwork culture, where people spend a long time designing standard forms to document each stage of the design,
# with less time actually spent *making things*.
# 
# Waterfall results in excessive adherence to a plan, even when mistakes in the design are obvious to people doing the work.
# 

# ## Software is not made of bricks

# 
# The waterfall approach to software engineering comes from the engineering tradition applied to building physical objects,
# where Architects and Engineers design buildings, and builders build them according to the design.
# 
# Software is intrinsically different:
# 

# ## Software is not made of bricks

# 
# > Software is not the same 'stuff' as that from which physical systems are constructed.
# Software systems differ in material respects from physical systems.
# Much of this has been rehearsed by Fred Brooks in his classic
# ['No Silver Bullet'](http://ieeexplore.ieee.org/xpl/login.jsp?reload=true&tp=&arnumber=1663532&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D1663532) paper.
# First, complexity and scale are different in the case of software systems: relatively functionally simple software systems comprise more independent parts, placed
# in relation to each other, than do physical systems of equivalent functional value.
# Second, and clearly linked to this, we do not have well developed components and composition mechanisms from which to build
# software systems (though clearly we are working hard on providing these) nor do we have a straightforward mathematical account that
# permits us to reason about the effects of composition.
# 

# ## Software is not made of bricks

# 
# > Third, software systems operate in a domain determined principally by arbitrary rules about information and symbolic communication whilst the
# operation of physical systems is governed by the laws of physics.
# Finally, software is readily changeable and thus is changed, it is used in settings where our uncertainty leads us to anticipate the need to change.
# 
# -- Prof. [Anthony Finkelstein](http://blog.prof.so/), UCL Dean of Engineering, and Professor of Software Systems Engineering
# 

# ## The Agile Manifesto

# 
# In 2001, authors including Martin Folwer, Ward Cunningham and Kent Beck met in a Utah ski resort, and published the following manifesto.
# 
#  [Manifesto for Agile Software Development](http://agilemanifesto.org/)
# 
#  We are uncovering better ways of developing
#  software by doing it and helping others do it.
#  Through this work we have come to value:
# 
#  * _Individuals and interactions_ over processes and tools
#  * _Working software_ over comprehensive documentation
#  * _Customer collaboration_ over contract negotiation
#  *  _Responding to change_ over following a plan
# 
#  That is, while there is value in the items on
#  the right, we value the items on the left more.
# 

# ## Agile is not absence of process

# 
# > The Agile movement is not anti-methodology, in fact, many of us want to restore credibility to the word methodology.
# > We want to restore a balance. We embrace modeling, but not in order to file some diagram in a dusty corporate repository.
# > We embrace documentation, but not hundreds of pages of never-maintained and rarely-used tomes. We plan, but recognize the
# > limits of planning in a turbulent environment. Those who would brand proponents of XP or SCRUM or any of the other
# > Agile Methodologies as "hackers" are ignorant of both the methodologies and the original definition of the term hacker
# 
# -- Jim Highsmith.
# 

# ## Elements of an Agile Process

# 
# * Continuous delivery
# * Self-organising teams
# * Iterative development
# * Ongoing design
# 

# ## Ongoing Design

# 
# Agile development doesn't eschew design. Design documents should still be written, but treated as living documents,
# updated as more insight is gained into the task, as work is done, and as requirements change.
# 
# Use of a Wiki or version control repository to store design documents thus works much better than using Word documents!
# 
# Test-driven design and refactoring are essential techniques to ensure that lack of "Big Design Up Front" doesn't produce
# badly constructed spaghetti software which doesn't meet requirements. By continously scouring our code for smells, and
# stopping to refactor, we evolve towards a well-structured design with weakly interacting units. By starting with tests
# which describe how our code should behave, we create executable specifications, giving us confidence that the code does
# what it is supposed to.
# 

# ## Iterative Development

# 
# Agile development maintains a backlog of features to be completed and bugs to be fixed. In each iteration, we start with a meeting where
# we decide which backlog tasks will be attempted during the development cycle, estimating how long each will take,
# and selecting an achievable set of goals for the "sprint". At the end of each cycle, we review the goals completed and missed,
# and consider what went well, what went badly, and what could be improved.
# 
# We try not to add work to a cycle mid-sprint. New tasks that emerge are added to the backlog, and considered in the next planning meeting.
# This reduces stress and distraction.
# 

# ## Continuous Delivery

# 
# In agile development, we try to get as quickly as possible to code that can be *demonstrated* to clients. A regular demo of progress
# to clients at the end of each development iteration says so much more than sharing a design document. "Release early, release often"
# is a common slogan. Most bugs are found by people *using* code -- so exposing code to users as early as possible will help find bugs quickly.
# 

# ## Self-organising teams

# 
# Code is created by people. People work best when they feel ownership and pride in their work. Division of responsiblities into designers
# and programmers results in a ["Code Monkey"](http://open.spotify.com/track/1rIFZk9tTUtHP3vULR5wXe) role, where the craftspersonship and 
# sense of responsibility for code quality is lost. Agile approaches encourage programmers, designers, clients, and businesspeople to see
# themselves as one team, working together, with fluid roles. Programmers grab issues from the backlog according to interest, aptitude,
# and community spirit.
# 

# ## Agile in Research

# 
# Agile approaches, where we try to turn the instincts and practices which emerge naturally when smart programmers get together into
# well-formulated best practices, have emerged as antidotes to both the chaotic free-form typing in of code, and the rigid
# paperwork-driven approaches of Waterfall.
# 
# If these approaches have turned out to be better even in industrial contexts, where requirements for code can be well understood,
# they are even more appropriate in a research context, where we are working in poorly understood fields with even less well captured
# requirements.
# 

# ## Conclusion

# 
# * Don't ignore design
# * See if there's a known design pattern that will help
# * Do try to think about how your code will work before you start typing
# * Do use design tools like UML to think about your design without coding straight away
# * Do try to write down some user stories
# * Do maintain design documents.
# 
# BUT
# 
# * Do change your design as you work, updating the documents if you have them
# * Don't go dark -- never do more than a couple of weeks programming without showing what you've done to colleagues
# * Don't get isolated from the reasons for your code's existence, stay involved in the research, don't be a Code Monkey.
# * Do keep a list of all the things your code needs, estimate and prioritise tasks carefully.
# 
# 
