#!/usr/bin/python

#This script finds the commit based on the source line count and comment line count

import os
import subprocess
import re

def main(argv=None):
  repositoryName = input('repository name:' )
  commentCountForCommit = input('comment lines: ')
  sourceCountForCommit = input('source lines: ')
  commentCountBeforeCommit = input('previous comment lines: ')
  sourceCountBeforeCommit = input('previous source lines: ') 
  
     
def findCommit(repositoryName,commentCountForCommit,sourceCountForCommit,
commentCountBeforeCommit,sourceCountBeforeCommit):
  print "find commit args: %s, %d, %d, %d, %d" % (repositoryName,commentCountForCommit,sourceCountForCommit,
commentCountBeforeCommit,sourceCountBeforeCommit)
  startingDir = os.getcwd()
  os.chdir(repositoryName)
  #print "current directory: %s" % (os.getcwd())
  commentSourceList = buildCommentSourceCountList()
  printList(commentSourceList,"commentSource.txt")
  targetCommitIndex = commentSourceList.index((commentCountForCommit,sourceCountForCommit))
  
  commitList = buildCommitList()
  foundCommit = False
  minIndex = 0
  maxIndex = len(commitList)
  currentIndex = targetCommitIndex
  commentSourceListLength = len(commentSourceList)
  while not foundCommit:
     print "checkingIndex: %d" % (currentIndex)
     hashToCheck = commitList[currentIndex]
     countsResult = getCountsForCommit(hashToCheck)
     if countsResult == None:
       print "Did not find source and comment count!!!!"
       currentIndex = currentIndex + 1 #loop again with index incremented
     else:
       (commentLineCountForTestedCommit,sourceLineCountForTestedCommit) = countsResult
       if commentCountForCommit == commentLineCountForTestedCommit and sourceCountForCommit == sourceLineCountForTestedCommit:
         print "first commit matched"
         hashToCheck2 = commitList[currentIndex + 1]
         commentLineCountForTestedCommit,sourceLineCountForTestedCommit = getCountsForCommit(hashToCheck2)
         if commentCountBeforeCommit == commentLineCountForTestedCommit and sourceCountBeforeCommit == sourceLineCountForTestedCommit:
           print "second commit matched"
           foundCommit=True
       if not foundCommit:
         tempCommentSourceList=commentSourceList[currentIndex+1:commentSourceListLength]
         currentIndex = tempCommentSourceList.index((commentLineCountForTestedCommit,sourceLineCountForTestedCommit))+currentIndex+1 # not sure if this is right but going to test it soon 
  os.chdir(startingDir)  
  return hashToCheck #the commit has been found so return it and stop looping 


  os.chdir(startingDir)
  if len(matchingLines) == 0:
    print "Error.  Did not find the specific commit"
  elif len(matchingLines) == 1:
    print "the commit is: %s" % (commitList[matchingLines[0]][0])
  else:   
    for match in matchingLines:
      commitToCheck = commitList[match-1]
      if commitToCheck[1] == commentCountBeforeCommit and commitToCheck[2] == sourceCountBeforeCommit:
        print "the commit is: %s in %s" % (commitList[match][0],repositoryName)
        break      

def printList(listToPrint,filename):
  fout = open(filename,'w')
  for index,item in enumerate(listToPrint):
    printString = "%d: %s\n" % (index,str(item))
    fout.write(printString)
  fout.close()
  

def getCountsForCommit(hashToCheck):
  #print "current commit: %s" % (commitHash)
  #print ["git","reset","--hard",commitHash]
  try:
    subprocess.check_output(["git","reset","--hard",hashToCheck])
    clocOutputByteString = subprocess.check_output(["../../cloc-1.62.pl","."])
    clocOutput = clocOutputByteString.decode(encoding='ascii',errors='strict')
    clocOutput = str(clocOutput)
    #print clocOutput
    for line in clocOutput.split("\n"):
      #print "|%s|" % (line)
      if line.startswith("SUM:"):
        currentLineContents = re.split(r'\s{2,}', line)
        print "found sum line !!!"
        commentCount = int(currentLineContents[3])
        sourceCount = int(currentLineContents[4])
        print "sum line contained: %d, %d" % (commentCount,sourceCount)
        return ((commentCount,sourceCount))
  except subprocess.CalledProcessError:
    pass
  return None

def buildCommentSourceCountList():
  fopen = open("lineCount.txt")
  commentSourceList = []
  for currentLine in fopen:
    if currentLine.startswith("SUM:"):
      #print currentLine
      currentLine = currentLine.strip()
      currentLineContents = re.split(r'\s{2,}', currentLine)
      commentLineCount = int(currentLineContents[3])
      sourceLineCount = int(currentLineContents[4])
      commentSourceList.append((commentLineCount,sourceLineCount))
  fopen.close()
  commentSourceList.reverse()
  return commentSourceList



def buildCommitList():
      
  fin = open("commitList.txt",'r')
  commitList = []
  for commitHash in fin:
    commitHash = commitHash.rstrip()
    commitList.append(commitHash)
  fin.close()
  return commitList

if __name__ == "__main__":
  main()    
