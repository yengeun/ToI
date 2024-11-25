from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def login_view(request):    # 로그인
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('main:dashboard')
    return render(request, 'accounts/login.html')

def signup_view(request):   # 회원가입
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        company = request.POST['group']
        user = User.objects.create_user(username=email, password=password)  # Django 기본 유저 모델로 계정 생성
        user.save() # DB에 저장
        return redirect('accounts:login')
    return render(request, 'accounts/signup.html')

def logout_view(request):   # 로그아웃
    logout(request)
    return redirect('accounts:login')  # 로그아웃 후 로그인 페이지로 이동
