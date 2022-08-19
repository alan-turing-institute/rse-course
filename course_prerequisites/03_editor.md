# Text Editor

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
