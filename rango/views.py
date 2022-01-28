from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
        }
    return render(request, 'rango/index.html', context=context_dict)
    # return HttpResponse("<a href='/rango/about'>Rango</a> says hey there partner!")

def about(request):
    context_dict = {
        'boldmessage': 'This tutorial has been put together by Alex'
        }
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("<a href='/rango/'>Rango</a> says here is the about page.")