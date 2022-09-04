from django.http.request import HttpRequest, QueryDict
from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def hello(request: HttpRequest):
    payload: QueryDict = request.GET

    if 'name' in payload:
        return HttpResponse(payload['name'])
    else:
        return HttpResponse('anonymous')