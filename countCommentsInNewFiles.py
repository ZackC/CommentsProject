#this file counts the number of license comments line in a git diff

import sys
import re
import textwrap

def main(argv):
  if len(argv) != 2:
    print "error: unexpected number of arguments; please include the file to read from"
  else:
    fin = open(argv[1],'r')
    inNewOrDeletedFile = False
    commentStartLine = -1
    commentEndLine = -1
    commentCountInNewAndDeletedFiles = 0
    inComment=False
    for lineCount,line in enumerate(fin):
      line=line.rstrip()
      #print "%s" % (line)
      startOfComment = line.find("/*")
      if startOfComment != -1:
        commentStartLine = lineCount
       #print "found start of comment"
        inComment=True
      else:
        endOfComment = line.find("*/")
        if endOfComment != -1 and inComment:
          commentEndLine = lineCount
          #print "found end of comment"
          if inNewOrDeletedFile:
            #dedentedText=textwrap.dedent("""
            #                        !!!!!found end of comment when in a new
            #                        or deleted file with
            #                        size: %d""" %
            #                            (commentEndLine-commentStartLine+1)).strip()
            #print textwrap.fill(dedentedText,80)
            commentCountInNewAndDeletedFiles=commentEndLine-commentStartLine+1+commentCountInNewAndDeletedFiles
          commentStartLine=-1
          commentEndLine=-1
          inComment=False
        else:
          licenseSearchResult= line.find('/dev/null')
          if licenseSearchResult != -1:
            #print "found added or deleted file line"
            inNewOrDeletedFile = True
          else:
              '''TODO: remove false positives for websites in comments'''
              singleLineComment = line.find('//')
              if singleLineComment != -1:
              #print "!!!!!found a single line comment"
              if inNewOrDeletedFile:
                #print "found a single line comment not in a new or deleted file"
                commentCountInNewAndDeletedFiles = commentCountInNewAndDeletedFiles + 1
            else:
              newFile = line.find('dif --git')
              if newFile != -1:
                #print "found a new file diff"
                inNewOrDeletedFile = False
                print "total comment count in new and old files: %d" % (commentCountInNewAndDeletedFiles)


if __name__ == "__main__":
  main(sys.argv)
