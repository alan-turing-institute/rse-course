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

**Note:** If you're working in Windows and haven't used a terminal or console before, it may be simpler to return to this step (and subsequent steps on this page) after completing the Git installation instructions (which gives you a Git Bash console)

### C++ compiler for Windows

If you're using Windows, in order to use `Cython` in the "Programming for Speed" module, you may need to install a `C++ compiler`, [see here for more details](https://github.com/cython/cython/wiki/CythonExtensionsOnWindows).