"""
URL configuration for tantan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='accounts:signin', permanent=False)),  # 기본 URL을 로그인 페이지로 리다이렉트
    path('accounts/', include('accounts.urls')),  # accounts
    path('main/', include('main.urls')),          # main
    path('calculator/', include('calculator.urls')),  # calculator
    path('', include('main.urls')),  # 기본 경로를 메인 대시보드로 연결
]