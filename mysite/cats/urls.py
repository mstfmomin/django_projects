from django.urls import path
from . import views

app_name = 'cats'

urlpatterns = [

    #ex: http://127.0.0.1:8000/cats/
    path('', views.CatList.as_view(), name='all'),

    #ex: http://127.0.0.1:8000/cats/breed
    path('breed/', views.BreedList.as_view(), name='breed_list'),

    #ex: http://127.0.0.1:8000/cats/breed
    path('breed/entry/', views.BreedEntry.as_view(), name='breed_entry'),

    #ex: http://127.0.0.1:8000/cats/cat
    path('cat/entry/', views.CatEntry.as_view(), name='cat_entry'),

    #ex: http://127.0.0.1:8000/cats/breed/1/update
    path('breed/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),

    #ex: http://127.0.0.1:8000/cats/breed/1/delete
    path('breed/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),


    #ex: http://127.0.0.1:8000/cats/cat/1/update
    path('cat/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),

    #ex: http://127.0.0.1:8000/cats/cat/1/delete
    path('cat/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),





]