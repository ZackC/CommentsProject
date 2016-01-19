#!/usr/bin/python

#This file counts the average code and comment count repositories at different commits in repoCountToExtractFrom number of repos.

import os
import sys
import random
import matplotlib.pyplot as plt

def main(argv=None):
  currentDirContents = os.listdir('.')
  originalPath = os.getcwd()
  for aFile in currentDirContents:
    commentCountList = []
    sourceCountList = []
    #print aFile
    fout = open(aFile,'r')
    
    for line in fout:
      #print line
      lineContents = line.split(", ")
      #print lineContents
      commentCountList.append(lineContents[0])
      sourceCountList.append(lineContents[1])
    plt.plot(commentCountList)
    plt.plot(sourceCountList)
    plt.ylabel("Lines of Code")
    plt.xlabel("Commit Number")
    plt.title(aFile)
    plt.show(block=False)
    raw_input("Press Enter to continue...")
    plt.clf()
    fout.close()

if __name__ == "__main__":
  main(sys.argv)
