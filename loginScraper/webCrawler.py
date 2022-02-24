from webLoader import WebLoader
import re


class WebCrawler:
    def __init__(self):
        self.studiengaengeLinks = set()
        self.inhalteLinks = set()

    def getStudiengaengeLinks(self, url):
        bs = WebLoader('https://www.fom.de/'+url).getBSObject()
        for link in bs.find_all('a', href=re.compile('studiengaenge/')):
            # for link in bs.find_all('a'):
            if 'href' in link.attrs:
                self.studiengaengeLinks.add(link.attrs['href'])
        return self.studiengaengeLinks

    def getInhalteLinks(self, url):
        bs = WebLoader('https://www.fom.de/'+url).getBSObject()
        for link in bs.find_all('a', href=re.compile('inhalte.html$')):
            if 'href' in link.attrs:
                self.inhalteLinks.add(link.attrs['href'])

    def getSemesterLinks(self, url):
        bs = WebLoader('https://campus.bildungscentrum.de/'+url).getBSObject()
        print(bs.text)