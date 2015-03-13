#!/bin/bash

repoFile=../sampleRepos.txt
rm -rf GitRepos
mkdir GitRepos
cd GitRepos
while read line
do
  echo "git clone $line"
  sleep 1
done < $repoFile
