from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def control(request):
    return render(request, 'control.html')

def logs(request):
    return render(request, 'logs.html')

def about(request):
    return render(request, 'about.html')
