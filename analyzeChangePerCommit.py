#!/usr/bin/python

#This file counts the average code and comment count repositories at different commits

def main(argv=None):
  currentDirContents = os.listdir('.')
  totalCommitList = []
  for dir in currentDirContents:
    if os.path.isdir(dir):
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
      for idx, commentCount, sourceCount in enumerate(reversed(currentRepoList)):
        if idx < len(totalCommitList):
          oldTotals = totalCommitList[idx]
          newCommentTotal = commentCount + oldTotals[0]
          newSourceTotal = soruceCount + oldTotals[1]
          newRepoCount = 1 + oldTotals[2]
          totalCommitList[idx] = (newCommentTotal,newSourceTotal,newRepoCount)
        else:
          totalCommitList.append((commentCount,sourceCount,1))
   for commentCount,sourceCount, repoCount in totalCommitList:
     print "%d, %d, %d, %.3f, %.3f" % (commentCount,sourceCount,repoCount,float(commentCount/repoCount),float(sourceCount/repoCount))
      
  
if __name__ == "__main__":
  main()
