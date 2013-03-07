from django.contrib.auth.signals import user_logged_in
from django.contrib import messages


def welcome_user(sender, user, request, **kwargs):
	messages.success(request, 'Welcome %s' % user.get_full_name())


user_logged_in.connect(welcome_user)