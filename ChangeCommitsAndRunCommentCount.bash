#!/bin/bash


#This file runs the line counting program cloc on each git repository in the starting directory and outputs each repostitory's result to the file lineCount.txt in the main folder of the repository

#dirList=`ls -d -- */ | tail -n 78`
dirList=`ls -d -- */`
outputFile="lineCountWithCommits.txt"
for dir in ${dirList[@]}
do
  cd $dir
  echo "starting on $dir"
  echo "" > $outputFile
  #removing lines that don't need ot be executed the second time through
  #git log > logResult.txt
  #python ../../getCommits.py logResult.txt > commitList.txt
  firstCommit=""
  while read line
  do
    if [ -z "$firstCommit" ]
    then
      firstCommit=$line
    fi
    git reset --hard $line
    echo "current commit: $line" >> $outputFile
    ../../cloc-1.62.pl . >> $outputFile
    echo "=======================" >> $outputFile 
  done < commitList.txt
  git reset --hard $firstCommit
  cd ..
done
