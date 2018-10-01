---
title: Windows
---

Windows
=======

Python
------

We recommend installing a complete scientific python distribution. One of these is
Anaconda.

Please download and install [Anaconda](https://www.continuum.io/downloads).
(Python 3.5 version.)

Sophos
------

To use the IPython notebook on a Windows computer with Sophos anti-virus installed it may be necessary to
open additional ports allowing communication between the notebook and its server.
The [solution](http://stackoverflow.com/questions/13036197/ipython-notebook-getting-output) is:

* open your Sophos Endpoint Security and Control Panel from your tray or start menu
* Select "configure" > "Anti-virus" > "Authorization" from the menu at the top
* Select the websites tab
* click the "Add" button and add 127.0.0.1 and localhost to the "Authorized websites" list
* restart computer (most likely not needed, just restart the IPython notebook)
* output works now :)

#Git

Install the [GitHub for Windows client](http://windows.github.com/). This comes with both a GUI
client as well as the [msysgit](http://msysgit.github.io/) terminal client which we will use in
Software Carpentry. You should register with [Github](github.com) for an account and sign into the
GUI client with this account. This will automatically set-up
[SSH based authentication](https://help.github.com/articles/generating-ssh-keys#platform-windows)
for the terminal client. The terminal client comes in 3 different flavours based on Windows CMD
(DOS like), Windows Powershell, and BASH. We will use the BASH client as this most closely resembles the
Linux and OS X terminal used by other students. In order to configure this open the Github
client. Sign in with your credentials and:

*  Select tools
*  Options
*  Default Shell
*  Git Bash
*  And Press Update to save.

Verify that this is working by opening the Git shell. The Shell window should have a title that
starts with MINGW32.

Editor
------

Unless you already use a specific editor which you are comfortable with we recommend using
[Notepad++](http://notepad-plus-plus.org/). Follow the [download link.](http://notepad-plus-pl
us.org/)

Using Notepad++ to edit text files including code should be straight forward but in addition you
should configure git to use notepad++ when writing commit messages (We will learn about these in the
version control session). The following sections goes through this:

Finding out where things got installed
--------------------------------------

Now, we need to find out where Notepad++ have been installed, this will be either in `C:\Program
Files (x86)` or in `C:\ProgramFiles`. The former is the norm on more modern versions of windows. If
you have the older version, replace `Program Files (x86)` with `Program Files` in the
instructions below. If you are unsure about this open Windows explore and navigate to the C
drive. If the C drive contains both a `Program Files (x86)` and `Program Files` folder Notepad++ is
most likely to be installed in `Program Files (x86)`. Verify this by opening the folder and look for
a `Notepad++` subfolder. On a non English widows installation the directories may have different names.
You should however still use the English names above. Just verify if the directory ends with (x86) or not.

Telling the shell where to find Notepad++
-----------------------------------------

We need to tell the new shell installed with git where Notepad++ is.

In order to do this we will edit a Widows environmental Variable called ```Path```
This is basically a list of directories separated by ';' where the shell will look for
programs.

To do this:

*  Open the control panel
*  Select system
*  Advanced system settings
*  Environment Variables
*  Select Path and press edit.

This will open a Dialogue box with a long string ```Variable value:```
At the end of the string you should add ```;C:\Program Files (x86)\Notepad++```
Where you substitute ```Program Files (x86)``` with the directory determined above.


Testing your install
--------------------

Check this works by opening the Github shell. Once you have a terminal open, type

``` bash
which notepad++
```

which should produce readout similar to `/c/Program Files (x86)/Notepad++/notepad++.exe`

Also verify the typing:
```bash
notepad++
```
opens the editor and the close it again.

``` bash
which git
```

which should produce `/bin/git`. The ``which``
command is used to figure out where a given program is located on disk.

Telling Git about Notepad
-------------------------

Now we need to update the default editor used by Git.

``` bash
git config --global core.editor "'notepad++.exe' -multiInst  -nosession -noPlugin"
```

Note that it is not obvious how to copy and paste text in a Windows terminal including Git Bash.
Copy and paste can be found by right clicking on the top bar of the window and selecting the
commands from the drop down menu (in a sub menu).

Testing python
--------------

Confirm that the Python installation has worked by typing:

``` bash
python -V
```

Which should result in details of your installed python version.

This should print the installed version of the python and git confirming that both are installed at
working correctly.

You should now have a working version of git, python, and notepad++, all accessible from your shell.
