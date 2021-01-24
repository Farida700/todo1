from django.shortcuts import render, HttpResponse, redirect
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

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text = text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

# def unmark_todo(request, id):
#     todo = ToDo.objects.get(id=id)
#     todo.is_favorite = False
#     todo.save()
#     return redirect(test)

def closed_todo(request,  id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)
