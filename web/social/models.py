from django.db import models
from django.db.models import Q

from common import rds


class SetModel(models.Model):
    def add_member(self,  stranger_id):

    def members(cls):
        return self.__class__.objects.filter(uid=self.uid)

    def load_to_redis(self):
        pass


class Swiped(models.Model):
    '''滑过的记录'''
    MARK = (
        ('like', '喜欢'),
        ('superlike', '喜欢'),
        ('dislike', '喜欢'),
    )
    uid = models.IntegerField()
    sid = models.IntegerField()
    mark = models.CharField(max_length=16, choices=MARK)

    @classmethod
    def is_liked(cls, uid, sid):
        condition = Q(mark='like') | Q(mark='superlike')
        if cls.objects.filter(condition, uid=uid, sid=sid).exists():
            return True
        return False

    @classmethod
    def swipe_right(cls, uid, sid):
        defaults = {'mark': 'like'}
        cls.objects.update_or_create(uid=user.id, sid=stranger_id, defaults=defaults)

    @classmethod
    def swipe_up(cls, uid, sid):
        defaults = {'mark': 'superlike'}
        cls.objects.update_or_create(uid=user.id, sid=stranger_id, defaults=defaults)

    @classmethod
    def swipe_left(cls, uid, sid):
        defaults = {'mark': 'dislike'}
        cls.objects.update_or_create(uid=user.id, sid=stranger_id, defaults=defaults)


class Friends(models.Model):
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def is_friends(cls, uid1, uid2):
        '''检查是否是朋友关系'''
        uid1, uid2 = sorted([uid1, uid2])
        return cls.objects.filter(uid1=uid1, uid2=uid2).exists()

    @classmethod
    def be_friend(cls, uid1, uid2):
        '''建立好友关系'''
        uid1, uid2 = sorted([uid1, uid2])
        cls.objects.get_or_create(uid1=uid1, uid2=uid2)

    @classmethod
    def break_off(cls, uid1, uid2):
        '''断绝好友关系'''
        uid1, uid2 = sorted([uid1, uid2])
        try:
            cls.objects.get(uid1=uid1, uid2=uid2).delete()
        except cls.DoesNotExists:
            pass

        condition = Q(uid=uid1, sid=uid2) | Q(uid=uid2, sid=uid1)
        Swiped.objects.filter(condition).update(mark='dislike')
