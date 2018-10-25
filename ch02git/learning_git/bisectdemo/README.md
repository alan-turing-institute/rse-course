# Git Bisect Demo

`squares.py` just spits out the square of an integer passed in as an argument.  The function of the script is irrelevant as we are really looking at git.  Running `breakme.sh` will create a buggy branch with 1000 dummy commits and 1 commit that introduces a regression in `squares.py`.  This environment can be used to demonstrate the value of the git bisect command.

## Create your buggy branch

**Keep in mind this will blow away any local branch named buggy.**

```bash
$ git clone https://github.com/shawnsi/bisectdemo.git 
$ ./breakme.sh
```

## Bisect

Running `squares.py` will now show an obvious error.

```bash
$ python squares.py 2
Traceback (most recent call last):
  File "squares.py", line 7, in <module>
    print(integer**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```

Now we can use `git bisect` to identify the first commit that introduced the regression.  Start this bisection then indicate known good and bad commits.

```bash
$ git bisect start
$ git bisect good master
$ git bisect bad HEAD
```

Test the current commit and tell git whether its good or bad.  The order of commands below is just an example.  Your individual bisection may proceed differently.

```bash
$ python squares.py 2
4
$ git bisect good
$ python squares.py 2
Traceback (most recent call last):
  File "squares.py", line 7, in <module>
    print(integer**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
$ git bisect bad
```

Eventually git will widdle the commit log down to one commit that introduced the regression.

```bash
$ git bisect good
15644003d085cf1a35e2c4c4af654d9e386f811a is the first bad commit
commit 15644003d085cf1a35e2c4c4af654d9e386f811a
Author: Shawn Siefkas <shawn.siefkas@meredith.com>
Date:   Thu Nov 14 09:23:55 2013 -0600

    Breaking argument type

:100644 100644 ff0746a9f0ac02303bd87ed7c3d1571776cbf28d ac23d6bb695e1563edbd3a3fcc0079e1be1793ae M      squares.py
```

### Automatic Bisection

This example can be further condensed via `git bisect run`:

```bash
$ git bisect start
$ git bisect good master
$ git bisect bad buggy
$ git bisect run python squares.py 2
```
