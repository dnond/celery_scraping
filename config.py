# -*- coding: utf-8 -*-

# サーバーのTimeZoneを使用する
CELERY_ENABLE_UTC = False

################
## Broker settings
BROKER_URL = 'redis://localhost:6379/0'

################
## Redis設定

# 結果受け取り接続設定
CELERY_RESULT_BACKEND = 'redis'

#  REDISのコネクションプール数。（結果の受け渡しも込み）
CELERY_REDIS_MAX_CONNECTIONS = 10

################
## BROKER接続設定

# BROKERの接続タイムアウト。Default: 4
BROKER_CONNECTION_TIMEOUT = 1

# BROKERの再接続回数。Default: 100
BROKER_CONNECTION_MAX_RETRIES = 3


#####################
## エラーメール設定

# エラー時にADMINSにメールを送るか。Default: Disabled
CELERY_SEND_TASK_ERROR_EMAILS = True 

# エラーメールの受信者。('名前','メルアド')タプルのリスト
ADMINS = [('me', 'huga@hogehoge.com'), ]

# エラーメールの送信先が複数の場合
# ADMINS = [('me', 'huga@hogehoge.com'), ('you', 'hugahuga@hogehoge.com')]

# エラーメールの送信元アドレス
SERVER_EMAIL = 'admin@celery.localnet'

# エラーメールの送信サーバー。Default : “localhost”.
EMAIL_HOST = 'localhost'

# エラーメールの送信サーバーのユーザー名
#EMAIL_HOST_USER = 'me'

# エラーメールの送信サーバーのパスワード
#EMAIL_HOST_PASSWORD = 'password'

# エラーメールの送信サーバーのポート番号。Default : 25.
EMAIL_PORT = 25

#EMAIL_USE_SSL 
#EMAIL_USE_TLS
