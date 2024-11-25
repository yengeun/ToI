from django.contrib import admin
from django.urls import path, include
from main.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', home, name='home'),  # 기본 경로를 home 뷰에 연결
]