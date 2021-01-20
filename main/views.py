from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "Библиотека.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("И кто только это придумал?")

def third(request):
    return HttpResponse("Забыла, что хотела написать(((")