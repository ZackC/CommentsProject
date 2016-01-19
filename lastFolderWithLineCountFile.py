import os
import os.path


def main(argv=None):
  #originalPath = os.getcwd()
  subDirectories = nex(os.walk(','))[1]
  for directory in subDirectories:
    fileString = directory+os.sep+"lineCountWithCommits.txt"
    print "checking path: %s" % fileString
    if(not os.path.exists(fileString)):
      print "file does not exist for %s" % directory
      break
  

if __name__=="__main__":
  main()

