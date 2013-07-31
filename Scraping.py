# -*- coding: utf-8 -*-

from pyquery import PyQuery

class Scraping(object):
    def scrape(self, url, callback=None):
        cPyQuery = PyQuery(url, parser='html')
        
        return callback(cPyQuery)


######
## 実行例
if __name__ == '__main__':
    cScraping = Scraping()
    
    def getTitle_cl(cPyQuery):
        title = cPyQuery('title').text()
        return title
         
    print cScraping.scrape('http://www.yahoo.co.jp', getTitle_cl)