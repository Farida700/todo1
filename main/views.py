from django.shortcuts import render, HttpResponse


def homepage(request):
    return HttpResponse("Привет мир!")

def test(request):
    return render(request, "test.html" )
