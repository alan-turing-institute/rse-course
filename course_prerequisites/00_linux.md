# Linux

## Package Manager

`Linux` users should be able to use their package manager to install all of this software (if you're using `Linux`, we assume you won't have any trouble with these requirements).

However note that if you are running an older `Linux` distribution you may get older versions with different look and features.
A recent `Linux` distribution is recommended.

## Python via package manager

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

## Python via Anaconda

We recommend you use [Anaconda](https://anaconda.org/), a complete independent scientific python distribution.

Download [Anaconda for Linux](https://www.anaconda.com/download/#linux) with your web browser, choosing the latest version.
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

## Python via Enthought Canopy

Alternatively you may install a complete independent scientific python distribution.
One of these is `Enthought Canopy`.

The `Enthought Canopy` Python distribution exists in two different versions.
A basic free version with a limited number of packages (`Canopy Express`) and a non free full version.
The full version can be obtained free of charge for academic use.

You may then use your Enthought user account to sign into the installed `Canopy` application and activate the full academic version.
`Canopy` comes with a package manager from where it is possible to install and update a large number of python packages.
The packages installed by default should cover our needs.

## Git

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

## GitHub

For the Git part of the course, you will need access to GitHub. You will need to

1. [Sign up](https://github.com/join)
2. [Generate an SSH key pair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
3. [Add the public key to your GitHub account and the private key to your computer's keychain](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
4. Lastly, you should [test your SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

## Editor

Many different text editors suitable for programming are available.
If you don't already have a favourite, you could look at one of these:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Atom](https://atom.io)
- [Sublime Text](https://www.sublimetext.com)
- [Vim](https://www.vim.org/)
- [Emacs](https://www.gnu.org/software/emacs/)

Regardless of which editor you have chosen you should configure `git` to use it.
Executing something like this in a terminal should work:

```bash
git config --global core.editor NameofYourEditorHere
```

The default shell is usually `bash` but if not you can get to `bash` by opening a terminal and typing `bash`.
