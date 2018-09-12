from user.models import User


def like(user, stranger_id):
    stranger = User.objects.get(pk=stranger_id)


def superlike(user, stranger_id):
    stranger = User.objects.get(pk=stranger_id)


def dislike(user, stranger_id):
    stranger = User.objects.get(pk=stranger_id)


def rewind(user, stranger_id):
    stranger = User.objects.get(pk=stranger_id)


def stepup(user, stranger_id):
    stranger = User.objects.get(pk=stranger_id)
