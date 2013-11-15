from django.shortcuts import render


def handle404(request):
    return render(request, 'mysite/handle404.html')


def handle500(request):
    return render(request, 'mysite/handle500.html')