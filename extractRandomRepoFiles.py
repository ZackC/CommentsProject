#!/usr/bin/python

#This file randomly extracts filesToExtract files from reposToExtractFrom repostories in a directory. The files are copied to a folder with the same name as the repository they came from.

import os
import random
import sys
import shutil

repoCountToExtractFrom = 10
fileCountToExtract = 10

def main(argv=None):
  if len(argv) != 2 or not os.path.isdir(argv[1]):
    print "an output directory is required.\nUsage: ./extractRandomRepoFiles.py someDir"
  else:
    outputParentDir = argv[1]
    currentDirContents = os.listdir('.')
    originalPath = os.getcwd()
    immediateChildDirectories = [x for x in currentDirContents if os.path.isdir(x)]
    childDirectoryCount = len(immediateChildDirectories)
    selectedDirs = random.sample(immediateChildDirectories, repoCountToExtractFrom)
    for aDir in selectedDirs:
      outputFolder = os.path.join(outputParentDir,aDir)
      os.makedirs(outputFolder)
      currentDir = os.path.join(originalPath,aDir)
      if not os.path.isdir(argv[1]):
        print "%s is not a path!\n" % currentDir
        sys.exit("")
      os.chdir(currentDir)
      fileListInRepo = []
      for (dirpath, dirnames, filenames) in os.walk(currentDir):
        filenames = [os.path.join(dirpath,theFile) for theFile in filenames]
        fileListInRepo.extend(filenames)
      fileListInRepo = [x for x in fileListInRepo if "." in x and not x.endswith(".txt") and not x.endswith(".jar")]
      selectedFiles = random.sample(fileListInRepo,fileCountToExtract)
      for aFile in selectedFiles:
        fileBasename = os.path.basename(aFile)
        fileDestination = os.path.join(outputFolder,fileBasename)
        shutil.copyfile(aFile,fileDestination)

if __name__ == "__main__":
  main(sys.argv)
