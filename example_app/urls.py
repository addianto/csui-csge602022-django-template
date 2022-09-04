from django.urls import path
from example_app.views import index, hello

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('hello', hello, name='hello'),
]