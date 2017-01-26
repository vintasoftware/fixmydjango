from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{user.first_name} {user.last_name}'.format(user=self)

    def get_short_name(self):
        return self.first_name
