#!/bin/bash

dirList=`ls -d -- */`
for dir in ${dirList[@]}
do
  cd $dir
  echo "" > lineCount.txt
  git log > logResult.txt
  python ../../getCommits.py logResult.txt > commitList.txt
  firstCommit=""
  while read line
  do
    if [ -z "$firstCommit" ]
    then
      firstCommit=$line
    fi
    git reset --hard $line
    ../../cloc-1.62.pl . >> lineCount.txt
    echo "=======================" >> lineCount.txt 
  done < commitList.txt
  git reset --hard $firstCommit
  cd ..
done
