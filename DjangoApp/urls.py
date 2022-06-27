
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', GetJoke.as_view(template_name='jokes.html'), name='DjangoApp View')


    
]


