from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # 메인
    path('', views.dashboard_view, name='main'),   # main
    path('co2/', views.co2_view, name='co2'),  # co2
]
