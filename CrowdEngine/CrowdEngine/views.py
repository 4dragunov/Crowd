from django.shortcuts import redirect, render

def redirect_crowd(request):
    data = 123
    return render(request, 'main.html', context={'data': data})
