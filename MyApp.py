# -*- coding: utf-8 -*-

import time, datetime

from celery import Celery
from celery.contrib.methods import task_method

import config
from Scraping import Scraping

import pprint

##### logger
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
now_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y/%m/%d/ %H:%M:%S')
##### celery
# インスタンスは「celery」で！　違う変数名だと怒られる。
celery = Celery('MyApp')
celery.config_from_object(config)

##### Taskクラス
Task = celery.create_task_cls()
class MyScrapingTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.debug("on_failure %s\t\t%s\n" % ( now_str, pprint.pformat(args) ))
        
        cMyApp = MyApp()
        cMyApp.task_scrape.apply_async( (args[1],), countdown=900)
        
    def on_success(self, retval, task_id, args, kwargs):
        logger.debug("on_success %s\t\t%s\n" % ( now_str, 'SUCCESS' ))

##### MyAppクラス
class MyApp(object):
    
    #taskメソッド
    @celery.task(filter=task_method, base=MyScrapingTask)
    def task_scrape(self, url):
        #titleタグ取得の関数
        def getTitle_cl(cPyQuery):
            title = cPyQuery('title').text()
            return title
        
        try:
            cScraping = Scraping()
            title = cScraping.scrape('http://www.yahoo.co.jp', getTitle_cl)
            
            if title == None or title == '':
                raise Exception
            
            logger.info("task_scrape %s\t\t%s\n" % ( now_str, title ))
            
        except Exception as exc:
            raise exc #on_failure
        
            

######
## 確認用
if __name__ == '__main__':
    print logger.__class__
    cMyApp = MyApp()
    cMyApp.task_scrape( 'http://www.yahoo.co.jp/')


