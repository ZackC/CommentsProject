#!/bin/bash


#This file runs the line counting program cloc on each git repository in the starting directory and outputs each repostitory's result to the file lineCount.txt in the main folder of the repository

#dirList=`ls -d -- */ | tail -n 78`
dirList=`ls -d -- */`
for dir in ${dirList[@]}
do
  cd $dir
  echo "starting on $dir"
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
