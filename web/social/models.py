from django.db import models

from common import rds


class SetModel(models.Model):
    def add_member(self,  stranger_id):

    def members(cls):
        return self.__class__.objects.filter(uid=self.uid)

    def load_to_redis(self):
        rds


class Liked(models.Model):
    uid = models.IntegerField()
    sid = models.IntegerField()


class SuperLiked(models.Model):
    uid = models.IntegerField()
    sid = models.IntegerField()


class Disliked(models.Model):
    uid = models.IntegerField()
    sid = models.IntegerField()
