#!/usr/bin/python

#This script analyzes how source code lines, comment lines, and the relationship between the two change between each commit.

import sys
import re
import os

minChange=0.50

def main(argv=None):
  if len(sys.argv) != 2:
    print "Usage: file_to_read_from"
    print "len: ",len(sys.argv)
  else:
    fin = open(sys.argv[1],'r')
    foundCount = False
    for line in fin:
      if line.startswith("SUM:"):
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
              print "old comment count: "+str(oldCommentCount)+", old source count: "+str(oldSourceLines)+", old ratio: "+str(oldRatio)
              print "new comment count: "+str(commentCount)+", new source count: "+str(sourceLines)+", new ratio: "+str(newRatio)
              print "total change: "+str(relativeChange)
              print "============================"
            else:
              print "total change: "+str(relativeChange)
              print "============================"'''
          if oldSourceLines != 0 and oldCommentCount != 0:
            commentRatio = float(commentCount)/float(oldCommentCount)
            sourceRatio = float(sourceLines)/float(oldSourceLines)
            relativeChange = abs(commentRatio-sourceRatio)
            if relativeChange > minChange:
              print "change in: "+os.getcwd()+"/"+sys.argv[1]
              print "old comment count: "+str(oldCommentCount)+", new comment count: "+str(commentCount)+", old ratio: "+str(commentRatio)
              print "new comment count: "+str(oldSourceLines)+", new source count: "+str(sourceLines)+", new ratio: "+str(sourceRatio)
              print "total change: "+str(relativeChange)
              print "============================"
            #else:
              #print "total change: "+str(relativeChange)
              #print "============================"
        else:
          foundCount = True
        commentCount = oldCommentCount
        sourceLines = oldSourceLines
        


if __name__ == "__main__":
  main()    


