# Installation Instructions

## Introduction

This document contains instructions for installation of the packages we'll be using during the course.
You will be following the training on your own machines, so please complete these instructions.
The instructions include Windows, Mac and Linux specific sections.

**If you encounter any problem during insallation** and you manage to solve them (feel free to ask us for help), please remember to add an issue to the [course repo](https://github.com/alan-turing-institute/rsd-engineeringcourse), explaining the problem and solution.
By doing this you will be helping to improve the instructions for future users! 🎉

## What we're installing

- the `Python` programming language (version `3.8` or greater) and `Conda`
- a selection of `Python` software packages that will be used during the course (via a Conda environment)
- `git` for the version control module
- a suitable text editor

Please ensure that you have a computer (ideally a laptop) with all of these installed. Even if you think you have all of these things already, it's worth reading through the sections below to make sure.

## Installing Python

Install the [Anaconda](https://www.anaconda.com/distribution/) distribution for your operating system (OS).

Open a terminal (console) window and check whether the installation has worked. You will require version `3.8` or greater of Python and Anaconda should install the most recent one by default:

```bash
python --version
```

If the version of Python you have is < `3.8.x` or you experience some difficulties with Anaconda, there are alternative ways to install Python.

<details>
  <summary>Alternative ways to install Python on Linux</summary><p></p>
    
  Python can be installed on Linux via package manager or Enthought Canopy.

  `Linux` users should be able to use their package manager to install all of this software (if you're using `Linux`, we assume you won't have any trouble with these requirements).

  However note that if you are running an older `Linux` distribution you may get older versions with different look and features.
  A recent `Linux` distribution is recommended.

  ## 

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