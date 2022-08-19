# Installation Instructions

## Introduction

This document contains instructions for installation of the packages we'll be using during the course.
You will be following the training on your own machines, so please complete these instructions.
The instructions include Windows, Mac and Linux specific sections.

<details>
  <summary>Note for Mac users</summary><p></p>
  
  We do not recommend following this training on older versions of `macOS` without an app store: upgrade to at least `macOS 10.9 (Mavericks)`.
  
</details><p></p>

**If you encounter any problem during insallation** and you manage to solve them (feel free to ask us for help), please remember to add an issue to the [course repo](https://github.com/alan-turing-institute/rsd-engineeringcourse), explaining the problem and solution.
By doing this you will be helping to improve the instructions for future users! 🎉

## What we're installing

- the `Python` programming language (version `3.8` or greater) and `Conda`
- a selection of `Python` software packages that will be used during the course (via a Conda environment)
- `git` for the version control module
- a suitable text editor

Please ensure that you have a computer (ideally a laptop) with all of these installed. Even if you think you have all of these things already, it's worth reading through the prerequisite pages to make sure.


## Troubleshooting

### Jupyter issues on Windows:

To use the Jupyter Lab (or Jupyter notebook) on a `Windows` computer with Sophos anti-virus installed it may be necessary to open additional ports allowing communication between the notebook and its server.
The [solution](http://stackoverflow.com/questions/13036197/ipython-notebook-getting-output) is:

- open your `Sophos Endpoint Security and Control Panel` from your tray or start menu
- Select `Configure > Anti-virus > Authorization` from the menu at the top
- Select the websites tab
- click the `Add` button and add `127.0.0.1` and `localhost` to the `Authorized websites` list
- restart computer (or just restart the Jupyter)