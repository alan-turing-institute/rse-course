# MacOS

## Upgrade MacOS

We do not recommend following this training on older versions of `macOS` without an app store: upgrade to at least `macOS 10.9 (Mavericks)`.

## XCode and Command line tools

Install the `XCode` command-line-tools by opening a terminal and run the following.

```bash
xcode-select --install
```

And follow the on screen instructions.

You may also install `Xcode` from the app store if you wish, but it is not needed.

## Git

The `XCode` command line tools come with `Git` so no need to do anything more, as long as you can run the following in your terminal:

```bash
git --version
```

## GitHub

For the Git part of the course, you require access to GitHub. You will need to

1. [Sign up](https://github.com/join), if you haven't already
2. [Generate an SSH key pair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
3. [Add the public key to your GitHub account and the private key to your computer's keychain](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
4. Lastly, you should [test your SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

## Homebrew

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

## Python

We recommend installing a complete scientific python distribution.
One of these is [Anaconda](https://www.anaconda.com/distribution/).
Please download and install [Anaconda](https://www.anaconda.com/download/) (latest version).

## Python from Homebrew

Alternatively if you wish to install `Python` manually you can use Homebrew.
`macOS` ships with `Python` and some packages.
However this has known limitations and we do not recommend it.
You can install a new version of `Python` from `homebrew` with the following.
Please follow the instructions above to install the `Xcode` command line tools and `homebrew` before attempting this.

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
Python 3.8.x
```

(where x will be replaced by a version number)

This will result in an installation of `python3` and `pip3` which you can use to have access to the latest `Python` features which will be taught in this course.

Then install additional `Python` packages by executing the following.

`brew install [package-name]`

- `pkg-config`
- `freetype`
- `gcc`

`pip3 install [package-name]`

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

## Editor and shell

The default text editor on `macOS` _textedit_ should be sufficient for our use.
Alternatively consider one of these editors:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Atom](https://atom.io)
- [Sublime Text](https://www.sublimetext.com)
- [Vim](https://www.vim.org/)
- [Emacs](https://www.gnu.org/software/emacs/)

To setup `git` to use _textedit_ executing the following in a terminal should do.

```bash
git config --global core.editor /Applications/TextEdit.app/Contents/MacOS/TextEdit
```

For VS Code:

```bash
git config --global core.editor "code --wait"
```

The default terminal on `macOS` should also be sufficient.
If you want a more advanced terminal [iTerm2](http://www.iterm2.com/) is an alternative.
