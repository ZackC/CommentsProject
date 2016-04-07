#!/usr/bin/python

#This script analyzes how source code lines, comment lines, and the relationship between the two change between each commit.

import sys
import re
import os
import subprocess
import traceback

minChange=0.50

def main(argv=None):
  if len(sys.argv) != 2:
    print "Usage: file_to_read_from"
    print "len: ",len(sys.argv)
  else:
    fin = open(sys.argv[1],'r')
    foundCount = False
    commitName="not set"
    previousCommitName = "not set"
    commitIsCorrect=False
    containsDigitPattern = re.compile(".*\d+.*")
    containsLetterPattern = re.compile(".*[A-Za-z]+.*")
    for line in fin:
      try:
        if line.startswith("SUM:") and commitIsCorrect:
          lineItems = line.split()
          #print "items in line"
          count=0
          oldCommentCount = int(lineItems[3])
          oldSourceLines = int(lineItems[4])
          if foundCount:
            '''if sourceLines != 0 and oldSourceLines != 0:
              oldRatio = float(oldCommentCount)/float(oldSourceLines)
              newRatio = float(commentCount)/float(sourceLines)
              relativeChange = abs(newRatio-oldRatio)
              if relativeChange > minChange:
                print "change in: "+os.getcwd()+"/"+sys.argv[1]
                print "old comment count: "+str(oldCommentCount)+", old source count: "+str(oldSourceLines)+",   old ratio: "+str(oldRatio)
                print "new comment count: "+str(commentCount)+", new source count: "+str(sourceLines)+", new ratio: "+str(newRatio)
                print "total change: "+str(relativeChange)
                print "============================"
              else:
                print "total change: "+str(relativeChange)
                print "============================"'''
            if oldSourceLines != 0 and oldCommentCount != 0:
              commentRatio = float(commentCount)/float(oldCommentCount)
              sourceRatio = float(sourceLines)/float(oldSourceLines)
              #relativeChange = abs(commentRatio-sourceRatio)
              relativeChange = commentRatio - sourceRatio
              diffResult=subprocess.check_output(["git","diff",previousCommitName,commitName])
              fout=open("gitDiffResult.txt",'w')
              fout.write(diffResult)
              fout.close()
              licenseLineResult=subprocess.check_output(["python","../../countLicenseLines.py","gitDiffResult.txt"])
              licenseLineResult=licenseLineResult.rstrip()
              colonIndex=licenseLineResult.find(":")
              licenseLineCount=licenseLineResult[colonIndex+1:len(licenseLineResult)]
              licenseLineCount=int(licenseLineCount)
              newFileResult=subprocess.check_output(["python","../../countCommentsInNewFiles.py","gitDiffResult.txt"])
              newFileResult=newFileResult.rstrip();
              colonIndex=newFileResult.find("L")
              newFileCommentCount=newFileResult[colonIndex+1:len(newFileResult)]
              newFileCommentCount=int(newFileCommentCount)
              #TODO: by subtracting licenseLineCount and newFileCommentCount you 
              #are substracting double for license comments in new files
              #this is fine for now with the initial pass of the data but you
              #should improve this later
              if relativeChange > minChange and commentCount - oldCommentCount - licenseLineCount - newFileCommentCount > 50:
                print "change in: "+os.getcwd()+"/"+sys.argv[1]
                print "new commit: %s" % (commitName)
                print "old commit: %s" % (previousCommitName)
                print "old comment count: "+str(oldCommentCount)+", new comment count: "+str(commentCount)+", old ratio: "+str(commentRatio)
                print "old source count: "+str(oldSourceLines)+", new source count: "+str(sourceLines)+", new ratio: "+str(sourceRatio)
                print "total change: "+str(relativeChange)
                print "============================"
            #else:
              #print "total change: "+str(relativeChange)
              #print "============================"
          else:
            foundCount = True
          commentCount = oldCommentCount
          sourceLines = oldSourceLines
        else:
          if line.startswith("current commit: "):
            lineItems = line.split()
            if lineItems[2].isalnum() and re.match(containsDigitPattern, lineItems[2]) != None and re.match(containsLetterPattern, lineItems[2]) != None:
              commitName = previousCommitName
              previousCommitName = lineItems[2]
              commitIsCorrect=True
            else:
              commitIsCorrect=False
      except:
        traceback.print_exc()
        print "error occured in the script!!"
        #sys.exit(1)


if __name__ == "__main__":
  main()    


