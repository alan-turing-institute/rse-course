# Windows

## Python

We recommend installing a complete scientific python distribution.
One of these is [Anaconda](https://www.anaconda.com/distribution/).

Please download and install [Anaconda](https://www.anaconda.com/download/) (Python 3.8 version).

## Sophos

To use the `IPython` notebook on a `Windows` computer with Sophos anti-virus installed it may be necessary to open additional ports allowing communication between the notebook and its server.
The [solution](http://stackoverflow.com/questions/13036197/ipython-notebook-getting-output) is:

- open your `Sophos Endpoint Security and Control Panel` from your tray or start menu
- Select `Configure > Anti-virus > Authorization` from the menu at the top
- Select the websites tab
- click the `Add` button and add `127.0.0.1` and `localhost` to the `Authorized websites` list
- restart computer (or just restart the `IPython` notebook)

## Git

Install the [GitHub for Windows client](http://windows.github.com/).
This comes with both a GUI client as well as the [Git Bash](https://gitforwindows.org/) terminal client which we will use during the course.
You should register with [Github](https://github.com) for an account and sign into the GUI client with this account.
This will automatically set-up [SSH based authentication](https://help.github.com/articles/generating-ssh-keys#platform-windows) for the terminal client.
The terminal client comes in 3 different flavours based on `Windows CMD` (DOS like), `Windows Powershell`, and `BASH`.
We will use the `BASH` client as this most closely resembles the `Linux` and `OS X` terminal used by other students.
In order to configure this open the Github client.
Sign in with your credentials and:

- Select tools
- Options
- Default Shell
- Git Bash
- And Press Update to save.

Verify that this is working by opening Git Bash.
The Shell window should have a title that starts with MINGW32.

## Editor

Unless you already use a specific editor which you are comfortable with we recommend using one of the following:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Atom](https://atom.io)
- [Notepad++](https://notepad-plus-plus.org/downloads/)
- [Sublime Text](https://www.sublimetext.com)
- [Vim](https://www.vim.org/)
- [Emacs](https://www.gnu.org/software/emacs/)

Using any of these to edit text files including code should be straight forward.
`Visual Studio Code` has integrations with [Git Bash](https://code.visualstudio.com/docs/editor/integrated-terminal) and the [Python prompt](https://code.visualstudio.com/docs/python/python-tutorial) that you may want to configure.

## Testing your install

Check this works by opening the Github shell.
Once you have a terminal open, type

```bash
which code
```

which should produce readout similar to `/c/Program Files (x86)/Code/Code.exe`

Also verify that typing:

```bash
code
```

opens the editor and then close it again.

Also test that

```bash
which git
```

produces some output like `/bin/git`.
The `which` command is used to figure out where a given program is located on disk.

## Telling Git about your editor

Now we need to update the default editor used by `Git`.

```bash
git config --global core.editor "code --wait"
```

Note that it is not obvious how to copy and paste text in a `Windows` terminal including `Git Bash`.
Copy and paste can be found by right clicking on the top bar of the window and selecting the commands from the drop down menu (in a sub menu).

## Testing Python

Confirm that the `Python` installation has worked by typing:

```bash
python -V
```

Which should result in details of your installed `Python` version.
This should print the installed version of the `Python` and `Git` confirming that both are installed at working correctly.
You should now have a working version of `Git`, `Python`, and your chosen editor, all accessible from your shell.
