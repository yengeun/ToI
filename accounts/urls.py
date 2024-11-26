from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),     # 로그인
    path('signup/', views.signup_view, name='signup'),  # 회원가입
    path('logout/', views.logout_view, name='logout'),  # 로그아웃
    path('signin/', views.signin_view, name='signin'),  # 로그인&회원가입
]
