# coding: utf-8

from django.test import TestCase, Client

from model_mommy import mommy


class TestConfig(object):

    def setUp(self):

        self._user_password = '123456'
        self.user = mommy.prepare('users.User', email='user@email.com')
        self.user.set_password(self._user_password)
        self.user.save()

        self.staff_user = mommy.prepare('users.User', email='staff@email.com', is_staff=True)
        self.staff_user.set_password(self._user_password)
        self.staff_user.save()

        self.superuser = mommy.prepare('users.User', email='superuser@email.com', is_staff=True,
                                       is_superuser=True)
        self.superuser.set_password(self._user_password)
        self.superuser.save()


class FixMyDjangoTestCase(TestConfig, TestCase):

    def setUp(self):
        super(FixMyDjangoTestCase, self).setUp()

        self.auth_client = Client()
        self.auth_client.login(email=self.user.email, password=self._user_password)

        self.staff_client = Client()
        self.staff_client.login(email=self.staff_user.email, password=self._user_password)

        self.superuser_client = Client()
        self.superuser_client.login(email=self.superuser.email, password=self._user_password)
