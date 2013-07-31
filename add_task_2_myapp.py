# -*- coding: utf-8 -*-
import sys
from MyApp import MyApp


## デフォルト値
target_url = 'http://www.yahoo.co.jp/'
countdown = 60

## 引数の取得
argvs = sys.argv
argc = len(argvs)
           
if (argc == 3):
    target_url = argvs[1]
    if argvs[2].isdigit():
        countdown = int( argvs[2] )
        
######
## 実行
if __name__ == '__main__':
    cMyApp = MyApp()
    cAsyncResult = cMyApp.task_scrape.apply_async( (target_url,), countdown=60)
    print "task_id:%s" % (cAsyncResult.id)
    
