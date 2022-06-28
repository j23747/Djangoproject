
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from jokeAPI.views import GetJokes




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GetJokes.as_view(template_name='jokes.html'), name='DjangoApp View')


    
]


