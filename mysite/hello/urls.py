from django.urls import path

from . import views

app_name = 'hello'

urlpatterns = [

    #ex: http://127.0.0.1:8000/hello/
    path('', views.hello, name='hello'),

    #ex: http://127.0.0.1:8000/hello/cookie
    path('cookie', views.cookie),
]