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


## Git & GitHub

#### Mac and Linux instructions:

<details>

  <summary>Installing Git on Mac</summary><p></p>

  Install the `XCode` command-line-tools by opening a terminal and run the following.

  ```bash
  xcode-select --install
  ```

  And follow the on screen instructions.

  You may also install `Xcode` from the app store if you wish, but it is not needed.

  The `XCode` command line tools come with `Git` so no need to do anything more, as long as you can run the following in your terminal:

  ```bash
  git --version
  ```

</details>

<details>

  <summary>Installing Git on Linux</summary><p></p>

  If `git` is not already available on your machine you can try to install it via your distribution package manager (e.g. `apt-get` or `yum`), for example:

  ```bash
  sudo apt-get install git
  ```

  You'll know it has worked when you can get the Git version by running

  ```
  git --version
  ```

  which should show that you have a [recent](https://en.wikipedia.org/wiki/Git#Releases) copy of Git. If your version is more than 18 months old, please update it.

  You will need to set at least your email address and name, for which you can follow the **Your Identity** section of [First Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

  You can check that they have been set correctly by running `git config user.name` and `git config user.email`.

</details><p></p>

For the Git part of the course, you require access to GitHub. Follow these instructions if you are working on Mac, Linux, or if you're a Windows user who has used the command line (terminal/console) before:

1. [Sign up](https://github.com/join), if you haven't already
2. [Generate an SSH key pair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
3. [Add the public key to your GitHub account and the private key to your computer's keychain](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
4. Lastly, you should [test your SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

#### Windows instructions:

Install the [GitHub Desktop Client](http://windows.github.com/).
This comes with both a GUI client as well as the [Git Bash](https://gitforwindows.org/) terminal client which we will use during the course. In some instances Git Bash may need to be installed separately. In order to use conda with Git Bash follow the instructions [here](https://discuss.codecademy.com/t/setting-up-conda-in-git-bash/534473)

Signing in to the GitHub Desktop Client should have automatically set-up [SSH based authentication](https://help.github.com/articles/generating-ssh-keys#platform-windows) for the terminal client.

Configure the default terminal client (there are three different flavours of terminal on Windows: `Windows CMD` (DOS like), `Windows Powershell`, and `BASH`) to use BASH, as this most closely resembles the `Linux` and `macOS` terminal used by other students:

  1. In the Desktop Client, select **Tools**
  2. Then **Options**
  3. **Default Shell**
  4. **Git Bash** 

You'll know it has worked when you can open a Git Bash terminal (the window should have a title that starts with MINGW32) and get the Git version by running

```bash
git --version
```

which should show that you have a [recent](https://en.wikipedia.org/wiki/Git#Releases) copy of Git. If your version is more than 18 months old, please update it.


## Text Editor

Unless you already use a specific editor which you are comfortable with we recommend using one of the following:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Notepad++](https://notepad-plus-plus.org/downloads/)
- [Vim](https://www.vim.org/)
- [Emacs](https://www.gnu.org/software/emacs/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

<details>

  <summary>Windows editor tips and final checks</summary><p></p>
  
  Using any of these to edit text files including code should be straight forward.
  `Visual Studio Code` has integrations with [Git Bash](https://code.visualstudio.com/docs/editor/integrated-terminal) and the [Python prompt](https://code.visualstudio.com/docs/python/python-tutorial) that you may want to configure.

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

  Now we need to update the default editor used by `Git`.

  ```bash
  git config --global core.editor "code --wait"
  ```

  Note that it is not obvious how to copy and paste text in a `Windows` terminal including `Git Bash`.
  Copy and paste can be found by right clicking on the top bar of the window and selecting the commands from the drop down menu (in a sub menu). Alternatively the keyboard shortcuts are ctrl+insert for copy and shift+insert for paste. 

  Confirm that the `Python` installation has worked by typing:

  ```bash
  python -V
  ```

  Which should result in details of your installed `Python` version.
  This should print the installed version of the `Python` and `Git` confirming that both are installed at working correctly.
  You should now have a working version of `Git`, `Python`, and your chosen editor, all accessible from your shell.
  
</details>

<details>

  <summary>Mac editor tips and final checks</summary><p></p>
  
  Mac editor tips and final checks

  The default text editor on `macOS` _textedit_ should be sufficient for our use. To setup `git` to use _textedit_ executing the following in a terminal should do.

  ```bash
  git config --global core.editor /Applications/TextEdit.app/Contents/MacOS/TextEdit
  ```

  For VS Code:

  ```bash
  git config --global core.editor "code --wait"
  ```

  The default terminal on `macOS` should also be sufficient.
  If you want a more advanced terminal [iTerm2](http://www.iterm2.com/) is an alternative.
  
</details>

<details>

  <summary>Linux editor tips and final checks</summary><p></p>
  
  Linux editor tips and final checks

  Regardless of which editor you have chosen you should configure `git` to use it.
  Executing something like this in a terminal should work:

  ```bash
  git config --global core.editor NameofYourEditorHere
  ```

  The default shell is usually `bash` but if not you can get to `bash` by opening a terminal and typing `bash`.
  
</details>

## Troubleshooting

### Jupyter issues on Windows:

To use the Jupyter Lab (or Jupyter notebook) on a `Windows` computer with Sophos anti-virus installed it may be necessary to open additional ports allowing communication between the notebook and its server.
The [solution](http://stackoverflow.com/questions/13036197/ipython-notebook-getting-output) is:

- open your `Sophos Endpoint Security and Control Panel` from your tray or start menu
- Select `Configure > Anti-virus > Authorization` from the menu at the top
- Select the websites tab
- click the `Add` button and add `127.0.0.1` and `localhost` to the `Authorized websites` list
- restart computer (or just restart the Jupyter)