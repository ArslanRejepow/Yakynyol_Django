from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

VELAYAT_CHOICES = (
    ('Balkan','balkan'),
    ('Ahal', 'ahal'),
    ('Mary','mary'),
    ('Lebap', 'lebap'),
    ('Dashoguz','dashoguz'),
    ('Ashgabat','ashgabat'),
)

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    mobile_no = models.CharField(max_length=15)
    velayat = models.CharField(max_length=10, choices=VELAYAT_CHOICES,)
    isActive = models.BooleanField(default = True)
    isComment = models.BooleanField(default = True)

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'