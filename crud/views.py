from django.shortcuts import render, HttpResponse

# Create your views here.
# Defining a Greeting Method to send and receive a HTTP Request


def greeting(request):
    return HttpResponse("Hello")
