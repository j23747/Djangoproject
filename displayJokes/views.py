from django.shortcuts import render
from django.http import HttpResponse
import requests


# get the data from rest API
def jokes(request):
    response = requests.get('https://api.chucknorris.io/jokes/random/')


    #Converting the response data into json

    jokes = response.json()

    return render(request, 'display_jokes.html', {'jokes': jokes})
    pass





