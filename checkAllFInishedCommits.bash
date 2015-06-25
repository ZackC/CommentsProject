#!/bin/bash

#This bash program scripts running the checkFinshedCommits.py script for all repositories in the folder

dirList=`ls -d -- */`
for dir in ${dirList[@]}
do
  echo "$dir"
  python checkFinishedCommits.py
  echo "=================="
done
