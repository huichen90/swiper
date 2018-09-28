from datetime import date

from django.db import models
from django.utils.functional import cached_property


class User(models.Model):
    SEX = (
        ('Male', '男'),
        ('Female', '女'),
    )

    phonenum = models.CharField(max_length=16, unique=True)
    nickname = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=128)

    # user info
    sex = models.CharField(max_length=16, choices=SEX)
    birth_year = models.IntegerField(default=1990)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    location = models.CharField(max_length=32, verbose_name='常居地')

    @cached_property
    def age(self):
        '''年龄'''
        birthday = datetime.date(birth_year, birth_month, birth_day)
        return (date.today() - birthday).days // 365

    @cached_property
    def avatar(self):
        return Avatar.objects.get_or_create(id=self.id)[0]

    @cached_property
    def profile(self):
        return Profile.objects.get_or_create(id=self.id)[0]

    def to_dict(self):
        return {
            'uid': self.id,
            'nickname': self.nickname,
            'age': self.age,
            'sex': self.sex,
            'location': self.location,
            'avatars': list(self.avatar),
        }


class Avatar(models.Model):
    '''用户头像'''
    first = models.URLField()
    second = models.URLField()
    third = models.URLField()
    fourth = models.URLField()
    fifth = models.URLField()
    sixth = models.URLField()

    def __iter__(self):
        urls = [first, self.second, self.third,
                self.fourth, self.fifth, self.sixth]
        return filter(None, urls)  # 取出非空头像


class Profile(models.Model):
    SEX = (
        ('Male', '男性')
        ('Female', '女性')
        ('All', '不限'')
    )
    # 交友设置
    location = models.CharField(max_length=32, verbose_name='目标城市')
    min_distance = models.FloatField(default=1.0, verbose_name='最小查找范围')
    max_distance = models.FloatField(default=50.0, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50, verbose_name='最大交友年龄')
    dating_sex = models.CharField(max_length=16, choices=SEX, verbose_name='匹配的性别')
    # 其他设置
    vibration = models.BooleanField(default=True, verbose_name='开启震动')
    only_matche = models.BooleanField(default=False, verbose_name='不让为匹配的人看我的相册')
    auto_play = models.BooleanField(default=False, verbose_name='自动播放视频')
