#!/bin/bash

echo "" > totalResults.txt
dirList=`ls -d -- */`
for dir in ${dirList[@]}
do
  cd $dir
  #echo `pwd`  
  ../../processLineCount.py lineCount.txt >> ../totalResults.txt
  cd ..
done
