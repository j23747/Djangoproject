from django.shortcuts import render
import requests


# Fetch API data & display function from the joke API


# def  index(request):
#     response=request.get('https://official-joke-api.appspot.com/jokes/random').json()
#     return render(request, 'index.html', {'response' :response})


def getJoke(TemplateView):
    teplate_name = 'jokes.html'
    
    def get_context_data(self, *args, **kwargs):
        pass

