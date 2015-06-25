#!/usr/bin/python

#This script counts the number of commits that have been processed and the total number of commits to process.  For some reason, the commit count is usually slightly higher than the processed count when all commits have been processed (something I should investigate further)

def main(argv=None):
  flog = open("logResult.txt",'r')
  fline = open("lineCount.txt",'r')
  commitCount = 0
  for line in flog:
    if "commit " in line:
      commitCount = commitCount + 1
  finishedCommits = 0    
  for line in fline:
    if "SUM" in line:
       finishedCommits = finishedCommits + 1
  print "number of commits in repo: "+str(commitCount)
  print "finished commits: "+str(finishedCommits)     

if __name__ == "__main__":
  main()
