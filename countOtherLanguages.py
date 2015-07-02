#!/usr/bin/python

#This file reads the directory and counts which languages are used in projects along with the expected language: Java.  It also counts how many total files are used in each language. If a second parameter is included, then the program will output the language count of the first commit instead of the last commit.

from operator import itemgetter

import os
import re
import sys

def main(argv=None):
  currentDirContents = os.listdir('.')
  languageDict = {}
  for dir in currentDirContents:
   if os.path.isdir(dir):
     fopen = open(dir+"/lineCount.txt")
     lastCommitLineCount = 0 #number of lines in the file to skip
     if len(argv)>1:
       for lineCount,line in enumerate(fopen):
         if "Language" in line:
           lastCommitLineCount = lineCount - 1
       fopen.seek(0)
     for lineCount,line in enumerate(fopen):
       if lineCount > lastCommitLineCount and "Language" in line:
         fopen.next()
         currentLine = fopen.next()
         while "-----" not in currentLine:
           #print currentLine
           currentLine = currentLine.strip()
           currentLineContents = re.split(r'\s{2,}', currentLine)
           languageName = currentLineContents[0]
           fileCount = int(currentLineContents[1])
           commentLineCount = int(currentLineContents[3])
           sourceLineCount = int(currentLineContents[4])
           if languageName in languageDict:
            oldContents = languageDict[languageName]
            newRepositoryCount = 1 + oldContents[0]
            newFileCount = fileCount + oldContents[1]
            newCommentLineCount = commentLineCount + oldContents[2]
            newSourceLineCount = sourceLineCount + oldContents[3]
            languageDict[languageName] = (newRepositoryCount, newFileCount, newCommentLineCount, newSourceLineCount)
           else:
             languageDict[languageName] = (1,fileCount,commentLineCount,sourceLineCount)
           currentLine = fopen.next()
         break
  for lang,currentCounts in sorted(languageDict.items(), key=itemgetter(1), reverse=True):
    print  " %s : %d repositories and %d files; %d comment lines and %d source code lines" % (lang,currentCounts[0],currentCounts[1],currentCounts[2],currentCounts[3])

if __name__ == "__main__":
  main(sys.argv)
