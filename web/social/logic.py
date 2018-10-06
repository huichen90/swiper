from social.models import Swiped
from social.models import Friends


def like(user, stranger_id):
    '''喜欢'''
    # 标记为喜欢
    Swiped.swipe_right(user.id, stranger_id)

    # 检查对方是否喜欢过自己
    if Swiped.is_liked(stranger_id, user.id):
        Friends.be_friend(user.id, stranger_id)
        # TODO: 向添加好友的双方推送消息


def superlike(user, stranger_id):
    '''超级喜欢'''
    # TODO: 会员身份检查
    # TODO: 每日超级喜欢次数减一

    # 标记为超级喜欢
    Swiped.swipe_up(user.id, stranger_id)

    # 检查对方是否喜欢过自己
    if Swiped.is_liked(stranger_id, user.id):
        Friends.be_friend(user.id, stranger_id)
        # TODO: 向添加好友的双方推送消息


def dislike(user, stranger_id):
    '''不喜欢'''
    Swiped.swipe_left(user.id, stranger_id)


def rewind(user, stranger_id):
    '''反悔'''
    # TODO: 会员身份检查
    try:
        Swiped.objects.get(uid=user.id, sid=stranger_id).delete()
    except Swiped.DoesNotExist:
        pass


def stepup(user):
    '''超级曝光'''
    pass
