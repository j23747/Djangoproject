from django.shortcuts import render
import requests
from django.views.generic import TemplateView
from . import views
# from . service import get_jokes

# Getting the Jokes and display them in HTML template



class GetJokes(TemplateView):
    template_name = 'jokes.html'
    
    def get_context_data(self, *args, **kwargs):
        pass

        # context = {
        #     'jokes' : get_jokes()
        # }    

        # return context

