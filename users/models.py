from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    id_telegramm = models.IntegerField(null=True, blank=True, name='id_telegramm')
    image = models.ImageField(upload_to='users_image', blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, name='rating')
    open_profile = models.BooleanField(default=True, name='open_profile')
    pro_profile = models.BooleanField(default=False, name='pro_profile')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'{self.username}'
