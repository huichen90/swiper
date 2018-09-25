_redis_url = 'redis://127.0.0.1:6379/0'

BROKER_URL = _redis_url
BROKER_POOL_LIMIT = 1000 # Borker 连接池，默认是10

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']

CELERY_TASK_SERIALIZER = 'pickle'
CELERY_TASK_RESULT_EXPIRES = 3600  # 任务过期时间

CELERY_RESULT_BACKEND = _redis_url
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_MAX_CACHED_RESULTS = 10000  # 任务结果最大缓存数量
