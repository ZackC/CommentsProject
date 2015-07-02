#!/usr/bin/python

#This file counts the average code and comment count repositories at different commits in repoCountToExtractFrom number of repos.

import os
import sys
import random

repoCountToExtractFrom = 30

def main(argv=None):
  if len(argv) != 2 or not os.path.isdir(argv[1]):
    print "ouput directory is required.\nUsage: ./analyzeChangePerCommitPerRepo.py outputDir"
  else:
    outputDir = argv[1]
    unfinishedDirList=["frameworks_base_disabled","intellij_community","platform_frameworks_base"]
    currentDirContents = os.listdir('.')
    originalPath = os.getcwd()
    immediateChildDirectories = [x for x in currentDirContents if os.path.isdir(x) and x not in unfinishedDirList]
    childDirectoryCount = len(immediateChildDirectories)
    selectedDirs = random.sample(immediateChildDirectories, repoCountToExtractFrom)
    for dir in selectedDirs:   
      fopen = open(dir+"/lineCount.txt")
      currentRepoList = []
      for line in fopen:
        if line.startswith("SUM:"):
          lineItems = line.split()
          #print "items in line"
          count=0
          commentLineCount = int(lineItems[3])
          sourceLineCount = int(lineItems[4])
          currentRepoList.append((commentLineCount,sourceLineCount))
      outputFile = os.path.join(outputDir,dir+".txt")
      fout = open(outputFile,'w')
      for idx, (commentCount, sourceCount) in enumerate(reversed(currentRepoList)):
        fout.write("%d, %d" % (commentCount,sourceCount)) #need to change this to write to file
      fout.close()
  
if __name__ == "__main__":
  main(sys.argv)
