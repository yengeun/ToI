from django.contrib import admin
from django.urls import path
from main import views # main앱의 views함수를 사용하기 위해 불러옵니다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showmain), # 아무것도 입력안한 경로에 main앱의 views.py의 showmain함수를 연결합니다.
]