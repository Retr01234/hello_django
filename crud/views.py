from django.shortcuts import render

# Create your views here.
# Defining a Greeting Method to send and receive a HTTP Request


def get_todo_items(request):
    return render(request, "crud/crud_app.html")
