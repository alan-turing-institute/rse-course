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

Please ensure that you have a computer (ideally a laptop) with all of these installed. Even if you think you have all of these things already, it's worth reading through the sections below to make sure.

## Python

Install the [Anaconda](https://www.anaconda.com/distribution/) distribution for your operating system (OS). On Windows and Mac this should include an install Wizard.

You should then test whether the installation has worked as expected by doing one of the following:

<details>
  <summary>On Windows or Mac...</summary><p></p>
  Open a terminal (console) window and check whether the installation has worked. You will require version `3.8` or greater of Python and Anaconda should install the most recent one by default:

  ```bash
  python --version
  ```
  
  **Note:** If you're working in Windows and haven't used a terminal or console before it may be simpler to return to this step after completing the remainder of the installation instructions on this page
</details>

<details>
  <summary>On Linux...</summary><p></p>
  Open a terminal window, go to the place where the file was downloaded and type:

  ```bash
  bash Anaconda3-
  ```

  and then press `Tab`.
  The name of the file you just downloaded should appear.

  Follow the text prompts ensuring that you:

  - agree to the licence
  - prepend `Anaconda` to your `PATH` (this makes the `Anaconda` distribution the default `Python`)

  You can test the installation by opening a new terminal and checking that:

  ```bash
  which python
  ```

  shows a path where you installed `Anaconda`.
</details><p></p>

If the version of Python you have is < `3.8.x` or you experience some difficulties with Anaconda, there are alternative ways to install Python.

<details>
  <summary>Alternative ways to install Python on Linux</summary><p></p>
    
  Python can be installed on Linux via package manager or Enthought Canopy.

  `Linux` users should be able to use their package manager to install all of this software (if you're using `Linux`, we assume you won't have any trouble with these requirements).

  However note that if you are running an older `Linux` distribution you may get older versions with different look and features.
  A recent `Linux` distribution is recommended.

  Recent versions of `Ubuntu` come with mostly up to date versions of all needed packages.
  The version of `IPython` might be slightly out of date.
  Advanced users may wish to upgrade this using `pip` or a manual install.
  On `Ubuntu` you should ensure that the following packages are installed using `apt-get`.

  - `python3-numpy`
  - `python3-scipy`
  - `python3-pytest`
  - `python3-matplotlib`
  - `python3-pip`
  - `jupyter`
  - `ipython3`
  - `ipython3-notebook`

  Older distributions may have outdated versions of specific packages.
  Other `Linux` distributions most likely also contain the needed `Python` packages but again they may also be outdated.

  Alternatively you may install a complete independent scientific python distribution.
  One of these is `Enthought Canopy`.

  The `Enthought Canopy` Python distribution exists in two different versions.
  A basic free version with a limited number of packages (`Canopy Express`) and a non free full version.
  The full version can be obtained free of charge for academic use.

  You may then use your Enthought user account to sign into the installed `Canopy` application and activate the full academic version.
  `Canopy` comes with a package manager from where it is possible to install and update a large number of python packages.
  The packages installed by default should cover our needs.
    
</details>

<details>
  <summary>Alternative ways to install Python on Mac</summary><p></p>

  [Homebrew](https://brew.sh) is a package manager for `macOS` which enables the installation of a lot of software useful for scientific computing.
  It is required for some of the installations below.
  `Homebrew` requires the `Xcode` tools above.

  Install `homebrew` via typing this at a terminal:

  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

  and then type.

  ```bash
  brew doctor
  ```

  And read the output to verify that everything is working as expected.
  If you are already running `MacPorts` or another package manager for `macOS` we don't recommend installing `homebrew` as well.

  Install Python:

  ```bash
  brew install python3
  ```

  In order to ensure that this version of `Python` is selected over the `macOS` default version you should execute the following command:

  ```bash
  echo export PATH='/usr/local/bin:$PATH' >> ~/.bash_profile
  ```

  and reopen the terminal. Verify that this is correctly installed by executing

  ```bash
  python --version
  ```

  Which should print:

  ```bash
  Python 3.x.x
  ```

  (where x.x is replaced by a version number higher than `3.8.0`)

  This will result in an installation of `python3` and `pip3` which you can use to have access to the latest `Python` features which will be taught in this course.

  Then install additional `Python` packages by executing the following.

  `brew install [package-name]`

  - `pkg-config`
  - `freetype`
  - `gcc`

  Python packages can be installed via `pip`. Install each of the following by running `pip install` in the terminal like so (if pip is unavailable, follow the "Python from Homebrew" section below)

  `pip install [package-name]`

  - `numpy`
  - `scipy`
  - `matplotlib`
  - `jupyter`
  - `ipython[all]`

  The following packages should be installed automatically as dependencies, but we recommend installing them manually just in case.

  - `tornado`
  - `jinja2`
  - `pyzmq`
  - `pytest`

</details>

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

## Additional things to install

### C++ compiler for Windows

If you're using Windows, in order to use `Cython` in the "Programming for Speed" module, you may need to install a `C++ compiler`, [see here for more details](https://github.com/cython/cython/wiki/CythonExtensionsOnWindows).

## Troubleshooting

### Jupyter issues on Windows:

To use the Jupyter Lab (or Jupyter notebook) on a `Windows` computer with Sophos anti-virus installed it may be necessary to open additional ports allowing communication between the notebook and its server.
The [solution](http://stackoverflow.com/questions/13036197/ipython-notebook-getting-output) is:

- open your `Sophos Endpoint Security and Control Panel` from your tray or start menu
- Select `Configure > Anti-virus > Authorization` from the menu at the top
- Select the websites tab
- click the `Add` button and add `127.0.0.1` and `localhost` to the `Authorized websites` list
- restart computer (or just restart the Jupyter)