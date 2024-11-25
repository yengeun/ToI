from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  # 사용자 이름 (유니크)
    email = models.EmailField(unique=True)  # 이메일 (유니크)
    password = models.CharField(max_length=128)  # 비밀번호 (해시 형태로 저장)
    created_at = models.DateTimeField(auto_now_add=True)  # 계정 생성 날짜

    def __str__(self):
        return self.username
