from django.shortcuts import render
from django.http import HttpResponse
import requests

def jokes(request):
    response = requests.get('https://api.chucknorris.io/jokes/random/')


    #Converting the response data into json

    jokes = response.json()
    print(jokes)

    return HttpResponse("jokes")
    pass





