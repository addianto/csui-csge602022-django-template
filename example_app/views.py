from django.http.response import HttpResponse
from django.shortcuts import render
from random import choice

TITLES = ['Anonymous', 'Doctor', 'Manager', 'Producer', 'Student', 'Teacher',
          'Trainer', 'Traveler']

def index(request):
    return render(request, 'index.html')

def hello(request):

    if len(request.GET) == 0:
        return render(request, 'hello.html', { 'visitor_name': choice(TITLES) })
    
    if 'name' in request.GET:
        return render(request, 'hello.html', { 'visitor_name': request.GET['name'] })
    else:
        return HttpResponse(status=400)