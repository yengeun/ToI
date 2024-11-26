from django.shortcuts import render
from django.http import JsonResponse

def calculate_view(request):
    if request.method == 'POST':
        co2_value = float(request.POST.get('co2', 0))
        annual_emission = co2_value * 12
        return JsonResponse({'annual_emission': annual_emission})
    return render(request, 'calculator/cal.html')