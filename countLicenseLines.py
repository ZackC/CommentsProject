#this file counts the number of license comments line in a git diff

import sys
import re


def main(argv):
  if len(argv) != 2:
    print "error: unexpected number of arguments; please include the file to read from"
  else:
    fin = open(argv[1],'r')
    inLicense = False
    commentStartLine = -1
    commentEndLine = -1
    totalLicenseCount = 0 
    for lineCount,line in enumerate(fin):
      startOfComment = line.find("/*")
      if startOfComment != -1:
        commentStartLine = lineCount
      else:
        endOfComment = line.find("*/")
        if endOfComment != -1:
          commentEndLine = lineCount
          if inLicense:
            if commentStartLine == -1:
              print "Error: comment start line was never set"
              sys.exit(1)
            else:
              totalLicenseCount=commentEndLine-commentStartLine+1+totalLicenseCount
          inLicense=False
          commentStartLine=-1
          commentEndLine=-1                
        else:
          licenseSearchResult= re.search('[Ll]icense',line)
          if licenseSearchResult != None:
            inLicense = True
    print "total license line count: %d" % (totalLicenseCount)


if __name__ == "__main__":
  main(sys.argv)
