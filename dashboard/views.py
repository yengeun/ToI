from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    # 임의 데이터
    data = {
        'labels': ['SK', 'LG', '성신', 'Windows', 'Other'],
        'values': [10000, 20000, 15000, 30000, 12000],
    }
    return render(request, 'main/main.html', {'data': data})

@login_required
def co2_view(request):
    return render(request, 'main/co2.html')
