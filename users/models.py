from django.contrib.auth.models import AbstractUser
# from django.db import models as m

class User(AbstractUser):
    pass

    class Meta:
        # db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def str(self):
        return self.username
