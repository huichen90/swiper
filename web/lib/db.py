from django.db import models

from lib.cache import rds
from common.keys import MODEL_KEY


def get(cls, *args, **kwargs):
    '''数据优先从缓存获取, 缓存取不到再从数据库获取'''
    # 创建 key
    pk = kwargs.get('pk') or kwargs.get('id')
    key = MODEL_KEY % (cls.__name__, pk)

    # 从缓存获取
    if pk is not None:
        model_obj = rds.get(key)
        if isinstance(model_obj, cls):
            return model_obj

    # 缓存里没有，直接从数据库获取，同时写入缓存
    model_obj = cls.objects.get(*args, **kwargs)
    rds.set(key, model_obj)


def get_or_create(cls, *args, **kwargs):
    # 创建 key
    pk = kwargs.get('pk') or kwargs.get('id')
    key = MODEL_KEY % (cls.__name__, pk)

    # 从缓存获取
    if pk is not None:
        model_obj = rds.get(key)
        if isinstance(model_obj, cls):
            return model_obj

    # 执行原生方法，并添加缓存
    model_obj = cls.objects.get_or_create(*args, **kwargs)
    rds.set(key, model_obj)


def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    '''存入数据库后，同时写入缓存'''
    ori_save = models.base.Model.save
    ori_save(self, force_insert, force_update, using, update_fields)

    # 添加缓存
    key = MODEL_KEY % (self.__class__.__name__, self.pk)
    rds.set(key, self)


def patch_model():
    '''动态更新 Model 的 save 和 get 方法'''
    # 动态添加一个类方法 get
    models.Model.get = classmethod(get)
    models.Model.get_or_create = classmethod(get_or_create)

    # 修改 save
    ori_save = models.base.Model.save
    models.Model.save = save

patch_model()
