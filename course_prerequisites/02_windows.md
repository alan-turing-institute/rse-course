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

Install the [GitHub Desktop Client](http://windows.github.com/).
This comes with both a GUI client as well as the [Git Bash](https://gitforwindows.org/) terminal client which we will use during the course.

You'll know it has worked when you can open a Git Bash terminal (the window should have a title that starts with MINGW32) and get the Git version by running

```bash
git --version
```

which should show that you have a [recent](https://en.wikipedia.org/wiki/Git#Releases) copy of Git. If your version is more than 18 months old, please update it.

## GitHub

For the Git part of the course, you require access to GitHub. You will need to [sign up](https://github.com/join) and follow either the **GitHub Setup using the Command Line** or **GitHub Setup using the Desktop Client** instructions, below.

### GitHub Setup using the Command Line

1. [Generate an SSH key pair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
2. [Add the public key to your GitHub account and the private key to your computer's keychain](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
3. [Test your SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

### GitHub Setup using the Desktop Client

1. Signing in to the GitHub Desktop Client should automatically set-up [SSH based authentication](https://help.github.com/articles/generating-ssh-keys#platform-windows) for the terminal client
2. Configure the default terminal client (there are three different flavours of terminal on Windows: `Windows CMD` (DOS like), `Windows Powershell`, and `BASH`) to use BASH, as this most closely resembles the `Linux` and `macOS` terminal used by other students:
    1. In the Desktop Client, select **Tools**
    2. Then **Options**
    3. **Default Shell**
    4. **Git Bash**

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
