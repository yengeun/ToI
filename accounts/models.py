from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):    #소속기업
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    company = models.CharField(max_length=255, blank=True, null=True)  # 소속 기업

    def __str__(self):
        return f'{self.user.username} - {self.company}'