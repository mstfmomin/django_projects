from django.urls import path
from . import views

app_name = 'autos'

urlpatterns = [

    #ex: http://127.0.0.1:8000/autos/
    path('', views.MainView.as_view(), name='all'),

    #ex: http://127.0.0.1:8000/autos/lookup
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    
    #ex: http://127.0.0.1:8000/autos/lookup/create
    path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),

    #ex: http://127.0.0.1:8000/autos/main/create
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),

    #ex: http://127.0.0.1:8000/autos/lookup/3/update
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),

    #ex: http://127.0.0.1:8000/autos/main/3/update
    path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),

    #ex: http://127.0.0.1:8000/autos/lookup/3/delete
    path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),

    path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),

]