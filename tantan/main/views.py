from django.shortcuts import render

def dashboard_view(request):
    # 임의 데이터
    data = {
        'labels': ['SK', 'LG', '성신', 'Windows', 'Other'],
        'values': [10000, 20000, 15000, 30000, 12000],
    }
    return render(request, 'main/main.html', {'data': data})
