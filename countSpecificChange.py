#!/usr/bin/python

#This script counts how many times a comment and source code line relation occurs in individual repositories and in total

#if a second arguements is provided, the script will print out which commits contain the importantCommits instead of a count

import sys
import re
import os
import findCommitInRepo
import datetime

totalCommentChange = 0
totalSourceChange = 0
commitCount = 0

def main(argv=None):
    printImportantCommits = (len(argv)==2) 
    currentDirContents = os.listdir('.')
    originalPath = os.getcwd()
    immediateChildDirectories = [x for x in currentDirContents if os.path.isdir(x)]
    countDict = {}
    for aDir in immediateChildDirectories:
      fopen = open(aDir+"/lineCount.txt")
      currentRepoList = []
      for line in fopen:
        if line.startswith("SUM:"):
          lineItems = re.split(r'\s{2,}', line)
          #print "items in line"
          commentLineCount = int(lineItems[3])
          sourceLineCount = int(lineItems[4])
          currentRepoList.append((commentLineCount,sourceLineCount))
      if len(currentRepoList) > 1:
        currentRepoList.reverse()
        for idx, (oldCommentCount, oldSourceCount) in enumerate(currentRepoList[:-1]):
          newCommentCount= currentRepoList[idx+1][0]
          newSourceCount = currentRepoList[idx+1][1]
          if isImportantCommit(oldCommentCount,oldSourceCount,newCommentCount,newSourceCount):
            if printImportantCommits:
               print "found important commit" #this is temporary
               print datetime.datetime.now().time()
               findCommitInRepo.findCommit(aDir,newCommentCount,newSourceCount,oldCommentCount,oldSourceCount)
            else: 
            #print "returned True!!!"
              if aDir in countDict:
                countDict[aDir]= countDict[aDir] + 1
              else:
                countDict[aDir] = 1
    if not printImportantCommits:
      total = 0
      for aDir,dirCount in countDict.iteritems():
        total = total + dirCount
        print "Count for %s: %d" % (aDir,dirCount)
      print "Totals- Repo Count: %d, Commit count: %d" % (len(countDict),total)
      averageCommentChange = float(totalCommentChange)/float(commitCount)
      averageSourceChange = float(totalSourceChange)/float(commitCount)
      print "Average Change - comments: %d, source: %d" % (averageCommentChange,averageSourceChange)
        
def isImportantCommit(oldCommentLineCount,oldSourceLineCount,newCommentLineCount,newSourceLineCount):
   commentChange = newCommentLineCount - oldCommentLineCount
   sourceChange = newSourceLineCount - oldSourceLineCount
   global totalCommentChange
   global totalSourceChange
   global commitCount
   totalCommentChange = totalCommentChange + commentChange
   totalSourceChange = totalSourceChange + sourceChange
   commitCount = commitCount + 1
   #print "commentChange: %d, sourceChange: %d" % (commentChange, sourceChange) 
   #if commentChange!=0 and sourceChange !=0:
   #   print "sourceChange > 0: %r" % (sourceChange>0)
   #   print "commentChange > 50: %r" % (commentChange > 50)
   #   print "float(commentChange)/float(sourceChange)>2):  %r" % (float(commentChange)/float(sourceChange)>2)
   if(sourceChange > 50 and commentChange > 100 and float(commentChange)/float(sourceChange)>2):
     #print "returning true"
     return True
   else:
     #print "returning false"
     return False

if __name__ == "__main__":
  main(sys.argv)    


