#!/bin/bash

#This scipt runs the process line count script (the one that analyzes source code lines, commment lines, etc.) on each repository in the folder and appends the output to the file totalResults.txt

echo "" > totalResults.txt
dirList=`ls -d -- */`
for dir in ${dirList[@]}
do
  cd $dir
  #echo `pwd`  
  ../../processLineCount.py lineCount.txt >> ../totalResults.txt
  cd ..
done
