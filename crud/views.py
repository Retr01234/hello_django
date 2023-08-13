from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

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
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_items')

    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'crud/add_item.html', context)
