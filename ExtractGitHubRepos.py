#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib2

startingUrl = "https://github.com/search?l=Java&p=1&q=language%3AJava&ref=advsearch&type=Repositories&utf8=%E2%9C%93"
githubString="https://github.com"

def main():
  soup = openPage(startingUrl)
  for x in range(50):
    extractRepos(soup)
    nextUrl = getNextUrl(soup)
    soup = openPage(nextUrl)
  
  #print(nextUrl)
  #print(soup.prettify())

def extractRepos(soup):
  repoListElement = soup.find(class_="repo-list js-repo-list")
  repoItems = repoListElement.find_all("li")
  for item in repoItems:
    repoUrl = githubString+unicode(item.h3.a["href"])
    repoSoup = openPage(repoUrl)
    repoGitLink = repoSoup.find(class_="clone-url open")
    finalRepoLink = repoGitLink.div.input["value"]
    print(finalRepoLink)



def openPage(urlString):
  htmlDoc = urllib2.urlopen(urlString)
  soup = BeautifulSoup(htmlDoc)
  return soup

def getNextUrl(soup):
  pageLinks = soup.find(class_="pagination")
  currentPage = pageLinks.find(class_="current")
  nextPageLink = currentPage.find_next_sibling("a")
  nextPageUrl = githubString+unicode(nextPageLink["href"])
  return nextPageUrl


if __name__ == "__main__":
  main()
