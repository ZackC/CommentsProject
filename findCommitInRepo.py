#!/usr/bin/python

#This script finds the commit based on the source line count and comment line count

import os
import subprocess

def main(argv=None):
  repositoryName = input('repository name:' )
  commentCountForCommit = input('comment lines: ')
  sourceCountForCommit = input('source lines: ')
  commentCountBeforeCommit = input('previous comment lines: ')
  sourceCountBeforeCommit = input('previous source lines: ') 
  
     
def findCommit(repositoryName,commentCountForCommit,sourceCountForCommit,
commentCountBeforeCommit,sourceCountBeforeCommit):
  startingDir = os.getcwd()
  os.chdir(repositoryName)
  print "current directory: %s" % (os.getcwd())
  commitList,matchingLines = buildCommitList(commentCountForCommit,sourceCountForCommit)
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
  

def buildCommitList(commentCountForCommit,sourceCountForCommit):
  fin = open("commitList.txt",'r')
  firstCommit = ""
  commitList = []
  matchingLines = []
  count = 0
  for commitHash in fin:
    if firstCommit == "":
      firstCommit = commitHash
    print "current commit: %s" % (commitHash)
    print ["git","reset","--hard",commitHash]
    subprocess.call(["git","reset","--hard",commitHash])
    clocOutputByteString = subprocess.check_output(["../../cloc-1.62.pl","."])
    clocOutput = clocOutputByteString.decode(encoding='ascii',errors='strict')
    for line in clocOutput:
      if line.startswith("SUM:"):
        currentLineContents = re.split(r'\s{2,}', currentLine)
        #print "items in line"
        commentCount = int(currentLineContents[3])
        sourceCount = int(currentLineContents[4])
        commitList.append((commitHash,commentCount,sourceCount))
        if commentCount == commentCountForCommmit and sourceCount == sourceCountForCommit:
          matchingLines.append(count)
        count = count + 1
  subprocess.call(["git","reset","--hard",firstCommit])  
  return commitList

if __name__ == "__main__":
  main()    
