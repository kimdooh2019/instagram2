from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    img_profile = models.ImageField('프로필이미지', blank=True, upload_to='uuuu')
    name = models.CharField('name', max_length=100)