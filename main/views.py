from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(request):
    return render(request, "Библиотека.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("И кто только это придумал?")

def third(request):
    return HttpResponse("Забыла, что хотела написать(((")