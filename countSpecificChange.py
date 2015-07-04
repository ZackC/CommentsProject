#!/usr/bin/python

#This script counts how many times a comment and source code line relation occurs in individual repositories and in total

import sys
import re
import os

def main(argv=None):
 
  
    currentDirContents = os.listdir('.')
    originalPath = os.getcwd()
    immediateChildDirectories = [x for x in currentDirContents if os.path.isdir(x)]
    countDict = {}
    for aDir in immediateChildDirectories:
      fopen = open(aDir+"/lineCount.txt")
      currentRepoList = []
      for line in fin:
        if line.startswith("SUM:"):
          lineItems = re.split(r'\s{2,}', line)
          #print "items in line"
          commentLineCount = int(lineItems[3])
          sourceLineCount = int(lineItems[4])
          currentRepoList.append((commentLineCount,sourceLineCount))
      currentRepoList = currentRepoList.reverse()
      for idx, (oldCommentCount, oldSourceCount) in enumerate(currentRepoList[:-1:]):
        newCommentCount= currentRepoList[idx+1][3]
        newSourceCount = currentRepoList[idx+1][4]
        if isImportantCommit(oldCommentCount,oldSourceCount,newCommentCount,newSourceCount):
          if aDir in countDict:
            countDict[aDir]= countDict[aDir] + 1
          else:
            countDict[aDir] = 1
    total = 0
    for aDir,dirCount in countDict:
      total = total + dirCount
      print "Count for %s: %d" % (aDir,dirCount)
    print "Total Count: %d" % (total)
        
def isImportantCommit(oldCommentLineCount,oldSourceLineCount,newCommentLineCount,newSourceLineCount):
   commentChange = newCommentLineCount - oldCommentLineCount
   sourceChange = newSourceLineCount - oldSourceLineCount
   if(sourceChange > 49 and float(commentChange)/float(sourceChange)>2):
     True
   else:
     False

if __name__ == "__main__":
  main()    


