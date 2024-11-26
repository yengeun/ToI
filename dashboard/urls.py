from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # 메인
    path('', views.dashboard_view, name='main'),   # dashboard
    path('co2/', views.co2_view, name='co2'),  # co2
]
