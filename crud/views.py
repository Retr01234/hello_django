from django.shortcuts import render
from .models import Item

# Create your views here.
# Defining a Greeting Method to send and receive a HTTP Request


def get_todo_items(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'crud/crud_app.html', context)
