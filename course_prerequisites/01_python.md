# Python

Install the [Anaconda](https://www.anaconda.com/distribution/) distribution for your operating system (OS). On Windows and Mac this should include an install Wizard.

<details>
  <summary>If on Linux...</summary><p></p>
  Open a terminal window, go to the place where the file was downloaded and type:

  ```bash
  bash Anaconda3-
  ```

  and then press `Tab`.
  The name of the file you just downloaded should appear.

  Follow the text prompts ensuring that you:

  - agree to the licence
  - prepend `Anaconda` to your `PATH` (this makes the `Anaconda` distribution the default `Python`)

</details><p></p>

You should then test whether the installation has worked as expected by doing the following:

Open a terminal (console) window and check whether the installation has worked. You will require version `3.8` or greater of Python and Anaconda should install the most recent one by default:

```bash
python --version
```

**Note:** If you're working in Windows and haven't used a terminal or console before, it may be simpler to return to this step after completing the Git installation instructions (which gives you a Git Bash console)

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

### C++ compiler for Windows

If you're using Windows, in order to use `Cython` in the "Programming for Speed" module, you may need to install a `C++ compiler`, [see here for more details](https://github.com/cython/cython/wiki/CythonExtensionsOnWindows).