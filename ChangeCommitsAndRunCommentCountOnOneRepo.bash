#!/bin/bash


#This file runs the line counting program cloc on each git repository in the starting directory and outputs each repostitory's result to the file lineCount.txt in the main folder of the repository


  firstCommit=""
  while read line
  do
    if [ -z "$firstCommit" ]
    then
      firstCommit=$line
    fi
    git reset --hard $line
    echo "current commit: $line" >> lineCountWithCommits.txt
    ../../cloc-1.62.pl . >> lineCountWithCommits.txt
    echo "=======================" >> lineCountWithCommits.txt 
  done < commitList.txt
  git reset --hard $firstCommit
