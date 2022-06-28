
from django.urls import include, path
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
# from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('displayJokes.urls'))

    # path('', GetJokes.as_view(template_name='jokes.html'), name='DjangoApp View')


    
]


