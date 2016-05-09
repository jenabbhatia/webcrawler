import pymomgo
import requests
import re 
import lxml
'''def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return'''

def get_next_target(page):
    start_link=page.find('<a href=')
    if start_link == -1:
        return None,0
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    url=page[start_quote+1 : end_quote]
    return url,end_quote

#appending links to tocrawl
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
    
#tocrawl=list of all pages left to crawl
#crawled=pages which are crawled
def crawl_web(seed):
    tocrawl=[seed]
    crawled=[]
    while tocrawl:
        page=tocrawl.pop()
        if page not in crawled:
            union(tocrawl,get_all_links(page)
            crawled.append(page)
    return crawled    
    
#getting a list of url's
def get_all_links(page):
    links=[]
    while True:
        url,endpos=get_next_target(page)
        if url:
            links.append(url)
            page=page[endpos:]
        else:
            break
    return links    
user_agent = {'User-agent': 'Mozilla/5.0'}
url=list(sys.argv)[1]
r = requests.get(url, headers = user_agent)
html=r.text
soup = BeautifulSoup(html,"lxml")

c=crawl_web(soup)
for l in c:
    print l

    

    