from django.shortcuts import render, redirect, get_object_or_404
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


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_items')

    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'crud/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_items')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_items')
