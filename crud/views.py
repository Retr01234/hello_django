from django.shortcuts import render, redirect
from .models import Item

# Create your views here.
# Defining a Greeting Method to send and receive a HTTP Request


def get_todo_items(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'crud/crud_app.html', context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_items')
    return render(request, 'crud/add_item.html')
