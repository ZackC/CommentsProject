#!/bin/bash

#This program reads a list of git respositories and clones each respository in the #list in the current directory

repoFile=../sampleRepos.txt
rm -rf GitRepos
mkdir GitRepos
cd GitRepos
while read line
do
  echo "git clone $line"
  sleep 1
done < $repoFile
