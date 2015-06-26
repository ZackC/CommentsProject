#!/usr/bin/python

#This file reads the directory and counts which languages are used in projects along with the expected language: Java.  It also counts how many total files are used in each language.

import os
import re

def main(argv=None):
  currentDirContents = os.listdir('.')
  languageDict = {}
  for dir in currentDirContents:
   if os.path.isdir(dir):
     fopen = open(dir+"/lineCount.txt")
     for line in fopen:
       if "Language" in line:
         fopen.next()
         currentLine = fopen.next()
         while "-----" not in currentLine:
           print currentLine
           currentLine = currentLine.strip()
           currentLineContents = re.split(r'\s{2,}', currentLine)
           languageName = currentLineContents[0]
           fileCount = int(currentLineContents[1])
           if languageName in languageDict:
            oldContents = languageDict[languageName]
            newRepositoryCount = 1 + oldContents[0]
            newFileCount = fileCount + oldContents[1]
            languageDict[languageName] = (newRepositoryCount, newFileCount)
           else:
             languageDict[languageName] = (1,fileCount)
           currentLine = fopen.next()
         break
  for lang,currentCounts in languageDict.items():
    print  " %s : %d repositories and %d files" % (lang,currentCounts[0],currentCounts[1])

if __name__ == "__main__":
  main()
