#this file counts the number of license comments line in a git diff

import sys
import re


def main(argv):
  if len(argv) != 2:
    print "error: unexpected number of arguments; please include the file to read from"
  else:
    fin = open(argv[1],'r')
    inNewOrDeletedFile = False
    commentStartLine = -1
    commentEndLine = -1
    totalLicenseCount = 0 
    for lineCount,line in enumerate(fin):
      startOfComment = line.find("/*")
      if startOfComment != -1:
        commentStartLine = lineCount
      else:
        endOfComment = line.find("*/")
        if endOfComment != -1 and startOfComment != -1:
          commentEndLine = lineCount
          if inNewOrDeletedFile:
            totalLicenseCount=commentEndLine-commentStartLine+1+totalLicenseCount
          commentStartLine=-1
          commentEndLine=-1                
        else:
          licenseSearchResult= line.find('/dev/null',line)
          if licenseSearchResult != None:
            inNewOrDeletedFile = True
          else:
            singleLineComment = line.find('//',line)
            if singleLineComment != None:
              totalLicenseCount = totalLicenseCount + 1 
            else:
              newFile = line.find('dif --git',line)  
              if newFile != None:
                inNewOrDeletedFile = False
    print "total license line count: %d" % (totalLicenseCount)


if __name__ == "__main__":
  main(sys.argv)
