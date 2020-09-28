from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('accounts/', include('django.contrib.auth.urls')),  # Add
    path('polls/', include('polls.urls')),
    # tell the url where to found the url for incoming request. As hello is requested, its
    # showing that hello context will be found in hello.urls 
    path('hello/', include('hello.urls')),
    path('admin/', admin.site.urls),
    path('autos/', include('autos.urls')), 
    path('cats/', include('cats.urls')),
]