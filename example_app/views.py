from django.http.request import HttpRequest, QueryDict
from django.http.response import HttpResponse
from django.shortcuts import render

TITLES = ['Anonymous', 'Doctor', 'Manager', 'Producer', 'Teacher', 'Trainer',
          'Traveler']

def index(request):
    return render(request, 'index.html')

def hello(request: HttpRequest) -> HttpResponse:
    from random import choice

    if len(request.GET) == 0:
        return HttpResponse(choice(TITLES))
    
    if 'name' in request.GET:
        return HttpResponse(request.GET['name'])
    else:
        return HttpResponse(status=400)