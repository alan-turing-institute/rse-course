# Git & GitHub

Check whether you have installed already.

```bash
git --version
```

If not, follow the instructions for your OS and try running this commnd again.
If your version of `git` is more than 18 months old (see [releases](https://en.wikipedia.org/wiki/Git#Releases)), please update it.

## Windows instructions:

Install the [GitHub Desktop Client](http://windows.github.com/).
This comes with both a GUI client as well as the [Git Bash](https://gitforwindows.org/) terminal client which we will use during the course. In some instances `Git Bash` may need to be installed separately.
In order to use `conda` with `Git Bash` follow the instructions [here](https://discuss.codecademy.com/t/setting-up-conda-in-git-bash/534473)

You will need to create an account on GitHub.
You can then sign-in to the GitHub Desktop Client which should automatically set-up [SSH based authentication](https://help.github.com/articles/generating-ssh-keys#platform-windows) for the terminal client.

Configure the default terminal client (there are three different flavours of terminal on Windows: `Windows CMD` (DOS like), `Windows Powershell`, and `BASH`) to use BASH, as this most closely resembles the `Linux` and `macOS` terminal used by other students:

1. In the Desktop Client, select **Tools**
2. Then **Options**
3. **Default Shell**
4. **Git Bash**

You'll know it has worked when you can open a Git Bash terminal; the window should have a title that starts with MINGW32 (scroll to the top of this page for how to check the git version).

## macOS and Linux instructions:

<details>

<summary>Installing Git on macOS</summary><p></p>

Install the `XCode` command-line-tools by opening a terminal and run the following.

```bash
xcode-select --install
```

and follow the on screen instructions.
You may also install `Xcode` from the app store if you wish, but it is not needed.
The `XCode` command line tools come with `Git` - please confirm you have installed it by running:

```bash
git --version
```

</details>

<details>

<summary>Installing Git on Linux</summary><p></p>

Install `git` via your distribution package manager (e.g. `apt-get` or `yum`), for example:

```bash
sudo apt-get install git
```

Check your version by running

```bash
git --version
```

</details>

To use `git` you will need to set up an account with your email address and name.
To do this you can follow the **Your Identity** section of [first time git setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

You can check that they have been set correctly by running `git config user.name` and `git config user.email`.
For the `git` module (Version Control with Git), you will also require access to GitHub.

Follow these instructions if you are working on macOS or Linux:

1. [Sign up](https://github.com/join), if you haven't already
2. [Generate an SSH key pair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
3. [Add the public key to your GitHub account and the private key to your computer's keychain](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
4. Lastly, you should [test your SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)
