from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    # 탄소 계산기
    path(' ', views.calculate_view, name='calculate'),
]
