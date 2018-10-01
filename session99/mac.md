---
title: Mac OSX
---

Mac
===

Upgrade OSX
---------

We do not recommend following this training on older versions of OSX without an app store: upgrade
to at least OSX Mavericks.

XCode and Command line tools
----------------------------

Install the XCode command-line-tools by opening a terminal and run the following.

``` bash
xcode-select --install
```
And follow the on screen instructions.

You may also install Xcode from the Mac app store if you wish, but it is not needed.

Pre Mavericks:

Install [XCode](https://itunes.apple.com/us/app/xcode/id497799835) using the Mac app store.

Then, go to Xcode...Preferences...Downloads... and install the command line tools option.

##Git

The XCode tools comes with Git so no need to do anything more.

Homebrew
--------
[Homebrew](brew.sh) is a package manager for OSX which enables the installation of a
lot of software useful for scientific computing. It is required for some of the installations
below. But not essential for Software Carpentry. Homebrew requires the Xcode tools above.

Install Homebrew via typing this at a terminal:

``` bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

and then type.

```bash
brew doctor
```

And read the output to verify that everything is working as expected.

If you are already running MacPorts or another package manager for OSX we don't recommend
installing homebrew.


Python
------

We recommend installing a complete scientific python distribution. One of these is
Anaconda.

Please download and install the Python 3.5 version of [Anaconda](https://www.continuum.io/downloads)


Python from Homebrew
--------------------

Alternatively if you wish to install python manually you can use Homebrew.
OSX ships with python and some packages. However this has known limitations and we do not recommend it.
You can install a new version of python from Homebrew with the following.
Please follow the instructions above to install the Xcode tools and Homebrew before attempting
this.

```bash
brew install python3
```

In order to ensure that this version of python is selected over the OSX default version you should
execute the following command:

```bash
echo export PATH='/usr/local/bin:$PATH' >> ~/.bash_profile
```
and reopen the terminal. Verify that this is correctly installed by executing

```
python --version
```

Which should print:

```
Python 3.6.1
```
This will result in an installation of `python3` and `pip3` which you can use to have access to the latest python features which will be taught in this course.

Then install additional python packages by executing the following.

brew install [package-name]
*  pkg-config
*  freetype
*  gcc

pip3 install [package-name]
*  numpy
*  scipy
*  matplotlib
*  ipython[all]

The following packages should be installed automatically as dependencies. But we recommend
installing them manually just in case.

*  tornado
*  jinja2
*  pyzmq
*  nose


Editor and shell
----------------

The default text editor on OS X *textedit* should be sufficient for our use. Alternatively
[this link](http://mac.appstorm.net/roundups/office-roundups/top-10-mac-text-editors/) lists a number of other good editors.

A new open source option is Github's Atom editor. You can get it from https://atom.io/
However, note that this is still in somewhat early development.

To setup git to use *textedit* executing the following in a terminal should do.

``` bash
git config --global core.editor /Applications/TextEdit.app/Contents/MacOS/TextEdit
```

The default terminal on OSX should also be sufficient. If you want a more advanced terminal
[iTerm2](http://www.iterm2.com/) is an alternative.
