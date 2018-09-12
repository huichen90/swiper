from redis import Redis
from django.conf import settings

# 创建全局 Redis 连接
rds = Redis(**settings.REDIS)
