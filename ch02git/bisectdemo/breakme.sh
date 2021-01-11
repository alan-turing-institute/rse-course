#!/bin/bash
#
# Creates 1000 dummy comment commits and randomly inserts a bug among those.
# This can be used to demo the value of the git bisect command.

function comment {
  COMMENT="Comment $1"
  echo "#$COMMENT" >> squares.py
  git add squares.py
  git commit -m "$COMMENT"
}

BREAKINDEX=$((RANDOM%1000))

git branch -D buggy
git checkout -b buggy

for i in $(seq 1 $BREAKINDEX); do
  comment $i
done

git cherry-pick origin/broken

for i in $(seq $((BREAKINDEX+1)) 1000); do
  comment $i
done

