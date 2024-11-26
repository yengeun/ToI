from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError


def signin_view(request):   # 로그인&회원가입
    return render(request, 'accounts/signin.html')

def login_view(request):    # 로그인
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:main')
        else:
            messages.error(request, '아이디나 패스워드가 일치하지 않습니다.')
    return render(request, 'accounts/login.html')

def signup_view(request):   # 회원가입
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordck = request.POST.get('passwordck')
        company = request.POST.get('company')
        # 비밀번호 확인
        if password != passwordck:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return render(request, 'accounts/signup.html')
        # 이메일 중복 확인
        if User.objects.filter(username=email).exists():
            messages.error(request, '이미 존재하는 이메일입니다.')
            return render(request, 'accounts/signup.html')
        # 사용자 생성
        try:
            user = User.objects.create_user(
                username=email,  # 이메일을 사용자 이름으로 사용
                email=email,
                password=password,
            )
            # 소속 기업 정보 저장
            user.profile.company = company
            user.profile.save()
            messages.success(request, '회원가입에 성공하셨습니다! 로그인을 해주세요.')
            return redirect('accounts:login')  # 회원가입 성공 시 로그인 페이지로 이동
        except Exception as e:
            messages.error(request, f'오류가 발생했습니다: {e}')
            return render(request, 'accounts/signup.html')
    return render(request, 'accounts/signup.html')

def logout_view(request):   # 로그아웃
    logout(request)
    return redirect('accounts:login')  # 로그아웃 후 로그인 페이지로 이동
